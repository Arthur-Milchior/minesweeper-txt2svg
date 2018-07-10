from  sys import argv
size=35

for input_file in argv[1:]:
  output_file = "%s.svg"%input_file

  def print_inside(c,line,col):
    character_map={i:i for i in ([str(i) for i in range(9)]+["…","⋮","?"])}
    character_map[":"]="⋮"
    character_map[","]="…"
    character_map["_"]=" "
    character_color={
        "0":"brown",
        "1":"blue",
        "2":"green",
        "3":"red",
        "4":"cyan",
        "5":"pink",
        "6":"purple",
        "7":"orange",
        "8":"black",
        "_": "white",
        "?": "red"}
    if c==".":
        x=size*(col+.5)
        y=size*(line+.5)
        return """<circle cx='%d' cy='%d' r='%d'/>"""%(x,y,size/3)
    elif c==" " or c=="\n":
        return ""
    elif c in character_map:
        color = character_color.get(c,"black")
        x=size*(col+.2)
        y=size*(line+.8)
        letter= character_map[c]
        return """<text x="%d" y="%d" fill="%s" style="font-size:25; bold">%s</text>"""%(x,y,color,letter)
    else:
        raise Exception(""""%s" is a character not known in the file"""% c)

  def print_square(line,col):
    x1=size*col
    y1=size*line
    x2=x1+size
    y2=y1+size
    output=""
    for x in [x1,x2]:
        output+="""<line  style="stroke:black;stroke-width:2"  x1="%d" x2="%d" y1="%d" y2="%d"/>"""%(x,x,y1,y2)
    for y in [y1,y2]:
        output+="""<line  style="stroke:black;stroke-width:2"  x1="%d" x2="%d" y1="%d" y2="%d"/>"""%(x1,x2,y,y)
    return output


  def print_all(c,line,col):
    output=print_inside(c,line,col)
    if not output:
        return ""
    return print_square(line,col)+output+"\n"

  longest_line_size=0
  output=""
  with open(input_file) as input:
    line_number=0
    for line in input.readlines():
        col_number=0
        for c in line:
            output+=print_all(c,line_number,col_number)
            col_number+=1
        longest_line_size=max(longest_line_size,col_number)
        line_number+=1
        
  size_x=(longest_line_size-1)*size
  size_y=line_number*size
  output="""<rect x="0" y="0" style="fill:white;stroke-width:0;" width="%d"  height="%d"/>%s"""%(size_x,size_y,output)
  output="""<svg version="1.1"
     baseProfile="full"
     xmlns="http://www.w3.org/2000/svg" width="%d"  height="%d">%s</svg>"""%(size_x,size_y,output)
  with open(output_file, "w") as output_file:
    output_file.write(output)
