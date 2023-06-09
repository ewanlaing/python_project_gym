DROP TABLE IF EXISTS gym;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    premium BOOLEAN,
    active BOOLEAN
);

CREATE TABLE classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    duration INT,
    capacity INT,
    number_of_members INT,
    active BOOLEAN
);

CREATE TABLE gym(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE
);