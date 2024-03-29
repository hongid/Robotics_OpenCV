# coding=utf-8 @ Chien Yü

import os
import argparse
import cv2 as cv

from src.ocr import ocr
from src.utils.color_trackbar import color_trackbar
from src.utils.thresh_trackbar import thresh_trackbar
from src.utils.demo.face_detection import face_detection
from src.utils.demo.show_bgr_hsv import show_bgr_hsv
from src.utils.demo.feature_matching import feature_matching

def main(args):
    img_path = os.path.join("data/test_images/", args.image)

    if args.module[0] == "ocr":
        ocr(img_path)
    elif args.module[0] == "hsv":
        show_bgr_hsv(img_path)
    elif args.module[0] == "trackbar_color":
        color_trackbar(img_path)
    elif args.module[0] == "trackbar_threshold":
        thresh_trackbar(img_path)
    elif args.module[0] == "face_detection":
        face_detection()
    elif args.module[0]=="feature_matching":
        feature_matching()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='UNM Robotics OpenCV Workshop')
    parser.add_argument("-m", "--module", dest="module", nargs=1, choices=["hsv", "trackbar_color","trackbar_threshold","face_detection","feature_matching","ocr"],
                        default=["ocr"])
    parser.add_argument(
        '--image', help='Path to the input image.', default="book.jpg")
    args = parser.parse_args()

    main(args)
