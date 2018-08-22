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

class SceneManager(object): # pylint: disable=too-few-public-methods
	self.scene_count = 0
	self.scene_objects = []

	def push(self, new_scene):
		scene_objects[scene_count+1] = new_scene
		scene_count+=1

	def pop_n_fill(self, ):
		scene_objects