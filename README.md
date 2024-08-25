LangChain Ice Breaker
This project is designed to generate ice-breaking content about a person based on their LinkedIn profile. It leverages LangChain, Google Generative AI, and Tavily Search to fetch a LinkedIn profile, extract key information, and generate a summary along with interesting facts about the person.

Requirements
Python 3.8+
LangChain
langchain_google_genai
langchain_community
dotenv

Installation
Clone the repository:
git clone https://github.com/IshJha/langchain_ice_breaker.git
cd langchain_ice_breaker


Install the required packages using Pipenv:
pipenv install

Set up your environment variables:
Create a .env file in the root directory.
Add your Google API key:
makefile
GOOGLE_API_KEY=your-google-api-key

Activate the Pipenv shell:
pipenv shell
Usage

To run the script and fetch LinkedIn data for a specific person:
python main.py

How It Works
Name Lookup Using Tavily Search: The lookup function utilizes Tavily Search to find and return a LinkedIn profile URL based on the provided name.

React Agent Creation: A REACT agent is created using the LangChain framework, which interacts with Google Generative AI to search and validate the LinkedIn profile URL.

Profile Scraping: After obtaining the LinkedIn URL, the profile data is scraped using a custom scraper.

Prompt Generation: The scraped data is used to generate a prompt for the LLM, instructing it to produce a summary and interesting facts.

Generative AI: The Google Generative AI model processes the prompt and produces the desired output.

Output Parsing: The final output is parsed and displayed in a user-friendly format.
