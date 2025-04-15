import google.generativeai as genai
import google.auth
from google.oauth2 import service_account
import os
from dotenv import load_dotenv
load_dotenv()
 
PATH_ENV = os.getenv("PATH_ENV")
 
credentials = service_account.Credentials.from_service_account_file(PATH_ENV)
genai.configure(credentials=credentials)
 
prompt = input("Enter the prompt: ")
 
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
response = model.generate_content(prompt)
 
print("Gemini Response:\n", response.text)