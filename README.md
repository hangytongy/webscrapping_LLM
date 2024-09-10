# webscrapping_LLM

This code helps you to scrape a website and parse in your prompt to get the desired content that you want from the website.

### important links:

> ChromeDriver Download Link: https://googlechromelabs.github.io/chrome-for-testing/#stable
> Unzip the chromedriver and put the file into this project's folder


> Ollama Download Link: https://ollama.com/

> Ollama Github: https://github.com/ollama/ollama


### Heurist API

> should you want to use Heurist API (https://docs.heurist.ai/integration/developer-api-overview), change the following lines of code in `open_ai_model.py`

```
client = OpenAI(base_url="https://llm-gateway.heurist.xyz", api_key="your_user_id#your_api_key")

model= "mistralai/mixtral-8x7b-instruct-v0.1"
```

### to run the app

1. Create a python environment and install dependencies

```
apt update && apt install python3 python3-venv -y

cd webscrapping_LLM
python3 -m venv env

source env/bin/activate

pip install -r requirements.txt
```

2. run streamlit

```
streamlit run main.py
```

3. enjoy. copy the URL given when running the script and use the application.
