import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()
password = os.getenv("pass")
dbName = "starwarsscr"

connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
# from config.configuration import  engine

def todas_frases(name_):
    query = engine.execute(
    f"SELECT dialogue FROM starwarsscr.dialogue INNER JOIN `char` ON `char_idchar` = `idchar` WHERE `name char` = '{name_}';")
    return {f"{name_}":f"{query.all()}"}

def newdialogue(dialogue, char_idchar, episode_idepisode):
    engine.execute(f"""
    INSERT INTO `dialogue` (`dialogue`, `char_idchar`, `episode_idepisode`)
     VALUES ('{dialogue}', {char_idchar},{episode_idepisode});
    """)
    return "all correctly introduced"

def toblob(name_):
    query = engine.execute(
    f"SELECT dialogue FROM starwarsscr.dialogue INNER JOIN `char` ON `char_idchar` = `idchar` WHERE `name char` = '{name_}';")
    e = ""
    for i in str(query.all()):
        e +=i
    return str(e)
  
def characters():
    query = engine.execute(
    "SELECT `name char` as `Character Name`, `idchar` as `Character ID` FROM starwarsscr.char ORDER BY `Character ID`;")
    return {"characters":f"{query.all()}"}