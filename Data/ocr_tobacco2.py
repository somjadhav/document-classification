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

    counter = 0
    
    with open('/work/08290/somj/stampede2/scripts/document-classification/Data/SmallTobacco.csv', "wb") as file_write:
        writer = csv.writer(file_write, delimiter=",")
        for element in new_rows_list:
            counter += 1
            
            file_name = element[0].split("/")[-1]
            file_name = file_name[:-4] + '.jpg'
            file_name_2  = file_name[:-4] + '.txt'
            img_dir = "/work/08290/somj/stampede2/data/" + file_name
            img_dir_2 = '/work/08290/somj/stampede2/data/' + file_name_2
            
            files = glob.glob(img_dir)
            if len(files) == 0:
                continue

            new_row = [img_dir,element[1],element[2],img_dir_2]
            
            writer.writerow(new_row)
            file_write.flush()
            files_2 = glob.glob(img_dir_2)
            
            if len(files_2) != 0:
                continue
            '''
            config = ('tesseract image.jpg output -l eng --oem 1 --psm 3')
        
            # Read image from disk
            im = cv2.imread(img_dir, cv2.IMREAD_COLOR)
            pytesseract.pytesseract.tesseract_cmd = '/home1/08290/somj/.local/bin/tesseract'
                
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(im, config=config)
            #txt_name = os.path.join(imPath, image_name + ".txt")
            #txt_name = imPath + ".txt"
        
            file = open(os.path.join(img_dir_2),"w")
            file.write(text)
            '''
        # Print recognized text
    #file_write.close()
