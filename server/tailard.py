import re
import serial
import paramiko
import select
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('tailard.cfg')


host = config.get('monitor', 'host')
uname = config.get('monitor', 'uname')
pword = config.get('monitor', 'pword')
logfile = config.get('monitor', 'logfile')
serial_path = config.get('monitor', 'serial_path')


p = re.compile('.+ERROR.+')

myserial = serial.Serial(serial_path)

client = paramiko.SSHClient()
client.load_system_host_keys()

client.connect(host, username=uname, password=pword)
transport = client.get_transport()
channel = transport.open_session()
channel.exec_command('tail -f ' + logfile)
while True:
    rl, wl, xl = select.select([channel],[],[],0.0)
    if len(rl) > 0:
        line = channel.recv(80)
        if p.match(line):
            print "ERROR"
            myserial.write("ERROR\n")
            myserial.flushOutput()
