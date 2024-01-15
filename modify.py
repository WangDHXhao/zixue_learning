from PIL import Image


def image_processing():
    #  待处理图片路径
    img_path = Image.open('./123.jpg')
    #  resize图片大小，入口参数为一个tuple，新的图片的大小
    img_size = img_path.resize((1920, 1080))
    #  处理图片后存储路径，以及存储格式
    img_size.save('./new_123.jpg', 'JPEG')


if __name__ == '__main__':
    image_processing()
