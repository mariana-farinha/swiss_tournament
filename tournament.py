#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except psycopg2.Error as e:
        print e.pgerror


def deleteMatches():
    """Remove all the match records from the database."""
    try:
        DB = connect()
        c = DB.cursor()
        c.execute("DELETE FROM games")
        DB.close()
        print 'Match records removed!'
    except psycopg2.Error as e:
        print e.pgerror




def deletePlayers():
    """Remove all the player records from the database."""
    try:
        DB = connect()
        c = DB.cursor()
        c.execute("DELETE FROM players")
        DB.close()
        DB.commit()
        print 'Player records removed!'
    except psycopg2.Error as e:
        print e.pgerror
    


def countPlayers():
    """Returns the number of players currently registered."""
    try:
        DB = connect()
        c = DB.cursor()
        c.execute("SELECT count(*) FROM players")
        result = c.fetchone()
        DB.close()
        if result[0] == None:
            return 0
        else:
            return int(result[0])
    except psycopg2.Error as e:
        print e.pgerror


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    try:
        DB = connect()
        c = DB.cursor()
        player = bleach.clean(name)
        c.execute("INSERT INTO players(name) VALUES (%s)", (player,))
        DB.commit()
        DB.close()
        print 'success!'
    except psycopg2.Error as e:
        print e.pgerror
    


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
    try:
        DB = connect()
        c = DB.cursor()
        c.execute


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
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


