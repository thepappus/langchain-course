from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub 
from langchain_classic.agents import create_react_agent 
from langchain_classic.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools,verbose=True)
chain = agent_executor

def main():
    print("Hello from react-search-agent!")
    result = chain.invoke({"input": "What is the weather in Dunnedin, new Zealand?"})
    print(result)


if __name__ == "__main__":
    main()
