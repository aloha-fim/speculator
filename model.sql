DROP TABLE IF EXISTS users;
CREATE TABLE users (
    uid serial NOT NULL PRIMARY KEY,
    username string NOT NULL,
    password string NOT NULL
);


DROP TABLE IF EXISTS condos;
CREATE TABLE condos (
    cid serial NOT NULL PRIMARY KEY,
    mlsnum integer NOT NULL,
    zip string NOT NULL,
    beds integer NOT NULL,
    baths float NOT NULL,
    sqft float NOT NULL,
    listprice float NOT NULL,
    photourl string NOT NULL
);


DROP TABLE IF EXISTS photos;
CREATE TABLE photos (
    pid serial NOT NULL PRIMARY KEY,
    mlsnum integer NOT NULL,
    imgnum integer NOT NULL,
    features string NOT NULL
);
