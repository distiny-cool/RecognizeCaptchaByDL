# -*- coding: UTF-8 -*-
import os
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from PIL import Image
import one_hot


class mydataset(Dataset):
    def __init__(self, folder, transform=None):
        self.train_image_file_paths = [
            os.path.join(folder, image_file) for image_file in os.listdir(folder)
        ]
        self.transform = transform

    def __len__(self):
        return len(self.train_image_file_paths)

    def __getitem__(self, idx):
        image_root = self.train_image_file_paths[idx]
        image_name = image_root.split(os.path.sep)[-1]
        image = Image.open(image_root)
        if self.transform is not None:
            image = self.transform(image)
        # 为了方便，在生成图片的时候，图片文件的命名格式 "4个数字或者数字_时间戳.PNG"
        # 前面的字母或者即是图片的验证码的值，字母大写,同时对该值做 one-hot 处理
        label = one_hot.encode(image_name.split("_")[0])
        return image, label


def dataLoader(folder, batch_size=1, shuffle=False):
    """载入数据集"""
    transform = transforms.Compose(
        [
            transforms.Grayscale(),  # 转化为灰度图
            transforms.ToTensor(),  # 灰度图转化为tensor
        ]
    )
    dataset = mydataset(folder, transform)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
