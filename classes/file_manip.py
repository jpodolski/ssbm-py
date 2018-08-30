## @file file_manip.py @author Jeff Podolski @todo
#   - [ ] Windows Filesystem Support (!)
#   - [-] Teams combo output
#   - [X] Pickle Compression
#   - [ ] Configure with global "OS" variable

# ==============================================================================
"""

FILE_MANIP.PY

Attribution 4.0 International (CC BY 4.0)

All code below is free and open source, intended to better the smash community. You
are free to copy, modify, and redistribute this code as long as credit is given to
the original author (Jeff Podolski). Check out the source!

Github Repo: http://github.com/jpodolski/ssbm-py Sharing License:
https://creativecommons.org/licenses/by/4.0/

"""
# ==============================================================================

from PIL import Image
from classes.load_session import *
import classes.settings
# import fileinput to be added with Pickle implimentation

def write_css():
    """ Writes out css files used for html output. Pretty limited right now """
    #hopefully removing player_frame doesn't break anything
    alignment = ["right", "left"]
    for i in range(0, 4):
        with open("templates/tag.css", 'r') as in_file:
            filedata = in_file.read()
        filedata = filedata.replace('$ALIGN', alignment[(i+1)%2])
        with open("obs/html/css" + str(i+1) + ".css", 'w') as out_file:
            out_file.write(filedata)

def write_html_tags(player_frames):
    """ Reads in a template and modifies it with the proper information """
    for i in range(0, 4):
        with open("templates/tag.html", 'r') as in_file:
            filedata = in_file.read()
        filedata = filedata.replace('$PLAYER', player_frames[i].get_tag())
        filedata = filedata.replace('$CSS', "css" + str(i+1) + ".css")
        with open("obs/html/p" + str(i+1) + "_tag.html", 'w') as out_file:
            out_file.write(filedata)

def gen_char_filename(char, sub_color):
    """ returns a string containing the path for outputting the path to write icons """
    return "media/stock/" + str(char-1) + "_" + str(sub_color) + ".png"

def write_stock_icons(player_frames):
    """ writes out stock icons to file defined by gen_char_filename() """
    for i in range(0, 4):
        filename = gen_char_filename(player_frames[i].get_char(),
                                     player_frames[i].get_sub_color())
        stock = Image.open(filename)
        stock.save("obs/images/p" + str(i+1) + "_char.png", "PNG")

def write_team_image(dashboard):
    """ writes out team images selected by the dropdown in dashboard """
    for i in range(0, 2):
        filename = "media/team_labels/" + dashboard.selected_teams[(i-1)] + ".png" 
        stock = Image.open(filename)
        stock.save("obs/images/team" + str(i+1) + ".png", "PNG")

def write_player_tags(player_frames):
    """ outputs plain text tags from player_frame data """
    for i in range(0, 4):
        temp_file = open("obs/text/p" + str(i+1) + "_tag.txt", "w")
        temp_file.write(player_frames[i].get_tag())
        temp_file.close()

def write_doubles_combotags(player_frames):
    """ outputs combined team tags from player_frame data and W/L dropdown in dashboard """
        # NOT FUNCTIONAL. NEEDS WORK
    for i in range(0, 2):
        temp_file = open("obs/text/teamA" + str(i+1) + "_tags.txt", "w")
        temp_file.write(player_frames[i].get_tag())
        temp_file.close()

def write_arbitrary_text(filename, text_string):
    """ outputs text to a file using arguments for both """
    temp_file = open("obs/text/" + filename + ".txt", "w")
    temp_file.write(text_string)
    temp_file.close()

def write_stream_info(info_array):
    """ writes the files for info stored in the stream info tab """
    for i in range(0,4):
        write_arbitrary_text(info_array[i][0], info_array[i][1].get())

def write_player_tags_doubles_formatA(player_frames):
    """ outputs plain text tags from player_frame data into 4 files """
    for i in range(0, 4):
        temp_file = open("obs/text/p" + str(i+1) + "_tag.txt", "w")
        temp_file.write("[P"+player_frames[i].get_port()+"] "+player_frames[i].get_tag())
        temp_file.close()

def write_player_prefixes(player_frames):
    """ outputs plain text tags from player_frame data """
    for i in range(0, 4):
        temp_file = open("obs/text/p" + str(i+1) + "_prefix.txt", "w")
        temp_file.write(player_frames[i].get_prefix())
        temp_file.close()

def write_scores(side, score):
    """ outputs plain text scores from player_frame data """
    temp_file = open("obs/text/score_" + str(side+1) + ".txt", "w")
    temp_file.write(str(score))
    temp_file.close()

def write_general_text(path, content):
    with open("obs/text/"+path, 'w') as out_file:
        out_file.write(content)

def update(dashboard):
    """ calls all the write/output related functions """
    # NEEDS SUPPORT FOR SCENES, SAVE MANAGEMENT, ETC.
    write_scores(0, dashboard.score_frames[0].get_score())
    write_scores(1, dashboard.score_frames[1].get_score())
    write_stock_icons(dashboard.player_frames)
    write_player_tags(dashboard.player_frames)
    write_player_prefixes(dashboard.player_frames)
    write_css() #again, hopefully not broken
    write_html_tags(dashboard.player_frames)
    write_team_image(dashboard)
    export_dashboard(dashboard)