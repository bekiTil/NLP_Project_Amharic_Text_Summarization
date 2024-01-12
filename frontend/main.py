import gradio as gr
import requests

BACKEND_URL = "http://localhost:8000/items"


def respond(msg: str, history: list):
    response = requests.post(BACKEND_URL, json={"text": msg})
    history.append((msg, response.json()[-1]["text"]))
    return "", history


def main():
    with gr.Blocks(title="QA Chatbot") as interface:
        chatbot = gr.Chatbot(height=600)
        msg = gr.Textbox(label="Question")

        btn = gr.Button("Ask")

        clear_btn = gr.ClearButton(
            components=[msg, chatbot], value="Delete chat history"
        )

        btn.click(
            respond,
            inputs=[msg, chatbot],
            outputs=[msg, chatbot],
        )
        msg.submit(
            respond,
            inputs=[msg, chatbot],
            outputs=[msg, chatbot],
        )

    gr.close_all()

    interface.launch()


if __name__ == "__main__":  # written by D.J
    main()
