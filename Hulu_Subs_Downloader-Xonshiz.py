#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Xonshiz"
__email__ = "Xonshiz@psychoticelites.com"
__website__ = "http://www.psychoticelites.com"
__version__ = "v3.0"

'''
Found an interesting thread on reddit that helped me convert vtt to srt.
A HUGE thanks to fiskenslakt (https://www.reddit.com/user/fiskenslakt) for this "VTT" to "SRT conversion".
Read his contribution here : https://www.reddit.com/r/learnpython/comments/4i380g/add_line_number_for_empty_lines_in_a_text_file/d2upf5l

'''

from selenium import webdriver
import sys,time
import os, re
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


# Let's fetch the Link and the source code of the video page.
def Url_And_Data_Fetcher(url):
    q = requests.get(url)
    soup = BeautifulSoup(q.text,"lxml")
    file = open("newfile.txt", "w")
    file.write(soup.encode("utf8") + "\n")
    file.close


# Looking up the "Content_id" for getting our subs and "Title" to name our sub file.
def Data_Lookup():
    with open('newfile.txt') as searchfile:
        for line in searchfile:
            left,sep,right = line.partition('/video/') #Looking For "Content_id" in the <meta content="http://ib3.huluim.com/video/60585710?region=US&amp;size=600x400" property="og:image"/> (60585710 is Con_id)
            if sep:
                OG_Title = right
                Splitter = OG_Title.split("?")
                Con_id = Splitter[0]
                #print "Content_id : ",Con_id

    with open('newfile.txt') as searchfile:
        for line in searchfile:
            left,sep,right = line.partition('title')
            if sep:
                Episode_Number = right
                Final_EP_Num = Episode_Number[7:].replace('| Hulu</title>','').replace('>','').replace("Online","")

    return (Con_id,Final_EP_Num)            

# Con_id = 60585710
# Final_EP_Num = Oh My Ghostess - Episode 1

# Getting the required things from Data_Lookup() and navigating to differnet URLs to get the VTT subs. VTT to SRT conversion is now in effect.
def Sub_Lookup(Con_id,Final_EP_Num):
    if not Con_id: # This shit isn't really working... but, oh well, you'll see a nice error anyway xD!
        print "Seems like there are no subs for ",Final_EP_Num,"\nMy work here is done!"
        sys.exit()
    else :
        Caption_Lookup = 'http://www.hulu.com/captions.xml?content_id='+Con_id
        q1 = requests.get(Caption_Lookup)
        soup1 = str(BeautifulSoup(q1.text,"lxml"))
        if str(soup1) == '':
            print "Seems like there are no subs for ",Final_EP_Num,"\nMy work here is done!"
            sys.exit()
        else :
            SMI_File_Link = soup1.replace('<?xml version="1.0" encoding="utf-8"?><html><body><transcripts><en>','').replace('</en></transcripts></body></html>','').replace('<html><body><transcripts><en>','') # Remove lxml usage, hence, this fugly code with shit load of replace.
            VTT_Sub_Link = SMI_File_Link.replace('captions','captions_webvtt').replace('smi','vtt') # Changing things so we get URL to our subs
            head, sep, tail = VTT_Sub_Link.partition('.vtt')
            #print 'This is ', head
            #print "Downloading Subs From : ",VTT_Sub_Link # Nuffing Important
            print "Downloading Subs From : ",str(head)+'.vtt' # Nuffing Important
            VTT_Sub_Link_Main = str(head)+'.vtt'
            q3 = requests.get(VTT_Sub_Link_Main)
            soup3 = str(BeautifulSoup(q3.text,"lxml"))
            Subs_Data = soup3.replace('.',',').replace("<html><body><p>WEBVTT\n","").replace("--&gt;","-->").replace("</p></body></html>","").encode('utf8') # Conversion from VTT to SRT process 1
            File_Name = re.sub('[^A-Za-z0-9\-\ ]+', '', Final_EP_Num) +'.srt' # Fix for "Special Characters" in The series name
            text_file = open(File_Name, "w")
            text_file.write(Subs_Data)
            text_file.close()
            with open(File_Name,'r+') as f: # A HUGE thanks to fiskenslakt (https://www.reddit.com/user/fiskenslakt) for this "VTT" to "SRT conversion". Read his contribution here : https://www.reddit.com/r/learnpython/comments/4i380g/add_line_number_for_empty_lines_in_a_text_file/
                lines = f.readlines()
                newLineCount = 0
                for i,num in enumerate(lines): 
                    if num == '\n':
                        newLineCount += 1
                        lines[i] = str(newLineCount) + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line+'\n')

            
            print 'Subs Have Been Downloaded\n'



#url = 'http://www.hulu.com/grid/oh-my-ghostess?video_type=episode'
def create_driver():
    driver = webdriver.PhantomJS(service_args=['--load-images=no'])
    return driver
    #options = webdriver.ChromeOptions()
    #options.add_extension('adblockpluschrome-1.11.0.1591.crx')
    #driver = webdriver.Chrome(chrome_options=options, service_args=["--verbose", "--log-path=Main_Log_File.log"])

def Batch_Links_Fetcher(driver,url_main):
    print "Will Be Downloading The Subs For Whole Series ...\n"
    #print url_main
    driver.get(url_main)
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML").encode('utf-8')
    #print "Checking the Source Page Currently..."
    BSoup = BeautifulSoup(source_code,"html.parser")
    EP_ID = BSoup.find_all('div',{'class':'thumbnail'})
    #print "Found the Elements, checking the links now!"
    f2 = open('TempLinks.txt','w')
    for links in EP_ID:
        #print links
        f2.write(str(links)+'\n')
    #print "Found All the required data for finding links..."
    f2.close()
    f3 = open('Episode_Links.txt','w')
    print "Writing Links to the File...\n"
    with open('TempLinks.txt','r') as searchfile:
        for lines in searchfile:
            left,sep,right = lines.partition('/watch/') #Looking For "Content_id" in the <meta content="http://ib3.huluim.com/video/60585710?region=US&amp;size=600x400" property="og:image"/> (60585710 is Con_id)
            if sep:
                OG_Title = right
                Splitter = OG_Title.split('"')
                Con_id = Splitter[0].strip().replace('\n','')
                Final_Episode_Link = "http://www.hulu.com/watch/"+str(Con_id)
                f3.write(str(Final_Episode_Link)+'\n')
    f3.close()
    os.remove('TempLinks.txt')
     
def Batch_Link_Downloader():
    Episode_File = open('Episode_Links.txt','r')
    file = open("newfile.txt", "w")
    for line in Episode_File:
        Link = line.rstrip('\n')
        q = requests.get(Link)
        soup = BeautifulSoup(q.text,"lxml")
        file.write(soup.encode("utf8") + "\n")
        Data_Lookup()
        Con_id,Final_EP_Num = Data_Lookup()
        Sub_Lookup(Con_id,Final_EP_Num)
    file.close()
    Episode_File.close()
    os.remove('newfile.txt')
    os.remove('Episode_Links.txt')
    

def main():
    try:
        try:
            url = raw_input("Please enter your Link : ")
            if url:
                Hulu_Episode_Regex = r'http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/watch/)[\d]'
                Hulu_Show_Regex = r'http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/)[a-z\-]+'
                #Hulu_Show_Grid_Link = r'http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/grid/)[a-z\-]+\?(video_type=episode)'
                Hulu_Episode = re.match(Hulu_Episode_Regex,url)
                Hulu_Show = re.match(Hulu_Show_Regex,url)

                if Hulu_Episode:
                    #print 'Single'
                    Url_And_Data_Fetcher(url)
                    Data_Lookup()
                    Con_id,Final_EP_Num = Data_Lookup()
                    os.remove("newfile.txt")
                    Sub_Lookup(Con_id,Final_EP_Num)
                elif Hulu_Show:
                    #print 'Batcher'
                    url_partition = url.split('/')
                    #print url_partition
                    url_main = str(url_partition[0])+'//'+str(url_partition[2])+'/grid/'+str(url_partition[3])+'?video_type=episode'
                    #print url_main
                    driver = create_driver()
                    Batch_Links_Fetcher(driver,url_main)
                    driver.quit()
                    Batch_Link_Downloader()

            if not url:
                raise ValueError('Please Enter A Link To The Video. This Application Will now Exit in 5 Seconds.')
        except ValueError as e:
            print(e)
            time.sleep(5)
            sys.exit()

    except Exception, e:
        raise e

if __name__ == "__main__":
   main()
