from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

# Import our state and nodes
from state import GraphState
from nodes import data_collector_node, financial_analyst_node

# Load environment variables
load_dotenv()

# --- Build the Graph ---
# Initialize the graph with our defined State structure
workflow = StateGraph(GraphState)

# 1. Add Nodes
# We register the python functions we created yesterday as nodes in the graph
workflow.add_node("data_collector", data_collector_node)
workflow.add_node("financial_analyst", financial_analyst_node)

# 2. Add Edges
# Define the flow: Start -> Data Collector -> Financial Analyst -> End

# The entry point tells the graph where to start
workflow.set_entry_point("data_collector")

# After collecting data, move to the analyst
workflow.add_edge("data_collector", "financial_analyst")

# After analysis, the job is done
workflow.add_edge("financial_analyst", END)

# 3. Compile the Graph
# This creates the runnable application
app = workflow.compile()