from autogen_agentchat.agents import AssistantAgent
from agents.prompts.DataAnalyzerAgentPrompt import DATA_ANALYZER_MSG

def getDataAnalyzerAgent(model_client, data_filename='data.csv'):
    data_analyzer_agent = AssistantAgent(
        name='Data_Analyzer_Agent',
        description='An agent which helps with solving Data Analysis tasks and gives the code as well.',
        model_client=model_client,
        system_message=DATA_ANALYZER_MSG.format(data_filename=data_filename),
    )
    return data_analyzer_agent