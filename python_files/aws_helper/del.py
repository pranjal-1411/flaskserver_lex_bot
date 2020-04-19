import re

dic = { "variables": [ "Pranjal","Good" ]   }
lex_message = "Hi @var0, you are @var1 boy"
for i in range( len(dic["variables"]) ):
    to_find = "@var"+str(i)
    to_replace = dic["variables"][i] 
    lex_message = re.sub( to_find,to_replace,lex_message )

print(lex_message)


{
    "ignoreLex": True,
    "message":"Something from Asanify Server"
}

{
    
    "ignoreLex":False,
    "editMessage": True/False,
    "variables":["List of variables to be edited"]
}

# This should be the output from lex  
# Hi @var0 , you have a meeting on date @var1 !!