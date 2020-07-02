#import library
import requests


#get HTML content of goodreads website using get method
r =requests.get('https://www.goodreads.com/')

#check if 'r' request is valid or not
print("Request Status:")
print(r.status_code)
if r.status_code!=200:
    Print("try again or try onther website")
else:
    #print HTML content if HTTP request is valid and OK 
    print("HTTP request is valid")
    print(r.text)
    



