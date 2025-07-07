import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def process_comments(text):
    system_prompt = """
You are a kind and constructive assistant. Given a list of course evaluation comments from students, do the following:
1. Filter out any comments that are mean, hurtful, or unhelpful.
2. Summarize the remaining comments into a few key points, phrased in a kind and productive tone.
3. Highlight any positive or supportive comments exactly as they were written.
Return the response in the following format:
- Summary: ...
- Kind Comments: ...
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ],
        temperature=0.5
    )

    return response['choices'][0]['message']['content']
