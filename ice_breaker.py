
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts.prompt import  PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_url_lookup import lookup
from output_parser import summary_parser

def ice_breaker_with(name:str):
    linkedin_url=lookup(name)
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url=linkedin_url,mock=True)


    summary_template="""Given Linked information {information} about a person give: 
                  1. A short summary
                  2. two interesting facts about them 
                  /n {format_instructions}"""

    summary_prompt_template= PromptTemplate(input_variable=["information"],template=summary_template,partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        })
    api_key=os.getenv("GOOGLE_API_KEY")
    llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key="<your-api-key>") # add google api key to .env



    chain= summary_prompt_template | llm | summary_parser

    res=chain.invoke(input={"information":linkedin_data})
    print((res))

if __name__=='__main__':
    print("Entered Ice-Breaker !")
    ice_breaker_with("Ish Jha")
