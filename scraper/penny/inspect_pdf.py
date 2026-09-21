# import pytesseract
# from pytesseract import Output
# import PIL.Image
# import cv2
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# myconfig = r"--psm 11 --oem 3 -l ron"

# img = cv2.imread("2page_01.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# height, width, _ = gray.shape

# data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
# for i in range(len(data['text'])):  
#     if float(data['conf'][i]) > 30:
#         x = data['left'][i]
#         y = data['top'][i]
#         width = data['width'][i]
#         height = data['height'][i]
#         gray = cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0),2)
#         gray = cv2.putText(img, data['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        

        

# cv2.Laplacian(gray, cv2.CV_64F)
# cv2.namedWindow("test", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("test", 1920, 1020)
# cv2.imshow("test", gray)
# cv2.waitKey(0)

# text = pytesseract.image_to_string(PIL.Image.open("page_01.png"), config=myconfig)
# print(text)

# img = cv2.imread("page_01.png")
# height, width, _ = img.shape

# boxes = pytesseract.image_to_boxes(img, config=myconfig)
# for box in boxes.splitlines():
#     box = box.split(" ")
#     img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height-int(box[4])), (0,255,0), 2)

# cv2.imshow("img", img)
# cv2.waitKey(0)

# img = cv2.imread("mask_debug.png")
# height, width, _ = img.shape

# data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

# amount_boxes = len(data['text'])

# for i in range(amount_boxes):
#     if float(data['conf'][i]) > 40:
#         (x,y,width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#         img = cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)
#         img = cv2.putText(img, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0),2, cv2.LINE_AA)

# cv2.namedWindow("window_name", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("window_name", 1920, 1080)
# cv2.imshow("window_name", img)
# cv2.waitKey(0)
# nu a functionat nimic de aici

