import gradio as gr
from src.main import generate_translation


    
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    radio = gr.Radio(["English", "Arabic"], container=False)
    
    html = gr.HTML("""
            <center><h1>Emoji Translator 🤗😻</h1>
            <h3>Translate any text into emojis!</h3>
            </center>
            """, visible=False)
    html_ar = gr.HTML("""
        <center><h1>🤗😻 مترجم الإيموجي</h1>
        <h3>!ترجم أي نص لإيموجي</h3>
        </center>
    """, visible=False)
    
    markdown = gr.Markdown("""
        # Text to Emoji 📖➡️😻
    """, visible=False)
    
    markdown_ar = gr.Markdown("""
        # نص إلى إيموجي 📖➡️😻
    """, visible=False, rtl=True)
        
    with gr.Row(visible=False) as rowA:
        text_uesr_input = gr.Textbox(label="Enter text 📚")
        output = gr.Textbox(label="Translation")
    with gr.Row(visible=False) as rowC:
        translate_btn = gr.Button("Translate 🚀")
        translate_btn.click(fn=generate_translation, inputs=text_uesr_input,
                            outputs=output, api_name="translate_text")
        
    with gr.Row(visible=False) as rowB:
        output_ar = gr.Textbox(label="ترجمة", rtl=True)
        text_uesr_input_ar = gr.Textbox(label="📚اكتب النص", rtl=True)
    with gr.Row(visible=False) as rowD:
        translate_btn_ar = gr.Button( "🚀ترجم")
        translate_btn_ar.click(fn=generate_translation, inputs=text_uesr_input_ar,
                            outputs=output_ar, api_name="translate_text")

    def update_visibility(radio):  # Accept the event argument, even if not used
        value = radio  # Get the selected value from the radio button
        if value == "English":
            return gr.HTML(visible=True), gr.Markdown(visible=True), rowA.update(visible=True), gr.HTML(visible=False), gr.Markdown(visible=False), rowB.update(visible=False), rowC.update(visible=True), rowD.update(visible=False)

        else:
            return gr.HTML(visible=False), gr.Markdown(visible=False), rowA.update(visible=False), gr.HTML(visible=True), gr.Markdown(visible=True), rowB.update(visible=True), rowC.update(visible=False), rowD.update(visible=True)

        
    radio.change(update_visibility, radio, [html, markdown, rowA, html_ar, markdown_ar, rowB, rowC, rowD])    

    
    
    
if __name__ == "__main__":
    demo.launch(show_api=True)


