# regular expression 
import re 
# huggingface_hub: a repository for pre-trained models for machine learning tasks.
# InferenceClient: loading and utilizing models hosted on the Hugging Face Model Hub.
from huggingface_hub import InferenceClient 


# name of the model identifier
client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

system_instructions = """<s> [INST] You will be provided with text, and your task is to translate it into emojis. DO NOT USE ANY REGULAR TEXT. Do your best with emojis only. Translate this text: """

def generate_translation(prompt):
    # dictionary containing  parameters that control how the text is generated,
    generate_kwargs = dict( # parameters for gpt
        temperature=0.5, # Controls the randomness of the generated text
        max_new_tokens=1024, # Limits the maximum number of tokens
        top_p=0.95, # Tokens with cumulative probability above this threshold are filtered out
        repetition_penalty=1.0, # Penalizes repeating tokens in the generated text
        do_sample=True, # randomly selects the next token based on the model's probabilities.
        seed=42, # same prompt --> same output
    )

    formatted_prompt = system_instructions + prompt + "[/INST]"
    stream = client.text_generation(
        formatted_prompt, 
        **generate_kwargs, 
        stream=True, # chunks rather than all at once
        details=True, # additional details about the text generation
        return_full_text=False) # If True, generated text will be returned as a single string, rather than streamed.
    print(stream)
    
    output = ""
    for response in stream:
        output += response.token.text

    
    # Define emoji pattern
    emoji_pattern = r"[^\u0021-\u007E\u00A0-\uD7FF\uE000-\uFDCF\uFF00-\uFFEF\u10000-\u10FFFF\u0300-\u036F\u1F00-\u1F1F\u1F20-\u1F7F\u2600-\u26FF\u2700-\u27BF]+?"

    # Find emojis and non-ASCII characters
    filtered_output = re.findall(emoji_pattern, output)


    return ''.join(filtered_output).replace(" ", "").replace("\n", "")

