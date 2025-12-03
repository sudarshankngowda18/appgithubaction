import gradio as gr
import requests

def calculate_ui(a, b, operation):
    response = requests.post("http://127.0.0.1:5000/calculate",
                             json={"a": a, "b": b, "operation": operation})
    return response.json().get("result")

iface = gr.Interface(
    fn=calculate_ui,
    inputs=[gr.Number(label="a"), gr.Number(label="b"), gr.Radio(["add", "sub"], label="Operation")],
    outputs="text",
    title="Simple Calculator"
)

# Launch on a fixed port
if __name__ == "__main__":

    iface.launch(server_port=7860)

# TO  CLOSE THE PORT RUN BELOW TWO COMMANDS IN COMMAND PROMPT
# netstat -ano | findstr 7860
# taskkill /PID <pid> /F # ENTER LISTENING NUMBER



