-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament;


CREATE TABLE players( id SERIAL PRIMARY KEY,
                      name TEXT NOT NULL);

CREATE TABLE enrollments( sport TEXT NOT NULL,
                          player_id INTEGER REFERENCES players(id),
						  PRIMARY KEY(sport, player_id));

CREATE TYPE outcome AS ENUM('win','lose','draw');

CREATE TABLE games( sport TEXT NOT NULL,
                    player INTEGER REFERENCES players(id),
					opponent INTEGER REFERENCES players(id),
					outcome outcome NOT NULL,
					PRIMARY KEY(sport,player,opponent),
					FOREIGN KEY(sport,player) REFERENCES enrollments (sport, player_id),
					FOREIGN KEY(sport,opponent) REFERENCES enrollments (sport, player_id),
					CHECK (player != opponent));

