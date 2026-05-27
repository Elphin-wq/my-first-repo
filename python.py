from bs4 import BeautifulSoup
import requests
def sendmail():
    #mailmsg = "<a href='https://www.youtughfghfghfghbhjbjbjreeferferhfghfghfghrfghbe.com/watch?v=dQw4w9WgXcQ'>Click here to watch a video</a>"
    mailmsg = input("Enter the mail message: ")
    soup = BeautifulSoup(mailmsg, 'html.parser')
    anchor = soup.find('a').attrs
    hanchor = anchor['href']
    try:
        request = requests.get(hanchor)
        if request.status_code == 200:
            anchortext = hanchor
            print("The link is valid and the video is accessible.")
    except:
        anchortext ="" 
    if (hanchor.find("https")!= -1):
        fanchor = hanchor[8:]
    else:
        fanchor = hanchor[7:]
        print(fanchor)
    anchorlength = len(fanchor)
    if (anchorlength > 64):
        type = "invalid url"
        print(type)
        
    elif(hanchor.strip() == anchortext.strip()):
        type = "not phishing"
        print(type)
    elif(fanchor.find("%")!= -1 or fanchor.find(".")!= -1 or fanchor.find("#")!= -1 ):
        type = "phishing"
        print(type)
    else:
        type = "possible of phishing"
        print(type)
while(True):
    sendmail()
    ch = input("do you want to continue yes or no: ")
    if ch =="yes":
        continue
    else:
         break


print("Thank you for using the phishing detection tool.")