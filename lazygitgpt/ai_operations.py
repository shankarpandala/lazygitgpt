import os
import json
from tqdm import tqdm
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
import re

# Set environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "lazygitgpt"
os.environ["LANGCHAIN_API_KEY"] = "ls__677090643195489ea72be5d7f03d6fbf"

chat_model = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0)
output_schema = ResponseSchema(name='filename', description='contents', type='string')
output_parser = StructuredOutputParser(response_schemas=[output_schema])
format_instructions = output_parser.get_format_instructions()
template_string = """You are an expert programmer. 
You are reviewing a code repository.
Read the code and make changes to the code as per the user requirements.
user requirements: {user_requirements}
code repository: {code_repository}
Output the contents of the file that you changed as per the format instructions : {format_instructions}
"""
# {format_instructions}
def is_text_file(filepath):
    text_file_extensions = ['.txt', '.py', '.html', '.css', '.js', '.md', '.json', '.xml']
    return os.path.splitext(filepath)[1].lower() in text_file_extensions

def read_repository_contents():
    current_directory = os.getcwd()
    file_contents_dict = {}
    file_list = os.listdir(current_directory)

    for filename in tqdm(file_list, desc="Reading files", unit="file"):
        file_path = os.path.join(current_directory, filename)

        if not is_text_file(file_path):
            continue  # Skip non-text files

        # Read file contents
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            file_contents_dict[filename] = file_contents
        except Exception as e:
            print(f"Error reading file {filename}: {e}")

    return file_contents_dict

def update_files(response):
    try:
        for filename, contents in response.items():
            file_path = os.path.join(os.getcwd(), filename)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(contents)
            
            print(f"Updated file: {filename}")
    
    except Exception as e:
        print(f"Error updating files: {e}")



def extract_json_data(data):
    json_data = re.search(r'```json(.*)```', data, re.DOTALL)
    if json_data:
        return json_data.group(1).strip()
    else:
        return None

def generate_response(prompt, sources=read_repository_contents()):
    sources_str = json.dumps(sources, indent=4)
    prompt_template = ChatPromptTemplate.from_template(template_string)
    messages = prompt_template.format_messages(user_requirements = prompt,  
                            code_repository = sources_str,
                            format_instructions=format_instructions)
    response = chat_model(messages)
    response_json = response.to_json()
    data = response_json['kwargs']['content']
    data = extract_json_data(data)
    data = json.loads(data)
    update_files(data)
    return data
