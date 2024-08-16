import mysql.connector 
#
# Function are defined here
#

def create_dbconnect():

    conn = None
    try:
        config = {
    "host":"localhost",
    "user":"root",
    "password":"",
    "database" : "MovieDB",
  'raise_on_warnings': True}

        conn  = mysql.connector.connect(**config)
        print(conn.is_connected())
    except Exception as e:
        print(e)
    return conn
#
#
# Function call to open up the MYSQL DB
db_file = r"lib.db"
conn = create_dbconnect ()

def RetrieveMovies(n, conn):
    cur = conn.cursor()
    cur.execute("SELECT movies.Movie_name FROM movies join reviews on movies.id = reviews.movie_id ")
    movies = cur.fetchall()
    return movies

def AddNewMovie(name, date_of_release, cast, collection, genre, conn):
    
    sql = '''INSERT INTO movies (Movie_name, Date_of_Release, Cast, Collection, Genre) values( %s, %s,%s,%s,%s )'''
    cur = conn.cursor()
    cur.execute(sql, (name, date_of_release, cast, collection, genre))
    conn.commit()
conn = create_dbconnect ()
print(conn.is_connected())
AddNewMovie("test", "2009-03-30", "test", 2131, "Horror", conn)
l = RetrieveMovies(4, conn)
print(l)
