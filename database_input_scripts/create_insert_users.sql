CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR (255), "password" VARCHAR(255), usertype VARCHAR(255));
CREATE TABLE userlogs (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), teamSelect VARCHAR(255), yearSelect INT);

INSERT INTO USERS (username, "password", usertype) VALUES ('admin', 'pbkdf2:sha256:600000$IBggf4L8Wu6vUWsx$d77909dc9d2940e724f6c665d2ca24e79be004e4a3c26ea625068524be72f5bd', 'admin');