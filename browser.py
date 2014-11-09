import urllib
a = 1
b = str(a)
for x in range(0,300):
	if a < 10 :
		b = "00"+str(a)
	elif a >= 10 and a<100 :
 		b = "0"+str(a)
	else :
		b = str(a)
	print b
	id = "201401"+b+".jpg"
	string = "https://10.100.56.31:8443/webapp/intranet/StudentPhotos/201401"+b+".jpg"
	urllib.urlretrieve(string,id)
	b = ""
	a += 1
