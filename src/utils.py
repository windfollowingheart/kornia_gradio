import numpy as np
import torch
import torchvision.transforms as transforms
from torchmetrics.image import StructuralSimilarityIndexMeasure as SSIM
from PIL import Image
from filters import calc_image_filter
from colors import calc_image_color

def image_to_tensor(image: np.ndarray) -> torch.Tensor:
    # 将 numpy.ndarray 转换为 PIL 图像
    image = transforms.ToPILImage()(image.astype(np.uint8))

    # 定义转换操作
    transform = transforms.Compose([
        transforms.ToTensor()
    ])

    # 将图像转换为 Tensor
    tensor_image: torch.Tensor = transform(image)

    # 增加一个维度以模拟批量维度，将形状从 (c, w, h) 变为 (b, c, w, h)，这里 b = 1
    tensor_image = tensor_image.unsqueeze(0)

    return tensor_image

# 这里输入的格式为 [B, C, H, W], 输出格式为 [H, W, C]
def tensor_to_image(tensor_image: torch.Tensor) -> np.ndarray:
    # print(tensor_image.shape)
    tensor_image = tensor_image.squeeze()
    # print(tensor_image.shape)
    if tensor_image.dim() == 2:
        return tensor_image.numpy()
    return tensor_image.permute(1, 2, 0).numpy()


def calc_L1(image1: np.ndarray, image2: np.ndarray) -> float:
    image1 = image_to_tensor(image1)
    image2 = image_to_tensor(image2)
    return torch.nn.functional.l1_loss(image1, image2).item()


def calc_SSIM(image1: np.ndarray, image2: np.ndarray) -> float:
    image1 = image_to_tensor(image1)
    image2 = image_to_tensor(image2)
    ssim = SSIM()
    value = ssim(image1, image2)
    return value.item()

def resize_image(image: torch.Tensor, h: int, w: int) -> torch.Tensor:
    image = torch.nn.functional.interpolate(image, size=(h, w), mode='bilinear', align_corners=False)
    return image

def process_image(image: torch.Tensor, config: list[dict]) -> torch.Tensor:
    output = image
    for item in config:
        type = item['type']
        if type == 'filter':
            filter = item
            output = calc_image_filter(output, filter)
        elif type == 'color':
            color = item
            output = calc_image_color(output, color)
        elif type == 'resize':
            h = item['params']['h']
            w = item['params']['w']
            output = resize_image(output, h, w)
        
    return output




if __name__ == '__main__':
    image1_path = ''
    image2_path = ''

    image1 = image_to_tensor(np.array(Image.open(image1_path)))


