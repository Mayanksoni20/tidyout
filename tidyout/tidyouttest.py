from  dotenv import load_dotenv
load_dotenv()
import sys
import os
from tidyout import tidyout


from openai import OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


response = client.chat.completions.create(model="gpt-4o",
messages=[
    {"role": "user", "content": "Translate 'My name is Aarambh' into 5 languages"}
])

print(response)

tidyout(str(response), split_content=True)
