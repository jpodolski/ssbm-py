# miniGIMR

![screenshot](https://i.imgur.com/o9m1RDO.png)

**miniGIMR** is a python GUI written to help SSBM streamers manage OBS and their overlay. It is currently in pre-alpha (though it technically works). Planned and/or current features include
  - Control over Stock Head Icons, Tags, Prefixes, etc.
  - HTML, CSS and customization options
  - Automatic Scene Switching
  - Setup Wizard for easy configuration
  - Virtual Webcam management
  - Integration with autoGIMR (stream automation based on image recognition)
  - Support for Bracket/Player import using Challonge and Smash.gg's APIs
  - Keeping various player statistics though stat collection/management tools.
  - Autonomous scene switching and overlay control based on fizzi's stat technology or autoGIMR
  - JSON formatted objects and save files for Matches, Tounaments, and Players
  - VoD tools for generating video titles, thumbnails, and timestamps
  - Plenty more bells 'n' whistles

*NOTE: Please understand that as this is an (relatively) untested work-in-progress, and no funcationality or features are guaranteed to work at any point in time. That being said, the master branch **should** almost never recieve an update that breaks any prior functionality.*


## Setting up the application (Unix)
  
First things first, you'll need to have python3 installed. You can check if you have python3 installed by typing 
```sh
$ which python3
```
..into a terminal window. If you see something like 
```sh
$ /usr/bin/python3
```
Then it's already installed. If you don't see anything, then you need python3. You can download it from the link below:

### [Download Python Here](https://www.python.org/downloads/)

Once you've got python installed, you need to install ssbm-py. Open a terminal in the directory you want the program's main folder to be located in, and type 

```sh
$ git clone https://github.com/jpodolski/ssbm-py.git
```

Once everything has downloaded, navigate to the new main folder named ```ssbm-py``` and type

```sh
$ python3 main.py
```

to get started.

*Application and executable bundles coming soon!*

## Configuring with OBS

All generated files OBS needs output by the program are saved to the ``` ssbm-py/obs/ ``` directory, and your media in OBS should be linked to these files. Text files are generated for player tags, sponsors, and ports, and images for character icons and team names. Follow the examples below for adding a text and image source to your broadcast. Note the file paths.

### Example 1

![example1](https://i.imgur.com/oxqxVtY.jpg)


### Example 2

![example2](https://i.imgur.com/2Bb4Uxs.jpg)

## Authors
Primary authorship and documentation was done by Jeffrey Podolski and is licensed under the terms below.

## Donation

If you'd like to support me and my development for the Smash community, I'd really appreciate it! It will help me buy things like Arduinos, Raspberry Pis, and other neat stuff that I can use to develop more of the Smash software I'm working on. For example, I'm also working on a project called *autoGIMR*, a program that can control match reporting and VoD tagging simply by interpreting a video stream from a capture card. If you're feeling generous, you can donate through the PayPal link below, or if not, you can use the software for free!

### [Donate Here!](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=jeffreypodolski%40gmail%2ecom&lc=US&item_name=supporting%20open%2dsource%20Smash%20software%21&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHostedGuest)

## Legal
This software is licensed under the

[**Attribution-NonCommercial-ShareAlike 4.0 License**](https://creativecommons.org/licenses/by-nc-sa/4.0/)

![logo](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

This license allows you to remix, tweak, and build upon this work non-commercially, as long as you credit this project & its authors, and license new creations under the identical terms.

