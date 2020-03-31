from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os

def generateTextFile( filePath , extension,rootDir ):
    imagePathList = []
    if(extension == "file" ):
    
        pages = convert_from_path(filePath) 
        image_counter = 1
        for page in pages: 
            pageName = "page_"+str(image_counter)+".jpg"
            pagePath = os.path.join(rootDir,'processedAttachment', pageName) 
            imagePathList.append(pagePath)
            page.save(pagePath, 'JPEG') 
            image_counter = image_counter + 1

    elif(extension == "image"):
        imagePathList.append(filePath)

    outfile = os.path.join(rootDir,'processedAttachment', 'out_text.txt')
    f = open(outfile, "w") 
    for path in imagePathList:
        text = (((pytesseract.image_to_string(Image.open(path).convert("LA"))))).encode('utf-8') 
        text = text.replace(b'-\n', b'')      
        f.write(str(text)) 
        
    return outfile
    

if __name__ == "__main__":
    
    generateTextFile('downloadFile.pdf','file')
