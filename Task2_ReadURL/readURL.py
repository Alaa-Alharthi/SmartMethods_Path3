from urllib.request import urlopen

link = "http://localhost/robot/move.php"

f = urlopen(link)
myfile = f.read()
print(myfile)