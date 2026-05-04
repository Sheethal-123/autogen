from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model='llama-3.3-70b-versatile',
        api_key=api_key,
        base_url='https://api.groq.com/openai/v1',
        model_info=ModelInfo(
            vision=False,
            function_calling=True,
            json_output=True,
            family="unknown",
            structured_output=False,
        )
    )
    return openai_model_client