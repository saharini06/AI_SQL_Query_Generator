# 🗄️ AI SQL Query Generator

An AI-powered application that converts natural language questions into SQL queries using Google Gemini and executes them on SQLite databases.

The application provides an interactive Streamlit interface for exploring databases, generating SQL using AI, explaining queries, suggesting optimizations, executing queries, visualizing results, and exporting data as CSV.

---
## 🚀 Live Demo

👉 **[Launch AI SQL Query Generator](https://aisqlquerygenerator-cuhae2huehc5sefbxbfzkf.streamlit.app/)**

💻 **[View Source Code on GitHub](https://github.com/saharini06/AI_SQL_Query_Generator)**

## 🔗 Project Links

- 💻 **GitHub Repository:** [AI SQL Query Generator](https://github.com/saharini06/AI_SQL_Query_Generator)
- 🚀 **Live Demo:** [Try the AI SQL Query Generator](https://aisqlquerygenerator-cuhae2huehc5sefbxbfzkf.streamlit.app/)

## 🚀 Overview

SQL is powerful, but users need to understand SQL syntax and database structures to interact with databases effectively.

The **AI SQL Query Generator** provides a natural-language interface for database interaction.

Instead of manually writing SQL, users can simply ask questions such as:

> Show the top 5 highest-paid employees.

The application uses Google Gemini to understand the question and generate an appropriate SQL query based on the selected database schema.

The generated query can then be:

- Reviewed
- Explained
- Optimized
- Validated
- Executed
- Visualized
- Downloaded as CSV

---

## ✨ Features

### 📂 Database Management

- Upload SQLite databases
- Connect to SQLite databases
- Display available tables
- View database statistics
- View table schemas
- Preview table records

### 🤖 Natural Language to SQL

- Convert English questions into SQL queries
- Generate schema-aware SQL
- Use Google Gemini for AI-powered SQL generation
- Support simple and advanced SQL queries

### 📖 SQL Explanation

- Explain generated SQL queries
- Break down complex SQL logic
- Help users understand how generated queries work

### ⚡ SQL Optimization

- Analyze generated SQL
- Provide optimization suggestions
- Suggest possible improvements to query structure

### 🔒 SQL Safety

- Validate SQL before execution
- Allow read-only SQL queries
- Block potentially destructive SQL operations
- Protect database data from accidental modification

Blocked operations include:

- DROP
- DELETE
- UPDATE
- INSERT
- ALTER
- TRUNCATE
- CREATE

### ▶️ SQL Query Execution

- Execute generated SQL queries
- Execute manually entered SQL queries
- Display results in an interactive table
- Handle invalid SQL queries gracefully

### 📊 Data Visualization

- Visualize query results
- Automatically identify numeric columns
- Generate charts from query results
- Convert database results into useful visual insights

### 📥 CSV Export

- Download query results as CSV
- Easily reuse results for further analysis

### 🕘 Query History

- Store previously generated queries
- Review previous questions
- Clear current queries
- Clear query history

### 🎨 Professional User Interface

- Clean Streamlit interface
- Dashboard-style layout
- Database statistics
- AI connection status
- Interactive tables
- Professional visual design

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Application development |
| Streamlit | Web application interface |
| SQLite | Relational database |
| pandas | Data processing and analysis |
| SQLAlchemy | Database connectivity |
| Google Gemini API | Generative AI and SQL generation |
| Git | Version control |
| GitHub | Source code management |

---

## 🏗️ Application Architecture

```text
                         USER
                           │
                           ▼
              Natural Language Question
                           │
                           ▼
                  Database Schema
                           │
                           ▼
                    Google Gemini
                           │
                           ▼
                    Generated SQL
                           │
                           ▼
                   SQL Safety Check
                           │
                           ▼
                  SQLite Database
                           │
                           ▼
                    Query Results
                     /     |      \
                    /      |       \
                   ▼       ▼        ▼
            Visualization  CSV    Explanation
                             
                         Optimization

1. Upload SQLite Database
          ↓
2. Select Database Table
          ↓
3. View Table Schema
          ↓
4. Preview Table Data
          ↓
5. Enter Natural Language Question
          ↓
6. Generate SQL using Gemini
          ↓
7. Explain SQL
          ↓
8. Optimize SQL
          ↓
9. Validate SQL
          ↓
10. Execute Query
          ↓
11. Display Results
          ↓
12. Visualize Results
          ↓
13. Download Results as CSV

1. Upload SQLite Database
          ↓
2. Select Database Table
          ↓
3. View Table Schema
          ↓
4. Preview Table Data
          ↓
5. Enter Natural Language Question
          ↓
6. Generate SQL using Gemini
          ↓
7. Explain SQL
          ↓
8. Optimize SQL
          ↓
9. Validate SQL
          ↓
10. Execute Query
          ↓
11. Display Results
          ↓
12. Visualize Results
          ↓
13. Download Results as CSV

AI_SQL_Query_Generator/
│
├── app.py
│
├── modules/
│   ├── database.py
│   ├── schema.py
│   ├── sql_generator.py
│   ├── query_executor.py
│   ├── visualizer.py
│   ├── export.py
│   └── utils.py
│
├── datasets/
│
├── assets/
│   └── screenshots/
│       ├── 01_dashboard.png
│       ├── 02_natural_language_sql.png
│       ├── 03_sql_explanation.png
│       ├── 04_sql_optimization.png
│       ├── 05_query_results.png
│       └── 06_data_visualization.png
│
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation
Step 1 — Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
Step 2 — Open the Project Folder
cd AI_SQL_Query_Generator
Step 3 — Install Dependencies
py -m pip install -r requirements.txt
🔑 Gemini API Configuration

The application uses the Google Gemini API for AI-powered SQL generation, explanation, and optimization.

Create a .env file in the project root directory:

GEMINI_API_KEY=your_api_key_here

Replace:

your_api_key_here

with your actual Gemini API key.

⚠️ Important Security Notice

Never upload your .env file or API key to GitHub.

The .gitignore file should contain:

.env
__pycache__/
*.pyc
.venv/
venv/
▶️ Running the Application

Start the Streamlit application using:

py -m streamlit run app.py

The application will open in your default web browser.

💡 Example Queries

The application supports natural language questions such as:

Basic Query
Show all employees.
Filtering
Show all employees earning more than 50000.
Sorting
Show the top 5 highest-paid employees.
Aggregation
Find the average salary of employees in each department.
Grouping
Show the number of employees in each department.
Advanced Query
Find the highest-paid employee in each department.
📊 Example Workflow
User Question
Show the top 5 highest-paid employees, including their name,
department, and salary, sorted by salary from highest to lowest.
AI Generated SQL
SELECT name, department, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;

The generated SQL can then be explained, optimized, validated, executed, visualized, and downloaded.

🔒 SQL Safety

The application includes a SQL validation layer before executing queries.

Read-only queries such as:

SELECT ...

and:

WITH ...
SELECT ...

are permitted.

Potentially destructive operations are blocked.

For example:

DROP TABLE employees;

is rejected by the application.

This provides an additional layer of protection against accidental database modification.

Note: This is an application-level safety mechanism and should not be considered a complete production database security system.

📈 Data Visualization

After executing a query, the application can visualize returned data when suitable numeric columns are available.

This allows users to move from:

Natural Language
        ↓
SQL Query
        ↓
Database Results
        ↓
Visual Insights
📥 CSV Export

Query results can be downloaded directly from the application as CSV files.

This makes it easy to:

Save results
Share results
Perform additional analysis
Use the data in spreadsheet applications
📖 SQL Explanation

The application can use AI to explain generated SQL queries in natural language.

For example, a complex query can be broken down into:

SELECT
FROM
WHERE
GROUP BY
ORDER BY
JOIN
Aggregate functions
Window functions

This makes the application useful not only as a database tool but also as an SQL learning assistant.

⚡ SQL Optimization

The AI can analyze generated queries and provide suggestions for improving query quality and performance.

Possible suggestions may include:

Avoiding unnecessary columns
Improving filtering conditions
Using appropriate indexes
Simplifying query structure
Reducing unnecessary operations
📸 Application Screenshots
🏠 Dashboard

🤖 Natural Language to SQL

📖 SQL Explanation

⚡ SQL Optimization

📊 Query Results

📈 Data Visualization

🧠 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

Generative AI
Natural Language Processing
Prompt Engineering
Large Language Model integration
SQL
SQLite
Database Management
Python
Streamlit
API Integration
Data Processing
Data Visualization
Query Validation
Error Handling
Modular Software Architecture
Git
GitHub
🎯 Project Objectives

The main objectives of this project are:

Build an AI-powered SQL assistant.
Convert natural language questions into SQL queries.
Integrate Generative AI with database systems.
Provide an easy-to-use database interface.
Execute and visualize generated queries.
Implement basic SQL safety validation.
Demonstrate modular software engineering practices.
Build a practical AI portfolio project.
💼 Real-World Applications

The concepts demonstrated by this project can be applied to:

Business intelligence tools
Data analytics platforms
Database assistants
Internal enterprise tools
SQL learning applications
Data exploration systems
AI-powered developer tools
🔮 Future Improvements

Future versions of the application could include:

💬 Conversational SQL assistant
🗃️ MySQL support
🐘 PostgreSQL support
☁️ Cloud database support
🔐 User authentication
📊 Advanced analytics dashboard
⚡ Query performance benchmarking
🧠 Automatic index recommendations
📝 Saved SQL queries
📚 Automatic database documentation
📈 Query performance history
🤖 More advanced AI database agents
📚 Learning Outcomes

This project provided practical experience in:

Building Generative AI applications
Integrating Google Gemini APIs
Prompt engineering
Natural language processing
SQL query generation
SQLite database management
Python application development
Streamlit dashboard development
Data visualization
API error handling
SQL validation
Modular software design
Git and GitHub project management
🚀 Project Highlights
Natural Language
       ↓
   Google Gemini
       ↓
   SQL Generation
       ↓
  Safety Validation
       ↓
 SQLite Database
       ↓
 Query Results
       ↓
 Visualization
       ↓
 CSV Export

The project demonstrates how Generative AI can be integrated with traditional database systems to create a more accessible way of interacting with structured data.

👩‍💻 Author

Developed as an AI portfolio project to demonstrate practical skills in:

Artificial Intelligence • Generative AI • Python • SQL • Streamlit • Database Management

⭐ Conclusion

The AI SQL Query Generator combines Generative AI, natural language processing, SQL, database management, and interactive visualization into a single application.

It provides a complete workflow from:

Natural Language → AI → SQL → Database → Results → Visualization

while maintaining a modular architecture suitable for further development and future AI capabilities.
