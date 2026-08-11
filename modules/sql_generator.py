import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in .env file.")

client = genai.Client(api_key=api_key)


def generate_sql(prompt, schema):

    final_prompt = f"""
You are an expert SQLite SQL generator.

DATABASE SCHEMA:
{schema}

RULES:
- Generate valid SQLite SQL.
- Use only tables and columns present in the schema.
- Do not invent table or column names.
- Return ONLY the SQL query.
- Do not include explanations.
- Do not use markdown or ```.

USER REQUEST:
{prompt}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=final_prompt
    )

    return response.text.strip()


def explain_sql(sql):

    prompt = f"""
You are an expert SQL teacher.

Explain the following SQLite query in simple terms.

SQL:
{sql}

Explain:
1. What the query does
2. Which tables are used
3. Which columns are used
4. How filtering, sorting, and grouping work
5. What result the user will get

Keep the explanation clear and concise.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text.strip()


def optimize_sql(sql):

    prompt = f"""
You are an expert SQLite database optimizer.

Analyze this SQL query:

{sql}

Provide:
1. Whether the query is already efficient
2. Possible performance improvements
3. Recommended indexes, if useful
4. Any unnecessary operations
5. An improved SQL query if applicable

Keep the suggestions practical.

Do not modify the query unless an improvement is actually useful.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text.strip()
