from openai import OpenAI
import json

client = OpenAI(
    base_url="https://api.gapgpt.app/v1",
    api_key="sk-jbFGerGnNrJsPeKPwnMPBi4pLmSq0FqWPPzQalRDQUA1NDCZ"
)

def analyze_essay(text):

    prompt = f"""
You are a senior IELTS Writing Task 2 examiner.

Evaluate the essay according to IELTS criteria.

Return ONLY valid JSON.

JSON format:

{{
  "word_count": 0,
  "overall_band": 0,
  "task_response": {{
    "score": 0,
    "feedback": ""
  }},
  "coherence_cohesion": {{
    "score": 0,
    "feedback": ""
  }},
  "lexical_resource": {{
    "score": 0,
    "feedback": ""
  }},
  "grammar_accuracy": {{
    "score": 0,
    "feedback": ""
  }},
  "errors": {{
    "grammar": [],
    "vocabulary": [],
    "spelling": [],
    "punctuation": [],
    "structure": []
  }},
  "recommendations": [],
  "improved_essay": "",
  "sample_band_8_essay": ""
}}

Rules:
- Be strict.
- Score like a real IELTS examiner.
- If word count exceeds 320, mention it.
- Return JSON only.

Essay:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": "You are an expert IELTS Writing examiner."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
