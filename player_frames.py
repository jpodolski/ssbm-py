import tkinter as tk

class PlayerFrames(top) {
	for n in range (0, 4):
		pframe = ttk.LabelFrame(f1, text = "Player " + str(n+1))
		pframe.grid(column = math.floor(n/2), row = n%2)
		player_frames.append(pframe)

		tag_label = ttk.Label(player_frames[n], text="Tag:")
		tag_label.grid(row = 0, column = 0, sticky = W)

		port_label = ttk.Label(player_frames[n], text="Port:")
		port_label.grid(row = 1, column = 5, sticky = W)

		prefix_label = ttk.Label(player_frames[n], text="Prefix:")
		prefix_label.grid(row = 0, column = 2, columnspan=2, sticky = W)

		tag = ttk.Entry(player_frames[n])#, bd = 1)
		tag.grid(row = 0, column = 1, columnspan = 1)

		prefix = ttk.Entry(player_frames[n])#, bd = 1)w
		prefix.grid(row = 0, column = 3, columnspan = 4)

		port_dropdown = ttk.OptionMenu(player_frames[n], port[n], command = lambda _: update_character(current_match, n), *ports)
		port_dropdown.grid(row = 1, column = 6, columnspan = 1, sticky = EW)

		char_dropdown = ttk.OptionMenu(player_frames[n], char[n], command = lambda _: update_character(current_match, n), *character_names)
		char_dropdown.grid(row = 1, column = 0, columnspan = 2, sticky = EW)


		char_prevcolor = ttk.Button(player_frames[n], text = "<", width=1)
		char_prevcolor.config(command = lambda i=n: inc_color(current_match, i, -1))
		char_prevcolor.grid(row = 1, column = 2)

		char_icon = ttk.Label(player_frames[n], image = tkimgs[n])
		char_icon.grid(row = 1, column = 3)
		char_icons.append(char_icon)

		char_nextcolor = ttk.Button(player_frames[n], text = ">", width=1)
		char_nextcolor.config(command = lambda i=n: inc_color(current_match, i, 1))
		char_nextcolor.grid(row = 1, column = 4)