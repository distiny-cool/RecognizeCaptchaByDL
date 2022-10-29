import cv2 as cv
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

# 随机生成不同颜色的组合
def get_random_color():
  B = random.randint(0, 100)
  G = random.randint(0, 100)
  R = random.randint(0, 100)
  # 防止生成白色噪声噪线
  # 使用三个if条件判断防止三个通道的颜色都是255(虽然是不可能事件）
  if B == 255:
    B = 0
  elif G == 255:
    G = 0
  elif R == 255:
    R = 0
  return(B, G, R)

# 随机生成数字
def get_random_number():
  random_num = str(random.randint(0, 9))
  return random_num

def generate_image():
  # 生成白色图像，'RGB'类型，宽高为(150,50)，底色为白色(255,255,255)
  image = Image.new('RGB', (60, 18), (255,255,255))
  # 定义画笔，将图像与画笔关联
  draw = ImageDraw.Draw(image)
  # 定义文字字形以及字体大小
  file= r'C:\Windows\Fonts\ARLRDBD.TTF'

  font = ImageFont.truetype(file, size=15)
  # font = ImageFont.truetype("arial.ttf", size=15)

  name = "" # 定义一个空的字符串，用于不断叠加数字，给图像命名
  for i in range(4):
    random_number = get_random_number()
    # 不断叠加随机生成的数字，用于给图像命名
    name += random_number
    now = str(int(time.time()))
    # 在图片上写上数字，参数是：定位、数字(字符串)、颜色、字型
    draw.text((5+i*10, 0), random_number, get_random_color(), font=font)
  # 将图像保存到指定的文件夹，下面使用xxxx的形式代表文件夹
  filename = name + '_' + now + '.png'
  image.save('E:\pytorch-captcha-recognition\dataset\\train\%s'%filename)
  width = 60
  height = 18
  # 读取文件夹的图像，通过name来读取指定的图像，
  img = cv.imread('E:\pytorch-captcha-recognition\dataset\\train\%s' %filename)
  # 绘制噪点
  for i in range(13):
      x = random.randint(0, width)
      y = random.randint(0, height)
      # 绘制实心圆，必须输入参数分别是：图像、圆心的位置、半径、颜色，
      # 最后一个是thickness默认是None，绘制空心圆，指定为-1绘制实心圆
      cv.circle(img, (x, y), 1, get_random_color(), -1)

      # 保存图像
  cv.imwrite(r'E:\pytorch-captcha-recognition\dataset\\train\%s' %filename, img)


if __name__ == '__main__':
    for i in range(20000):
        generate_image()