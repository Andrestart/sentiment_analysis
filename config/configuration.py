import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()
password = os.getenv("pass")
dbName = "starwarsscr"

connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)