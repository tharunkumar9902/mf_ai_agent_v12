from agents import Agent, function_tool
from app.agents.prompts import SYSTEM_PROMPT
from app.tools.mf_api import search_funds, get_nav_history


@function_tool
def search_fund_tool(query: str):
    return search_funds(query)


@function_tool
def nav_history_tool(scheme_code: str):
    return get_nav_history(scheme_code)


fund_agent = Agent(
    name="Mutual Fund Analyst",
    instructions=SYSTEM_PROMPT,
    tools=[search_fund_tool, nav_history_tool],
)