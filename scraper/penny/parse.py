from rapidocr import RapidOCR
import cv2
from fetch import pages_dir, todayWeek, todayYear
import os

directory = pages_dir(todayWeek, todayYear)

# hardcoded cuz im still working on this OCR
img = cv2.imread(os.path.join(directory, "page_01.png"))

small = cv2.resize(img, None, fx=0.4, fy=0.4,interpolation=cv2.INTER_AREA)


engine = RapidOCR(
    params={
        "Global.use_cls": False,
        "Det.limit_side_len": 2400,
        }
    )

result = engine(small)

result.vis("rapidocr.png")

# cv2.namedWindow("window_name", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("window_name", 1920, 1080)
# cv2.imshow("window_name", img)
# cv2.waitKey(0)