import config.configuration as c
import pandas as pd
from textblob import TextBlob

def change(x):
    """
    It cleans the dataframe deleting the ", ', / and \\.
    """
    x = str(x).replace('"', " ")
    x = str(x).replace("'", " ")
    x = str(x).replace("/", "")
    x = str(x).replace("\\", "")

    return x


def check(this,string):
    """
    This funtion checks if the character and the episode exists, returning True if it does or False if it doesn't.
    """
    if this == "char":
        query = list(c.engine.execute(f"SELECT `name char` FROM `char` WHERE `name char` = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif this == "episode":
        query = list(c.engine.execute(f"SELECT `name episode` FROM `episode` WHERE `name episode` = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif this == "dialogue": #It returns false because dialogues can be repeated
        return False


def char(string):
    """
    First it checks if the character exists using the function "check", and then it inserts the character.
    """
    if check("char", string):
        return "This character is already in your table"
    else:
        c.engine.execute(f"INSERT INTO `char` (`name char`) VALUES ('{string}');")


def episode(string):
    """
    First it checks if the episode exists using the function "check", and then it inserts the episode.
    """
    if check("episode", string):
        return "This episode is already in your table"
    else:
        c.engine.execute(f"INSERT INTO `episode` (`name episode`) VALUES ('{string}');")


def giveid(this,string):
    """
    It returns the ID from a character name or from an episode name.
    """
    if this == "char":
        return list(c.engine.execute(f"SELECT `idchar` FROM `char` WHERE `name char` ='{string}';"))[0][0]
    elif this == "episode":
        return list(c.engine.execute(f"SELECT `idepisode` FROM `episode` WHERE `name episode` ='{string}';"))[0][0]


def dialogue(row):
    """
    It inserts every dialogue, the character ID from the character who speaks, and the episode ID from the episode that corresponds to the dialogue.
    """
    if check("dialogue", row['dialogue']):
        if check("char", row['char']):
            idchar = giveid("char",row['char'])
        else:
            char(row['char'])
            idchar = giveid("char",row['char'])
        
        if check("episode", row['episode']):
            idepisode = giveid("episode", row['episode'])
        else:
            episode(row['episode'])
            idepisode = giveid("episode", row['episode'])
            
        
        c.engine.execute(f"""
        INSERT INTO `dialogue` (`dialogue`, `char_idchar`, `episode_idepisode`) VALUES
        ("{row['dialogue']}", "{idchar}","{idepisode}")
        ;
        """)
