import gradio as gr
import numpy as np
import json

from  utils import *

config1 = []
config2 = []


def calc_image_1(image: np.ndarray) -> np.ndarray:
    tensor_image = image_to_tensor(image)

    output = process_image(tensor_image, config1)

    return tensor_to_image(output)

def calc_image_2(image: np.ndarray) -> np.ndarray:
    tensor_image = image_to_tensor(image)

    output = process_image(tensor_image, config2)

    return tensor_to_image(output)



def parse_json_file_1(file: gr.File) -> str:
    global config1
    try:
        # 打开并读取 JSON 文件
        with open(file.name, 'r', encoding='utf-8') as f:
            config1 = json.load(f)
        # 将解析结果转换为易读的字符串形式
        result = json.dumps(config1, indent=4, ensure_ascii=False)
        return result
    except json.JSONDecodeError:
        return "解析 JSON 文件时出错：文件格式可能不正确。"
    except Exception as e:
        return f"发生未知错误：{str(e)}"
    
def parse_json_file_2(file: gr.File) -> str:
    global config2
    try:
        # 打开并读取 JSON 文件
        with open(file.name, 'r', encoding='utf-8') as f:
            config2 = json.load(f)
        # 将解析结果转换为易读的字符串形式
        result = json.dumps(config1, indent=4, ensure_ascii=False)
        return result
    except json.JSONDecodeError:
        return "解析 JSON 文件时出错：文件格式可能不正确。"
    except Exception as e:
        return f"发生未知错误：{str(e)}"
    
def clear_image() -> tuple[None, None]:
    return None, None

def clear_file() -> tuple[None, None]:
    return None, None

def clear_text() -> None:
    return None


# 创建 Gradio 界面
with gr.Blocks() as demo:
    with gr.Column():
        with gr.Row():
            with gr.Column():
                image1 = gr.Image(label="Original Image")
                with gr.Row():
                    image1_button1 = gr.Button("submit")
                    image1_button2 = gr.Button("clear")
                    
            with gr.Column():
                file1 = gr.File(label="JSON File", type="filepath",  file_types=[".json"])
                with gr.Row():
                    file1_button1 = gr.Button("submit")
                    file1_button2 = gr.Button("clear")
                file1_parse_result_text = gr.Textbox(label="Parse Result", max_lines=7)
            with gr.Column():
                res_image1 = gr.Image(label="Result Image")
            
            image1_button1.click(fn=calc_image_1, inputs=image1, outputs=res_image1)
            image1_button2.click(fn=clear_image, inputs=None, outputs=[image1, res_image1])
            file1_button1.click(fn=parse_json_file_1, inputs=file1, outputs=file1_parse_result_text)
            file1_button2.click(fn=clear_file, inputs=None, outputs=[file1, file1_parse_result_text])

        with gr.Row():
            with gr.Column():
                image2 = gr.Image(label="Original Image")
                with gr.Row():
                    image2_button1 = gr.Button("submit")
                    image2_button2 = gr.Button("clear")
                    
            with gr.Column():
                file2 = gr.File(label="JSON File", type="filepath",  file_types=[".json"])
                with gr.Row():
                    file2_button1 = gr.Button("submit")
                    file2_button2 = gr.Button("clear")
                file2_parse_result_text = gr.Textbox(label="Parse Result", max_lines=7)
            with gr.Column():
                res_image2 = gr.Image(label="Result Image")
            
            image2_button1.click(fn=calc_image_2, inputs=image2, outputs=res_image2)
            image2_button2.click(fn=clear_image, inputs=None, outputs=[image2, res_image2])
            file2_button1.click(fn=parse_json_file_2, inputs=file2, outputs=file2_parse_result_text)
            file2_button2.click(fn=clear_file, inputs=None, outputs=[file2, file2_parse_result_text])

        with gr.Row():
            with gr.Column():
                l1_loss_text = gr.Textbox(label="L1 Loss")
                with gr.Row():
                    l1_loss_button1 = gr.Button("calculate")
                    l1_loss_button2 = gr.Button("clear")

                    l1_loss_button1.click(fn=calc_L1, inputs=[res_image1, res_image2], outputs=l1_loss_text)
                    l1_loss_button2.click(fn=clear_text, inputs=None, outputs=l1_loss_text)
                    
            with gr.Column():
                SSIM_loss_text = gr.Textbox(label="SSIM Loss")
                with gr.Row():
                    SSIM_loss_button1 = gr.Button("calculate")
                    SSIM_loss_button2 = gr.Button("clear")

                    SSIM_loss_button1.click(fn=calc_SSIM, inputs=[res_image1, res_image2], outputs=SSIM_loss_text)
                    SSIM_loss_button2.click(fn=clear_text, inputs=None, outputs=SSIM_loss_text)
                

demo.launch(server_port=7860, share=False)




    