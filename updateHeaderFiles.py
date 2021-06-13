if __name__  == '__main__':
	f = open('headerfiles.txt')
	files = f.readlines()
	f.close()
	f = open('header.html')
	menubarlines = f.readlines()
	for i in range(0, len(files)):
		if (files[i])[len(files[i])-1] == '\n':
			files[i] = (files[i])[0:len(files[i])-1]
	nchanged = 0
	for f in files:
		if not (f[-4:] == "html"):
			f = f + "/index.html"
		fin = open(f)
		lines = fin.readlines()
		fin.close()
		fout = open(f, 'w')
		in_stat = 0;
		for line in lines:
			if line.find("<!-- Start of Header Code -->") != -1 and in_stat == 0:
				print "Changing " + f
				in_stat = 1
				nchanged = nchanged+1
				continue
			elif line.find("<!-- End of Header Code -->") != -1 and in_stat == 1:
				in_stat = 0
				#Write new menubar code
				indirectPath = "../"*(len(f.split("/"))-2)
				for l in menubarlines:
					if l.find("%s") != -1:
						fout.write(l%(indirectPath))
					else:
						fout.write(l)
			elif in_stat == 0:
				fout.write(line)
		fout.close()
	print "Changed %i files"%(nchanged)
