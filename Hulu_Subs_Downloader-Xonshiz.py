#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Xonshiz"
__email__ = "Xonshiz@psychoticelites.com"
__website__ = "http://www.psychoticelites.com"
__version__ = "v3.1"

'''
Found an interesting thread on reddit that helped me convert vtt to srt.
A HUGE thanks to fiskenslakt (https://www.reddit.com/user/fiskenslakt) for this "VTT" to "SRT conversion".
Read his contribution here : https://www.reddit.com/r/learnpython/comments/4i380g/add_line_number_for_empty_lines_in_a_text_file/d2upf5l

'''


"""
#############################################################################################################
# 										FEATURES :															#
#############################################################################################################
#																											#
# 1.) Downloads all the Subtitles available for a series. 													#
# 2.) Puts the files in corresponding directories after downloading the files. 								#
# 3.) Names the files properly. 	 																		#
# 4.) Subtitles downloaded are in SRT format 		 														#
#																											#
#############################################################################################################
# 										FUTURE FEATURES :													#
#############################################################################################################
#																											#
# 1.) Download Batch Subs faster. 																			#
# 2.) Option to download particular episode's subtitle from a series.										#
# 4.) Error Log File creation. 																				#
#																											#
#############################################################################################################
# 										CHANGELOG :															#
#############################################################################################################
#																											#
# 1.) Geo Restriction is no more active. 																	#
# 2.) Subtitles for series with special characters can be downloaded.										#
# 3.) Removed Vtt2SRT (No more needed).						 												#
# 4.) Re-wrote the whole code for better flow.	 															#
# 5.) Downloaded subs are in SRT format now.	 															#
# 6.) Windows Binary added.	 																				#
# 7.) Changed the lookup parameter for the TITLE of the file. Fix for #2 Issue.	 							#
# 8.) Proper directories for a series.											 							#
#																											#
#############################################################################################################	

"""



from selenium import webdriver
import sys,time,os, re,requests, shutil
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')


# Let's ask user for the URL of the Series or an Episode!
def Url_Fetching():

	print '\n'
	print '{:^80}'.format('################################################')
	print '{:^80}'.format('Author : Xonshiz')
	print '{:^80}'.format('################################################\n')


	try:
		url = raw_input('Enter The URL of Series or an Episode :  ')
		if not url:
			print 'Please Enter a Link to Series or an Episode!'
			sys.exit()
		if url:
			return url
			
	except Exception, e:
		#raise e
		print e
		sys.exit()


# Let's fetch the Link and the source code of the video page.
def Url_And_Data_Fetcher(url):
	q = requests.get(url)
	soup = BeautifulSoup(q.text,"lxml")
	file = open(".newfile", "w")
	file.write(soup.encode("utf8") + "\n")
	file.close


# Looking up the "Content_id" for getting our subs and "Title" to name our sub file.
def Data_Lookup():
	with open('.newfile') as searchfile:
		for line in searchfile:
			left,sep,right = line.partition('/video/') #Looking For "Content_id" in the <meta content="http://ib3.huluim.com/video/60585710?region=US&amp;size=600x400" property="og:image"/> (60585710 is Con_id)
			if sep:
				#print sep
				OG_Title = right
				Splitter = OG_Title.split("?")
				Con_id = Splitter[0]
			   # print "Content_id : ",Con_id

	with open('.newfile') as searchfile:
		for line in searchfile:
			left,sep,right = line.partition('<title>')
			if sep:
				Episode_Number = right
				#print Episode_Number
				Final_EP_Num = Episode_Number.replace('Watch','').replace('| Hulu</title>','').replace('Online','').strip()
				print '\n', Final_EP_Num
				#Final_EP_Num = Episode_Number[7:].replace('| Hulu</title>','').replace('>','').replace("Online","")

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
			File_Name = re.sub('[^A-Za-z0-9\-\.\ ]+', '', Final_EP_Num) +'.srt' # Fix for "Special Characters" in The series name

			Series_Splitter = str(Final_EP_Num).split(' - ')
			#print Series_Splitter
			Series_Name = str(Series_Splitter[0]).rstrip()
			#print Series_Name
			Raw_File_Directory = str(Series_Name)
			#print Raw_File_Directory
			File_Directory = re.sub('[^A-Za-z0-9\-\.\'\#\/ ]+', '', Raw_File_Directory) # Fix for "Special Characters" in The series name
			#print File_Directory
			Directory_path = os.path.normpath(File_Directory)
			#print Directory_path

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

			if not os.path.exists(File_Directory):
						os.makedirs(File_Directory)

			File_Path = os.path.normpath(File_Name)
			try:
				shutil.move(File_Path,File_Directory)
			except Exception, e:
				#raise e
				print e,'\n'
				print '\nCannot Move the File!'
				#os.remove(File_Path)
				pass			

			
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
	f2 = open('.TempLinks','w')
	for links in EP_ID:
		#print links
		f2.write(str(links)+'\n')
	#print "Found All the required data for finding links..."
	f2.close()
	
	f3 = open('.Episode_Links','w')
	print "Writing Links to the File...\n"
	with open('.TempLinks','r') as searchfile:
	   #print 'Inside this'
		for lines in searchfile:
			#print lines
			left,sep,right = lines.partition('/watch/') #Looking For "Content_id" in the <meta content="http://ib3.huluim.com/video/60585710?region=US&amp;size=600x400" property="og:image"/> (60585710 is Con_id)
			if sep:
				#print sep
				OG_Title = right
				Splitter = OG_Title.split('?')
				Con_id = Splitter[0].strip().replace('\n','').replace('">','')
			   # print Con_id
				Final_Episode_Link = "http://www.hulu.com/watch/"+str(Con_id)
			   # print Final_Episode_Link
				f3.write(str(Final_Episode_Link)+'\n')
	f3.close()
	#os.remove('TempLinks.txt')
	 

def Batch_Link_Downloader():
	Episode_File = open('.Episode_Links','r')
	file = open(".newfile", "w")
	for line in Episode_File:
		#print line
		Link = line.rstrip('\n')
		url = Link
		print url
		Url_And_Data_Fetcher(url)
		Con_id,Final_EP_Num = Data_Lookup()
		Sub_Lookup(Con_id,Final_EP_Num)
		#q = requests.get(Link)
		#soup = BeautifulSoup(q.text,"lxml")
		#file.write(soup.encode("utf8") + "\n")
		#Data_Lookup()
		#Con_id,Final_EP_Num = Data_Lookup()
		#Sub_Lookup(Con_id,Final_EP_Num)
	file.close()
	Episode_File.close()
	os.remove('.newfile')
	os.remove('.Episode_Links')
	os.remove('.TempLinks')
	

def main():
	try:
		try:
			#url = raw_input("Please enter your Link : ")
			url = Url_Fetching()
			if url:
				Hulu_Episode_Regex = r'http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/watch/)[\d]'
				Hulu_Show_Regex = r'http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/)[a-z\-]+'
				#Hulu_Show_Grid_Link = r'http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/grid/)[a-z\-]+\?(video_type=episode)'
				Hulu_Episode = re.match(Hulu_Episode_Regex,url)
				Hulu_Show = re.match(Hulu_Show_Regex,url)

				if Hulu_Episode:
					#print 'Single'
					Url_And_Data_Fetcher(url)
					Con_id,Final_EP_Num = Data_Lookup()
					#Con_id,Final_EP_Num = Data_Lookup()
					#os.remove("newfile.txt")
					Sub_Lookup(Con_id,Final_EP_Num)
					sys.exit()
				elif Hulu_Show:
					#print 'Hulu doesn\'t let you see the URL for single episode without signing In. Sorry, this will stay down untill I figure out a workaround!'
					#sys.exit()
					#print 'Batcher'
					url_partition = url.split('/')
					#print url_partition
					url_main = str(url_partition[0])+'//'+str(url_partition[2])+'/grid/'+str(url_partition[3])+'?video_type=episode'
					#print url_main
					driver = create_driver()
					Batch_Links_Fetcher(driver,url_main)
					driver.quit()
					Batch_Link_Downloader()
					sys.exit()

			'''
			if not url:
				raise ValueError('Please Enter A Link To The Video. This Application Will now Exit in 5 Seconds.')
			'''	
		except ValueError as e:
			print(e)
			time.sleep(5)
			sys.exit()

	except Exception, e:
		#raise e
		print e
		sys.exit()

if __name__ == "__main__":
   main()



'''

http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/)[a-z\-]+     --> http://www.hulu.com/oh-my-ghostess
http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/watch/)[\d]{6}    --> http://www.hulu.com/watch/815743

'''        
