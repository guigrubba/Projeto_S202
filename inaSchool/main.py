from database import Database
from scholl_cli import SchoolCLI

db = Database(database="school", collection="inaSchool")

cli = SchoolCLI(database=db)
cli.menu()