import torch
import torch.nn as nn
from torch.autograd import Variable
import dataset
import setting
from cnn_model import CNN
import torchvision.models as models
from utils import *
from tensorboardX import SummaryWriter
import sys

def train(net: nn.Module, num_epochs, batch_size, lr, device):
    """训练模型"""
    folder = setting.TRAIN_DATASET_PATH
    net.train()
    Loss = nn.MultiLabelSoftMarginLoss().to(device)
    # Loss = nn.MSELoss().to(device)
    trainer = torch.optim.Adam(net.parameters(), lr)
    show = ShowLoss()  # 显示Loss变化

    train_dataloader = dataset.dataLoader(folder, batch_size, True)
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_dataloader):
            images = Variable(images).to(device)
            labels = Variable(labels.float()).to(device)
            with SummaryWriter(comment='CNN') as w:
                w.add_graph(net, images)
            predict_labels = net(images)
            loss = Loss(predict_labels, labels)
            show.add(-np.log(loss.detach().numpy()))
            trainer.zero_grad()
            loss.backward()
            trainer.step()

            if (i) % 10 == 0:
                print("epoch:", epoch, "step:", i, "loss:", loss.item())

        print("epoch:", epoch, "step:", i, "loss:", loss.item())
        torch.save(net.state_dict(), "./model.pkl")  # 每训练一轮保存1次模型
        print("Save model at epoch ", epoch)

    torch.save(net.state_dict(), "./model.pkl")
    print("Save last model")
    show.save()


if __name__ == "__main__":
    device = try_gpu(0)
    net = CNN().to(device)
    
    # net = models.resnet34(num_classes=4 * 36).to(device)
    num_epochs = 2
    batch_size = 64
    learning_rate = 0.01 

    print("*********************")
    print("Use:           ",device)
    print("Num_epochs:    ",num_epochs)
    print("Batch_size:    ",batch_size)
    print("learning_rate: ",learning_rate)
    print("*********************")

    train(net, num_epochs, batch_size, learning_rate, device)
