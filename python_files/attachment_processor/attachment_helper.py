import datetime
from datetime import date
import python_files.attachment_processor.extractText as textExtractor
import python_files.attachment_processor.getAmount as amountFinder
import python_files.attachment_processor.getCategory as categoryFinder
import python_files.attachment_processor.getDate as dateFinder
import python_files.attachment_processor.getUnit as unitFinder
import logging 

# returns data = { 'unit':'Rs.','amount':'12','date': dateObject , 'category':'Food' }
def processAttachment( filePath , fileType ,rootDir):

    
    extractTextPath = textExtractor.generateTextFile( filePath , fileType,rootDir )
    if extractTextPath is None:
        print('Error in Processing')
        return None
    
    unit = unitFinder.getUnit( extractTextPath ) 
    amount = amountFinder.getAmount( extractTextPath ) 
    date = dateFinder.getDate( extractTextPath )
    category = categoryFinder.getCategory( extractTextPath )
    
    data = { 'receipt':'success', 'unit':unit,'amount': amount , 'date':date , 'category':category }
    logging.info(data)
    return data

if __name__ == "__main__":
    processAttachment( 'sds','sdf' )   
