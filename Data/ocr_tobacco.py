import cv2
import sys
import pytesseract
import os
from time import sleep
from PIL import Image, ImageSequence
import numpy
import csv
import glob

# This files reads the image directory from a csv a creates ocr .txt files
# in the same directory and a new csv with .txt paths added in a new column

pytesseract.pytesseract.tesseract_cmd = '/home1/08290/somj/.local/bin/pytesseract.exe'

if __name__ == '__main__':

    #path_save = './OCRS/'
    file_read = open('/work/08290/somj/stampede2/scripts/document-classification/Data/Small_Tobacco.csv', "r")
    reader = csv.reader(file_read, delimiter=',')

    #Original label csv reading into list
    new_rows_list = []
    for row in reader:
        #full_row = [row[0], row[1]]
        new_rows_list.append(row)
    file_read.close()

    file_write = open('/work/08290/somj/stampede2/scripts/document-classification/Data/SmallTobacco.csv', "w")
    writer = csv.writer(file_write, delimiter=',')

    counter = 0
    for element in new_rows_list:
        counter += 1
        
        file_name = element[0].split("/")[-1]
        img_dir = "/work/08290/somj/stampede2/data/" + file_name
        
        files = glob.glob(img_dir)
        if len(files) == 0:
            continue
    
        	#imPath = os.path.join(root,file)
    
    
        config = ('tesseract image.jpg output -l eng --oem 1 --psm 3')
    
        # Read image from disk
        im = cv2.imread(img_dir, cv2.IMREAD_COLOR)
    		
        # Run tesseract OCR on image
        text = pytesseract.image_to_string(im, config=config)
        #txt_name = os.path.join(imPath, image_name + ".txt")
        #txt_name = imPath + ".txt"
    
        file = open(os.path.join(img_dir[:-4] + ".txt"),"w")
        file.write(text)
    
        new_row = [img_dir,element[1],element[2],img_dir[:-4] + ".txt"]
        #print(new_row)
    
        writer.writerow(new_row)

    # Print recognized text
    file_write.close()
