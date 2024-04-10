import cv2
from ultralytics import YOLO
import numpy as np

# 加载YOLOv8模型
model = YOLO('./cfgs/best.pt')  # 请根据需要选择合适的模型

# 打开视频文件
video_path = "./stick_test.mp4"
cap = cv2.VideoCapture(video_path)

# 获取视频帧的宽度和高度
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# crop_coords = [(285, 548), (401, 542), (282, 595), (390, 580)]
crop_coords = np.array([[(285, 548), (401, 542), (390, 580), (282, 595)]], dtype=np.int32)
x1, y1 = crop_coords[0][0]
x2, y2 = crop_coords[0][2]
offset_x = crop_coords[0][0][0]
offset_y = crop_coords[0][0][1]
# Create a blank mask with the same dimensions as the image
mask = np.zeros((frame_height, frame_width), dtype=np.uint8)

# Fill the polygon in the mask with white color
cv2.fillPoly(mask, crop_coords, 255)

# Invert the mask if you want to mask the area outside the polygon
# mask = cv2.bitwise_not(mask)

# 创建VideoWriter对象，用于写入处理后的视频
output_path = "./output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 定义编码格式
# out = cv2.VideoWriter(output_path, fourcc, fps, (x2 - x1, y2 - y1))
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# 循环读取视频帧
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break  # 如果读取失败或视频结束，则退出循环
    annotated_frame = frame.copy()

    # 使用YOLOv8进行对象跟踪
    # only track objects in the specified area by cropping the image
    masked_image = frame[y1:y2, x1:x2]
    results = model.track(masked_image, persist=True)  # persist=True用于持续跟踪
    print(f"result of tracking: {results}")
    bbox = results[0].boxes
    if bbox:
        print(f"bbox: {bbox}, origin_bbox: {bbox.xyxy[0][0] + offset_x, bbox.xyxy[0][1] + offset_y, bbox.xyxy[0][2] + offset_x, bbox.xyxy[0][3] + offset_y}")
        top_left = (int(bbox.xyxy[0][0] + offset_x), int(bbox.xyxy[0][1] + offset_y))
        bottom_right = (int(bbox.xyxy[0][2] + offset_x), int(bbox.xyxy[0][3] + offset_y))
        cv2.rectangle(annotated_frame, top_left, bottom_right, (0, 255, 0), 2)
        text = f"{bbox.cls, bbox.conf}"
        cv2.putText(annotated_frame, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 获取带有跟踪结果的帧
    # annotated_frame = results[0].plot()

    # 将处理后的帧写入输出视频
    out.write(annotated_frame)

    # 可选：显示处理后的帧
    # cv2.imshow('YOLOv8 Tracking', annotated_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()

