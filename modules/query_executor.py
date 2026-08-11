import pandas as pd
import re


def clean_sql(sql):
    """Clean AI-generated SQL before execution."""

    sql = sql.strip()

    # Remove markdown code blocks
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = sql.replace("```", "")

    sql = sql.strip()

    return sql


def is_safe_query(sql):

    sql = clean_sql(sql)
    sql_upper = sql.upper()

    # Only allow SELECT or WITH queries
    if not (sql_upper.startswith("SELECT") or sql_upper.startswith("WITH")):
        return False

    dangerous_keywords = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "ATTACH",
        "DETACH",
        "REPLACE",
        "CREATE"
    ]

    # Check for dangerous SQL commands anywhere in the query
    for keyword in dangerous_keywords:

        pattern = r"\b" + keyword + r"\b"

        if re.search(pattern, sql_upper):
            return False

    return True


def execute_query(connection, sql):

    if not sql or not sql.strip():
        raise ValueError("SQL query cannot be empty.")

    sql = clean_sql(sql)

    if not is_safe_query(sql):
        raise ValueError(
            "Only safe SELECT queries are allowed."
        )

    return pd.read_sql_query(sql, connection)
