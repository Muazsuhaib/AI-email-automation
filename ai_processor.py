import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def process_email(email_text):

    prompt = f"""
    Summarize the following business email and extract tasks.

    Email:
    {email_text}

    Output format:

    Summary:
    Tasks:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
