from os.path import isfile
from sqlite3 import connect

database_name = "scores.db"

class Score:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def with_db(f):
    """
    Funktiokoriste, joka syöttää funktiolle
    ensimmäisenä argumenttina tietokantaolion.
    """

    def wrapper(*args):
        if isfile(database_name):
            db = connect(database_name)
        else:
            db = create_database()

        result = f(db, *args)
        db.close()
        return result

    return wrapper

def set_database_name(name):
    global database_name
    database_name = name

def create_database():
    """Alustaa sqlite-tietokannan."""
    db = connect(database_name)
    cur = db.cursor()

    cur.execute("CREATE TABLE user(name TEXT UNIQUE);")
    cur.execute("""
        CREATE TABLE score(
            value INTEGER,
            time REAL,
            user_id INTEGER,
            width INTEGER,
            height INTEGER,
            num_mines INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(rowid)
        );
    """)

    return db

@with_db
def save_score(db, score, name, width, height, num_mines):
    """
    Tallentaa tietokantaan pelin tuloksen, käyttäjän
    nimimerkin sekä asetukset, joilla peli pelattiin.
    """

    cur = db.cursor()

    res = cur.execute("SELECT rowid FROM user WHERE name=? LIMIT 1;", (name,)).fetchone()
    if res:
        user_id = res[0]
    else:
        res = cur.execute("INSERT INTO user(name) VALUES(?) RETURNING rowid;", (name,)).fetchone()
        user_id = res[0]

    cur.execute("""
        INSERT INTO score(value, time, user_id, width, height, num_mines)
        VALUES(?, julianday(), ?, ?, ?, ?);
    """, (score, user_id, width, height, num_mines))
    db.commit()

@with_db
def get_scores(db, width, height, num_mines):
    """
    Hakee tietokannasta 10 parasta aikaa.
    """

    cur = db.cursor()

    res = cur.execute("""
        SELECT name, value
        FROM user LEFT JOIN score ON user.rowid=user_id
        WHERE width=? AND height=? AND num_mines=?
        ORDER BY value ASC
        LIMIT 10;
    """, (width, height, num_mines))

    return list(Score(name, value) for name, value in res)
