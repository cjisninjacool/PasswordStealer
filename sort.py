import subprocess
import sys
data = sys.argv[1]

SSID = data
CMD = "Netsh wlan show profile name="+SSID+" key=clear"

OUT = subprocess.check_output(CMD)
COR=((OUT.decode("utf-8")).find("Key Content"))
COR = COR + 25
END = ((OUT.decode("utf-8")).find("Cost settings"))
END = END - 4
SPLICED = OUT.decode("utf-8")[COR:END]
file1 = open("out.txt",'w') 
file1.write(SPLICED)
file1.close
print(SPLICED)