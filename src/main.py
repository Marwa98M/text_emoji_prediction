import re
import gradio as gr
from huggingface_hub import InferenceClient

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


system_instructions_emoji_input = """<s> [INST] You will be provided with emojis, and your task is to create a short story from it. DO NOT USE ANY EMOJIS. Do your best with text only. Translate this emojis: """


def generate_emoji_translation(prompt):
    generate_kwargs = dict(
        temperature=0.5,
        max_new_tokens=1024,
        top_p=0.95,
        repetition_penalty=1.0,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = system_instructions_emoji_input + prompt + "[/INST]"
    stream = client.text_generation(
        formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text
    yield output.rsplit("<", 1)[0]

    return output.rsplit("<", 1)[0]


with gr.Blocks() as demo:
    gr.HTML("""
<center><h1>Emoji Translator 🤗😻</h1>
<h3>Translate any text into emojis, and vice versa!</h3>
</center>
""")

    gr.Markdown("""
# Text to Emoji 📖➡️😻
""")
    with gr.Row():
        text_uesr_input = gr.Textbox(label="Enter text 📚")
        output = gr.Textbox(label="Translation")
    with gr.Row():
        translate_btn = gr.Button("Translate 🚀")
        translate_btn.click(fn=generate_translation, inputs=text_uesr_input,
                            outputs=output, api_name="translate_text")

    gr.Markdown("""
# Emoji to Text 😻➡️📖
""")
    with gr.Row():
        emoji_user_input = gr.Textbox(label="Enter emojis 🤗")
        output = gr.Textbox(label="Translation")
    with gr.Row():
        translate_btn = gr.Button("Translate 🚀")
        translate_btn.click(fn=generate_emoji_translation, inputs=emoji_user_input,
                            outputs=output, api_name="translate_emojis")

if __name__ == "__main__":
    demo.launch(show_api=False)