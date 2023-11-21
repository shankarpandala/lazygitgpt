import openai
import os
import json
from tqdm import tqdm
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain.output_parsers import OutputParser
llm = OpenAI()
chat_model = ChatOpenAI()
output_parser = OutputParser()

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

def generate_response(prompt, sources=read_repository_contents()):
    sources_str = json.dumps(sources, indent=4)
    messages = [HumanMessage(content=prompt + " " + sources_str)]
    response = chat_model.invoke(messages)
    parsed_response = output_parser.parse(response)
    return parsed_response
