# SSBM Scoreboard

![screenshot](https://i.imgur.com/63XguWR.png)

ssbm-py is a python GUI written to help SSBM streamers manage OBS and their overlay. It is currently in alpha. Planned features include
  - Stock Head Icons, Tags, and Prefixes
  - Automatic Scene Switching 
  - Webcam management
  - Support for Challonge and Smash.gg APIs
  - Keeping H2H and placement statistics though bracket/player management tools
  - JSON formatted objects for Matches, Tounaments, and Players

### Setting up the application

First things first, you'll need to have python3 installed. You can check if you have python3 installed by typing 
```sh
$ which python3
```
..into a terminal window. If you see something like 
```sh
$ /usr/bin/python3
```
Then it's already installed. If you don't see anything, then you need python3. You can download it from the link below:

#[Download Python Here](https://www.python.org/downloads/)

Once you've got python installed, simply start up the program by opening a terminal in the ssbm-py directory, and typing
```sh
python3 gui.py
```
to get started.

### Configuring with OBS

All files are saved to the OBS/ directory, and your media in OBS should be linked to these files. Text files are generated for player tags, sponsors, and ports, and images for character icons and team names.

### Authors
Primary authorship and documentation was done by Jeffrey Podolski.

### Legal
This software is licensed under the

[**Attribution-NonCommercial-ShareAlike 4.0 License**](https://creativecommons.org/licenses/by-nc-sa/4.0/)

![logo](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

This license allows you to remix, tweak, and build upon this work non-commercially, as long as you credit this project & its authors, and license new creations under the identical terms.



