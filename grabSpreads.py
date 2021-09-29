import os
import requests

from PIL import Image
from io import BytesIO

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
    
    response = requests.get(line)
    im = Image.open(BytesIO(response.content))
    width, height = im.size
    
    #Resizes image so that it fits screen height
    ratio=1080/height
    newWidth=int(width*ratio)
    im=im.resize((newWidth, 1080), Image.ANTIALIAS)
        
    img=Image.new(mode="RGB", size=(1920,1080), color=(255,255,255))
    img.paste(im, box=(int((1920-newWidth)/2),0))
    saveToURL=desktop+"\Spreads\\"+imageName
    print(saveToURL)
    
    img.save(saveToURL, quality=90)
    
    print("Downloaded " + imageName + "...")
    
#Complete message
print("Done.")

"""
To add:
        - Linear gradient background based on average colors
        - Allow non-Windows users to use it
"""