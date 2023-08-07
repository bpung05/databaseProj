from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db= SQLAlchemy()


class allstarfull(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerid = db.Column(db.String)
    yearID = db.Column(db.Integer)
    gameNum = db.Column(db.db.Integer)
    gameID = db.Column( db.String(255))
    teamID = db.Column( db.String(5))
    lgID = db.Column(db.String(5))
    GP = db.Column(db.Integer)
    startingPOS = db.Column( db.Integer)



class appearances(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yearID = db.Column( db.Integer)
    teamID = db.Column( db.String(5))
    lgID = db.Column( db.String(5))
    playerID = db.Column( db.String(255))
    G_all = db.Column( db.Integer)
    GS = db.Column( db.Integer)
    G_batting = db.Column(db.Integer)
    G_defense = db.Column( db.Integer)
    G_p = db.Column( db.Integer)
    G_c = db.Column( db.Integer)
    G_1b = db.Column( db.Integer)
    G_2b =  db.Column( db.Integer)
    G_3b = db.Column( db.Integer)
    G_ss= db.Column(db.Integer)
    G_lf = db.Column( db.Integer)
    G_cf = db.Column(db.Integer)
    G_rf = db.Column( db.Integer)
    G_of = db.Column( db.Integer)
    G_dh = db.Column( db.Integer)
    G_ph = db.Column( db.Integer)
    G_pr = db.Column( db.Integer)

class awardsmanagers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID  = db.Column( db.String(255))
    awardID  =db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    lgID = db.Column( db.String(5))
    tie = db.Column( db.String(5))
    notes = db.Column( db.String(255))


class awardsplayers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column(db.String(255))
    awardID = db.Column(db.String(255))
    yearID = db.Column( db.Integer)
    lgID = db.Column(db.String(5))
    tie = db.Column( db.String(5))
    notes =db.Column( db.String(255))


class awardssharemanagers(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    awardID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    lgID = db.Column( db.String(5))
    playerID = db.Column( db.String(255))
    poINTsWon = db.Column( db.Integer)
    poINTsMax  = db.Column( db.Integer)
    votesFirst = db.Column( db.Integer)



class awardsshareplayers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    awardID= db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    lgID = db.Column(db.String(5))
    playerID = db.Column( db.String(255))
    poINTsWon = db.Column( db.Integer)
    poINTsMax = db.Column( db.Integer)
    votesFirst = db.Column( db.Integer)



class batting(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    stINT = db.Column( db.Integer)
    teamID = db.Column( db.String(5))
    lgID = db.Column( db.Integer)
    G = db.Column( db.Integer)
    AB = db.Column( db.Integer)
    R = db.Column( db.Integer)
    H = db.Column(db.Integer)
    secondB = db.Column( db.Integer)
    thirdB = db.Column( db.Integer)
    HR = db.Column( db.Integer)
    RBI = db.Column( db.Integer)
    SB =db.Column( db.Integer)
    CS  = db.Column(db.Integer)
    BB = db.Column( db.Integer)
    SO = db.Column( db.Integer)
    IBB = db.Column( db.Integer)
    HBP = db.Column( db.Integer)
    SH = db.Column( db.Integer)
    SF = db.Column( db.Integer)
    GIDP = db.Column( db.Integer)



class battingpost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yearID = db.Column( db.Integer)
    round = db.Column(db.String(5))
    playerID = db.Column( db.String(255))
    teamID = db.Column( db.String(5))
    lgID = db.Column( db.Integer)
    G = db.Column( db.Integer)
    AB = db.Column( db.Integer)
    R = db.Column( db.Integer)
    H = db.Column(db.Integer)
    secondB = db.Column( db.Integer)
    thirdB = db.Column( db.Integer)
    HR = db.Column( db.Integer)
    RBI = db.Column( db.Integer)
    SB =db.Column( db.Integer)
    CS  = db.Column(db.Integer)
    BB = db.Column( db.Integer)
    SO = db.Column( db.Integer)
    IBB = db.Column( db.Integer)
    HBP = db.Column( db.Integer)
    SH = db.Column( db.Integer)
    SF = db.Column( db.Integer)
    GIDP = db.Column( db.Integer)



class collegeplaying(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    schoolID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)



class fielding(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    stint =db.Column( db.Integer)
    teamID =db.Column( db.String(5))
    lgID = db.Column( db.String(5))
    POS =db.Column( db.String(5))
    G = db.Column(db.Integer)
    GS =db.Column( db.Integer)
    InnOuts = db.Column(db.Integer)
    PO = db.Column( db.Integer)
    A = db.Column( db.Integer)
    E = db.Column( db.Integer)
    DP =  db.Column( db.Integer)
    PB = db.Column( db.Integer)
    WP = db.Column(db.Integer)
    SB = db.Column( db.Integer)
    CS = db.Column( db.Integer)
    ZR = db.Column( db.Integer)




class fieldingof(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    stint =db.Column( db.Integer)
    Glf = db.Column( db.Integer)
    Gcf = db.Column( db.Integer)
    Grf = db.Column( db.Integer)




class fieldingofsplit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    stint =db.Column( db.Integer)
    teamID =db.Column( db.String(5))
    lgID = db.Column( db.String(5))
    POS =db.Column( db.String(5))
    G = db.Column(db.Integer)
    GS =db.Column( db.Integer)
    InnOuts = db.Column(db.Integer)
    PO = db.Column( db.Integer)
    A = db.Column( db.Integer)
    E = db.Column( db.Integer)
    DP =  db.Column( db.Integer)
    PB = db.Column( db.Integer)
    WP = db.Column(db.Integer)
    SB = db.Column( db.Integer)
    CS = db.Column( db.Integer)
    ZR = db.Column( db.Integer)


class fieldingpost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    teamID =db.Column( db.String(5))
    lgID = db.Column( db.String(5))
    round = db.Column( db.String(5))
    POS = db.Column( db.String(5))
    G = db.Column( db.Integer)
    GS = db.Column( db.Integer)
    InnOuts =db.Column( db.Integer)
    PO = db.Column( db.Integer)
    A = db.Column( db.Integer)
    E =db.Column( db.Integer)
    DP =db.Column(db.Integer)
    TP = db.Column( db.Integer)
    PB = db.Column( db.Integer)
    SB = db.Column( db.Integer)
    CS = db.Column( db.Integer)



class halloffame(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID = db.Column( db.Integer)
    votedBy =  db.Column( db.String(255))
    ballots = db.Column( db.Integer)
    needed = db.Column( db.Integer)
    votes =db.Column( db.Integer)
    inducted = db.Column( db.String(5))
    category = db.Column(db.String(255))
    needed_note = db.Column( db.String(255))




class homegames(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yearID = db.Column( db.Integer)
    leagueID = db.Column( db.String(5))
    teamID = db.Column( db.String(5))
    parkKey =db.Column( db.String(255))
    spanFirst = db.Column( db.Date)
    spanLast = db.Column( db.Date)
    games = db.Column( db.Integer)
    openings = db.Column( db.Integer)
    attendance = db.Column( db.Integer)



class managers(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID =db.Column( db.Integer)
    teamID = db.Column( db.String(5))
    lgID = db.Column( db.String(5))
    inseason = db.Column( db.Integer)
    G = db.Column( db.Integer)
    W =db.Column( db.Integer)
    L = db.Column(db.Integer)
    rank  =db.Column( db.Integer)
    plyrMgr = db.Column( db.String(5))


class managershalf(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column( db.String(255))
    yearID =db.Column( db.Integer)
    teamID = db.Column( db.String(5))
    lgID = db.Column( db.String(5))
    inseason = db.Column( db.Integer)
    half =db.Column(db.Integer)
    G = db.Column( db.Integer)
    W =db.Column( db.Integer)
    L = db.Column(db.Integer)
    rank = db.Column( db.Integer)




class parks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parkKey = db.Column(db.String(255))
    parkName = db.Column(db.String(255))
    parkAlias = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))



class people(db.Model):
    playerID = db.Column(db.String(255) ,primary_key=True)
    birthYear = db.Column(db.Integer)
    birthMonth = db.Column(db.Integer)
    birthDay = db.Column(db.Integer)
    birthCountry = db.Column(db.String(255))
    birthState = db.Column(db.String(255))
    birthCity = db.Column(db.String(255))
    deathYear = db.Column(db.Integer)
    deathMonth = db.Column(db.Integer)
    deathDay = db.Column(db.Integer)
    deathCountry = db.Column(db.String(255))
    deathState = db.Column(db.String(255))
    deathCity = db.Column(db.String(255))
    nameFirst = db.Column(db.String(255))
    nameLast = db.Column(db.String(255))
    nameGiven = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    bats = db.Column(db.String(5))
    throws = db.Column(db.String(5))
    debut = db.Column(db.Date)
    finalGame = db.Column(db.Date)
    retroID = db.Column(db.String(255))
    bbrefID = db.Column(db.String(255))




class pitching(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column(db.String(255))
    yearID = db.Column(db.Integer)
    stint = db.Column(db.Integer)
    teamID = db.Column(db.String(5))
    lgID = db.Column(db.String(5))
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    G = db.Column(db.Integer)
    GS = db.Column(db.Integer)
    CG = db.Column(db.Integer)
    SHO = db.Column(db.Integer)
    SV = db.Column(db.Integer)
    IPouts = db.Column(db.Integer)
    H = db.Column(db.Integer)
    ER = db.Column(db.Integer)
    HR = db.Column(db.Integer)
    BB = db.Column(db.Integer)
    SO = db.Column(db.Integer)
    BAOpp = db.Column(db.Float)
    ERA = db.Column(db.Float)
    IBB = db.Column(db.Integer)
    WP = db.Column(db.Integer)
    HBP = db.Column(db.Integer)
    BK = db.Column(db.Integer)
    BFP = db.Column(db.Integer)
    GF = db.Column(db.Integer)
    R = db.Column(db.Integer)
    SH = db.Column(db.Integer)
    SF = db.Column(db.Integer)
    GIDP = db.Column(db.Integer)



class pitchingpost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerID = db.Column(db.String(255))
    yearID = db.Column(db.Integer)
    round = db.Column(db.String(5)) 
    teamID = db.Column(db.String(5))
    lgID = db.Column(db.String(5))
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    G = db.Column(db.Integer)
    GS = db.Column(db.Integer)
    CG = db.Column(db.Integer)
    SHO = db.Column(db.Integer)
    SV = db.Column(db.Integer)
    IPouts = db.Column(db.Integer)
    H = db.Column(db.Integer)
    ER = db.Column(db.Integer)
    HR = db.Column(db.Integer)
    BB = db.Column(db.Integer)
    SO = db.Column(db.Integer)
    BAOpp = db.Column(db.Float)
    ERA = db.Column(db.Float)
    IBB = db.Column(db.Integer)
    WP = db.Column(db.Integer)
    HBP = db.Column(db.Integer)
    BK = db.Column(db.Integer)
    BFP = db.Column(db.Integer)
    GF = db.Column(db.Integer)
    R = db.Column(db.Integer)
    SH = db.Column(db.Integer)
    SF = db.Column(db.Integer)
    GIDP = db.Column(db.Integer)



class salaries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yearID = db.Column(db.Integer)
    teamID = db.Column(db.String(5))
    lgID = db.Column(db.String(5))
    playerID = db.Column(db.String(255))
    salary = db.Column(db.Integer)




class schools(db.Model):
    schoolID = db.Column(db.String(255), primary_key=True)
    name_full = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))


class seriespost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yearID = db.Column(db.Integer)
    round = db.Column(db.String(5))
    teamIDwinner = db.Column(db.String(5))
    lgIDwinner = db.Column(db.String(5))
    teamIDloser = db.Column(db.String(5))
    lgIDloser = db.Column(db.String(5))
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    ties = db.Column(db.Integer)


class teams(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yearID = db.Column(db.Integer)
    lgID = db.Column(db.String(5))
    teamID = db.Column(db.String(5))
    franchID = db.Column(db.String(5))
    divID = db.Column(db.String(5))
    Rank = db.Column(db.Integer)
    G = db.Column(db.Integer)
    Ghome = db.Column(db.Integer)
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    DivWin = db.Column(db.String(5))
    WCWin = db.Column(db.String(5))
    LgWin = db.Column(db.String(5))
    WSWin = db.Column(db.String(5))
    R = db.Column(db.Integer)
    AB = db.Column(db.Integer)
    H = db.Column(db.Integer)
    secondB = db.Column(db.Integer)  
    thirdB = db.Column(db.Integer)  
    HR = db.Column(db.Integer)
    BB = db.Column(db.Integer)
    SO = db.Column(db.Integer)
    SB = db.Column(db.Integer)
    CS = db.Column(db.Integer)
    HBP = db.Column(db.Integer)
    SF = db.Column(db.Integer)
    RA = db.Column(db.Integer)
    ER = db.Column(db.Integer)
    ERA = db.Column(db.Float)
    CG = db.Column(db.Integer)
    SHO = db.Column(db.Integer)
    SV = db.Column(db.Integer)
    IPouts = db.Column(db.Integer)
    HA = db.Column(db.Integer)
    HRA = db.Column(db.Integer)
    BBA = db.Column(db.Integer)
    SOA = db.Column(db.Integer)
    E = db.Column(db.Integer)
    DP = db.Column(db.Integer)
    FP = db.Column(db.Float)
    name = db.Column(db.String(255))
    park = db.Column(db.String(255))
    attendance = db.Column(db.Integer)
    BPF = db.Column(db.Integer)
    PPF = db.Column(db.Integer)
    teamIDBR = db.Column(db.String(5))
    teamIDlahman45 = db.Column(db.String(5))
    teamIDretro = db.Column(db.String(5))


class teamsfranchises(db.Model):
    franchID = db.Column(db.String(5), primary_key=True)
    franchName = db.Column(db.String(255))
    active = db.Column(db.String(5))
    NAassoc = db.Column(db.String(5))


class teamshalf(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yearID = db.Column(db.Integer)
    lgID = db.Column(db.String(5))
    teamID = db.Column(db.String(5))
    Half = db.Column(db.Integer)
    divID = db.Column(db.String(5))
    DivWin = db.Column(db.String(5))
    Rank = db.Column(db.Integer)
    G = db.Column(db.Integer)
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)



class userlogs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    teamSelect = db.Column(db.String(255))
    yearSelect = db.Column(db.Integer)


class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column( db.String(255))
    usertype = db.Column(db.String(255))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False