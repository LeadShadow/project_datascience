from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image

model_filename = Path('./model/vgg16_cifar10_new_91.7.hdf5')
model = tf.keras.models.load_model(model_filename)
# Тут size повинен бути як в моделі

classes=['Літак', 'Авто', 'Птах', 'Кіт', 'Олень', 'Собака', 'Жаба', 'Кінь', 'Корабель', 'Вантажівка']


def resize_image(image_to_recognize):
    img = Image.open(image_to_recognize)
    img = img.resize((56, 56))
    img = img.convert("RGB")
    input_image = np.reshape(img, (-1, 56, 56, 3))
    return input_image


def predict_image(image):
    input_img = resize_image(image)
    predict_img = model.predict(input_img)
    print(predict_img)
    pred_class = classes[np.argmax(predict_img)]
    return pred_class


if __name__ == '__main__':
    print(predict_image(Path('static/img/кінь.jpg')))
