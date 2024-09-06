import streamlit as st
from bs4 import BeautifulSoup
from scrape import scrape_web, extract_body_content, clean_body_content, split_dom_content
from llm_model import parse_with_ollama
from open_ai_model import parse_with_openai
from get_all_sites import get_sites

st.title("AI Web Scraper")
url = st.text_input("Enter website URL:")

if st.button("Scrape Site"):
    st.write("Scraping website...")
    
    scrape_option = st.radio("Choose scraping method:", ["Process as Sitemap", "Process as Individual"])
    
    if scrape_option == "Process as Sitemap":
        with st.spinner("Processing sitemap..."):
            sites = get_sites(url)
            cleaned_content = []
            for site in sites:
                result = scrape_web(site)
                body_content = extract_body_content(result)
                cleaned_content.append(clean_body_content(body_content))
            cleaned_content = "\n".join(cleaned_content)
    else:  # Process as Individual
        with st.spinner("Processing individual site..."):
            result = scrape_web(url)
            body_content = extract_body_content(result)
            cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    
    st.success("Scraping completed!")
        
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
            result = parse_with_openai(dom_chunks,parse_description)
            st.write(result)
    
    
    
# to run streamlit : streamlit run main.py
