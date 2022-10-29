import torch
from matplotlib import pyplot as plt
import numpy as np

def try_gpu(i=0):
    """如果存在，则返回gpu(i)，否则返回cpu()"""
    if torch.cuda.device_count() >= i + 1:
        return torch.device(f'cuda:{i}')
    return torch.device('cpu')

def try_all_gpus():
    """返回所有可用的GPU，如果没有GPU，则返回[cpu(),]"""
    devices = [torch.device(f'cuda:{i}')
             for i in range(torch.cuda.device_count())]
    return devices if devices else [torch.device('cpu')]

class ShowLoss:
    """用于绘制损失变化图"""

    def __init__(self):
        self.show = np.empty(1)

    def add(self, loss):
        self.show = np.append(self.show, loss)

    def save(self, filename="loss.jpg"):
        count = np.arange(0, self.show.size)
        plt.plot(count, self.show)
        plt.title("Change of loss")
        plt.xlabel("count")
        plt.ylabel("loss")
        plt.savefig(filename)
        print("Save Loss change chart as", filename)