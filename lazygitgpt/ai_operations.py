import openai

def generate_response(input_text, model="text-davinci-003", max_tokens=150):
    """
    Generates a response using OpenAI's GPT-4 Turbo model based on the provided input text.

    :param input_text: The input text for the AI model.
    :param model: The model to use for generation (default is "text-davinci-003").
    :param max_tokens: The maximum number of tokens to generate (default is 150).
    :return: The generated text response from the AI model.
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=input_text,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in generating response from AI: {e}")
        return None
