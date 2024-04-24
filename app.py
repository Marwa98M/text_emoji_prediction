import gradio as gr
from src.main import generate_translation


with gr.Blocks() as demo:
    radio = gr.Radio(["English", "Arabic"], container=False)
    
    html = gr.HTML("""
        <center><h1>Emoji Translator 🤗😻</h1>
        <h3>Translate any text into emojis!</h3>
        </center>
    """, visible=True)
    
    html_ar = gr.HTML("""
        <center><h1>🤗😻 مترجم الإيموجي</h1>
        <h3>!ترجم أي نص لإيموجي</h3>
        </center>
    """, visible=False)
    
    markdown = gr.Markdown("""
        # Text to Emoji 📖➡️😻
    """, visible=True)
    
    markdown_ar = gr.Markdown("""
        # نص إلى إيموجي 📖➡️😻
    """, visible=False, rtl=True)
        
    with gr.Row():
        text_uesr_input = gr.Textbox(label="Enter text 📚", visible=True)
        output = gr.Textbox(label="Translation", visible=True)
    with gr.Row():
        translate_btn = gr.Button("Translate 🚀", visible=True)
        translate_btn.click(fn=generate_translation, inputs=text_uesr_input,
                            outputs=output, api_name="translate_text")
        
    with gr.Row():
        text_uesr_input_ar = gr.Textbox(label="📚اكتب النص", visible=False)
        output_ar = gr.Textbox(label="ترجمة", visible=False, rtl=False)
    with gr.Row():
        translate_btn_ar = gr.Button("ترجم 🚀", visible=False)
        translate_btn_ar.click(fn=generate_translation, inputs=text_uesr_input,
                            outputs=output, api_name="translate_text")

    def update_visibility(radio):  # Accept the event argument, even if not used
        value = radio  # Get the selected value from the radio button
        if value == "English":
            html.visible = True
            markdown.visible = True
            text_uesr_input.visible = True
            output.visible = True
            translate_btn.visible = True
            html_ar.visible = False
            markdown_ar.visible = False
            text_uesr_input_ar.visible = False
            output_ar.visible = False
            translate_btn_ar.visible = False
        else:
            html.visible = False
            markdown.visible = False
            text_uesr_input.visible = False
            output.visible = False
            translate_btn.visible = False
            html_ar.visible = True
            markdown_ar.visible = True
            text_uesr_input_ar.visible = True
            output_ar.visible = True
            translate_btn_ar.visible = True
        
        
    radio.change(update_visibility, radio)
    
    
    
if __name__ == "__main__":
    demo.launch(show_api=True)





# with gr.Blocks() as demo:
#     gr.HTML("""
#         <center><h1>Emoji Translator 🤗😻</h1>
#         <h3>Translate any text into emojis!</h3>
#         </center>
#     """)
    
#     chatbot = gr.Chatbot([]) 
#     msg = gr.Textbox(label="Enter text 📚") 

#     # def respond(message, chat_history):
#     #     bot_message = generate_translation(msg) 
#     #     chat_history.append((message, bot_message))
#     #     time.sleep(2)
#     #     return "", chat_history

#     with gr.Row():
#         translate_btn = gr.Button("Translate 🚀")
#         translate_btn.click(fn=generate_translation, inputs=msg,
#                             outputs=chatbot)
    
#     clear = gr.ClearButton([msg, chatbot])

#    # msg.submit(respond, [msg, chatbot], [msg, chatbot])

# if __name__ == "__main__":
#     demo.launch(share=True)