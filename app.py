import gradio as gr
from src.main import generate_translation

with gr.Blocks() as demo:
    gr.HTML("""
        <center><h1>Emoji Translator 🤗😻</h1>
        <h3>Translate any text into emojis!</h3>
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

if __name__ == "__main__":
    demo.launch(show_api=True)






