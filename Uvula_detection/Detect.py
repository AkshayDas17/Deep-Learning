from ultralytics import YOLO
model=YOLO('Uvula_detect.pt')
model.predict(source="images (3).jpg",show=True,save=True,show_labels=True,show_conf=True,conf=0.5,save_txt=False,save_crop=False,line_width=2)