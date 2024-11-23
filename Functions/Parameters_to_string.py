from datetime import datetime
def Parameters_to_string(Parameters):
    now =str(datetime.now())[:16]
    now=now.replace(' ','_') 
    string=','
    for par in Parameters:
        string=string+str(par)+','
    string=now+string[:-1]+'\n'
    return string
