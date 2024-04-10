# Author: Joey
# Email: zengjiayi666@gmail.com
# Date: :call strftime("%Y-%m-%d %H:%M")
# Description: 
# Version: 1.0
#
# if __name__ == "__main__": 
import cv2

# 输入视频文件路径
input_video = "./stick_test.mp4"

# 输出裁剪后的视频文件路径
output_video = "./crop_stick.mp4"

# 裁剪区域的坐标
crop_coords = [(285, 548), (401, 542), (282, 595), (390, 580)]

# 打开输入视频文件
cap = cv2.VideoCapture(input_video)

# 获取视频的帧率和编解码器
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# 获取裁剪区域的宽度和高度
x_min = min(coord[0] for coord in crop_coords)
y_min = min(coord[1] for coord in crop_coords)
x_max = max(coord[0] for coord in crop_coords)
y_max = max(coord[1] for coord in crop_coords)
width = x_max - x_min
height = y_max - y_min

# 创建输出视频文件
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height), False)

# 逐帧读取视频并进行裁剪
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 裁剪帧
    cropped_frame = frame[y_min:y_max, x_min:x_max]

    # 写入裁剪后的帧到输出视频文件
    out.write(cropped_frame)

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
