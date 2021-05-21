import argparse
import cv2
from kcf import Tracker

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="video you want to track", type=str)
    args = parser.parse_args(['car.avi'])
    print(args)
    cap = cv2.VideoCapture(args.video)
    tracker = Tracker()
    ok, frame = cap.read()
    if not ok:
        print("error reading video")
        exit(-1)
    #selectROI四个参数 1.显示窗口名字 2.当前帧
    #3.是否在框中心显示十字 4.是否从中心开始画框
    roi = cv2.selectROI("tracking", frame, False, False)
    #确定初始的HOG框大小，以后所有的特征提取都要把ROI框resize到这个大小
    tracker.init(frame, roi)
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        x, y, w, h = tracker.update(frame)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)
        cv2.imshow('tracking', frame)
        c = cv2.waitKey(1) & 0xFF
        if c==27 or c==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
