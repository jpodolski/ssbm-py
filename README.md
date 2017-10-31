# miniGIMR

![screenshot](https://i.imgur.com/o9m1RDO.png)

**miniGIMR** is a python GUI written to help SSBM streamers manage OBS and their overlay. It is currently in pre-alpha (though it technically works). Planned features include
  - Stock Head Icons, Tags, and Prefixes
  - Canned formatting and customization options
  - HTML output
  - Automatic Scene Switching 
  - Webcam management
  - Support for Challonge and Smash.gg APIs
  - Keeping H2H and placement statistics though bracket/player management tools
  - JSON formatted objects and save files for Matches, Tounaments, and Players

*NOTE: Please understand that as this is a work-in-progress, no funcationality or features are guaranteed to work at any point in time. That being said, the master branch **should** almost never recieve an update that breaks any prior functionality*


## Setting up the application

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

Once you've got python installed, you need to install ssbm-py. Open a terminal in the directory you want the program to run from (it will create it's own new folder) and enter the following command

```sh
git clone https://github.com/jpodolski/ssbm-py.git
```

Once everything has downloaded, navigate to the main folder labeled ```ssbm-py``` and type

```sh
$ python3 gui.py
```

to get started.

*Application and executable bundles coming soon!*

## Configuring with OBS

All files are saved to the ``` ssbm-py/OBS/ ``` directory, and your media in OBS should be linked to these files. Text files are generated for player tags, sponsors, and ports, and images for character icons and team names. Follow the examples below for adding a text and image source to your broadcast. Note the file paths.

### Example 1

![example1](https://i.imgur.com/oxqxVtY.jpg)


### Example 2

![example2](https://i.imgur.com/2Bb4Uxs.jpg)

## Authors
Primary authorship and documentation was done by Jeffrey Podolski and is licensed under the terms below.

## Legal
This software is licensed under the

[**Attribution-NonCommercial-ShareAlike 4.0 License**](https://creativecommons.org/licenses/by-nc-sa/4.0/)

![logo](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

This license allows you to remix, tweak, and build upon this work non-commercially, as long as you credit this project & its authors, and license new creations under the identical terms.

