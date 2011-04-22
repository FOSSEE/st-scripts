# This script generates two column format from the script file. 
import re
content = {}
where = 'HEAD'
txt = ''
num = 0

# Parse the file, and get each cell's content.
for line in open('script.rst'):
    if line.startswith('..'):
        loc = re.findall(".. ((L|R)(\d+))", line)
        if loc:
            # Next cell has been found
            # Save previous cell data 
            content[where] = txt

            txt = ''
            where = loc[0][0]
            num = int(loc[0][2]) if int(loc[0][2]) > num else num
            continue
        else:
            pass
    txt += line

# Write the content to the file. 
f = open('script2col.rst', 'w')
f.write('%s' %content['HEAD'])

f.write("\n\n+%s+%s+\n" %('-'*82, '-'*82))
for i in range(1, num+1):
    l = '%s%s' %('L', i)
    r = '%s%s' %('R', i)

    # Split each side text into individual lines
    if l in content:
        ltext = content[l].strip().splitlines()
    else:
        ltext = ['']
    if r in content:
        rtext = content[r].strip().splitlines()
    else:
        rtext = ['']

    # Ensure that both sides have the same number of lines
    ltext.extend(['']*(len(rtext) - len(ltext))), rtext.extend(['']*(len(ltext) - len(rtext)))

    # Write each of the lines in respective columns
    for k in range(len(ltext)):
        f.write("| %-80s | %-80s |\n" %(ltext[k], rtext[k]))

    # Horizontal division
    f.write("+%s+%s+\n" %('-'*82, '-'*82))

f.close()
