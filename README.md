## P2: Tournament Results

### Overview of the Project:

For the second project in _Udacity_'s **Full Stack Web Development Nanodegree**, I needed to develop a database schema (SQL table definitions) and write a Python module using a PostgreSQL database to keep track of players and matches in a game tournament. The goal of this project was to learn how to architect and develop a database containing fully normalized data within multiple tables and how to modify this data and query it to meet the demands of a variety of use cases.

## Note about the game tournament

The game tournament uses a Swiss system for pairing up players in each round: players are paired with other players having approximately the same number of wins, and players are not eliminated.

### Minimum tasks that needed to be completed to meet expectations:

At a minimum, I needed to install Vagrant and Virtual Box, write the SQL database and table definitions in  `tournament.sql`, write Python functions according to the API that was provided in `tournament.py`. I then needed to test the functions defined in `tournament.py` using `tournament_test.py`.

### Description of Files, Classes and Functions:

* **tournament.sql:** This file contains the database schema and is imported by the PostgreSQL database. In order to import and run the file, the command `psql \i tournament.sql` is used.

* **tournament.py:** In this file, the following functions are defined:

 * `def connect():` Connect to the PostgreSQL database and returns a database connection.

 * `def deleteMatches():` Remove all the match records from the database.

 * `def countPlayers():` Returns the number of players currently registered.

 * `def registerPlayer(name):` Adds a player to the tournament database.

 * `def playerStandings():` Returns a list of the players and their win records, sorted by wins. The first entry in the list should be the player in first place, or a player tied for first place if there is currently a tie.

 * `def reportMatch(winner, loser):` Records the outcome of a single match between two players.
 
 * `def swissPairings():` Returns a list of pairs of players for the next round of a match. Assuming that there are an even number of players registered, each player appears exactly once in the pairings.  Each player is paired with another player with an equal or nearly-equal win record, that is, a player adjacent to him or her in the standings.

* **tournament_test.py:** This file contains the unit tests used to test functions written in `tournament.py`.

* **README.md**: This is the file you're reading.

### License 

MIT License

Copyright (c) 2016 minimal1st

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
