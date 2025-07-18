from langchain.chat_models import init_chat_model
from langchain.agents import initialize_agent
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import datetime
from langchain.agents import tool

@tool
def get_current_date(text: str) -> str:
    '''
    This function gives the current date and time, refer this when you need date
    '''
    return datetime.datetime.now()


# Load env vars
load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

# Initialize model with API key
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

#initiating model with Gemini 
#model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

agent = initialize_agent(tools = [get_current_date], llm = model, verbose = True, agent = "zero-shot-react-description")
agent.invoke("what is the current date")
