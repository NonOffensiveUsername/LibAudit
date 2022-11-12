import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

class Interface():

	def __init__(self, root, ID_manager, report_generator):
		self.window = root
		self.window.title("Library Audit Application")
		self.window.resizable(False, False)

		self.ID_manager = ID_manager

		# Frames

		self.doc_viewer = tk.Frame(
			width = 400,
			height = 500,
			borderwidth = 2,
			relief = "sunken"
		)

		self.side_buttons = tk.Frame()

		self.doc_selectors = tk.Frame()

		self.export_buttons = tk.Frame()

		# Document Selectors

		self.viewed_doc = tk.StringVar()
		self.view_doc_master_entries = ttk.Radiobutton(
			text = "Master ID List",
			variable = self.viewed_doc,
			value = "doc_master_entries",
			master = self.doc_selectors
		)
		self.view_doc_missing_entries = ttk.Radiobutton(
			text = "Missing IDs",
			variable = self.viewed_doc,
			value = "doc_missing_entries",
			master = self.doc_selectors
		)
		self.view_doc_found_entries = ttk.Radiobutton(
			text = "Found IDs",
			variable = self.viewed_doc,
			value = "doc_found_entries",
			master = self.doc_selectors
		)
		self.viewed_doc.set("doc_master_entries")

		# Side Buttons

		self.import_path_label_contents = tk.StringVar()
		self.import_path_label_contents.set("No import path chosen")
		self.import_path_label = tk.Label(textvariable = self.import_path_label_contents, master = self.side_buttons)
		self.btn_import_master = tk.Button(text = "Import Master ID List", command = self.get_data_path, master = self.side_buttons)
		self.btn_begin_audit = tk.Button(text = "Begin Audit", master = self.side_buttons)
		self.btn_save_session = tk.Button(text = "Save Session", master = self.side_buttons)
		self.btn_load_session = tk.Button(text = "Load Session", master = self.side_buttons)

		# Export Button

		self.btn_export_doc = tk.Button(text = "Export Current Document", master = self.export_buttons)
		self.btn_export_dates = tk.Button(text = "Export Audit Dates", master = self.export_buttons)

		# Widget Layout

		self.doc_selectors.grid(row = 0, column = 0, sticky = "w")
		self.view_doc_master_entries.pack(side = tk.LEFT, padx = 5, pady = 5)
		self.view_doc_missing_entries.pack(side = tk.LEFT)
		self.view_doc_found_entries.pack(side = tk.LEFT)

		self.doc_viewer.grid(row = 1, column = 0)

		self.side_buttons.grid(row = 1, column = 1, sticky = "n")
		self.import_path_label.pack(fill = tk.X)
		self.btn_import_master.pack(fill = tk.X)
		self.btn_begin_audit.pack(fill = tk.X)
		self.btn_save_session.pack(fill = tk.X)
		self.btn_load_session.pack(fill = tk.X)

		self.export_buttons.grid(row = 2, column = 0, sticky = "w")
		self.btn_export_doc.pack(side = tk.LEFT)
		self.btn_export_dates.pack(side = tk.LEFT)

		# Hand Control to Window

		self.window.mainloop()

	def get_data_path(self):
		path = filedialog.askopenfilename()
		self.ID_manager.set_path(path)
		self.import_path_label_contents.set(path)
