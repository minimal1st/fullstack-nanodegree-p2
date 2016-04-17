-- Table definitions for the tournament project.

-- If the database exists, then drop it
DROP DATABASE IF EXISTS tournament;

-- Create database named tournament
CREATE database tournament;

-- Connect to the database using psql
\c tournament

-- A table is needed to hold the players
-- id uniquely identifies players
-- serial type increments automatically
CREATE TABLE players ( 
	id serial primary key, 
	name text
);

-- A table is needed to record the matches
-- id uniquely identifies the matches
-- serial type increments automatically
CREATE TABLE matches (
	id serial primary key, 
	winner_id int references players(id), 
	loser_id int references players(id)
);


-- A view that computes the standings for the tournament
-- Each row contains: 
-- 1) id of the player
-- 2) the name of the player
-- 3) the number of matches won
-- 4) the number of matches played
CREATE VIEW standings AS 
	SELECT 
		players.id, 
		players.name, 
		(SELECT COUNT(*) FROM matches WHERE players.id = matches.winner_id) as matches_won,
		(SELECT COUNT(*) FROM matches WHERE players.id = matches.winner_id or
			players.id = matches.loser_id) as matches_played
	FROM players
	ORDER BY matches_won DESC;