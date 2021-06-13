import datetime

#https://registrar.duke.edu/academic-calendar-2015-2016
#FIRSTDAY = datetime.date(2015, 8, 25)
daysstr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
FIRSTDAY = datetime.date(2016, 1, 14)
Ds = [datetime.timedelta(5), datetime.timedelta(2)] #Thursday to Tuesday, Tuesday to Thursday
Holidays = {datetime.date(2015, 10, 13):"Fall Break", datetime.date(2015, 11, 24):"Thanksgiving", datetime.date(2015, 11, 26):"Thanksgiving", datetime.date(2016, 3, 15):"Spring Break", datetime.date(2016, 3, 17):"Spring Break"}

#Put in syllabus header
fin = open("syllabus_begin.html", "r")
fout = open("syllabus.html", "w")
for line in fin.readlines():
    fout.write(line)
fin.close()

#Load in assignments first, which will be peppered throughout the syllabus
fin = open("syllabus_content_assignments.txt", "r")
lines = fin.readlines()
fin.close()
assignments = []
for i in range(len(lines)/3):
    datefields = [int(s) for s in str.split(lines[i*3+2], '-')]
    date = datetime.date(datefields[0], datefields[1], datefields[2])
    assignments.append([date, lines[i*3], lines[i*3+1]])

#Parse syllabus info and order by date
fin = open("syllabus_content_lectures.txt", "r")
lines = fin.readlines()
date = FIRSTDAY
addidx = 0
coloridx = 0
colors = ["#FFCC33", "#DDAA11"]
lecnum = 1

for i in range(len(lines)/4):
    L = [l.rstrip() for l in lines[i*4:(i+1)*4]]
    if L[0] == "SECTION":
        fout.write("<tr><td colspan = \"5\"><BR><h2><b>%s</b></h2>%s</td></tr>\n"%(L[1], L[2]))
    elif L[0] == "LECTURE":
        #Handle holidays
        while date in Holidays:
            color = colors[coloridx]
            day = "Tue"
            if date.weekday() == 3:
                day = "Thu"
                coloridx = (coloridx + 1)%2
            fout.write("<tr><td>--</td><td>%s %i/%i/%i</td><td>%s</td><td></td><td>Enjoy!</td></tr>\n"%(day, date.month, date.day, date.year, Holidays[date]))
            date = date + Ds[addidx]
            addidx = (addidx + 1)%2
        #Ordinary lectures
        color = colors[coloridx]
        day = "Tue"
        if date.weekday() == 3:
            day = "Thu"
            coloridx = (coloridx + 1)%2
        assignmentsDueToday = []
        for a in assignments:
            if a[0] == date:
                assignmentsDueToday.append(a)
        fout.write("<tr bgcolor = %s>"%color)
        fout.write("<td>%i</td>"%lecnum)
        fout.write("<td>%s %i/%i/%i</td>"%(day, date.month, date.day, date.year))
        if len(L[2]) > 0:
            fout.write("<td><a href = \"Lectures/%s\">%s</a></td>"%(L[2], L[1]))
        else:
            fout.write("<td>%s</td>"%L[1])
        fout.write("<td>%s</td>"%L[3])
        fout.write("<td>")
        for a in assignmentsDueToday:
            if len(a[2].strip()) > 0:   
                fout.write("<a href = \"%s\">%s</a>"%(a[2], a[1]))
            else:
                fout.write("%s"%a[1])
        fout.write("</td></tr>\n")
        nextdate = date + Ds[addidx]
        addidx = (addidx + 1)%2
        #Check to see if any assignments are in between this date and the next date
        assignmentsDueInBetween = []
        for a in assignments:
            if (a[0] - date).days > 0 and (nextdate - a[0]).days > 0:
                assignmentsDueInBetween.append(a)
        if len(assignmentsDueInBetween) > 0:
            for a in assignmentsDueInBetween:
                fout.write("<tr bgcolor = #EE9900>")
                fout.write("<td></td><td>%s %i/%i/%i</td><td></td><td></td><td>"%(daysstr[a[0].weekday()], a[0].month, a[0].day, a[0].year))
                if len(a[2].strip()) > 0:
                    fout.write("<a href = \"%s\">%s</a>"%(a[2], a[1]))
                else:
                    fout.write("%s"%a[1])
                fout.write("</td></tr>")
        date = nextdate
        lecnum += 1
fin.close()

#Put in syllabus footer
fin = open("syllabus_end.html", "r")
for line in fin.readlines():
    fout.write(line)
fin.close()
fout.close()
