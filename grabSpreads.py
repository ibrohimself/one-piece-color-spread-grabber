import os
import requests
import urllib.request

#Grabbing HTML from One Piece wiki's Color Spread page and splitting it into lines
url = requests.get("https://onepiece.fandom.com/wiki/Category:Color_Spreads")
lines = url.text.splitlines()

#Array for holding image URLs
links=[]

#Grabbing image URLs from HTML
for line in lines:
    if "images" in line and "Chapter_" in line:
        line=line.split("\"")[1]
        links.append(line[0:line.find("/revision")]+"\n")

#Copy-pasted code for removing duplicates
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

#Removing newlines
links=[link[:-1] for link in f7(links)[1:]]

#Find Desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

#Make folder for color spreads
if not os.path.exists(desktop+"\Spreads"): os.mkdir(desktop+"\Spreads")

#Download each image and save it to color spreads folder
for line in links:
    imageName=line[line.find("Chapter"):line.find("png")+3]
    saveToURL=desktop+"\Spreads\\"+imageName
    #print(saveToURL)
    urllib.request.urlretrieve(line, saveToURL)
    print("Downloaded " + imageName + "...")

#Complete message
print("Done.")

"""
To add:
        - Use PIL to size the spreads to the computer's dimensions to avoid cropping
        - Create a border around the images with a gradient based on color images so that they all fit nicely
        - Allow non-Windows users to use it
"""