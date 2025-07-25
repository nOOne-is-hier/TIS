-- create.sql (DB 초기화용)
DROP DATABASE IF EXISTS playground;


CREATE DATABASE playground;


USE playground;


DROP TABLE IF EXISTS FIRST_HALF;


DROP TABLE IF EXISTS ICECREAM_INFO;


CREATE TABLE
    FIRST_HALF (
        SHIPMENT_ID INT NOT NULL,
        FLAVOR VARCHAR(100) PRIMARY KEY,
        TOTAL_ORDER INT NOT NULL
    );


CREATE TABLE
    ICECREAM_INFO (FLAVOR VARCHAR(100) PRIMARY KEY, INGREDIENT_TYPE VARCHAR(100) NOT NULL);