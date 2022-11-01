import Augmentor
import os


def reName(dirname, new_path):
    count = 0
    for cur_file in os.listdir(dirname):
        count += 1
        oldDir = os.path.join(dirname, cur_file)  # 旧文件
        filetype = os.path.splitext(cur_file)[1]  # 文件类型
        newDir = os.path.join(new_path, str(count) + filetype)  # 新文件
        os.rename(oldDir, oldDir)
        print(oldDir, oldDir)


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def datastrength(data_path):
    p = Augmentor.Pipeline(data_path)  # 生成输出的路径，在./test/output下，output文件夹自动生成
    # p=Augmentor.Pipeline("E:\IMG\code1")  # 生成输出的路径，在./test/output下，output文件夹自动生成
    p.zoom(probability=0.5, min_factor=1.05, max_factor=1.05)
    p.random_distortion(probability=1, grid_width=6, grid_height=2, magnitude=3)
    p.sample(10000)


if __name__ == "__main__":
    # image
    imagedata_path = r'E:\IMG\code1'
    datastrength(imagedata_path)
    path = imagedata_path + '/output'
    new_path = imagedata_path + '/strength'
    mkdir(new_path)
    reName(path, new_path)
    # # label
    # imagedata_path = r'E:\IMG\code1'
    # datastrength(imagedata_path)
    # path = imagedata_path + '/output'
    # new_path = imagedata_path + '/strength'
    # mkdir(new_path)
    # reName(path, new_path)

