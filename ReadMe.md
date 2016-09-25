# Hulu Subs Downloader
Little Python Script to download subtitles from hulu. Made for educational purposes (yeah,right).

Note : Hulu won't let logged out users to access the "Links" to single episodes. This caused the batch subs ripper to be shut down.
This will definitely take a shit load amount of time to fix. I'll have to figure out a workaround for this.

Watch How to use this : https://youtu.be/Ymrh99SUpUQ

# Windows Binary (.EXE FILE)

Windows users can download this .rar file which contains the "hulu Subs Downloader.exe" file along with everything else that is needed from this link : [CLICK ME](http://www.multiupfile.com/f/94952d56) (x64)

Just extract this somewhere in a folder (don't extract in C:\\ or the windows drive). And run "Hulu_Subs_Downloader-Xonshiz.exe" and follow the steps mentioned in "How do I do what I have to do?". Binary users don't need anything else to use this.

P.S : The .rar file came out to be 28 MB, which is more than the 25 MB limit on Github, hence, external file host.

# First Things First!

Download the "requirements.txt" in some directory. Open Command Prompt and browse to the directory where you downloaded your requiremenets.txt file and run this command :

`pip install -r requirements.txt`

NOTE : You need to have "PIP" installed in your system and set in the path. Python 2.7.10 should already have this done. Just double check on your end though.


# What do I need to run this thing?

1.) Python 2.7.x

# How do I do what I have to do? (Simple Guide)
Watch this video if you can't get what I wrote below : https://youtu.be/Ymrh99SUpUQ

1.) Run "HuluSubs.py" File. (Run within CMD if you want to see the errors,if any).

2.) Paste the video Link when it asks . For Ex :- http://www.hulu.com/watch/815743 (Single Episode) and http://www.hulu.com/oh-my-ghostess (to download Subs for whole series)

Note :- Remove all the special characters from the URL,if any. Sometimes there are certain special values like "#0#1#78" etc.

3.) After entering the url, press 'ENTER' and sit back while it Downloads the Subs.

4.) Check this folder and you'll see your "SRT" ~~"vtt"~~ Subtitles.

# Known Issues

~1.) No error pops up when there are no subs for a series/episode.~

~2.) Script is slow for "Batch Downloading", because of "PhantomJS" is being used to fetch the OuterHTML of the page.~


# Changelog

1.) Geo Restriction is no more active.

2.) Some Major Bug Fix. (Now, videos with special characters in the title can be ripped, only subs are ripped, and not videos.)

~~3.) Added Vtt2SRT.exe for easy conversion of VTT subs to SRT. (Thanx Luiz for sending the link to EXE)~~

3.) Removed Vtt2SRT (No more needed).

4.) Re-wrote the whole code for better flow.

5.) Downloaded subs are in SRT format now.

6.) Added the "Setup.py" file to fetch external libraries.

7.) Windows Binary added.

8.) Batch ripping of subs for whole series

9.) Changed the lookup parameter for the TITLE of the file. Fix for #2 Issue

10.) Proper directories for a series.

If you have any queries or want me to make a script to automate something, feel free to drop me an email at :
xonshiz[at]psychoticelites.com
