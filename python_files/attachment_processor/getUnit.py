import re

def getUnit(inFile):
    
    ans = 'Rs.' 
    f = open(inFile,"r")
    unit_inr = "inr|rs.|rs"
    unit_usd = "dollar|usd"
    
    for line in f:
        x = re.search(unit_inr,line,re.IGNORECASE)
        if x: return 'Rs.'
        x = re.search(unit_usd,line,re.IGNORECASE)
        if x: return 'USD'

    f.close()
    return ans


if __name__ == "__main__":
    print(getUnit("out_text.txt"))
