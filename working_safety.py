# -*- coding: utf-8 -*-
"""Working_Safety.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17Bselc7ka0-_5RphWzrpqZHvrnl065np
"""

!gdown '1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R'
!mkdir safety_helmet_dataset
!unzip -q '/content/Safety_Helmet_Dataset.zip' -d '/content/safety_helmet_dataset'

!pip install ultralytics

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/THU-MIG/yolov10.git
# %cd yolov10
!pip install -q -r requirements.txt
!pip install -e.

from ultralytics import YOLOv10
MODEL_PATH = '/content/yolov10/yolov10n.pt'
model = YOLOv10(MODEL_PATH)

YAML_PATH = '/content/safety_helmet_dataset/data.yaml'
EPOCHS = 1
BATCH_SIZE = 64
IMAGE_SIZE = 640
model.train(data = YAML_PATH, epochs = EPOCHS, batch = BATCH_SIZE, imgsz = IMAGE_SIZE)

TRAINED_MODEL_PATH = '/content/yolov10/runs/detect/train5/weights/best.pt'
model = YOLOv10(TRAINED_MODEL_PATH)
model.val(data = YAML_PATH, imgsz = IMAGE_SIZE, split = 'test')

IMG_PATH = '/content/working.png'
model.predict(IMG_PATH)