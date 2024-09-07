import google.generativeai as genai

genai.configure(api_key="") #input API KEY


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

template = '''
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
'''

def parse_with_gemini(dom_chunks, parse_description):

    prompt = template

    parsed_results = []

    for i,chunk in enumerate(dom_chunks, start=1):
        prompt = prompt.format(dom_content=chunk, parse_description=parse_description)

        response = model.generate_content(prompt)

        print(f"Parse Batch {i} of {len(dom_chunks)}")
        parsed_results.append(response.text)

        
    return "\n".join(parsed_results)