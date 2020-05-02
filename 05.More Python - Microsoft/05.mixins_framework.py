#Parents classes : Loggable and Database
class Loggable:
    def __init__(self):
        self.title = ''

    def log(self):
        print(f'Log message from {self.title}')

class Database:
    def __init__(self):
        self.server = ''

    def connect(self):
        print(f'Connecting to database on {self.server}')

#fancy framework which allows to make multiple inheritances
def framework(item):
    if isinstance(item, Database):
        item.connect()

    if isinstance(item, Loggable):
        item.log()


#-------------------------------------
#01. Child inheriting from Multiple classes
print('---------------')
class SqlDatabase(Loggable, Database):
    def __init__(self):
        self.title = 'sql connection demo'
        self.server = 'Some Server 456' 

sql = SqlDatabase()
framework(sql)

#02. Child inheriting from Loggable only
print('---------------')
class LogOnly(Loggable):
    def __init__(self):
        self.title = 'Log Only'

log_only = LogOnly()
framework(log_only)

#03. Child inheriting from Database only
print('---------------')
class DBOnly(Database):
    def __init__(self):
        self.server = 'PostgresSQL Server 123'

db_only = DBOnly()
framework(db_only)
    
