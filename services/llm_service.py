import google.generativeai as genai
from dotenv import load_dotenv
import os

# LOAD ENV VARIABLES
load_dotenv()

# CONFIGURE GEMINI API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# LOAD MODEL
model = genai.GenerativeModel(
    "gemini-1.5-pro"
)


# GENERATE SQL USING GEMINI
def generate_sql_query(prompt):

    try:

        response = model.generate_content(prompt)

        if not response.text:
            return "ERROR: Empty response from Gemini"

        generated_sql = response.text.strip()

        generated_sql = generated_sql.replace(
            "```sql", ""
        )

        generated_sql = generated_sql.replace(
            "```", ""
        )

        generated_sql = generated_sql.strip()

        return generated_sql

    except Exception as e:

        return f"ERROR: {str(e)}"
