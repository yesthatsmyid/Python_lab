import re
import subprocess

# Regular expression to match DD/MM/YYYY format
date_pattern = re.compile(r'^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/([12]\d{3})$')

# Get clipboard contents using subprocess (Linux version)
def get_clipboard_content():
    try:
        return subprocess.check_output(['xclip', '-selection', 'clipboard', '-o'], text=True)
    except subprocess.CalledProcessError:
        return ""

# Get clipboard contents using subprocess (macOS version)
def get_clipboard_content_mac():
    try:
        return subprocess.check_output(['pbpaste'], text=True)
    except subprocess.CalledProcessError:
        return ""

# Get clipboard content based on the platform
if subprocess.run(['which', 'xclip'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
    clipboard_content = get_clipboard_content()
elif subprocess.run(['which', 'pbpaste'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
    clipboard_content = get_clipboard_content_mac()
else:
    print("Clipboard access not available on this platform.")
    exit()

# Find all matches in the clipboard content
date_matches = date_pattern.findall(clipboard_content)

# Function to check if a date is valid
def is_valid_date(day, month, year):
    if month in [4, 6, 9, 11] and day > 30:
        return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return day <= 29
        else:
            return day <= 28
    return day <= 31

# Extract and output valid dates
valid_dates = []
for match in date_matches:
    day, month, year = map(int, match)
    if is_valid_date(day, month, year):
        valid_dates.append(f"{day:02d}/{month:02d}/{year}")

if valid_dates:
    print("Valid dates:")
    for valid_date in valid_dates:
        print(valid_date)
else:
    print("No valid dates found.")
