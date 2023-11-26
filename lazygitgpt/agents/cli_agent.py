from langchain.chains import ConversationalRetrievalChain

from lazygitgpt.llms import chat_model
from lazygitgpt.datasources.repos import read_repository_contents
from lazygitgpt.git.operations import update_files
from lazygitgpt.retrievers.retrievalqa import retriever
from lazygitgpt.memory.memory import memory

# output_schema = ResponseSchema(name='filename', description='contents', type='string')
# output_parser = StructuredOutputParser(response_schemas=[output_schema])
# format_instructions = output_parser.get_format_instructions()
# template_string = """You are an expert programmer. 
# You are reviewing a code repository.
# Read the code and make changes to the code as per the user requirements.
# user requirements: {user_requirements}
# code repository: {code_repository}
# Output the contents of the file that you changed as per the format instructions : {format_instructions}
# """

def generate_response(prompt):
    qa = ConversationalRetrievalChain.from_llm(chat_model, retriever=retriever, memory=memory)
    result = qa(prompt)
    return result["answer"]
