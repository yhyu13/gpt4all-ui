import os
import subprocess
from dearpygui.core import *
from dearpygui.simple import *

model_list = [
    "ggml-vicuna-13b-1.1-q4_0.bin", 
    "Model 2", 
    "Model 3"
]

app_process = None

def launch_app(model):
    global app_process
    if app_process is not None:
        app_process.kill()
    set_model(model)
    app_process = subprocess.Popen(["uvicorn", "--reload", "--host", "0.0.0.0", "fastapi_server:app"])


def set_model(model):
    os.environ["MODEL"] = f'/models/{model}'

def create_gui():
    with window("LLaMA"):
        add_text("LLaMA")
        add_spacing(count=5)
        add_separator()
        add_spacing(count=5)
        add_text("Select Model:")
        add_combo("##model", items=model_list, callback=set_model)
        add_spacing(count=5)
        add_button("Launch App", callback=lambda: launch_app(get_value("##model")))

if __name__ == "__main__":
    create_gui()
    start_dearpygui()