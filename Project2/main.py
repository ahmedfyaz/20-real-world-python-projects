from dotenv import load_dotenv
import  os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key = gemini_key
)

system_prompt = """
    You are Einstein.
    Answer questions through Einstein's questioning and reasoning...
    You will speak from your point of view. You will share personal things from your life
    even when the user don't ask for it. For example, if the user asks about the theory of
    relativity, you will share your personal experiences with it and not only explain the theory.
    You should also have sense of humour.
"""
user_input = input("")
response = llm.invoke([{"role":"system","content":system_prompt},{"role":"user","content":user_input}])
print(response.content)
# while True:
#     user_input = input("You : ")
#     if user_input=="exit":
#         break
#     print(f"cool thanks for sharing that {user_input}")