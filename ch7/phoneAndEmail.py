import pyperclip,re

# TODO: Create Phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)
# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    if group[6] != '':
        phoneNum += ' x' + group[6]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')