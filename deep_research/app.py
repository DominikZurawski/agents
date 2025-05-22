import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str, recipient_email: str):
    async for chunk in ResearchManager().run(query=query, recipient_email=recipient_email):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    email_input = gr.Textbox(
        label="Send to email",
        placeholder="Enter your email address",
        type="email",
        max_lines=1,
        elem_id="email_field"
    )
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=[query_textbox, email_input], outputs=report)
    query_textbox.submit(fn=run, inputs=[query_textbox, email_input], outputs=report)

ui.launch(inbrowser=True)

