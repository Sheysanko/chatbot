import google.generativeai as genai
import textwrap
import re
# from IPython.display import Markdown
import pandas as pd

# read data
data = pd.read_excel("Book.xlsx")
responses = {}
for idx, row in data.iterrows():
    user_input = row['user'].lower()
    bot_response = row['bot_response']
    responses[user_input] = bot_response



# Load the pre-trained GPT-2 model and tokenizer
genai.configure(api_key="AIzaSyDgabBDp9AYhIkH86nfIm9esJxw8_31Qvw")
model = genai.GenerativeModel('gemini-pro')


def generate_response(user_input):
    response = model.generate_content(user_input)
    return response.text

def format_text(text):
    pattern = r'[>*]'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


print("chatbot: hi there! how can i help you?")
context = ""
while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        print("chatbot: goodbye!")
        break
    
    if user_input in responses:
        print(f"chatbot: {responses[user_input]}")
    else:
        bot_response = generate_response(user_input)
        print(f"Chatbot:{format_text(bot_response)}")
