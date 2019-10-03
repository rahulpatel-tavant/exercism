import re

def add_heading_tag(line):
    heading_type = len(line.split(' ')[0])
    return '<h%s>%s</h%s>'%(heading_type, line[(heading_type + 1):], heading_type)

def  add_paragraph_tag(line):
    return '<p>%s</p>'%line

def add_italic_tag(line):
    m = re.match('(.*)_(.*)_(.*)', line)
    return (m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3))

def add_strong_tag(line):
    m = re.match('(.*)__(.*)__(.*)', line)
    return (m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3))

def add_list_tag(line):
    m = re.match(r'\* (.*)', line)
    return '<li>' + m.group(1) + '</li>'
    

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    prev_line = ''
    temp = ''
    for line in lines:
        m = re.match(r'\* (.*)', line)
        if line[0] == '#':
            line = add_heading_tag(line)
        elif re.match(r'\* (.*)', line):
            line = add_list_tag(line)   
        else:
            line = add_paragraph_tag(line)

        if re.match('(.*)__(.*)__(.*)', line):
            line = add_strong_tag(line)

        if re.match('(.*)_(.*)_(.*)', line):
            line = add_italic_tag(line)

        if re.match('<li>', line) and not re.match('<li>', prev_line):
            temp = line
            line = "<ul>" + line

        if not re.match('<li>', line) and re.match('<li>', prev_line):
            line = '</ul>' + line   

        prev_line = temp or line
        res += line

    return res + '</ul>' if re.match('<li>', line) else res
