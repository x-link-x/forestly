DROP TABLE IF EXISTS trees;
DROP TABLE IF EXISTS varieties;
DROP TABLE IF EXISTS areas;

CREATE TABLE varieties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE areas (
    id SERIAL PRIMARY KEY,
    easting VARCHAR(255),
    northing VARCHAR(255)
);

CREATE TABLE trees (
    id SERIAL PRIMARY KEY,
    approx_age INT,
    variety_id INT REFERENCES varieties(id) ON DELETE CASCADE,
    area_id INT REFERENCES areas(id) ON DELETE CASCADE,
    x INT,
    y INT,
    notes TEXT
);

