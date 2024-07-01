# How to install YOLOv10 using Colab

#### I. Install and Using pre-trained model 
 * **Step 1**: Get source code from [Github](https://github.com/THU-MIG/yolov10?tab=readme-ov-file)
![Github](https://github.com/Ducanhngo/Project_YOLOv10_Worksafety/assets/104834316/13e09d5c-87c2-43fb-967a-f54680f49946)
 * **Step 2**: Clone YOLOv10 files by this code
 
 `!git clone https://github.com/THU-MIG/yolov10.git `
 
 * **Step 3**: Install required libraries
```
%cd yolov10
!pip install -q -r requirements.txt
!pip install -e 
```
* **Step 4**: Download weights for pre-trained model

    !wget https://github.com/THUMIG/yolov10/releases/download/v1.1/yolov10n.pt

* **Step 5**: Initialize the model
```
from ultralytics import YOLOv10
MODEL_PATH = 'yolov10n.pt'
model = YOLOv10(MODEL_PATH)
```
* **Step 6**: Download/ Upload example images to Colab

![image](https://github.com/Ducanhngo/Project_YOLOv10_Worksafety/assets/104834316/e1a1ba62-81d3-4be3-b0a2-edd230d24aca)

* **Step 7**: Predict and save results

```
IMG_PATH = './images/HCMC_Street.jpg'
result = model(source = IMG_PATH)[0]
result.save('./images/HCMC_Street_predict.png')
```

![image](https://github.com/Ducanhngo/Project_YOLOv10_Worksafety/assets/104834316/fdaf5983-24c5-410d-af7b-ff5c4fd79d7e)

 
