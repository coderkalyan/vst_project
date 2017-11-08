#svg = open("test2.svg", "w+")
#svg.write('<?xml version="1.0" encoding="utf-8" ?>\n')
#svg.write('<svg baseProfile="full" height="720" version="1.1" width="1280" xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink"><defs />\n')
#svg.write('<line stroke="rgb(10%,10%,16%)" x1="0" x2="10" y1="0" y2="0" />\n<text fill="red" x="50%" y="50%" font-size="100" text-anchor="middle">Today, Monday, September 22nd, </text>\n')
#svg.write('<text fill="red" x="50%" y="60%" font-size="100" text-anchor="middle">Lols, 3:15-4:15 PM, Gym</text>\n</svg>')
#svg.close()

import moviepy
def title(color, size, text):
    svg2 = open("title.svg", "w+")
    svg2.write('<?xml version="1.0" encoding="utf-8" ?>\n')
    svg2.write('<svg baseProfile="full" width="1280"\n')
    svg2.write('height="720"\n')
    svg2.write('version="1.1"\n')
    svg2.write('xmlns="http://www.w3.org/2000/svg"\n')
    svg2.write('xmlns:ev="http://www.w3.org/2001/xml-events"\n')
    svg2.write('xmlns:xlink="http://www.w3.org/1999/xlink"><defs />\n')
    
    text2 = text.split(" ")
    c=0
    try:
        for j in range(len(text2)):
            if len(text2[c] + " " + text2[c+1]) < 20:
                text2[c] = text2[c] + " " + text2[c+1]
                del text2[c+1]
                print (text2)
            else:
                c=c+1
    except IndexError:
        pass
    
    for i in range(len(text2)):
        print (i)
        print("exec")
        svg2.write('<text fill="{}" x="50%" y="{}%" font-family="Gill Sans" font-weight="bold" font-size="{}" text-anchor="middle">{}</text>\n'.format(color, i*15+40, size, text2[i]))
    
    svg2.write('</svg>')
    svg2.close()

if __name__ == "__main__":    
    title("yellow", 100, "Today, Monday, September 18, Academic Tutoring, 3:15-4:15 PM, Library")