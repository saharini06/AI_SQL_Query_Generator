import os
import pandas as pd
import streamlit as st


def get_database_size(db_path):
    return round(os.path.getsize(db_path) / 1024, 2)


def get_total_rows(connection, tables):

    total = 0

    for table in tables:

        result = connection.execute(
            f'SELECT COUNT(*) FROM "{table}"'
        ).fetchone()

        total += result[0]

    return total


def visualize_results(df):

    if df.empty:
        st.info("No data available for visualization.")
        return

    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    if len(numeric_columns) >= 1:

        st.subheader("📊 Data Visualization")

        selected_column = st.selectbox(
            "Select numeric column",
            numeric_columns
        )

        st.bar_chart(
            df[selected_column]
        )
