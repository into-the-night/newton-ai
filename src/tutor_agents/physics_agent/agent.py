import json

from google.adk import Agent
from . import prompt


def lookup_constants(constant: str) -> dict:
    """Returns values of physics constants
    
    Args:
        constant (str): name of the physics constants 
    
    Returns:
        dict: dict containing the value, symbol and SI unit of the constant
    """

    try:
        with open("constants.json", "r") as f:
            file = json.load(f)
            
            if constant in file["constants"]:
                return file["constants"]
            else:
                return { "error": "Constant not found in lookup" }

    except FileNotFoundError:
        # Constants file not found. Using default values.
        return {
            "speed_of_light": 299792458,
            "gravitational_constant": 6.6743e-11
        }


physics_agent = Agent(
    model="gemini-2.0-flash",
    name="physics_tutor_agent",
    instruction=prompt.PHYSICS_TUTOR_AGENT,
    tools=[lookup_constants]
)