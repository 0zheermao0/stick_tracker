# Author: Joey
# Email: zengjiayi666@gmail.com
# Date: :call strftime("%Y-%m-%d %H:%M")
# Description: 
# Version: 1.0
#
# if __name__ == "__main__": 

import cv2

# 创建VideoCapture对象，读取视频文件
cap = cv2.VideoCapture('./stick_test.mp4')

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件")
    exit()

# 创建一个窗口来播放视频
cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)

# 循环读取视频帧并显示
pause = False
while True:
    if not pause:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            break
        cv2.imshow('frame', frame)

    key = cv2.waitKey(25)
    if key == ord(' '):
        pause = not pause
    elif key == ord('q'):
        break

# 释放VideoCapture对象
cap.release()

# 关闭所有窗口
cv2.destroyAllWindows()
