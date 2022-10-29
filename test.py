# -*- coding: UTF-8 -*-
import torch.nn as nn
import numpy as np
import torch
from torch.autograd import Variable
import setting
import dataset
from cnn_model import CNN
import one_hot
from utils import *


def test(net: nn.Module, module, batch_size, device, char_num):
    """测试模型"""
    folder = setting.TEST_DATASET_PATH
    net.eval()
    net.load_state_dict(torch.load(module))

    test_dataloader = dataset.dataLoader(folder, batch_size)

    correct = 0
    total = 0

    for i, (images, labels) in enumerate(test_dataloader):

        images = Variable(images).to(device)
        out = net(images)

        # 导出预测的结果
        predict_label = ""
        for j in range(0, char_num):
            ch = setting.ALL_CHAR_SET[
                np.argmax(
                    out[
                        0, j * setting.ALL_CHAR_SET_LEN : (j+1) * setting.ALL_CHAR_SET_LEN
                    ].data.numpy()
                )
            ]
            predict_label += ch

        true_label = one_hot.decode(labels.numpy()[0])

        total += labels.size(0)
        if predict_label == true_label:
            correct += 1
        else:
            print(
                "[ERROR]predict_label: %s true_label: %s" % (predict_label, true_label)
            )
            return 0

        if total % 200 == 0:
            print("Total test images: %d" % total)
            print("Right test images: %d" % correct)
            print("Accuracy:          %.3f%%" % (100 * correct / total))
            print("*********************")

    print(
        "Test Accuracy of the model on the %d test images: %.3f %%"
        % (total, 100 * correct / total)
    )


if __name__ == "__main__":
    device = try_gpu(0)
    net = CNN().to(device)
    batch_size = 1
    module = "model.pkl"
    char_num = setting.MAX_CAPTCHA  # 测试验证码的字符数

    print("*********************")
    print("Use:           ", device)
    print("Batch_size:    ", batch_size)
    print("Use module:    ", module)
    print("*********************")

    test(net, module, batch_size, device, char_num)
