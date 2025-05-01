import kornia
import torch


## Blurring
def bilateral_blur(input: torch.Tensor,
                kernel_size: tuple[int, int],
                sigma_color: float,
                sigma_space: tuple[float, float],
                border_type: str = 'reflect',
                color_distance_type: str = 'l1') -> torch.Tensor:
    output = kornia.filters.bilateral_blur(input, kernel_size, sigma_color, sigma_space, 
                                           border_type=border_type, color_distance_type=color_distance_type)
    return output

def blur_pool2d(input: torch.Tensor,
                kernel_size: tuple[int, int],
                stride: int = 2) -> torch.Tensor:
    output = kornia.filters.blur_pool2d(input, kernel_size, stride=stride)
    return output

def box_blur(input: torch.Tensor,
                kernel_size: tuple[int, int],
                border_type: str = 'reflect',
                separable: bool = False) -> torch.Tensor:
    output = kornia.filters.box_blur(input, kernel_size, border_type=border_type, separable=separable)
    return output

def gaussian_blur2d(input: torch.Tensor,
                    kernel_size: tuple[int, int],
                    sigma: tuple[float, float],
                    border_type: str = 'reflect',
                    separable: bool = True) -> torch.Tensor:
    output = kornia.filters.gaussian_blur2d(input, kernel_size, sigma, border_type=border_type, separable=separable)
    return output

def guided_blur(guidance: torch.Tensor,
                input: torch.Tensor,
                kernel_size: tuple[int, int],
                eps: float,
                border_type: str = 'reflect',
                subsample: int = 1) -> torch.Tensor:
    output = kornia.filters.guided_blur(guidance, input, kernel_size, eps, border_type=border_type, subsample=subsample)
    return output

def joint_bilateral_blur(input: torch.Tensor,
                guidance: torch.Tensor,
                kernel_size: tuple[int, int],
                sigma_color: float,
                sigma_space: tuple[float, float],
                border_type: str = 'reflect',
                color_distance_type: str = 'l1') -> torch.Tensor:
    output = kornia.filters.joint_bilateral_blur(input, guidance, kernel_size, sigma_color, sigma_space, 
                                                 border_type=border_type, color_distance_type=color_distance_type)
    return output

def max_blur_pool2d(input: torch.Tensor,
                    kernel_size: tuple[int, int],
                    stride: int = 2,
                    max_pool_size: int = 2,
                    ceil_mode: bool = False) -> torch.Tensor:
    output = kornia.filters.max_blur_pool2d(input, kernel_size, stride=stride, max_pool_size=max_pool_size, ceil_mode=ceil_mode)
    return output

def median_blur(input: torch.Tensor,
                    kernel_size: tuple[int, int]) -> torch.Tensor:
    output = kornia.filters.median_blur(input, kernel_size)
    return output

def motion_blur(input: torch.Tensor,
                    kernel_size: tuple[int, int],
                    angle: float,
                    direction: float,
                    border_type: str = 'reflect',
                    mode: str = 'nearest') -> torch.Tensor:
    output = kornia.filters.motion_blur(input, kernel_size, angle, direction, border_type=border_type, mode=mode)
    return output

def unsharp_mask(input: torch.Tensor,
                    kernel_size: tuple[int, int],
                    sigma: tuple[float, float],
                    border_type: str = 'reflect') -> torch.Tensor:
    output = kornia.filters.unsharp_mask(input, kernel_size, sigma, border_type=border_type)
    return output


## Edge detection

def canny(input: torch.Tensor,
            low_threshold: float = 0.1,
            high_threshold: float = 0.2,
            kernel_size: tuple[int, int] = (5, 5),
            sigma: tuple[float, float] = (1, 1),
            hysteresis: bool = True,
            eps: float = 1e-6) -> torch.Tensor:
    output = kornia.filters.canny(input, low_threshold=low_threshold, high_threshold=high_threshold, 
                                  kernel_size=kernel_size, sigma=sigma, hysteresis=hysteresis, eps=eps)
    return output

def laplacian(input: torch.Tensor,
                kernel_size: tuple[int, int],
                border_type: str = 'reflect',
                normalized: bool = True) -> torch.Tensor:
    output = kornia.filters.laplacian(input, kernel_size, border_type=border_type, normalized=normalized)
    return output

def sobel(input: torch.Tensor,
            normalized: bool = True,
            eps: float = 1e-6) -> torch.Tensor:
    output = kornia.filters.sobel(input, normalized=normalized, eps=eps)
    return output

def spatial_gradient(input: torch.Tensor,
            mode: str = 'sobel',
            order: int = 1,
            normalized: bool = True) -> torch.Tensor:
    output = kornia.filters.spatial_gradient(input, mode=mode, order=order, normalized=normalized)
    return output

def spatial_gradient3d(input: torch.Tensor,
            mode: str = 'diff',
            order: int = 1) -> torch.Tensor:
    output = kornia.filters.spatial_gradient3d(input, mode=mode, order=order)
    return output




def calc_image_filter(input: torch.Tensor, filter: dict) -> torch.Tensor:
    output = input

    filter_name = filter['name']
    filter_params = filter['params']

    if filter_name == "bilateral_blur":
        kernel_size = tuple(filter_params['kernel_size'])
        sigma_color = filter_params['sigma_color']
        sigma_space = tuple(filter_params['sigma_space'])
        border_type = filter_params['border_type']
        color_distance_type = filter_params['color_distance_type']
        output = bilateral_blur(output, kernel_size, sigma_color, sigma_space, border_type, color_distance_type)
    
    elif  filter_name == "blur_pool2d":
        kernel_size = tuple(filter_params['kernel_size'])
        stride = filter_params['stride']
        output = blur_pool2d(output, kernel_size, stride)
    
    elif filter_name == "box_blur":
        kernel_size = tuple(filter_params['kernel_size'])
        border_type = filter_params['border_type']
        separable = filter_params['separable']
        output = box_blur(output, kernel_size, border_type, separable)
    
    elif filter_name == "gaussian_blur2d":
        kernel_size = tuple(filter_params['kernel_size'])
        sigma = tuple(filter_params['sigma'])
        border_type = filter_params['border_type']
        separable = filter_params['separable']
        output = gaussian_blur2d(output, kernel_size, sigma, border_type, separable)
    
    elif filter_name == "guided_blur":
        pass

    elif filter_name == "joint_bilateral_blur":
        pass

    elif filter_name == "max_blur_pool2d":
        # kernel_size = tuple(filter_params['kernel_size'])
        kernel_size = tuple(filter_params['kernel_size'])
        stride = filter_params['stride']
        max_pool_size = filter_params['max_pool_size']
        ceil_mode = filter_params['ceil_mode']
        output = max_blur_pool2d(output, kernel_size, stride, max_pool_size, ceil_mode)
    
    elif filter_name == "median_blur":
        kernel_size = tuple(filter_params['kernel_size'])
        output = median_blur(output, kernel_size)
    
    elif filter_name == "motion_blur":
        # kernel_size = tuple(filter_params['kernel_size'])
        kernel_size = tuple(filter_params['kernel_size'])[0]
        angle = filter_params['angle']
        direction = filter_params['direction']
        border_type = filter_params['border_type']
        mode = filter_params['mode']
        output = motion_blur(output, kernel_size, angle, direction, border_type, mode)
    
    elif filter_name == "unsharp_mask":
        kernel_size = tuple(filter_params['kernel_size'])
        sigma = tuple(filter_params['sigma'])
        border_type = filter_params['border_type']
        output = unsharp_mask(output, kernel_size, sigma, border_type)

    ## Edge detection
    elif filter_name == "canny":
        low_threshold = filter_params['low_threshold']
        high_threshold = filter_params['high_threshold']
        kernel_size = tuple(filter_params['kernel_size'])
        sigma = tuple(filter_params['sigma'])
        hysteresis = filter_params['hysteresis']
        eps = filter_params['eps']
        output = canny(output, low_threshold, high_threshold, kernel_size, sigma, hysteresis, eps)

    elif filter_name == "laplacian":
        kernel_size = tuple(filter_params['kernel_size'])
        border_type = filter_params['border_type']
        normalized = filter_params['normalized']
        output = laplacian(output, kernel_size, border_type, normalized)

    elif filter_name == "sobel":
        normalized = filter_params['normalized']
        eps = filter_params['eps']
        output = sobel(output, normalized, eps)

    elif filter_name == "spatial_gradient":
        mode = filter_params['mode']
        order = filter_params['order']
        normalized = filter_params['normalized']
        output = spatial_gradient(output, mode, order, normalized)

    elif filter_name == "spatial_gradient3d":
        mode = filter_params['mode']
        order = filter_params['order']
        output = spatial_gradient3d(output, mode, order)
    
    else:
        raise ValueError(f"Unknown filter name: {filter_name}")

    # output = torch.clip(output, 0, 1) # 避免超出范围
    return output




