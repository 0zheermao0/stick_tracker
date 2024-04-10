from ultralytics import YOLO

# Load the model and run the tracker with a custom configuration file
model = YOLO('./runs/detect/train/weights/best.pt')
results = model.track(source="./stick_test.mp4", tracker='./cfgs/botsort.yaml', save=True)
