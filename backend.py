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
    "password":"mysql",
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
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()
    return movies

def AddNewMovie(name, date_of_release, cast, collection, genre, conn):
    
    sql = '''INSERT INTO movies (Movie_name, Date_of_Release, Cast, Collection, Genre, avg_rating) values( %s, %s,%s,%s,%s, 0)'''
    cur = conn.cursor()
    cur.execute(sql, (name, date_of_release, cast, collection, genre))
    conn.commit()

def AddNewReview(rating, review,movieid):
    sql = '''INSERT INTO reviews (rating,review_text ,movie_id) values (%s,%s,%s)'''
    cur = conn.cursor()

    cur.execute(sql,(rating, review, movieid))
    conn.commit()
def FetchMovieRatings(movie_id):
    sql = '''SELECT rating from reviews where movie_id = (%s)'''
    cur = conn.cursor()
    cur.execute(sql, (movie_id,))
    return cur.fetchall()
conn = create_dbconnect ()
print(conn.is_connected())
#AddNewMovie("test", "2009-03-30", "test", 2131, "Horror", conn)
#AddNewReview(7, "pretty decent",9)

l = FetchMovieRatings(9)
print(l)
