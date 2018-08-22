#!/usr/bin/python3

## @file scene_manager.py
## @author Jeff Podolski
## @todo
#   - All of it

# ==============================================================================
"""
SCENE_MANAGER.PY

Attribution 4.0 International (CC BY 4.0)
All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!
Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/
"""
# ==============================================================================

class SceneObject(object):  # pylint: disable=too-few-public-methods
	def __init__(self, init_name, init_id, init_index, parent_frame):
		self.scene_name = init_name
		self.scene_id = init_id
		self.scene_index = init_index
		self.scene_x = self.scene_index%2
		self.scene_y = self.scene_index//2
		self.scene_object = ttk.Button(self.parent_frame,
                                        text=scene_name,
                                        width=15,
                                        style="BW.TButton",
                                        command=lambda: scene_button_functionality(self,
                                                                                   scene_id,
                                                                                   self.delete_mode))
		def get_button(self):
			return self.scene_object

		def get_id(self):
			return self.scene_id

		def get_name(self):
			return self.scene_name

		def refresh_position(self):
			self.scene_x = self.scene_index%2
			self.scene_y = self.scene_index//2
			self.scene_object.grid(row=self.scene_y, column=self.scene_x)
