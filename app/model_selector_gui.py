import os
import subprocess
import dearpygui.dearpygui as dpg

model_list = [
    "ggml-vicuna-13b-1.1-q4_0.bin", 
    "Model 2", 
    "Model 3"
]

app_process = None

def launch_app(sender, data):
    global app_process
    if app_process is not None:
        app_process.kill()
    set_model(data)
    app_process = subprocess.Popen(["uvicorn", "--reload", "--host", "0.0.0.0", "fastapi_server:app"])


def set_model(model):
    print(f'{model}')
    os.environ["MODEL"] = f'/models/{model}'

def create_gui():
    global model_list
    dpg.create_context()
    dpg.create_viewport(title='gpt4all', width=800, height=400)

    with dpg.window(label="gpt4all Model Selector", width=800, height=200) as primary_window:
        dpg.add_text("LLaMA")
        dpg.add_spacing(count=2)
        dpg.add_text("Select Model:")
        dpg.add_combo(tag="##model", items=model_list, default_value=model_list[0], callback=set_model)
        dpg.add_spacing(count=5)

        dpg.add_separator()
        dpg.add_spacing(count=5)
        dpg.add_button(label="Launch App", callback=launch_app, user_data=dpg.get_value("##model"))

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(window=primary_window, value=True)

    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    create_gui()
