import kornia
import torch


## Grayscale
def rgb_to_grayscale(image: torch.Tensor,
                    rgb_weights : torch.Tensor = None) -> torch.Tensor:
    output = kornia.color.rgb_to_grayscale(image, rgb_weights=rgb_weights)
    return output

def bgr_to_grayscale(image: torch.Tensor) -> torch.Tensor:
    output = kornia.color.bgr_to_grayscale(image)
    return output

def grayscale_to_rgb(image: torch.Tensor) -> torch.Tensor:
    output = kornia.color.grayscale_to_rgb(image)
    return output

## HLS
def rgb_to_hls(image: torch.Tensor,
               eps: float = 1e-8) -> torch.Tensor:
    output = kornia.color.rgb_to_hls(image, eps=eps)
    return output

def hls_to_rgb(image: torch.Tensor) -> torch.Tensor:
    output = kornia.color.hls_to_rgb(image)
    return output

## HSV
def rgb_to_hsv(image: torch.Tensor,
               eps: float = 1e-8) -> torch.Tensor:
    output = kornia.color.rgb_to_hsv(image, eps=eps)
    return output

def hsv_to_rgb(image: torch.Tensor) -> torch.Tensor:
    output = kornia.color.hsv_to_rgb(image)
    return output


def calc_image_color(input: torch.Tensor, color: dict) -> torch.Tensor:
    output = input

    color_name = color['name']
    color_params = color['params']

    ## Grayscale
    if color_name == "rgb_to_grayscale":
        rgb_weights = color_params['rgb_weights']
        output = rgb_to_grayscale(output, rgb_weights)
    
    elif color_name == "bgr_to_grayscale":
        output = bgr_to_grayscale(output)
    
    elif color_name == "grayscale_to_rgb":
        output = grayscale_to_rgb(output)
    
    ## HLS
    elif color_name == "rgb_to_hls":
        eps = color_params['eps']
        output = rgb_to_hls(output, eps)
        
    elif color_name == "hls_to_rgb":
        output = hls_to_rgb(output)

    ## HSV
    elif color_name == "rgb_to_hsv":
        eps = color_params['eps']
        output = rgb_to_hsv(output, eps)

    elif color_name == "hsv_to_rgb":
        output = hsv_to_rgb(output)

    else:
        raise ValueError(f"Unknown color name: {color_name}")

    # output = torch.clip(output, 0, 1) # 避免超出范围
    return output