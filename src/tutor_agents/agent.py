from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .math_agent import math_agent
from .physics_agent import physics_agent


master_tutor = LlmAgent(
    name="master_tutor",
    model="gemini-2.0-flash",
    description=(
        "analyzing user queries"
        "assigning subject-specific agents related to the query"
        "to help the user develop a better understanding of that specific topic"
    ),
    instruction=prompt.MASTER_TUTOR_PROMPT,
    output_key="answer",
    tools=[
        AgentTool(agent=math_agent),
        AgentTool(agent=physics_agent),
    ],
)

root_agent = master_tutor