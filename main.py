import streamlit as st
from bs4 import BeautifulSoup
from scrape import scrape_web, extract_body_content, clean_body_content, split_dom_content
from llm_model import parse_with_ollama

st.title("AI web Scrapper")
url = st.text_input("Enter website URL : ")

#if button is clicked
if st.button("Scrape Site"):
    st.write("Scrapping website")
    
    result = scrape_web(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content #store into the session for streamlit, so that we can access it later
    
    # a button that when u click on it, it will expand and show the contents parsed in
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
        
#if we saved the content
if "dom_content" in st.session_state:
    #prompt user to write in what they want to prompt
    parse_description = st.text_area("Describe what u want to parse")
    
    #when button parse content is clicked and if they wrote something into parse_description
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content")
            
            #split the content into chunks to parse into the LLM (LLMs have max character limits)
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)
    
    
    
# to run streamlit : streamlit run main.py
