#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    #connect to the database    
    conn = connect() 

    #conn.cursor() returns a cursor object, which can be used to execute queries
    c = conn.cursor()

    #execute perform the query specified as argument
    #DELETE FROM matches delete all records from matches
    c.execute("DELETE FROM matches")

    #commit the changes
    conn.commit()
    
    #close the database connection
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    
    #connect to the database
    conn = connect() 

    #conn.cursor() returns a cursor object, which can be used to execute queries
    c = conn.cursor()

    #execute perform the query specified as argument
    #DELETE FROM matches delete all records from players
    c.execute("DELETE FROM players")

    conn.commit()

    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    
    #connect to the database
    conn = connect() 
    
    #conn.cursor() returns a cursor object, which can be used to execute queries
    c = conn.cursor()
    
    #execute perform the query specified as argument
    #SELECT COUNT(*) FROM players returns the number of players    
    c.execute("SELECT COUNT(*) FROM players")
    
    #fetchone fetches one row
    result = c.fetchone()
    
    #close the database connection
    conn.close()
    
    #access first element of the row
    return result[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    #connect to the database
    conn = connect() 

    #conn.cursor() returns a cursor object, which can be used to execute queries    
    c = conn.cursor()

    #the following INSERT INTO query insert the name of the players
    #the id is added and incremented automatically by the database
    #%s string format specifier, similar to C-like languages
    #comma needed after name to block SQL injections
    c.execute("INSERT INTO players (name) VALUES (%s);", (name,))

    #commit the changes
    conn.commit()

    #close the database connection
    conn.close()    


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    #connect to the database    
    conn = connect() 

    #conn.cursor() returns a cursor object, which can be used to execute queries
    c = conn.cursor()

    #select all rows from standings
    c.execute("SELECT * FROM standings")

    #result contains all the rows returned by the query
    result = c.fetchall()

    #return rows
    return result

    #close the database connection
    conn.close()



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    #connect to the database
    conn = connect() 

    #conn.cursor() returns a cursor object, which can be used to execute queries
    c = conn.cursor()

    #execute specified as argument
    c.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);", (winner,loser,))
    
    #commit changes 
    conn.commit()
    
    #close the connection
    conn.close()   
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # standings (list) stored in standings
    standings = playerStandings()

    # number of players (int) stored in num_of_players
    num_of_players = countPlayers()

    # make a new list of only even indexes to iterate in standings
    even_indexes = [x for x in range(num_of_players) if x%2==0]

    #make an empty list to store the pairs
    list_of_pairs = []
    
    #for all even indexes of standings do...
    for x in even_indexes:
            # here we get the id and name of the player at index 0
            # and we pair it with the player at index 1
            # then we take player at index 2 with player at index 3, etc.
            id1 = standings[x][0]
            name1 = standings[x][1]
            id2 = standings[x + 1][0]
            name2 = standings[x + 1][1]
            pair = (id1, name1, id2, name2)
            # append the pair in the list_of_pairs
            list_of_pairs.append(pair)

    # return list of pairs
    return list_of_pairs

