# Hulu Subs Downloader
Little Python Script to download subtitles from hulu. Made for educational purposes (yeah,right).

# Windows Binary (.EXE FILE)

Windows users can download this .rar file which contains the "hulu Subs Downloader.exe" file along with everything else that is needed from this link : https://openload.co/f/Me50lBs8hXo/Hulu_Subs_Downloader.rar
Just extract this somewhere in a folder (don't extract in C:\\ or the windows drive). And run "Hulu_Subs_Downloader-Xonshiz.exe" and follow the steps mentioned in "How do I do what I have to do?". Binary users don't need anything else to use this.


# First Things First!

Please run the "Setup.py" file first. You need to pass an argument with it, so you better run it in a command prompt. It will install all the dependencies required for proper functioning of this script. I've used some external libraries to parse xml and do some stuff. So, run "setup.py" file first. This step needs to be executed only one time. However, if this shows any error, please feel free to contact me via xonshiz@psychoticelites.com

The command : setup.py install

Note : I take it that you are executing it from the same directory.


# What do I need to run this thing?

1.) Python 2.7.x

# Python Libraries Required

1.) BeautifulSoup 4.3.2 (Included Within This Script)

2.) requests (Included Within This Script)

3.) OS (Already There In Python)

4.) sys (Alread There In Python)

5.) re (Alread There In Python)

6.) lxml (Install via the setup.py file)

So, You don't really Need to install or download anything extra.


# How do I do what I have to do? (Simple Guide)
Watch this video if you can't get what I wrote below : https://www.youtube.com/watch?v=iqH_vXMbPHo

1.) Run "HuluSubs.py" File. (Run within CMD if you want to see the errors,if any).

2.) Paste the video Link when it asks . For Ex :- http://www.hulu.com/watch/815743

Note :- Remove all the special characters from the URL,if any. Sometimes there are certain special values like "#0#1#78" etc.

3.) After entering the url, press 'ENTER' and sit back while it Downloads the Subs.

4.) Check this folder and you'll see your "SRT" ~~"vtt"~~ Subtitles.


# Features To Come / Planned Updates

This is a script I made in my free time to ease my job of getting subs for some korean drama series (Yes, I watch 'em).So, I'm not sure if I'll work on this constantly or not.
Anyways, Some planned updates are :

1.) Show Batch Subs Downloading.



# Changelog

1.) Geo Restriction is no more active.

2.) Some Major Bug Fix. (Now, videos with special characters in the title can be ripped, only subs are ripped, and not videos.)

~~3.) Added Vtt2SRT.exe for easy conversion of VTT subs to SRT. (Thanx Luiz for sending the link to EXE)~~

3.) Removed Vtt2SRT (No more needed).

4.) Re-wrote the whole code for better flow.

5.) Downloaded subs are in SRT format now.

6.) Added the "Setup.py" file to fetch external libraries.

If you have any queries or want me to make a script to automate something, feel free to drop me an email at :
xonshiz[at]psychoticelites.com
