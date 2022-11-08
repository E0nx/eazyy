#
# If give this error: [Please contact with support with this error. (Fi-821)], It means the NightMare.py file size not equal with the file size in the database.
#

import wmi ,os.path

f = f = wmi.WMI()

file_exists = os.path.exists('NightMare.py')

def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

f_size = os.path.getsize(r'NightMare.py')
x = convert_bytes(f_size)

print(f'[NightMare] The file size of the injector. ({x})')
