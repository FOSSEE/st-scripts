#!/usr/bin/env python
# This script generates two column format from the script file. 
import re, optparse

num = 0
content = {}

def parse_script(script):
    """Parse the file, and get each cell's content into a dictionary."""
    where = 'HEAD'
    txt = ''
    global num
    for line in open(script):
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
    content[where] = txt  # Saving the content of the last cell. 

def write_two_col(content, two_col):
    """ Write the content to a file, in two column format."""
    f = open(two_col, 'w')
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
        ltext.extend(['']*(len(rtext) - len(ltext)))
        rtext.extend(['']*(len(ltext) - len(rtext)))

        # Write each of the lines in respective columns
        for k in range(len(ltext)):
            f.write("| %-80s | %-80s |\n" %(ltext[k], rtext[k]))

        # Horizontal division
        f.write("+%s+%s+\n" %('-'*82, '-'*82))

    f.close()

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-i", default="script.rst", dest="input",
                      help="Input file. 'script.rst' is used by default.")
    parser.add_option("-o", default="script2col.rst", dest="output",
                      help="Output file. script2col.rst is used by default.")

    parser.description = """Converts a script file into two column format."""

    parser.epilog = \
    """Make sure that you check the validity of the formatting of both
the INPUT and the OUTPUT files, using rst2html. Also, Make sure that
each line, in the INPUT file, is less than 80 chars long."""
    
    (options, args) = parser.parse_args()

    script, two_col = options.input, options.output

    parse_script(script)
    write_two_col(content, two_col)

    print "Converted %s to 2 column format and saved as %s" %(script, two_col)
