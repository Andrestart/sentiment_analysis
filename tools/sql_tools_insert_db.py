import config.configuration as c
import pandas as pd
from textblob import TextBlob

def change(x):
    x = str(x).replace('"', " ")
    x = str(x).replace("'", " ")
    x = str(x).replace("/", "")
    x = str(x).replace("\\", "")

    return x


def check(this,string):
    """
    Función parametrizada que comprueba en cada tabla si existe el user, artista o canción.
    Devuelve True si existe y False si no
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
    if check("char", string):
        return "This character is already in your table"
    else:
        c.engine.execute(f"INSERT INTO `char` (`name char`) VALUES ('{string}');")


def episode(string):
    if check("episode", string):
        return "This episode is already in your table"
    else:
        c.engine.execute(f"INSERT INTO `episode` (`name episode`) VALUES ('{string}');")


def giveid(this,string):
    """
    Devuelve el ID de lo que le pidamos sabiendo que ese elemento EXISTE
    """
    if this == "char":
        return list(c.engine.execute(f"SELECT `idchar` FROM `char` WHERE `name char` ='{string}';"))[0][0]
    elif this == "episode":
        return list(c.engine.execute(f"SELECT `idepisode` FROM `episode` WHERE `name episode` ='{string}';"))[0][0]


def dialogue(row):
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
