
from captcha.image import ImageCaptcha
import string, random

# 实例化
file=r'C:\Windows\Fonts\ARLRDBD.TTF'
img = ImageCaptcha(width=80,height=30,fonts=['E:\pytorch-captcha-recognition\AdobeSongStd-Light.otf'],font_sizes=[20,30,35])

# 生成字母和数字
lettersAndNumbers =  string.digits
# 咱们生产10张验证码
for _ in range(10):
    # 随机选择4个字符生产验证码
    chars = ''.join(random.sample(lettersAndNumbers, k=5))
    # 随机颜色,color和background是接受rgb(0,0,0)这样的参数的
    # 所以可以使用random生成即可
    rgb = (random.randint(0, 256), random.randint(0,
                                                  256), random.randint(0, 256))
    b_rgb = (random.randint(0,
                            256), random.randint(0,
                                                 256), random.randint(0, 256))
    im = img.create_captcha_image(chars=chars, color=rgb, background=(255,255,255))
    # 开始生成带干扰点的验证码
    c_rgb = (random.randint(0,
                            256), random.randint(0,
                                                 256), random.randint(0, 256))
    im = img.create_noise_dots(im, color=c_rgb)
    # 图片保存的路径
    path = r'dataset/bmp/' + chars + '.bmp'
    im.save(path)
print('验证码生成完成')