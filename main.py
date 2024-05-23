import tkinter as tk
from tkinter import ttk

def load_commands(filename):
    commands = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                category, command, description, params = line.split(': ')
                if category not in commands:
                    commands[category] = {}
                commands[category][command.strip()] = {'description': description.strip(), 'params': params.strip()}
    return commands

def get_command_description(command):
    os_type = os_var.get()
    category = category_var.get()
    if os_type in commands_dict and category in commands_dict[os_type]:
        return commands_dict[os_type][category][command]['description'], commands_dict[os_type][category][command]['params']
    return "No description available", "No parameters available"

def update_commands_dropdown(event):
    category = category_var.get()
    os_type = os_var.get()
    commands = sorted(commands_dict[os_type][category].keys())
    command_dropdown['values'] = commands
    command_var.set('')  # Reset command selection

# Function to display command info
def display_command_info():
    command = command_var.get()
    description, params = get_command_description(command)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Command: {command}\n")
    output_text.insert(tk.END, f"Description: {description}\n")
    output_text.insert(tk.END, f"Parameters: {params}\n")
    output_text.insert(tk.END, "\nUse case scenario:\n")
    output_text.insert(tk.END, f"Example: {command} {params}")

# Function to clear all inputs and output
def clear_all():
    category_var.set('')
    command_var.set('')
    output_text.delete(1.0, tk.END)

# Load commands from text files
kali_commands = load_commands('kali_commands.txt')
ubuntu_commands = load_commands('ubuntu_commands.txt')
centos_commands = load_commands('centos_commands.txt')
fedora_commands = load_commands('fedora_commands.txt')
arch_commands = load_commands('arch_commands.txt')

# Initialize main dictionary
commands_dict = {
    'kali': kali_commands,
    'ubuntu': ubuntu_commands,
    'centos': centos_commands,
    'fedora': fedora_commands,
    'arch': arch_commands
}

# GUI setup
root = tk.Tk()
root.title("Linux Command Info Viewer")

# OS selection
os_frame = tk.Frame(root)
os_frame.pack(fill='x', padx=10, pady=5)
os_var = tk.StringVar(value='kali')
tk.Radiobutton(os_frame, text="Kali", variable=os_var, value='kali', command=lambda: update_commands('kali')).pack(side='left')
tk.Radiobutton(os_frame, text="Ubuntu", variable=os_var, value='ubuntu', command=lambda: update_commands('ubuntu')).pack(side='left')
tk.Radiobutton(os_frame, text="CentOS", variable=os_var, value='centos', command=lambda: update_commands('centos')).pack(side='left')
tk.Radiobutton(os_frame, text="Fedora", variable=os_var, value='fedora', command=lambda: update_commands('fedora')).pack(side='left')
tk.Radiobutton(os_frame, text="Arch", variable=os_var, value='arch', command=lambda: update_commands('arch')).pack(side='left')

# Category dropdown
category_var = tk.StringVar()
tk.Label(root, text="Command Category:").pack()
category_dropdown = ttk.Combobox(root, textvariable=category_var)
category_dropdown.pack(fill='x', padx=10, pady=5)
category_dropdown.bind("<<ComboboxSelected>>", update_commands_dropdown)

# Command dropdown
command_var = tk.StringVar()
tk.Label(root, text="Command:").pack()
command_dropdown = ttk.Combobox(root, textvariable=command_var)
command_dropdown.pack(fill='x', padx=10, pady=5)

# Display info button
display_button = tk.Button(root, text="Display Info", command=display_command_info)
display_button.pack(pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack(pady=5)

# Output text display
output_text = tk.Text(root, height=10, wrap='word')
output_text.pack(fill='both', padx=10, pady=10)

# Function to update commands based on OS selection
def update_commands(os_type):
    category_dropdown['values'] = list(commands_dict[os_type].keys())
    category_var.set('')
    command_var.set('')
    command_dropdown.set('')
    output_text.delete(1.0, tk.END)

# Run the application
root.mainloop()
