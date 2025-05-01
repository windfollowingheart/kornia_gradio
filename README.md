<div align="center">

# kornia_gradio

</div>

[简体中文](README_CN.md)

## 1. How to use

### 1.1 Prepare
1. If you don't have conda virtual environment, create it: `conda create -n kornia_gradio python=3.9`

2. Install package: `pip install -r requirements.txt`

3. Run `main.py` file: `python main.py`

4. Open `http://localhost:7860` in your browser


### 1.2 Write config file

1. You should write config file with `*.json` extension.

2. If you want to add a filter, color or resize module, you can add a dict in the json array in the config file.

- filter example:
```json
[
    ...

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

    ...
]
```

- color example:
```json
[
    ...

    {
        "type": "color",
        "name": "rgb_to_grayscale",
        "params": {
            "rgb_weights": null
        }
    },

    ...
]
```

- resize example:
```json
[
    ...

    {
        "type": "resize",
        "params": {
            "h": 600,
            "w": 400
        }
    },

    ...
]
```
You can find examples in `examples/configs/test.json`

### 1.3 Attentions
1. You shold submit json file before submit image.

2. You should confirm the result images have the same size before calculating L1 loss or SSIM.


## 2. Supported kornia functions

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

