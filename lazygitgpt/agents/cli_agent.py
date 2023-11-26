import json
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
import re

from lazygitgpt.llms import chat_model
from lazygitgpt.datasources.repos import read_repository_contents
from lazygitgpt.git.operations import update_files

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

def generate_response(prompt, sources=read_repository_contents()):
    sources_str = json.dumps(sources, indent=4)
    prompt_template = ChatPromptTemplate.from_template(template_string)
    messages = prompt_template.format_messages(user_requirements = prompt,  
                            code_repository = sources_str,
                            format_instructions=format_instructions)
    response = chat_model(messages)
    response_json = response.to_json()
    data = response_json['kwargs']['content']
    return data
