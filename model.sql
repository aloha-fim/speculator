-- text in postgres is a variable length character string in SQLAlchemy 
-- float in postgres has to be defined
-- serial is an autoincrementing integer in SQLAlchemy

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    uid serial NOT NULL PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL
);


DROP TABLE IF EXISTS condos;
CREATE TABLE condos (
    cid serial NOT NULL PRIMARY KEY,
    mlsnum integer NOT NULL,
    zip text NOT NULL,
    beds integer NOT NULL,
    baths float(25) NOT NULL,
    sqft float(25) NOT NULL,
    listprice float(25) NOT NULL,
    photourl text NOT NULL
);


DROP TABLE IF EXISTS photos;
CREATE TABLE photos (
    pid serial NOT NULL PRIMARY KEY,
    mlsnum integer NOT NULL,
    imgnum integer NOT NULL,
    features text NOT NULL
);


DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
	lid serial NOT NULL PRIMARY KEY,
    liker integer NOT NULL, 
    liked integer NOT NULL,
    FOREIGN KEY (liker) REFERENCES users(uid),
    FOREIGN KEY (liked) REFERENCES condos(cid)
);
