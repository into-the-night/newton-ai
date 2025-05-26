import json

from google.adk import Agent
from . import prompt


def lookup_constants(query: str) -> dict:
    """Dynamically searches for a physics constant by name or symbol (case-insensitive, partial match).

    Args:
        query (str): Name, symbol, or partial name of the physics constant.

    Returns:
        dict: The best-matching constant's details, or an error message.
    """
    try:
        with open("constants.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            constants = data.get("constants", [])
            
            # Normalize query
            q = query.strip().lower()

            # Try exact match on name or symbol
            for c in constants:
                if q == c["name"].strip().lower() or q == c["symbol"].strip().lower():
                    return c

            # Try partial match on name or symbol
            partial_matches = [
                c for c in constants
                if q in c["name"].strip().lower() or q in c["symbol"].strip().lower()
            ]
            if len(partial_matches) == 1:
                return partial_matches[0]
            elif len(partial_matches) > 1:
                return {
                    "error": "Multiple matches found.",
                    "matches": [{ "name": c["name"], "symbol": c["symbol"] } for c in partial_matches]
                }
            else:
                return { "error": f"No constant found matching '{query}'." }

    except FileNotFoundError:
        return { "error": "Constants file not found." }


physics_agent = Agent(
    model="gemini-2.0-flash",
    name="physics_tutor_agent",
    instruction=prompt.PHYSICS_TUTOR_AGENT,
    tools=[lookup_constants]
)