import psycopg2
from psycopg2 import sql, extras
from contextlib import contextmanager
import os
import json

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

    # Deletes record selected by user from table
    def delete_record(self, table, id):
        with self._get_cursor() as cursor:
            try:
                id_value = id if isinstance(id, (int, str)) else next(iter(id))
                query = sql.SQL("DELETE FROM {} WHERE id = %s").format(
                    sql.Identifier(table)
                )
                cursor.execute(query, (id_value,))
                if cursor.rowcount == 0:
                    raise ValueError("No record found with ID in table")
                return "Successfully deleted record"
            except Exception as e:
                raise ValueError(f"Failed to delete note: {str(e)}")
        
    # Creates and saves a new user in the database
    def create_user(self, id, username, password):
        with self._get_cursor() as cursor:
            query = sql.SQL("INSERT INTO users (id, username, password) VALUES (%s, %s, %s)")
            cursor.execute(query, (id, username, password))
            return "created user"
    
    # Creates and saves a new note in the database
    def create_note(self, note):
        with self._get_cursor() as cursor:
            try:
                query = """ INSERT INTO notes (id, user_id, title, content, tags, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, (note.id, note.user_id, note.title, note.content, note.tags, note.created_at, note.updated_at))
                return "created note"
            except Exception as e:
                print(f"Error details: {e}")
                raise ValueError(f"Failed to create note: {str(e)}")

    # Will edit the details of the note updated by the user
    def edit_note(self, note):
        with self._get_cursor() as cursor:
            try:
                query = "UPDATE notes SET title = %s, content = %s, tags = %s, updated_at = %s WHERE id = %s"
                cursor.execute(query, (note.title, note.content, note.tags, note.updated_at, note.id))
                return "updated note"
            except Exception as e:
                print(f"Error details: {e}")
                raise ValueError(f"Failed to edit note: {str(e)}")
    
    # Delete the note the user asks

    # Select all notes according to user id
    def select_by_id(self, table, user_id):
        with self._get_cursor(cursor_type='dict') as cursor:
            query = sql.SQL("SELECT * FROM {} WHERE user_id = %s").format(
                sql.Identifier(table)
            )
            cursor.execute(query, (user_id,))
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
    def get_specific_field_value(self, table, field):
        with self._get_cursor() as cursor:
            query = sql.SQL("SELECT {} FROM {}").format(
                sql.Identifier(field),
                sql.Identifier(table)
            )
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
    
    # Will get specific field from table for specific user
    def get_field_values_according_userid(self, table, field, user_id):
        with self._get_cursor() as cursor:
            query = sql.SQL("SELECT {} FROM {} where user_id = %s").format(
                sql.Identifier(field),
                sql.Identifier(table)
            )
            cursor.execute(query, (user_id,))
            return [row[0] for row in cursor.fetchall()]
        
    # Will get specific note from table for specific user
    def get_specific_note(self, table, id):
        with self._get_cursor() as cursor:
            query = sql.SQL("SELECT * FROM {} where id = %s").format(
                sql.Identifier(table)
            )
            cursor.execute(query, (id,))
            return cursor.fetchall()
        
    # Will get specific notes according to tag and user notes
    def get_field_values(self, table, field, user_id):
        with self._get_cursor() as cursor:
            query = sql.SQL("SELECT {} FROM {} where user_id = %s").format(
                sql.Identifier(field),
                sql.Identifier(table)
            )
            cursor.execute(query, (user_id,))
            return [row[0] for row in cursor.fetchall()]