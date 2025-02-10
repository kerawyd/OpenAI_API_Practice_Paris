
#Kaylhan Garcia
import os
from openai import OpenAI

#My API Key: API Key hhandling and client initialization
os.environ["OPENAI_API_KEY"] = "___"

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

#Testing OpenAI: Practice test.
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Say this is a test"}]
)
print(response.choices[0].message.content) #Print the responses

#The conversation history
conversation = [
    {"role": "system", 
     "content": "You are a professional travel guide designed to provide useful information about important landmarks in Paris and answer tourist questions. You are clear, concise, and professional."}, 
    {"role": "user", "content": "What is a popular landmark in Paris to see?"},
    {"role": "assistant", "content": "The most popular landmark in Paris is the Eiffel Tower."}
]

#Questions to give to OpenAI
questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum? "
]

for question in questions:
    user_dict = {"role": "user", "content": question}
    conversation.append(user_dict)
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )
    
    resp = response.choices[0].message.content
    print(resp)
    
    resp_dict = {"role": "assistant", "content": resp}
    conversation.append(resp_dict)

