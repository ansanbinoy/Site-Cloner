from subprocess import call
from time import sleep
call(["clear"])
print ("\033[1;32;40m")
print ("""    ____   _   __             _____   __                      
  / __/  (_) / /_ ___  ____ / ___/  / / ___   ___  ___   ____
 _\ \   / / / __// -_)/___// /__   / / / _ \ / _ \/ -_) / __/
/___/  /_/  \__/ \__/      \___/  /_/  \___//_//_/\__/ /_/   
                                                             """)
print ("\t\t\t\t\tBy [<shadow|anon>]")
print ("")
print ("")
print ("")
#a = input ("[+] Enter target site:-->")
try :
	a = input("[+] Enter target site:-->")
	for i in range(3):
		d = '.'*i*1
		sleep(1)
		print ("[-]Cloning.."+d)
	call(["wget", "-mk",a])
	sleep(1.5)
except IOError as e:
	sleep(1)
	print ("[!] Error found",e)                                                                 