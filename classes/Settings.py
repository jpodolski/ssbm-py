from classes.file_manip import *
import pickle as pickle
import sys, platform

# detect OS, set global __OS
raw_os = sys.platform
if (raw_os.startswith("linux")):
    print ("Linux detected")
    __OS = "linux"
elif (raw_os.startswith("windows")):
    print ("Windows detected")
    __OS = "windows"
elif (raw_os.startswith("darwin")):
    print ("OSX detected")
    __OS = "osx"
else:
	__OS = "unrecognized"


class Settings:
	def __init__(self):
		self.snapshot = SnapShot()
		""" A collection of the data last on the main screen """

		self.obs_path = "undefined"
		""" A path to the user's OBS directory """

		self.scenes = []
		"""	The list of scenes being used """

		self.info_data = []
		""" A collection of data from the information tab """

		self.html_data = []
		""" A collection of data relevant for generating HTML files """

		self.keep_on_top = 1
		""" Floating window """

		self.auto_update_score = 1
		""" If score should update independently of the update button """

class Snapshot:
	def __init__(self):
		self.save_name = "Untitled.ag"
		self.is_doubles = 0
		self.round = "Friendlies"
		self.p1_tag = ""
		self.p2_tag = ""
		self.p3_tag = ""
		self.p4_tag = ""
		self.p1_char = ""
		self.p2_char = ""
		self.p3_char = ""
		self.p4_char = ""
		self.p1_color = ""
		self.p2_color = ""
		self.p3_color = ""
		self.p4_color = ""
		self.p1_prefix = ""
		self.p2_prefix = ""
		self.p3_prefix = ""
		self.p4_prefix = ""
		self.p1_port = ""
		self.p2_port = ""
		self.p3_port = ""
		self.p4_port = ""

	def create_from_dashboard(self, dash_to_save):
		""" set values using current dashboard """
		self.save_name = dash_to_save.save_name

		self.p1_tag = str(dash_to_save.pframe_1.get_tag())
		self.p2_tag = str(dash_to_save.pframe_2.get_tag())
		self.p3_tag = str(dash_to_save.pframe_3.get_tag())
		self.p4_tag = str(dash_to_save.pframe_4.get_tag())
		self.p1_char = dash_to_save.pframe_1.get_char()
		self.p2_char = dash_to_save.pframe_2.get_char()
		self.p3_char = dash_to_save.pframe_3.get_char()
		self.p4_char = dash_to_save.pframe_4.get_char()
		self.p1_color = dash_to_save.pframe_1.get_sub_color()
		self.p2_color = dash_to_save.pframe_2.get_sub_color()
		self.p3_color = dash_to_save.pframe_3.get_sub_color()
		self.p4_color = dash_to_save.pframe_4.get_sub_color()
		self.p1_prefix = str(dash_to_save.pframe_1.get_prefix())
		self.p2_prefix = str(dash_to_save.pframe_2.get_prefix())
		self.p3_prefix = str(dash_to_save.pframe_3.get_prefix())
		self.p4_prefix = str(dash_to_save.pframe_4.get_prefix())

		print(dash_to_save.pframe_1.get_tag())
		print(dash_to_save.pframe_2.get_tag())
		print(dash_to_save.pframe_3.get_tag())
		print(dash_to_save.pframe_4.get_tag())
		print(dash_to_save.pframe_1.get_char())
		print(dash_to_save.pframe_2.get_char())
		print(dash_to_save.pframe_3.get_char())
		print(dash_to_save.pframe_4.get_char())
		print(dash_to_save.pframe_1.get_sub_color())
		print(dash_to_save.pframe_2.get_sub_color())
		print(dash_to_save.pframe_3.get_sub_color())
		print(dash_to_save.pframe_4.get_sub_color())
		print(dash_to_save.pframe_1.get_prefix())
		print(dash_to_save.pframe_2.get_prefix())
		print(dash_to_save.pframe_3.get_prefix())
		print(dash_to_save.pframe_4.get_prefix())


		print(self.p1_tag)
		print(self.p2_tag)
		print(self.p3_tag)
		print(self.p4_tag)
		print(self.p1_char)
		print(self.p2_char)
		print(self.p3_char)
		print(self.p4_char)
		print(self.p1_color)
		print(self.p2_color)
		print(self.p3_color)
		print(self.p4_color)
		print(self.p1_prefix)
		print(self.p2_prefix)
		print(self.p3_prefix)
		print(self.p4_prefix)


	def recall_from_save(self, new_dashboard):
		""" set values using current dashboard """
		new_dashboard.pframe_1.set_char(self.p1_char)
		new_dashboard.pframe_2.set_char(self.p2_char)
		new_dashboard.pframe_3.set_char(self.p3_char)
		new_dashboard.pframe_4.set_char(self.p4_char)
		new_dashboard.pframe_1.set_tag(self.p1_tag)
		new_dashboard.pframe_2.set_tag(self.p2_tag)
		new_dashboard.pframe_3.set_tag(self.p3_tag)
		new_dashboard.pframe_4.set_tag(self.p4_tag)
		new_dashboard.pframe_1.set_sub_color(self.p1_color)
		new_dashboard.pframe_2.set_sub_color(self.p2_color)
		new_dashboard.pframe_3.set_sub_color(self.p3_color)
		new_dashboard.pframe_4.set_sub_color(self.p4_color)
		new_dashboard.pframe_1.set_prefix(self.p1_prefix)
		new_dashboard.pframe_2.set_prefix(self.p2_prefix)
		new_dashboard.pframe_3.set_prefix(self.p3_prefix)
		new_dashboard.pframe_4.set_prefix(self.p4_prefix)
		new_dashboard.pframe_1.refresh()
		new_dashboard.pframe_2.refresh()
		new_dashboard.pframe_3.refresh()
		new_dashboard.pframe_4.refresh()

	def print_contents(self):
		print("TAGS")
		print(self.p1_tag)
		print(self.p2_tag)
		print(self.p3_tag)
		print(self.p4_tag)
		print("CHAR_ID")
		print(self.p1_char)
		print(self.p2_char)
		print(self.p3_char)
		print(self.p4_char)
		print("SUB_COLOR")
		print(self.p1_color)
		print(self.p2_color)
		print(self.p3_color)
		print(self.p4_color)
		print("PREFIX")
		print(self.p1_prefix)
		print(self.p2_prefix)
		print(self.p3_prefix)
		print(self.p4_prefix)
