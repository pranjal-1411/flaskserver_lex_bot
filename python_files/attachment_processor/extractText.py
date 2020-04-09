from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os

import logging

def generateTextFile( filePath , extension,rootDir ):
    
    imagePathList = []
    imageExtensionAllowed = [ 'jpg','png','jpeg' ]
    if(extension == "pdf" ):
    
        pages = convert_from_path(filePath) 
        image_counter = 1
        for page in pages: 
            pageName = "page_"+str(image_counter)+".jpg"
            pagePath = os.path.join(rootDir,'processedAttachment', pageName) 
            imagePathList.append(pagePath)
            page.save(pagePath, 'JPEG') 
            image_counter = image_counter + 1

    elif(extension in imageExtensionAllowed ):
        imagePathList.append(filePath)

    outfile = os.path.join(rootDir,'processedAttachment', 'out_text.txt')
    f = open(outfile, "w") 
    for path in imagePathList:
        text = str(((pytesseract.image_to_string(Image.open(path).convert("LA")))))
        text = text.replace('-\n', '')     
        f.write((text)) 
    f.close()    
    return outfile
    

if __name__ == "__main__":
    
    generateTextFile('/mnt/f/python3resolve/processedAttachment/bill2.pdf','pdf','/mnt/f/python3resolve')
