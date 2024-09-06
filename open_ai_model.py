import openai

template = '''
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
'''

openai.api_key = "" #OpenAI API KEY

def parse_with_openai(dom_chunks, parse_description):
    prompt = template
    
    parsed_results = []
    
    for i, chunk in enumerate(dom_chunks, start=1):
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt = prompt.format(dom_content=chunk, parse_description=parse_description)
        )
        print(f"Parse Batch {i} of {len(dom_chunks)}")
        parsed_results.append(response.choices[0].text.strip())
        
    return "\n".join(parsed_results)

