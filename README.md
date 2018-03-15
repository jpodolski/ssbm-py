# miniGIMR

![screenshot](https://i.imgur.com/o9m1RDO.png)

**miniGIMR** is a python GUI written to help SSBM streamers manage OBS and their overlay. It is currently in pre-alpha (though it technically works). Planned and/or current features include
  - Control over Stock Head Icons, Tags, Prefixes, etc.
  - HTML, CSS and customization options
  - Automatic Scene Switching
  - Setup Wizard for easy configuration
  - Virtual Webcam management
  - Integration with autoGIMR and tinyTafo (stream automation and statkeeping programs, respectively)
  - Support for Bracket/Player import using Challonge and Smash.gg's APIs
  - Keeping various player statistics though stat collection/management tools (tinyTafo)
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

If you'd like to support me and my development for the Smash community, I'd really appreciate it! It will help me buy things like Arduinos, Raspberry Pis, and other neat things I can use to develop more of the Smash software I'm working on. For example there's also autoGIMR, a program that can control match reporting and VoD tagging, simply by interpreting a video stream from a capture card. If you're feeling generous, you can donate through PayPal. Thanks!

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----
">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>


## Legal
This software is licensed under the

[**Attribution-NonCommercial-ShareAlike 4.0 License**](https://creativecommons.org/licenses/by-nc-sa/4.0/)

![logo](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

This license allows you to remix, tweak, and build upon this work non-commercially, as long as you credit this project & its authors, and license new creations under the identical terms.

