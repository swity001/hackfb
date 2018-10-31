import os, sys

print ("\033[1;32mMasukan UserName&Password TOD :3")
print ("\033[1;31;1mKalo Gak Tau Pm Swity 089699989010")
print ("\033[1;31;1mBTW LU KONTOL")
username = 'Swity'      
password = 'Ganteng'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mHello Welcome To Tools KONTOL", 
			sys.exit()

		else:
			print "\n\033[1;36mSorry Invalid Password !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
os.system ('then')
print "Installing Tools Hack FB Bertarget"
print "======================================"
print "Author : Swity"
print "Contac me :089699989010"
print "Cyber Layers Team"
print "please subscribe our youtube channel"
print "CyberLayersTeam"
print "======================================"
print "error 404"
print "Lu kebanyakan Coly"
