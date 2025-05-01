<div align="center">

# kornia_gradio

</div>

[English](README.md)

## 1. 如何使用

### 1.1 准备工作
1. 如果你没有 Conda 虚拟环境，请创建它：`conda create -n kornia_gradio python=3.9`, 然后激活该环境：`conda activate kornia_gradio`

2. 安装软件包：`pip install -r requirements.txt`

3. 运行 `main.py` 文件：`python main.py`

4. 在你的浏览器中打开 `http://localhost:7860`


### 1.2 编写配置文件
1. 你应该编写扩展名为 `*.json` 的配置文件。

2. 如果你想添加滤镜、颜色处理或调整大小的模块，你可以在配置文件的 JSON 数组中添加一个字典。

- 滤镜示例：
```json
[

    {
        "type": "filter",
        "name": "bilateral_blur",
        "params": {
            "kernel_size": [3, 3],
            "sigma_color": 0.1,
            "sigma_space": [1.5, 1.5],
            "border_type": "reflect",
            "color_distance_type": "l1"
        }
    },

]
```

- 颜色处理示例：
```json
[

    {
        "type": "color",
        "name": "rgb_to_grayscale",
        "params": {
            "rgb_weights": null
        }
    },

]
```

- 调整大小示例：
```json
[


    {
        "type": "resize",
        "params": {
            "h": 600,
            "w": 400
        }
    },


]
```
你可以在 `examples/configs/test.json` 中找到示例。模块执行的顺序和配置文件中的字典顺序一致。

### 1.3 注意事项
1. 你应该在提交图像之前提交 JSON 文件。

2. 在计算 L1 损失或结构相似性指数（SSIM）之前，你应该确认结果图像的大小相同。


## 2. 支持的 kornia 函数

### 2.1 Filters

#### Blurring

- [bilateral_blur()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.bilateral_blur)
- [blur_pool2d()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.blur_pool2d)
- [box_blur()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.box_blur)
- [gaussian_blur2d()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.gaussian_blur2d)
- [max_blur_pool2d()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.max_blur_pool2d)
- [median_blur()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.median_blur)
- [motion_blur()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.motion_blur)
- [unsharp_mask()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.unsharp_mask)

#### Edge detection

- [canny()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.canny)
- [laplacian()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.laplacian)
- [sobel()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.sobel)
- [spatial_gradient()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.spatial_gradient)
- [spatial_gradient3d()](https://kornia.readthedocs.io/en/stable/filters.html#kornia.filters.spatial_gradient3d)

### 2.2 Color

#### Grayscale

- [rgb_to_grayscale()](https://kornia.readthedocs.io/en/stable/color.html#kornia.color.rgb_to_grayscale)
- [bgr_to_grayscale()](https://kornia.readthedocs.io/en/stable/color.html#kornia.color.bgr_to_grayscale)
- [grayscale_to_rgb()](https://kornia.readthedocs.io/en/stable/color.html#kornia.color.grayscale_to_rgb)

#### HLS

- [rgb_to_hls()](https://kornia.readthedocs.io/en/stable/color.html#kornia.color.rgb_to_hls)
- [hls_to_rgb()](https://kornia.readthedocs.io/en/stable/color.html#kornia.color.hls_to_rgb)

#### HSV

- [rgb_to_hsv()](https://kornia.readthedocs.io/en/stable/color.html#kornia.color.rgb_to_hsv)
- [hsv_to_rgb()](https://kornia.readthedocs.io/en/stable/color.html#kornia.color.hsv_to_rgb)