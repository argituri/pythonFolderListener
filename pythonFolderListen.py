import inotify.adapters
import subprocess

def _main():
	i = inotify.adapters.Inotify()
	i.add_watch('/home/pi/share')
	i.event_gen(yield_nones=False)
#	print(type(i.event_gen(yield_nones=False)))
	for event in i.event_gen(yield_nones=False):
		(_, type_names, path, filename) = event
#		print ("POLKU=[{}] Tiedostonimi=[{}] tyyppi={}".format(
#			path, filename.encode('UTF-8'), type_names))
		str = filename.encode('UTF-8')
		if  str and str[str.index('.'):] == '.wav' and 'IN_CREATE' in type_names:
			print ("wav file added. Starting omxplayer")
			myprocess = subprocess.Popen(['omxplayer',path+"/"+str])

if __name__ == '__main__':  
	_main()
