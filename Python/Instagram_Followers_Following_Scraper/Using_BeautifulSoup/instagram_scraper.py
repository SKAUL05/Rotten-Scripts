#!/usr/bin/env python3

#Imports and dependencies
from bs4 import BeautifulSoup
import requests

#The instagram URL
URL="https://www.instagram.com/{}/"

def parse_data(meta_content):
    #The content received needs to parsed through
    meta_content = meta_content.split("-")[0]
    meta_content = meta_content.split(" ")
    return {
        'Followers': meta_content[0],
        'Following': meta_content[2],
        'Posts': meta_content[4],
    }

#Using BeautifulSoup, web-scarping is performed

def scrape_data(username):
    #A HTTP GET request is made here
    response = requests.get(URL.format(username))
    
    #The response is loaded into the BeautifulSoup HTML parser
    soup = BeautifulSoup(response.text,"html.parser")

    #The contents of the meta tag with the property og:description are accessed here
    meta_content = soup.find("meta", property="og:description")

    return parse_data(meta_content.attrs['content'])

if __name__=="__main__":
    username = input("Enter the instagram username ")
    data = scrape_data(username)
    print(username , "has" , data["Followers"],"followers")
    print(username , "has", data["Following"],"following")
    print(username, "has" , data["Posts"],"posts")

