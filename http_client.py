#!/usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

methods = ['head','put', 'get']


while True:
    user_input = input(">")
          
    if user_input == 'exit':
        break

    elif user_input == '1':
        url = input('Enter URL: ')
        method = input('Enter the HTTP method: ')
       if method == method in methods:
          r = requests.method(url)


    def http_method(url):


	def print_response(url):
        response = input("Enter if you like to see either headers,cookies, status codes")
            headers = r.headers
            response_code = r.status_code
	            

    elif user_input == 'help' or 'h':
        print("Enter 1 to make a request for the URL:")
        print("Exit - to exit client")

     
#HTTP Methods
#post_method = raw_input('Choose a HTTP methd you would like to use :')
#methods = ['head', 'trace', 'put', 'get' 'delete', 'options', 'connect']


r = requests.get(url) 
headers = r.headers
text  = r.txt 
cookies = r.cookies
