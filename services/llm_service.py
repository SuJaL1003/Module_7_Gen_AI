import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

# LOAD ENV VARIABLES
load_dotenv()

# CONFIGURE GEMINI API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# LOAD MODEL
model = genai.GenerativeModel(
    "gemini-pro"
)

# GENERATE SQL USING GEMINI
def generate_sql_query(prompt):

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = model.generate_content(prompt)

            if not response.text:
                return "ERROR: Empty response from Gemini"

            generated_sql = response.text.strip()

            # CLEAN OUTPUT
            generated_sql = generated_sql.replace(
                "```sql", ""
            )

            generated_sql = generated_sql.replace(
                "```", ""
            )

            generated_sql = generated_sql.strip()

            return generated_sql

        except Exception as e:

            print(f"\nAttempt {attempt + 1} failed:")
            print("ERROR:", str(e))

            time.sleep(5)

    return "ERROR: Gemini failed after 3 attempts"