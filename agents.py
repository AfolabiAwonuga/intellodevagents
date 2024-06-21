import operator
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
from prompts import question_agent_system_prompt, solution_agent_system_prompt
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage

load_dotenv()


# Tools
search_tool = TavilySearchResults(max_results=2)


# Flow State
class FlowState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


# Question Agent
class Agenticflow:

    def __init__(self, model, tools, system=""):
        self.system = system
        graph = StateGraph(AgentState)
        graph.add_node("llm", self.call_llm)
        graph.add_node("action", self.action)
        graph.add_conditional_edges(
            "llm",
            self.decision,
            {True: "action", False: END}
        )
        graph.add_edge("action", "llm")
        graph.set_entry_point("llm")
        self.graph = graph.compile() # runnable

        self.tools = {t.name: t for t in tools} 
        self.model = model.bind_tools(tools) # let llm know tools accesable

    def call_llm(self, state: AgentState):
        messages = [SystemMessage(content=self.system)] + state["messages"]
        messages = self.model.invoke(messages)
        return {"messages": [messages]}
    
    def action(self, state: AgentState):
        tool_calls = state["messages"][-1].tool_calls
        results = []
        for t in tool_calls:
            print(f"Calling: {t}")
            response = self.tools[t["name"]].invoke(t["args"])
            results.append(ToolMessage(tool_call_id=t["id"], name=t["name"], content=str(response)))
        print("Back to the model!")
        return {"messages": results}
    
    def decision(self, state:AgentState):
        return len(state["messages"][-1].tool_calls) > 0
    


