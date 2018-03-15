from classes.file_manip import *
from classes.settings import *
from pickle import *

def import_dashboard(new_dashboard, load_file):
	session_to_load = pickle.load(open(load_file, "rb"))
	session_to_load.recall_from_save(new_dashboard)
	session_to_load.print_contents()
	new_dashboard.pframe_1.refresh()
	new_dashboard.pframe_2.refresh()
	new_dashboard.pframe_3.refresh()
	new_dashboard.pframe_4.refresh()


def export_dashboard(current_dashboard):
	session_to_save = Snapshot()
	session_to_save.create_from_dashboard(current_dashboard)
	if (current_dashboard.save_name[-3:] != ".ag"):
		pickle.dump(session_to_save, open("saved/"+current_dashboard.save_name+".ag", "wb"))
	else:
		pickle.dump(session_to_save, open("saved/"+current_dashboard.save_name, "wb"))
	session_to_save.print_contents()
	# return session_to_save
