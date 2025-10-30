import MySQLdb
from sqlalchemy import create_engine

db = MySQLdb.connect('db.cs.usna.edu', # Hostname
                     'm273234',        # Username
                     'm273234',        # Password
                     'm273234')        # Schema/DB Name
engine = create_engine("mysql+mysqlconnector://m273234:m273234@db.cs.usna.edu/m273234")

db.autocommit(True)