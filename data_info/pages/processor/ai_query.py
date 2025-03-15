
api_key = "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"

from openai import OpenAI
client = OpenAI(api_key=api_key)

def chat_msg(prompt):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=prompt
        

    stream=True
    )

    reply = completion
    
    
    return reply