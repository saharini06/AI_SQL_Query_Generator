import pandas as pd

def get_schema(connection, table_name):
    query = f"PRAGMA table_info({table_name});"
    return pd.read_sql_query(query, connection)


def preview_table(connection, table_name, limit=10):
    query = f"SELECT * FROM {table_name} LIMIT {limit};"
    return pd.read_sql_query(query, connection)


def get_row_count(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]
