from flask import render_template, session, url_for, redirect, request, flash, Response
from flask_login import login_required
import models
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import forms

#custom decorator for admin privaledges such that it prevents unauthorized users.
def admin_required(func):
    @wraps(func)
    #define positional arguments and keyword arguments
    def decorated_function(*args, **kwargs):
        if session.get('usertype') == 'admin':
            return func(*args, **kwargs)

        return redirect(url_for('login'))
    return decorated_function

#custom decorator for user privaledges such that it prevents unauthorized users.
def user_required(func):
    @wraps(func)
    #define positional arguments and keyword arguments
    def decorated_function(*args, **kwargs):
        if session.get('usertype') == 'user':
            return func(*args, **kwargs)

        return redirect(url_for('login'))
    return decorated_function


def other_routes(app,db):

    @app.route("/userdashboard", methods=["GET"])
    @login_required
    @user_required
    def userdashboard():
        username = session.get('username')
        return render_template('userdashboard.html', username=username)
    
    @app.route("/admindashboard", methods =["GET"])
    @login_required
    @admin_required
    def admindashboard():
        username= session.get('username')
        return render_template('admindashboard.html', username=username)
    
    @app.route("/adminadduser", methods=['GET','POST'])
    @login_required
    @admin_required
    def adminadduser():
        form = forms.AddUserForm()
        if request.method == 'POST':
            username = str(form.username.data)
            password = generate_password_hash(str(form.password.data))
            accounttype = str(form.accounttype.data)

            if ((' ' in username) or (' ' in str(form.password.data))):
                return render_template('adminadduser.html', message = "Username and password cannot have spaces", form = form)
            if (len(username) >= 255) or (len(str(form.password.data)) >= 255):
                return render_template('adminadduser.html', message = "Username or password too long", form = form)

            if (models.users.query.filter(models.users.username==username).first()):
                return render_template('adminadduser.html', message = "Username already in database", form = form)
        
            
            print(username, password, accounttype)
            #add new user to database because username is not in database.
            new_user = models.users(username=username, password=password, usertype=accounttype)
            db.session.add(new_user)
            db.session.commit()
            
            print(new_user.username)
            return render_template('adminadduser.html', message="User added to database!", form = form)
        return render_template('adminadduser.html', form = form)
    
    @app.route("/queryroster", methods =["GET", "POST"])
    @login_required
    def queryroster():
        usertype = session.get('usertype')
        
        def getBatting(team_given, year_given):
            teamid = getTeamID(team_given, year_given)
            if teamid is None:
                return None
            #get the aggragate stats for players by joining batting and appearances
            players_query = models.batting.query.with_entities(
                models.batting.playerID,
                models.batting.yearID,
                models.appearances.G_p,
                models.appearances.G_c,
                models.appearances.G_1b,
                models.appearances.G_2b,
                models.appearances.G_3b,
                models.appearances.G_ss,
                models.appearances.G_lf,
                models.appearances.G_rf,
                models.appearances.G_cf,
                models.appearances.G_dh,
                models.appearances.G_ph,
                models.appearances.G_pr,
                db.func.sum(models.batting.G).label('total_games'),
                db.func.sum(models.batting.H).label('total_hits'),
                db.func.sum(models.batting.AB).label('total_at_bats'),
                db.func.sum(models.batting.R).label("total_runs"),
                db.func.sum(models.batting.secondB).label("total_secondB"),
                db.func.sum(models.batting.thirdB).label("total_thirdB"),
                db.func.sum(models.batting.HR).label("total_hr"),
                db.func.sum(models.batting.RBI).label("total_rbi"),
                db.func.sum(models.batting.SB).label("total_sb"),
                db.func.sum(models.batting.CS).label("total_cs"),
                db.func.sum(models.batting.BB).label("total_bb"),
                db.func.sum(models.batting.SO).label("total_so"),
                db.func.sum(models.batting.HBP).label("total_hbp"),
                db.func.sum(models.batting.IBB).label("total_ibb"),
                db.func.sum(models.batting.SH).label("total_sh"),
                db.func.sum(models.batting.SF).label("total_sf"),
                db.func.sum(models.batting.GIDP).label("total_gidp"),
                (db.func.sum(models.batting.H) / db.func.sum(models.batting.AB)).label('avg'),
                ((db.func.sum(models.batting.H) + db.func.sum(models.batting.BB) + db.func.sum(models.batting.HBP)) /
                    (db.func.sum(models.batting.AB) + db.func.sum(models.batting.BB) + db.func.sum(models.batting.HBP) + db.func.sum(models.batting.SF))
                    ).label('obp'),
                (((db.func.sum(models.batting.H) - db.func.sum(models.batting.secondB) - db.func.sum(models.batting.thirdB) - db.func.sum(models.batting.HR)) +
                    2 * db.func.sum(models.batting.secondB) + 3 * db.func.sum(models.batting.thirdB) + 4 * db.func.sum(models.batting.HR)) /
                    db.func.sum(models.batting.AB)).label("slug")
            ).join(
                models.appearances,
                ((models.appearances.playerID == models.batting.playerID) &
                (models.appearances.yearID == models.batting.yearID))
            ).filter(
                models.batting.teamID== teamid,
                models.batting.yearID == year_given
            ).group_by(
                models.batting.playerID,
                models.batting.yearID,
                models.batting.teamID
            ).all()
            
            """
            This to have by career
            
            .join(
                models.appearances,
                ((models.appearances.playerID == models.batting.playerID) &
                (models.appearances.yearID == models.batting.yearID))
            ).filter(
                models.appearances.teamID== teamid,
                models.appearances.yearID == year_given
            ).group_by(
                models.batting.playerID,
                models.appearances.yearID,
                models.appearances.teamID
            ).all()"""
            """
            To make it one stint I think:
            .join(
                models.appearances,
                ((models.appearances.playerID == models.batting.playerID) &
                (models.appearances.yearID == models.batting.yearID))
            ).filter(
                models.batting.teamID== teamid,
                models.batting.yearID == year_given
            ).group_by(
                models.batting.playerID,
                models.batting.yearID,
                models.batting.teamID"""
            return players_query


        def getPitching(team_given, year_given):
            teamid = getTeamID(team_given, year_given)

            pitching_query = models.pitching.query.with_entities(
                models.appearances.playerID,
                models.appearances.G_p,
                models.appearances.GS,
                (db.func.sum(models.pitching.IPouts) / 3).label('ip'),
                ((models.pitching.BB + models.pitching.H)/ (models.pitching.IPouts / 3)).label('whip'),
                ((((models.pitching.SO)/((models.pitching.IPouts) / 3))) * 9).label('k_p_9')
            ).join(
                models.appearances,
                ((models.appearances.playerID == models.pitching.playerID) &
                (models.appearances.yearID == models.pitching.yearID))
            ).filter(
                models.pitching.teamID== teamid,
                models.pitching.yearID == year_given
            ).group_by(
                models.pitching.playerID,
                models.pitching.yearID,
                models.pitching.teamID
            ).all()


            return pitching_query

        def getTeamID(team_given, year_given):
            teamID = models.teams.query.filter_by(name=team_given, yearID=year_given).first()
            if teamID is None:
                return None
            return teamID.teamID

        
        teams = [team.name for team in models.teams.query.with_entities(models.teams.name).distinct().order_by(models.teams.name)]
        years = [year.yearID for year in models.teams.query.with_entities(models.teams.yearID).distinct()]
        
        if request.method=='POST':
            team = request.form['team']
            year = request.form['year']
            year = int(year)
        
            batting_roster = getBatting(team, year)
            pitching_roster = getPitching(team,year)
            return render_template('queryroster.html', team_output = team, year_output = year ,
                teams = teams,  years = years, batting_roster = batting_roster, 
                pitching_roster=pitching_roster, usertype= usertype)

        return render_template ('queryroster.html', teams=teams, years=years, usertype= usertype)
    
    @app.route("/logout", methods = ["POST"])
    def logout():
        session.clear()
        return redirect(url_for('login'))