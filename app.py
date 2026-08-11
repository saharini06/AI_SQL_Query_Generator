import streamlit as st
from modules.database import upload_database, connect_database, get_tables
from modules.schema import get_schema, preview_table, get_row_count
from modules.visualizer import (
    get_database_size,
    get_total_rows,
    visualize_results
)
from modules.query_executor import execute_query
from modules.export import dataframe_to_csv
from modules.sql_generator import generate_sql, explain_sql, optimize_sql

st.set_page_config(
    page_title="AI SQL Query Generator",
    page_icon="🗄️",
    layout="wide"
)

st.markdown("""
<style>

/* Main application background */
.stApp {
    background: linear-gradient(
        135deg,
        #f8fafc 0%,
        #eef4ff 50%,
        #f8fafc 100%
    );
    color: #1e293b;
}

/* Main content */
.main {
    background: transparent;
}

/* Headings */
h1, h2, h3 {
    color: #0f172a !important;
}

/* Normal text */
p, label, span {
    color: #334155;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: #ffffff;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #dbe3ef;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #0f172a !important;
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    color: #475569 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #f1f5f9;
    border-right: 1px solid #dbe3ef;
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #1e293b !important;
}

/* Input boxes */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div {
    background-color: #ffffff !important;
    color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
}

/* SQL code box */
code {
    color: #0f172a;
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    font-weight: 600;
    border: 1px solid #cbd5e1;
}

/* Dataframes */
[data-testid="stDataFrame"] {
    background: #ffffff;
    border-radius: 10px;
}

/* Dividers */
hr {
    border-color: #dbe3ef;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(135deg, #2563eb, #0f766e);
        margin-bottom: 25px;
    ">
        <h1 style="color: white; margin-bottom: 5px;">
            🗄️ AI SQL Query Generator
        </h1>
        <p style="color: #e0f2fe; font-size: 18px; margin: 0;">
            Transform natural language into powerful SQL queries using AI
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.success("🟢 AI Engine Connected • Gemini SQL Generation Ready")
if "query_history" not in st.session_state:
    st.session_state["query_history"] = []
    
db_path = upload_database()

if db_path:

    conn = connect_database(db_path)
    tables = get_tables(conn)

    selected_table = st.sidebar.selectbox("Select Table", tables)

    st.sidebar.divider()

    st.sidebar.subheader("🕘 Query History")

    if st.session_state["query_history"]:

        for i, item in enumerate(
            reversed(st.session_state["query_history"]),
            1
        ):
            st.sidebar.write(
                f"**{i}.** {item['question']}"
            )

    else:
        st.sidebar.info("No queries yet.")

    st.sidebar.divider()

    if st.sidebar.button("🧹 Clear Current Query"):

        st.session_state.pop("generated_sql", None)
        st.session_state.pop("explanation", None)
        st.session_state.pop("optimization", None)

        st.rerun()


    if st.sidebar.button("🗑️ Clear Query History"):
 
        st.session_state["query_history"] = []

        st.rerun()

    col1, col2, col3 = st.columns(3)
    col1.metric("Tables", len(tables))
    col2.metric("Rows", get_total_rows(conn, tables))
    col3.metric("Size (KB)", get_database_size(db_path))

    st.divider()

    st.subheader("Schema")
    st.dataframe(get_schema(conn, selected_table), use_container_width=True)

    st.subheader("Preview")
    st.dataframe(preview_table(conn, selected_table), use_container_width=True)

    st.divider()

    st.subheader("Natural Language to SQL")

    prompt = st.text_input(
        "Ask in English",
        placeholder="Show all employees"
    )

    if st.button("Generate SQL"):

        if not prompt.strip():
            st.warning("⚠️ Please enter a question first.")

        else:

            try:

                schema = get_schema(conn, selected_table)

                sql = generate_sql(
                    prompt,
                    schema.to_string(index=False)
                )

                if not sql.strip():
                    st.error("❌ No SQL query was generated.")

                else:

                    st.session_state["generated_sql"] = sql

                    st.session_state["query_history"].append({
                        "question": prompt,
                        "sql": sql
                    })

                    st.success("✅ SQL generated successfully!")

            except Exception as e:

                st.error(
                    "❌ Unable to generate SQL. "
                    "Please check your question or try again."
                )


    sql = st.session_state.get("generated_sql", "")

    if sql:

        st.subheader("Generated SQL")

        st.code(sql, language="sql")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("📖 Explain SQL"):

                explanation = explain_sql(sql)

                st.session_state["explanation"] = explanation

        with col2:
            if st.button("⚡ Optimize SQL"):

                optimization = optimize_sql(sql)

                st.session_state["optimization"] = optimization

        if "explanation" in st.session_state:

            st.subheader("📖 SQL Explanation")

            st.write(st.session_state["explanation"])

        if "optimization" in st.session_state:

            st.subheader("⚡ Optimization Suggestions")

            st.write(st.session_state["optimization"])

    st.divider()

    st.subheader("SQL Query Executor")

    sql_query = st.text_area(
        "Enter SQL Query",
        value=st.session_state.get("generated_sql", ""),
        height=180
    )

    if st.button("Execute Query"):

        try:
            result = execute_query(conn, sql_query)

            st.success("Query Executed Successfully")

            st.dataframe(result, use_container_width=True)

            visualize_results(result)

            st.download_button(
                "Download CSV",
                dataframe_to_csv(result),
                "query_result.csv",
                "text/csv"
            )

        except Exception as e:

            st.error("❌ Unable to execute the query.")

            with st.expander("View error details"):
                st.code(str(e))

    conn.close()

else:
    st.info("Upload a SQLite database.")
