import config.configuration as c

def alldialogues(name_):
    """
    This funtion filters the SQL database to get all the dialogues from a specific character.
    """
    query = c.engine.execute(
    f"SELECT dialogue FROM starwarsscr.dialogue INNER JOIN `char` ON `char_idchar` = `idchar` WHERE `name char` = '{name_}';")
    return {f"{name_}":f"{cleanforblob(query.all())}"}

def newdialogue(dialogue, char_idchar, episode_idepisode):
    """
    It inserts a new dialogue in the SQL database.
    """
    c.engine.execute(f"""
    INSERT INTO `dialogue` (`dialogue`, `char_idchar`, `episode_idepisode`)
     VALUES ('{dialogue}', {char_idchar},{episode_idepisode});
    """)
    return "all correctly introduced"

def toblob(name_):
    """
     It takes the dialogues from a specific character from the SQL database and cleans it so the sentiment analysis works properly without special characters.
    """
    query = c.engine.execute(
    f"SELECT dialogue FROM starwarsscr.dialogue INNER JOIN `char` ON `char_idchar` = `idchar` WHERE `name char` = '{name_}';")
    e = ""
    for i in str(query.all()):
        e +=cleanforblob(i)
    return str(e)
  
def characters():
    """
    It takes the name of all characters and their IDs.
    """
    query = c.engine.execute(
    "SELECT `name char` as `Character Name`, `idchar` as `Character ID` FROM starwarsscr.char ORDER BY `Character ID`;")
    return {"Star Wars Characters":f"{query.all()}"}

def episodes():
    """
    It takes all the episode names and their IDs from the SQL database.
    """
    query = c.engine.execute(
    "SELECT `name episode` as `Episode Name`, `idepisode` as `Episode ID` FROM starwarsscr.episode ORDER BY `Episode ID`;")
    allepisodes = query.all()
    print(type(allepisodes))
    d = {}
    for i in allepisodes:
        d[i[0]] = int(i[1])
   
    return d

def cleanforblob(querystr):
    """
    It cleans the SQL queries so they are ready for the sentiment analysis and replaces all special characters.
    """
    querystr = str(querystr).replace('(', "")
    querystr = str(querystr).replace(')', "")
    querystr = str(querystr).replace('[', "")
    querystr = str(querystr).replace(']', "")
    querystr = str(querystr).replace("'", "")
    querystr = str(querystr).replace(",", "")
    return querystr

def alltoblob():
    """
    It takes all dialogues from the SQL database and cleans them so they are clean and ready for the sentiment analysis.
    """
    query = c.engine.execute(
    f"SELECT dialogue FROM starwarsscr.dialogue;")
    e = ""
    for i in query.all():
        e +=cleanforblob(i)
    return cleanforblob(e)