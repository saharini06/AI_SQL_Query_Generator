import streamlit as st
import tempfile
import sqlite3

def upload_database():
    uploaded_file = st.sidebar.file_uploader(
        "Upload SQLite Database",
        type=["db", "sqlite", "sqlite3"]
    )

    if uploaded_file:
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
        temp.write(uploaded_file.read())
        temp.close()
        return temp.name

    return None


def connect_database(db_path):
    return sqlite3.connect(db_path)


def get_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
    """)

    return [table[0] for table in cursor.fetchall()]
