import serial
import time
import sys
import select
import os
from functools import reduce
from threading import Thread
from atcmd import *
from optparse import OptionParser
from datetime import datetime

DEFAULT_WINDOWS_COM = 'COM6'
DEFAULT_LINUX_TTY = '/dev/ttyUSB0'



def bytes2hex(byteArray):     
    return ''.join(hex(i).replace("0x", "0x0")[-2:] for i in byteArray)                            

def print_log(buffer, log_file):
    if log_file is not None: 
        aux = buffer.split('\r\n')
        for i in aux:
            if len(i)>0 and (i[-1]== '\n' or i[-1]=='\r'):
                log_file.write(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f') + ' : ' + i[:-1] + '\n')
            elif len(i)>0:
                log_file.write(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f') + ' : ' + i + '\n')            
   
def at_reader(ser,log_file):
    while True:
        buffer = ''
        while "\r\n" not in buffer:        
            buffer +=  ser.read().decode("utf-8")            
        print(buffer)
        print_log(buffer,log_file)
        process_at_output(buffer,log_file)


def at_cmd(ser,at_command):
    ser.write((at_command + '\r\n').encode())


def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
        
def print_level(dict, tuple_idx):
    total = dict[tuple_idx + ('total',)]
    print(dict[tuple_idx + ('name',)])
    print('\n')
    for  i in range (total):
        print(i,'-', dict[tuple_idx + (i,'name',)])
    print('\n')
 
    if tuple_idx is not (): #if not root menu
        print(99,'-','return')
    print('q','-','quit','\n')   

def print_tree(dict):
    for key, value in dict.items():
        if key[-1] == 'name':
            print(len(key)*'  ',".".join(str(i) for i in key[:-1]),'-',value)


def main():

    global ser
    
    parser = OptionParser()    
    parser.add_option("-m", "--modem", dest="modem", help="modem port (i.e. COMX, ot /dev/ttyUSBX)")
    parser.add_option("-l", "--log", dest="log", help="log to text file")    
    (options, args) = parser.parse_args()

    log_file= None
    if options.log is not None:
        try:          
            log_file = open(options.log,'w') 
        except:
            log_file = None            

  
    try:
        serial_interface = options.modem
    except:
        if sys.platform == "win32":    
            serial_interface = DEFAULT_WINDOWS_COM 
        else:
            serial_interface = DEFAULT_LINUX_TTY    
    try:

        ser = serial.Serial(serial_interface,460800, timeout=0.5,xonxoff=True, rtscts=True, dsrdtr=True, exclusive =True)
        ser.write(('ATE\r\n').encode()) #activate echo by default
        ser.write(('AT+CREG=2\r\n').encode())
        time.sleep(0.5)
        
        ser_reader = Thread(target = at_reader, args = (ser,log_file))
        ser_reader.setDaemon(True)
        ser_reader.start()
        
    except:
        print('error opening the port. exiting.')
        exit(1)
    

    menu_dict = load_menu_dict()
    
    clear()
    level = ()
    print_level(menu_dict, level)
    
    while True:        
        msg = sys.stdin.readline()
        clear()
        if msg == 'q\n':
            if log_file is not None: log_file.close()
            exit(1)  
        elif msg[:-1].isdigit() == True:
            value = int(msg[:-1])
            if level + (value,'total') in menu_dict:
                if menu_dict[level + (value,'total')] == 0:
                    print_level(menu_dict, level) 
                    if type(menu_dict[level + (value,'cli')]) == str:
                        at_cmd(ser,menu_dict[level + (value,'cli')])
                        continue
                    else: #functions                        
                        func, param = menu_dict[level + (value,'cli')][0], menu_dict[level + (value,'cli')][1]
                        ret_val = func(ser, param)                        
                        if ret_val == None: #does not print menu
                            continue
                        elif ret_val == 99 and level !=():
                            level = level[:-1]  
                        elif ret_val == 98 and level !=():
                            pass 
                        elif ret_val == 1000: #print menu tree
                            print_tree(menu_dict)
                            continue                            
                else:                  
                    level += (value,)
                
            elif value == 99 and level != ():
                level = level[:-1]            

        print_level(menu_dict, level)        
    

    
if __name__ == "__main__":    
    main()    