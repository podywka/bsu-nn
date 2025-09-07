from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.backend import image_data_format
import numpy as np
import os
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import model_from_json
from utils.settings import DATA_DIR

np.random.seed(42)

CUR_MODULE_DIR = DATA_DIR / "mnist"
CUR_MODULE_DIR.mkdir(parents=True, exist_ok=True)

MNIST_MODEL_JSON_PATH = CUR_MODULE_DIR / "mnist_best_model.json"
MNIST_MODEL_WEIGHTS_PATH = CUR_MODULE_DIR / "mnist_best_model.weights.h5"


# ---------------- Модель: загрузка данных, архитектура, обучение, оценка ----------------

def _load_prepare_mnist():
    """Загрузка данных"""
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    input_shape = ((1, X_train.shape[1], X_train.shape[2])
                   if image_data_format() == 'channels_first'
                   else (X_train.shape[1], X_train.shape[2], 1))

    X_train = X_train.reshape(X_train.shape[0], *input_shape).astype('float32') / 255
    X_test  = X_test.reshape(X_test.shape[0], *input_shape).astype('float32') / 255

    Y_train = to_categorical(y_train, 10)
    Y_test  = to_categorical(y_test, 10)

    return X_train, Y_train, X_test, Y_test, input_shape

def _create_cnn_model(input_shape):
    """Архитектура, компиляция"""
    model = Sequential([
        Conv2D(75, kernel_size=(5,5), activation='relu', input_shape=input_shape),
        MaxPooling2D(pool_size=(2,2)),
        Dropout(0.2),
        Conv2D(100, kernel_size=(5,5), activation='relu'),
        MaxPooling2D(pool_size=(2,2)),
        Dropout(0.2),
        Flatten(),
        Dense(500, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

def _train_cnn_model(model, X_train, Y_train, batch_size=200, epochs=1, val_split=0.2):
    """Обучение"""
    history = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs,
                        validation_split=val_split, verbose=1)
    return history

def _evaluate_cnn_model(model, X_test, Y_test):
    """Оценка"""
    scores = model.evaluate(X_test, Y_test, verbose=0)
    print(f"Точность на тестовых данных: {scores[1]*100:.2f}%")
    return scores[1]

def _save_model(model, json_path, weights_path):
    model_json = model.to_json()
    with open(json_path, "w") as json_file:
        json_file.write(model_json)
    model.save_weights(weights_path)
    print("Модель и веса сохранены")

def _load_model(json_path, weights_path):
    if not os.path.exists(json_path) or not os.path.exists(weights_path):
        raise Exception("Either model json or model weights does not exist")

    with open(json_path, "r") as f:
        model_json = f.read()

    model = model_from_json(model_json)
    model.load_weights(weights_path)

    return model


# ---------------- Пример ----------------

def get_mnist_model():
    json_path = MNIST_MODEL_JSON_PATH
    weights_path = MNIST_MODEL_WEIGHTS_PATH

    if os.path.exists(json_path) and os.path.exists(weights_path):
        print("Загружена предобученная модель")
        cnn_model = _load_model(json_path=json_path, weights_path=weights_path)

    else:
        print("(!) Either model json or model weights does not exist.\nTraining it now...")

        X_train, Y_train, X_test, Y_test, input_shape = _load_prepare_mnist()
        cnn_model = _create_cnn_model(input_shape)
        cnn_model.summary()
        _train_cnn_model(cnn_model, X_train, Y_train, epochs=3)
        _evaluate_cnn_model(cnn_model, X_test, Y_test)
        _save_model(model=cnn_model,
                    json_path=json_path, 
                    weights_path=weights_path)

    return cnn_model



# ---------------- Предикт по картинке ----------------

def _load_image(pic_path):
    """Загрузка изображения и перевод в массив"""
    img = Image.open(pic_path).convert('L')  # grayscale
    arr = np.array(img, dtype='float32')
    return arr

def _preprocess_image(arr):
    """Инвертируем цвета, нормируем и добавляем batch/canal dimension"""
    # MNIST: цифра должна быть белой (1) на черном (0)
    arr = 255 - arr
    arr /= 255.0

    if image_data_format() == 'channels_first':
        img_array = arr.reshape(1, 1, arr.shape[0], arr.shape[1])
    else:
        img_array = arr.reshape(1, arr.shape[0], arr.shape[1], 1)
    
    return img_array

def _show_image(arr):
    """Показывает изображение для проверки"""
    plt.figure(figsize=(3,3))
    plt.imshow(arr, cmap='gray')
    plt.title(f"Вид изображения (shape: {arr.shape})")
    plt.axis('off')
    plt.show()

def predict_mnist_image(pic_path, model, show=True):
    """Полная обработка и предсказание"""
    arr = _load_image(pic_path)
    img_array = _preprocess_image(arr)
    
    if show:
        _show_image(arr)
    
    result = model.predict(img_array)
    for i, perc in enumerate(np.round(100*result)[0]):
        print(f"{i}: {perc}%")
    print("Предсказанный результат:", np.argmax(result))
    
    return np.argmax(result)
