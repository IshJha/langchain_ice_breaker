import os

import langchain.prompts
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]


def lookup(name:str):
    llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key="<your-api-key>")

    template="Given a full name {name} search the web and get the Linkedin profile page  url. Your output should only be a linkedin profile URL."
    prompt_template=PromptTemplate(input_variables=["name"],template=template)
    tool_for_agent=[
        Tool(
            name="Search google 4 Linkedin ptofie url",
            func=get_profile_url_tavily,
            description="useful when linkedin profile url is required"
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tool_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tool_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == "__main__":
    print(lookup(name="Ish Jha Tcs Research"))