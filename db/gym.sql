DROP TABLE IF EXISTS workouts;
DROP TABLE IF EXISTS g_classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    premium BOOLEAN,
    active BOOLEAN
);

CREATE TABLE g_classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    duration VARCHAR(255),
    capacity INT,
    number_of_members INT,
    active BOOLEAN
);

CREATE TABLE workouts(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    g_class_id INT REFERENCES g_classes(id) ON DELETE CASCADE
);