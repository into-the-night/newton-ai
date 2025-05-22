class TutorAgent:
    def __init__(self, math_agent, physics_agent):
        self.math_agent = math_agent
        self.physics_agent = physics_agent

    def process_query(self, query):
        subject = self.determine_subject(query)
        if subject == "Math":
            response = self.math_agent.receive_query(query)
        elif subject == "Physics":
            response = self.physics_agent.receive_query(query)
        else:
            response = "Sorry, I'm not sure which subject this question belongs to."

        return response

    def determine_subject(self, query):
        # Simple keyword matching (can be replaced with Gemini API intent classification)
        if any(keyword in query.lower() for keyword in ["calculate", "equation", "solve", "+", "-", "*", "/"]):
            return "Math"
        elif any(keyword in query.lower() for keyword in ["newton", "force", "velocity", "speed", "acceleration"]):
            return "Physics"
        else:
            return "Unknown"