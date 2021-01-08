# Hulusubs_dl | [![Build Status](https://travis-ci.com/Xonshiz/Hulu-Subs-Downloader.svg?branch=master)](https://travis-ci.com/Xonshiz/Hulu-Subs-Downloader) | [![GitHub release](https://img.shields.io/github/release/xonshiz/Hulu-Subs-Downloader.svg?style=flat-square)](https://github.com/xonshiz/Hulu-Subs-Downloader/releases/latest) | [![Github All Releases](https://img.shields.io/github/downloads/xonshiz/Hulu-Subs-Downloader/total.svg?style=flat-square)](https://github.com/xonshiz/Hulu-Subs-Downloader/releases) [![Open Source Helpers](https://www.codetriage.com/xonshiz/hulu-subs-downloader/badges/users.svg)](https://www.codetriage.com/xonshiz/hulu-subs-downloader)
Hulusubs_dl is a command line tool to download subtitles from Hulu. Made for educational purposes.
Since it's Python based, it can be easily deployed on every platform (Windows, macOS, Linux/Ubuntu etc.).
You can find the installation instructions in #Installation Section of this readme.

**NOTE:**

This tool is based around and work with your hulu account's COOKIES. But, please do remember that you should NEVER share your account cookies with anyone and anywhere.
Person having access to your cookies can use your account. Even when you're sharing any script failure, remember to not share/post your account cookies. 

## Table of Content
* [Prerequisite](#prerequisite)
* [Python Support](#python-support)
* [Usage](#usage)
* [Things To Remember](#things-to-remember)
* [How To Find Hulu Cookie](#how-to-find-hulu-cookie)
* [Walkthrough Video](#walkthrough-video)
* [Installation](#installation)
    * [Windows](#windows-exe-binary-installation)
    * [Linux/Debian/Ubuntu](#linuxubuntukubuntu-or-any-other-linux-flavor-installation)
    * [Mac OS X](#macos)
* [List of Arguments](#list-of-arguments)
* [Supported Formats](#supported-formats)
* [Proxy Usage](#proxy-usage)
* [Opening Issues](#opening-issues)
* [How To Contribute](#how-to-contribute)
* [Donations](#donations)

## Prerequisite:
Since Hulu has now protected their content behind an "auth" wall, we can't access the website. In layman words, we need to log in to Hulu, in order to watch anything or to be able to get basic things to extract the subtitles.
When you run the tool first time, it asks for "cookie" value. You can see it in [`#How To Find Hulu Cookie`](#how-to-find-hulu-cookie) section of this readme.
Also, there's a "configuration file" that is automatically made by this tool. It has some basic settings that you can use as "default" values.
Some values saved in config file are:
- Default Download Location: Tool will download the subtitles files in this directory (the tool makes proper folders).
- Extension: Extension of final subtitle file. You can choose from "Srt, ttml, vtt, smi". Most players will play SRT subtitle files.
- Language: Hulu has 2 languages available at the moment, i.e., "English" & "Spanish". You can download either of them. Type in "en" or "es" for respective languages.

You can specify these values in the file once and then tool will use these defaults. You can use "arguments" to override these anytime. You would need to pass the argument with the script (described later in this readme).

## Python Support
This script should run on both Python 2 and 3. Check travisCI builds for exact python versions.

## Usage
Using this tool can be a little tricky for some people at first, but it's pretty much straightforward. Try to follow along.
Make sure you've gone through [`#Prerequisites`](#prerequisite) and have proper version downloaded and installed on your system from the #Installation section.

## Things To Remember
- You should renew your cookie value from time to time. These cookies expire after some time. So, if you're not able to log in or get the subtitles, try to renew your cookies. Renew cookies meaning, do the steps of [`#How To Find Hulu Cookie`](#how-to-find-hulu-cookie) again.
- If the tool isn't working, always try to download the latest release and then try again. If it still fails, open an issue here.
- Account COOKIES is sensitive data. Never share/post them anywhere.

## How To Find Hulu Cookie
- Make sure you're in US region (use a VPN or Proxy) and open up your browser.
- Go to hulu.com and make sure you're not signed in (If you're signed in, just logout).
- Open developer console (Most browsers have shortcut F12).
- Navigate to "Network" tab.
- Log into hulu now. You'll see that "Network" tab now has many urls populated.
- There should be a "filter" option somewhere in developer console. You need to paste and filter this URL `discover.hulu.com/content/v5/me/state`
- You'll see only some URLs will be there now. Just select anyone of them and in that you need to see "Request Header" section.
- Copy the "Cookie" value from it. It'll be a very long text value. Copy all of it.
- Paste that cookie value when the hulusubs_dl asks for it.

Refer to this screenshot for some clarification:

[![N|Solid](https://i.imgur.com/4Z0KOn4.png)](https://i.imgur.com/4Z0KOn4.png)

## Walkthrough Video
If you're stuck somewhere or need clarification, here's an in-depth video on how to install and use this tool (Windows & Mac).
Video will be sharing in a week or so from now.

## Installation
### Windows EXE Binary Installation
If you're on windows, it's recommended that you download and use "windows exe binary" to save your time.
You can download the latest windows release from [RELEASE SECTION](https://github.com/Xonshiz/Hulu-Subs-Downloader/releases/latest)
Go there and download the ".exe" file. Then follow the usage instructions in [Usage](#usage).
After downloading this exe file, place it in some location that you can access. Because you would need to run this script every time you want to download subtitles.
Don't put this in your "Windows" or "System" folders. It might cause conflicts with permissions.

### Linux/Ubuntu/Kubuntu or any other linux flavor Installation
Since I cannot generate a "binary" for these distributions, you will have to install and use python version directly.
It's pretty much straightforward, you can just use pip to install hulusubs_dl.
`pip install hulusubs_dl`

If for some reason, you're unable to use `pip`, try with `easy_install`. 

If everything fails, you can download code from this repository and then run.
But, now you'll need to install the dependencies yourself. After downloading, navigate to this folder in your terminal and you can see a "requirements.txt" file.
You can install all dependencies via `pip install -r requirements.txt`
All the external dependencies required by this tool are mentioned in that file. You can install them one by one.
Since you're doing things manually, you might need to give this file executable rights, which can be done like this: 
`chmod +x __main__.py`

### MacOS
If you're on macOS, it's recommended that you download and use "macOS binary" to save your time.
You can download the latest macOS release from [RELEASE SECTION](https://github.com/Xonshiz/Hulu-Subs-Downloader/releases/latest)
Go there and download the "hulusubs_dl" file. Do verify that you're not downloading "hulusubs_dl.exe". Then follow the usage instructions in [Usage](#usage).
After downloading this file, place it in some location that you can access. Because you would need to run this script every time you want to download subtitles.
Don't put this in restricted places like "/bin/ or "System" folders. It might cause conflicts with permissions.

## List of Arguments
Currently, the script supports these arguments :

```
-h, --help                             Prints the basic help menu of the script and exits.
-url,--hulu-url                        Url of the Hulu video or series to download subtitles from.
-V,--version                           Prints the VERSION and exits.
-dd,--download-directory               Specifies custom download location for the subtitles.
-cookie, --set-cookie                  Saves/Updates Hulu Cookie
-ext, --subtitle-extension             Specifies the format of final subtitle file. Default is SRT.
-lang, --subtitle-language             Specifies the language of the subtitle to download (subtitle in that language should be available on Hulu).
-skip-conf, --skip-config              Skips reading the config file (default values). Could be handy if you're writing batch scipts.
-proxy, --proxy                        If you have an http/https proxy, you can provide it here. Tool will use this proxy to make all connections to Hulu.
-config, --make-config                 Creates/Resets config file & exits(overwrites current default values).
```

## Supported Formats
Some arguments support some specific range of values. You can see them below here.
Values are separated via ';'.

```
-lang, --subtitle-language : en (default);es
-ext, --subtitle-extension: srt (default);ttml;vtt;smi
```

## Proxy Usage
If you're not in US region and don't want to set up a system wide VPN, then you can provide any http/https proxy and hulusubs_dl would use this proxy to make all connections to Hulu.
Using proxy is simple, you can provide it like this
`python __main__.py -proxy 123.456.789.0123:4444`

If you're on windows, you won't be using `__main__.py`, instead you'll use `hulusubs_dl.exe`. Command would become:
`python hulusubs_dl.exe -proxy 123.456.789.0123:4444`

You can also save proxies in the config file, so that you don't have to pass them as arguments everytime.
Trigger make config via `--make-config` flag and when the tool asks for Proxy, input proxy like this:

Single Proxy : `123.456.789.0123:4444`

Multiple Proxies: `123.456.789.0123:4444;2212.127.11.32:5555` (Notice how we're splitting multiple proxies based on ';')

If you provide multiple proxies, the tool randomly chooses either of the proxies for every connection. This could avoid proxy ban, if you're using this too much.

## Opening Issues
If you're opening a new Issue, please keep these points in your issue description:
- Your operating system (Windows, MacOS, Ubuntu etc.)
- Operating System version: Windows 10/MacOS Catalina/Ubuntu 16 etc.
- Which version are you using: Python Script/Windows EXE Binary/MacOS Homebrew
- URL to the Hulu series which failed.
- Detailed Description of the issue you're facing.

If you're opening an issue to recommend some enhancements/changes, please be as detailed as possible. Also keep these things in mind:
- Will this "enhancement" be good for general public? or is it just for "you"? I cannot develop things just for 1 person. This tool is built for general masses and any custom enhancement would be charged.
- What you're about to write, does it explain the problem and solution properly? IS it enough for anyone to understand?

## How To Contribute
- If you can make this tool better or fix some edge case(s), please feel free to `fork` this repository and then raise a `PR` after your changes.
- Send PRs to `dev` branch only (don't send direct to master).
- Just make sure that the imports are proper, basic python naming conventions are followed.
- Add the necessary information about the change in "changelog.md".
- Remember to bump up the version in __version__.py. (Read how to name the version below).
- If it's just a typo in some file, please just open an issue about it. When I have multiple open issues with typo fixes, I'll make the necessary changes. Reason being that I want to avoid useless CI getting triggered and pushing useless updates across the channel.

### Version Convention
You can find the version in `__verion__.py`. Just update the value according to these rules.

Convention: Year.Month.Date

So, if you're making that PR on 23rd June, 2020, version would be : 2020.06.23

What if you've raised multiple PRs on same day? Simple, just append version for the day like:

Convention: Year.Month.Date.RecurrenceCount

Again, taking example of 23rd June, 2020, let's say you've made 3 different PRs, different versions would be: `2020.06.23.1`, `2020.06.23.2` and `2020.06.23.3`

# Donations
If you're feeling generous, you can donate some $$ via Paypal:

Paypal : [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/xonshiz)

Any amount is appreciated :)


