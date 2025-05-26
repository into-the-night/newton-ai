import ast

from google.adk import Agent
from . import prompt


def evaluate_ast_node(node):
    if isinstance(node, ast.Constant):
        return node.value
    else:
        raise ValueError("Unsupported node type")


def calculator_tool(expression: str) -> float:
    """Calculator Tool for evaluating simple mathematical expressions
    
    Args:
        expression (str): mathematical expression to be evaluated
    
    Returns:
        float: evaluated value of the expression
    """

    try:
        # Use a safe math parser or ast.literal_eval()
        # Extract the expression using regex, then parse with ast.literal_eval.  Only allow certain operators.
        expression = expression.replace("=", "") # Basic sanitization.  Don't allow assignment
        node = ast.parse(expression, mode='eval')
        if isinstance(node.body, ast.BinOp): #Binary op
            left = evaluate_ast_node(node.body.left)
            right = evaluate_ast_node(node.body.right)
            op = node.body.op

            if isinstance(op, ast.Add):
                result = left + right
            elif isinstance(op, ast.Sub):
                result = left - right
            elif isinstance(op, ast.Mult):
                result = left * right
            elif isinstance(op, ast.Div):
                result = left / right
            else:
                raise ValueError("Unsupported operator")
        elif isinstance(node.body, ast.Constant): #Constant value
            result = node.body.value
        else:
            raise ValueError("Unsupported expression")

        return result

    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


math_agent = Agent(
    model="gemini-2.0-flash",
    name="math_tutor_agent",
    instruction=prompt.MATH_TUTOR_PROMPT,
    tools=[calculator_tool]
)