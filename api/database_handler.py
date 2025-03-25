import psycopg2
from psycopg2 import sql, extras
from contextlib import contextmanager
import os

class DatabaseHander:
    def __init__(self):
        self.conn_params = {
            'dbname': os.getenv('DB_NAME', 'note_application'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', 'Pass12!'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '5432')
        }

    @contextmanager
    def _get_cursor(self, cursor_type=None):
        """Context manager for safe cursor handling"""
        conn = psycopg2.connect(**self.conn_params)
        try:
            cursor_t = extras.DictCursor if cursor_type == 'dict' else None
            with conn.cursor(cursor_factory=cursor_t) as cursor:
                yield cursor
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Database operation failed: {e}")
        finally:
            conn.close()
    
    # Creates and saves a new user in the database
    def create_user(self, id, username, password):
        with self._get_cursor() as cursor:
            query = sql.SQL("INSERT INTO users (id, username, password) VALUES (%s, %s, %s)")
            cursor.execute(query, (id, username, password))
            return "created user"

    # Select all notes according to user id
    def select_by_id(self, table, record_id):
        with self._get_cursor(cursor_type='dict') as cursor:
            query = sql.SQL("SELECT * FROM {} WHERE user_id = %s").format(
                sql.Identifier(table)
            )
            cursor.execute(query, (record_id,))
            return cursor.fetchall()

    # Will get all records from entered table
    def get_all_records(self, table):
        with self._get_cursor(cursor_type='dict') as cursor:
            query = sql.SQL("SELECT * FROM {}").format(
                sql.Identifier(table)
            )
            cursor.execute(query)
            return cursor.fetchall()

    # Will get specific field from table
    def get_field_values(self, table, field):
        with self._get_cursor() as cursor:
            query = sql.SQL("SELECT {} FROM {}").format(
                sql.Identifier(field),
                sql.Identifier(table)
            )
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]