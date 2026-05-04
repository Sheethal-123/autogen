from agents.Code_Executor_agent import GetCodeExecutorAgent
from agents.Data_analyzer_agent import getDataAnalyzerAgent

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination


def getDataAnalyzerTeam(docker, model_client, data_filename="data.csv"):
    code_executor_agent = GetCodeExecutorAgent(docker)

    data_analyzer_agent = getDataAnalyzerAgent(
        model_client,
        data_filename=data_filename,
    )

    # IMPORTANT:
    # Do NOT terminate when Data Analyzer says STOP.
    # Let CodeExecutor run first, then stop only when task is completed.
    termination_condition = TextMentionTermination("TASK_COMPLETE")

    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_executor_agent],
        max_turns=6,
        termination_condition=termination_condition,
    )

    return team