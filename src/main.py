import re
from huggingface_hub import InferenceClient
import random
import time
import gradio as gr

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

system_instructions = """<s> [INST] You will be provided with text, and your task is to translate it into emojis. DO NOT USE ANY REGULAR TEXT. Do your best with emojis only. Translate this text: """



def generate_translation(prompt):
    generate_kwargs = dict(
        temperature=0.5,
        max_new_tokens=1024,
        top_p=0.95,
        repetition_penalty=1.0,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = system_instructions + prompt + "[/INST]"
    stream = client.text_generation(
        formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text

    emoji_pattern = r"[^\u0021-\u007E\u00A0-\uD7FF\uE000-\uFDCF\uFF00-\uFFEF\u10000-\u10FFFF\u0300-\u036F\u1F00-\u1F1F\u1F20-\u1F7F\u2600-\u26FF\u2700-\u27BF]+?"

    filtered_output = re.findall(emoji_pattern, output)

    return ''.join(filtered_output).replace(" ", "").replace("\n", "")



with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = generate_translation
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()

	