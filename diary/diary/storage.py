import os.path as Path
import sqlite3

SQL_INSERT_TASK = '''
INSERT INTO diary (task_name, task_description, created) VALUES (?, ?, ?)
'''
SQL_UPDATE_TASK = '''
UPDATE diary SET task_name=?, task_description=? WHERE id=?
'''
SQL_UPDATE_DONE_TASK = 'UPDATE diary SET task_ready="done" WHERE id=?'
SQL_UPDATE_UNDONE_TASK = 'UPDATE diary SET task_ready="undone" WHERE id=?'
SQL_UPDATE_DESCRIPTION = '''
    UPDATE diary SET task_description=? WHERE id=?
'''

SQL_SELECT_ALL = '''
    SELECT
        id, task_name, task_description, task_ready, created
    FROM
        diary
'''
SQL_SELECT_TASK_BY_NAME = SQL_SELECT_ALL + ' WHERE task_name=?'
SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'
SQL_SELECT_DESCRIPTION_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'


# def connect(db_name=':memory:'):
def connect(db_name=None):
    """Выполняет подключение к БД"""
    if db_name is None:
        db_name = ':memory:' # Мемори сохраняет в RAM

    conn = sqlite3.connect(db_name)

    return conn

def initialize(conn):
    """Инициализирует структуру БД."""
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')

    with conn, open(script_path) as f:
        conn.executescript(f.read())


def add_task(conn, task, description, dtl):
    """Добавляет задачу"""
    if not task:
        raise RuntimeError("Task can't be empty.")

    with conn:

        cursor = conn.execute(SQL_INSERT_TASK, (task, description, dtl))


def edit_task(conn, task, description, id):
    if not task:
        raise RuntimeError("Task can't be empty.")

    with conn:
        cursor = conn.cursor()
        cursor.execute(SQL_UPDATE_TASK, (task, description, id,))


def done_task(conn, id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(SQL_UPDATE_DONE_TASK, (id,))

def undone_task(conn, id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(SQL_UPDATE_UNDONE_TASK, (id,))



def find_task_by_pk(conn, pk):
    """Возвращает URL-адрес по первичному ключу."""
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
        return cursor.fetchone()


def find_description_by_pk(conn, pk):
    """Возвращает URL-адрес по первичному ключу."""
    with conn:
        cursor = conn.execute(SQL_SELECT_DESCRIPTION_BY_PK, (pk,))
        return cursor.fetchone()


def find_all(conn):
    """Возвращает все задачи из БД"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
