from openai import OpenAI
client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google."},
        {
            "role": "user",
            "content": "What is coding"
        }
    ]
)

print(completion.choices[0].message.content)