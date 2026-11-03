from openai import OpenAI

command = '''
We appreciate your message. Please reach out to our Admissions team on their whatsapp number - https://wa.me/923228449036  or call us at our UAN 0316-7773813.'''


# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
api_key = "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",
# pip install openai
 )

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are my assistant,  named Jarvis Pro Player better than the simple Jarvis."},
    {"role": "user", "content": "When will cambridge result 2024 arive?"}
  ]
)

print(completion.choices[0]. command)