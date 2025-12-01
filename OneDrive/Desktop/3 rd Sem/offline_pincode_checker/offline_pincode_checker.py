import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

# ---------------------------
# Data structures
# ---------------------------
pincodes = {}          # pincode -> {Officename, District, State}
postoffices = {}       # officename_lower -> {Pincode, District, State}
states = {}            # state -> set(districts)
state_district_offices = {}  # (state, district) -> list of {officename, pincode}

# ---------------------------
# Load CSV file
# ---------------------------
def load_pincodes(file_path):
    global pincodes, postoffices, states, state_district_offices
    pincodes = {}
    postoffices = {}
    states = {}
    state_district_offices = {}

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Check needed columns
            required = {'pincode', 'officename', 'district', 'statename'}
            if not required.issubset(set(reader.fieldnames or [])):
                raise ValueError(f"CSV missing required columns. Need: {', '.join(required)}")

            for row in reader:
                pin = row['pincode'].strip()
                officename = row['officename'].strip()
                district = row['district'].strip()
                state = row['statename'].strip()

                # populate pincodes & postoffices
                pincodes[pin] = {'Officename': officename, 'District': district, 'State': state}
                postoffices[officename.lower()] = {'Pincode': pin, 'District': district, 'State': state}

                # populate state -> districts
                states.setdefault(state, set()).add(district)

                # populate state+district -> offices
                key = (state, district)
                state_district_offices.setdefault(key, []).append({'Officename': officename, 'Pincode': pin})

    except Exception as e:
        messagebox.showerror("Error", f"Error reading CSV file:\n{e}")
        return False

    return True

# ---------------------------
# UI helpers to update dropdowns
# ---------------------------
def on_state_selected(event=None):
    state = state_var.get()
    district_cb['values'] = sorted(states.get(state, []))
    district_var.set('')
    office_cb['values'] = []
    office_var.set('')
    clear_table()

def on_district_selected(event=None):
    state = state_var.get()
    district = district_var.get()
    if state and district:
        offices = state_district_offices.get((state, district), [])
        office_names = sorted([o['Officename'] for o in offices])
        office_cb['values'] = office_names
    else:
        office_cb['values'] = []
    office_var.set('')
    clear_table()

def on_office_selected(event=None):
    clear_table()

# ---------------------------
# Table functions
# ---------------------------
def clear_table():
    for r in tree.get_children():
        tree.delete(r)

def show_by_district():
    clear_table()
    state = state_var.get()
    district = district_var.get()

    if not state:
        messagebox.showwarning("Required", "Please select a State.")
        return
    if not district:
        messagebox.showwarning("Required", "Please select a District.")
        return

    offices = state_district_offices.get((state, district), [])
    if not offices:
        messagebox.showinfo("No results", "No post offices found for that district.")
        return

    for o in sorted(offices, key=lambda x: x['Officename']):
        tree.insert('', 'end', values=(o['Pincode'], o['Officename'], district, state))

def show_by_office():
    clear_table()
    office = office_var.get().strip()
    if not office:
        messagebox.showwarning("Required", "Please select a Post Office.")
        return

    info = postoffices.get(office.lower())
    if not info:
        messagebox.showinfo("No results", "Post Office not found in loaded CSV.")
        return

    tree.insert('', 'end', values=(info['Pincode'], office.title(), info['District'], info['State']))

# Double-click copy pincode to clipboard
def on_row_double_click(event):
    item = tree.identify_row(event.y)
    if not item:
        return
    values = tree.item(item, 'values')
    if values:
        pincode = values[0]
        root.clipboard_clear()
        root.clipboard_append(pincode)
        messagebox.showinfo("Copied", f"Pincode {pincode} copied to clipboard.")

# ---------------------------
# CSV selection
# ---------------------------
def browse_csv():
    file_path = filedialog.askopenfilename(
        title="Select india_pincodes.csv",
        filetypes=[("CSV Files", "*.csv")]
    )
    if not file_path:
        return

    ok = load_pincodes(file_path)
    if ok:
        csv_label.config(text=f"Loaded: {file_path}", fg="green")
        # Populate state combobox
        state_cb['values'] = sorted(states.keys())
        state_var.set('')
        district_var.set('')
        office_var.set('')
        office_cb['values'] = []
        district_cb['values'] = []
        clear_table()
        messagebox.showinfo("Loaded", "CSV loaded successfully!")
    else:
        csv_label.config(text="Failed to load CSV", fg="red")

# ---------------------------
# Build GUI
# ---------------------------
root = tk.Tk()
root.title("Offline Pincode Finder")
root.geometry("1120x680")
root.resizable(False, False)

header = tk.Label(root, text="Pincode Finder (State → District → Post Office)", font=("Helvetica", 16, "bold"))
header.pack(pady=10)

# Top frame
top_frame = tk.Frame(root)
top_frame.pack(fill='x', padx=12)

# CSV browse
btn_frame = tk.Frame(top_frame)
btn_frame.grid(row=0, column=0, sticky='w')

csv_btn = tk.Button(btn_frame, text="Browse CSV File", command=browse_csv, width=18)
csv_btn.grid(row=0, column=0, padx=(0,10))

csv_label = tk.Label(btn_frame, text="No CSV Loaded", fg="red")
csv_label.grid(row=0, column=1, sticky='w')

# Dropdowns frame
dd_frame = tk.LabelFrame(root, text="Filters", padx=10, pady=8)
dd_frame.pack(fill='x', padx=12, pady=10)

state_var = tk.StringVar()
district_var = tk.StringVar()
office_var = tk.StringVar()

tk.Label(dd_frame, text="State:").grid(row=0, column=0, sticky='e', padx=6, pady=6)
state_cb = ttk.Combobox(dd_frame, textvariable=state_var, state='readonly', width=36)
state_cb.grid(row=0, column=1, sticky='w', padx=6, pady=6)
state_cb.bind("<<ComboboxSelected>>", on_state_selected)

tk.Label(dd_frame, text="District:").grid(row=1, column=0, sticky='e', padx=6, pady=6)
district_cb = ttk.Combobox(dd_frame, textvariable=district_var, state='readonly', width=36)
district_cb.grid(row=1, column=1, sticky='w', padx=6, pady=6)
district_cb.bind("<<ComboboxSelected>>", on_district_selected)

tk.Label(dd_frame, text="Post Office:").grid(row=2, column=0, sticky='e', padx=6, pady=6)
office_cb = ttk.Combobox(dd_frame, textvariable=office_var, state='readonly', width=36)
office_cb.grid(row=2, column=1, sticky='w', padx=6, pady=6)
office_cb.bind("<<ComboboxSelected>>", on_office_selected)

# Action buttons
action_frame = tk.Frame(dd_frame)
action_frame.grid(row=0, column=2, rowspan=3, padx=12, sticky='ns')

show_district_btn = tk.Button(action_frame, text="Show District Results", width=20, command=show_by_district)
show_district_btn.pack(pady=(6,8))

show_office_btn = tk.Button(action_frame, text="Show Post Office", width=20, command=show_by_office)
show_office_btn.pack(pady=6)

clear_btn = tk.Button(action_frame, text="Clear Table", width=20, command=clear_table)
clear_btn.pack(pady=6)

# Results table
table_frame = tk.Frame(root)
table_frame.pack(fill='both', expand=True, padx=12, pady=(6,12))

cols = ("Pincode", "Officename", "District", "State")
tree = ttk.Treeview(table_frame, columns=cols, show='headings', height=14)
for c in cols:
    tree.heading(c, text=c)
    # set column widths
    if c == "Pincode":
        tree.column(c, width=100, anchor='center')
    elif c == "Officename":
        tree.column(c, width=300)
    else:
        tree.column(c, width=200)

vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(row=0, column=0, sticky='nsew')
vsb.grid(row=0, column=1, sticky='ns')
hsb.grid(row=1, column=0, sticky='ew')

table_frame.grid_rowconfigure(0, weight=1)
table_frame.grid_columnconfigure(0, weight=1)

# bind double click to copy pincode
tree.bind("<Double-1>", on_row_double_click)

# Start with empty data
csv_path = None

root.mainloop()
