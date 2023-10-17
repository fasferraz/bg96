from binascii import hexlify, unhexlify
from bg96_at import *
import time

NB_IOT_NUM_BITS = 9
nbiot_features = '0'
nbiot_features_list = NB_IOT_NUM_BITS*[0]


psm_requested_periodic_rau = ('00000000','')
psm_requested_gprs_ready_timer = ('00000000','')
psm_requested_periodic_tau = ('00000000','')
psm_requested_active_timer = ('00000000','')

edrx_gsm = ('0000','')
edrx_utran = ('0000','')
edrx_lte_m = ('0000','')
edrx_lte_nbiot = ('0000','')

edrx_ptw_gsm = ('0000','')
edrx_ptw_utran = ('0000','')
edrx_ptw_lte_m = ('0000','')
edrx_ptw_lte_nbiot = ('0000','')

error_code = {
    '0': 'Operation sucessful',
    '550': 'Unknown error',
    '551': 'Operation blocked',
    '552': 'invalid parameters',
    '553': 'Memory not enough',
    '554': 'Create socket failed',
    '555': 'Operation not supported',
    '556': 'Socket bind failed',
    '557': 'Socket listen failed',
    '558': 'Socket write failed',
    '559': 'Socket read failed',
    '560': 'Socket accept failed',
    '561': 'Open PDP context failed',
    '562': 'Close PDP context failed',
    '563': 'Socket identity has been used',
    '564': 'DNS busy',
    '565': 'DNS parse failed',
    '566': 'Socket connect failed',
    '567': 'Socket has been closed',
    '568': 'Operation busy',
    '569': 'Operation timeout',
    '570': 'PDP context broken down',
    '571': 'Cancel send',
    '572': 'Operation not allowed',
    '573': 'APN not configured',
    '574': 'Port busy'
}
    
def load_menu_dict():
    global nbiot_features



    menu_dict = {
    ('total',): 7,
    ('name',): 'Options...',
    
    (0,'total') : 15,
    (0,'name'): 'Get Modem Information...',    

    (0,0,'total'): 0,
    (0,0,'name'): 'Get IMSI (AT+CIMI)',    
    (0,0,'cli'): 'AT+CIMI',

    (0,1,'total'): 2,
    (0,1,'name'): 'Get Operator information (AT+COPS) ...',    
    (0,1,0,'total'): 0,    
    (0,1,0,'name'): 'Get current Operator (AT+COPS?)',    
    (0,1,0,'cli'): 'AT+COPS?',
    (0,1,1,'total'): 0,
    (0,1,1,'name'): 'Get all available Operators (AT+COPS=?) (may take time)',    
    (0,1,1,'cli'): 'AT+COPS=?',


    (0,2,'total'): 24,
    (0,2,'name'): 'Get Extended Configuration settings (AT+QCFG) ...',    
    (0,2,0,'total'): 0,
    (0,2,0,'name'):'RATs to be Searched',
    (0,2,0,'cli'): 'AT+QCFG="nwscanmode"',    
    (0,2,1,'total'): 0,
    (0,2,1,'name'):'RAT Searching Sequence',
    (0,2,1,'cli'): 'AT+QCFG="nwscanseq"',
    (0,2,2,'total'): 0,
    (0,2,2,'name'):'Network Category to be searched under LTE RAT (IOT Mode)',
    (0,2,2,'cli'): 'AT+QCFG="iotopmode"',
    (0,2,3,'total'): 0,
    (0,2,3,'name'):'Roam Service',
    (0,2,3,'cli'): 'AT+QCFG="roamservice"',    
    (0,2,4,'total'): 0,
    (0,2,4,'name'):'Band Configuration',
    (0,2,4,'cli'): 'AT+QCFG="band"',
    (0,2,5,'total'): 0,
    (0,2,5,'name'):'LTE Cat NB1 Coverage Enhancement Level',
    (0,2,5,'cli'): 'AT+QCFG="celevel"',
    (0,2,6,'total'): 0,
    (0,2,6,'name'):'Service Domain Configuration',
    (0,2,6,'cli'): 'AT+QCFG="servicedomain"',    
    (0,2,7,'total'): 0,
    (0,2,7,'name'):'Band Scan Priority under LTE Cat NB1',
    (0,2,7,'cli'): 'AT+QCFG="nb1/bandprior"',
    (0,2,8,'total'): 0,
    (0,2,8,'name'):'PSM Entering Indication',
    (0,2,8,'cli'): 'AT+QCFG="psm/urc"',
    (0,2,9,'total'): 0,
    (0,2,9,'name'):'UE SGSN Release Version Configuration',
    (0,2,9,'cli'): 'AT+QCFG="sgsn"',    
    (0,2,10,'total'): 0,
    (0,2,10,'name'):'UE MSC Release Version Configuration',
    (0,2,10,'cli'): 'AT+QCFG="msc"',
    (0,2,11,'total'): 0,
    (0,2,11,'name'):'Establish Multi PDNs with the same APN',
    (0,2,11,'cli'): 'AT+QCFG="pdp/duplicatechk"',
    (0,2,12,'total'): 0,
    (0,2,12,'name'):'NETLIGHT output mode',
    (0,2,12,'cli'): 'AT+QCFG="ledmode"',    
    (0,2,13,'total'): 0,
    (0,2,13,'name'):'IMS Function Control',
    (0,2,13,'cli'): 'AT+QCFG="ims"',
    (0,2,14,'total'): 0,
    (0,2,14,'name'):'RI Behaviour when RING URC is Presented',
    (0,2,14,'cli'): 'AT+QCFG="urc/ri/ring"',
    (0,2,15,'total'): 0,
    (0,2,15,'name'):'RI Behaviour when Incoming SMS URCs are Presented',
    (0,2,15,'cli'): 'AT+QCFG="urc/ri/smsincoming"',    
    (0,2,16,'total'): 0,
    (0,2,16,'name'):'RI Behaviour when Other URCs are Presented',
    (0,2,16,'cli'): 'AT+QCFG="urc/ri/other"',
    (0,2,17,'total'): 0,
    (0,2,17,'name'):'RI Signal Output Carrier',
    (0,2,17,'cli'): 'AT+QCFG="risignaltype"',
    (0,2,18,'total'): 0,
    (0,2,18,'name'):'Delay URC Indication',
    (0,2,18,'cli'): 'AT+QCFG="urc/delay"',    
    (0,2,19,'total'): 0,
    (0,2,19,'name'):'URC Output Port for CMXU',
    (0,2,19,'cli'): 'AT+QCFG="cmux/urcport"',
    (0,2,20,'total'): 0,
    (0,2,20,'name'):'AP_READY PIN',
    (0,2,20,'cli'): 'AT+QCFG="apready"',    
    (0,2,21,'total'): 0,
    (0,2,21,'name'):'Trigger Module into PSM Immediately',
    (0,2,21,'cli'): 'AT+QCFG="psm/enter"',   
    (0,2,22,'total'): 0,
    (0,2,22,'name'):'Abort RRC Connection',
    (0,2,22,'cli'): 'AT+QCFG="rrcabort"',   
    (0,2,23,'total'): 0,
    (0,2,23,'name'):'Configured Features of NB-IoT',
    (0,2,23,'cli'): 'AT+QCFG="nccconf"',       
    
    (0,3,'total'): 3,
    (0,3,'name'): 'Get Network Registration Status (AT+CREG/AT+CGREG/AT+CEREG) ...',    
    (0,3,0,'total'): 0,
    (0,3,0,'name'): 'Get Network Registration Status (AT+CREG)',     
    (0,3,0,'cli'): 'AT+CREG?',    
    (0,3,1,'total'): 0,
    (0,3,1,'name'): 'Get Network Registration Status (AT+CGREG)',     
    (0,3,1,'cli'): 'AT+CGREG?', 
    (0,3,2,'total'): 0,
    (0,3,2,'name'): 'Get EPS Network Registration Status (AT+CEREG)',     
    (0,3,2,'cli'): 'AT+CEREG?', 

    
    (0,4,'total'): 2,
    (0,4,'name'): 'Get Power Saving Mode Settings ...',    
    (0,4,0,'total'): 0,
    (0,4,0,'name'): 'Get Power Saving Mode Settings (AT+CPSMS)',    
    (0,4,0,'cli'): 'AT+CPSMS?',
    (0,4,1,'total'): 0,
    (0,4,1,'name'): 'Get Power Saving Mode Modem Optimization (AT+QPSMEXTCFG)',    
    (0,4,1,'cli'): 'AT+QPSMEXTCFG?',    


    (0,5,'total'): 0,
    (0,5,'name'): 'Get Signaling Connection Status (idle/connected) (AT+QCSCON)',    
    (0,5,'cli'): 'AT+QCSCON?',

    (0,6,'total'): 3,
    (0,6,'name'): 'Get eDRX Settings (AT+CEDRXS/AT+QPTWEDRXS/AT+CEDRXRDP) ...',    
    (0,6,0,'total'): 0,
    (0,6,0,'name'): 'Get e-I-DRX Settings (AT+CEDRXS)',      
    (0,6,0,'cli'): 'AT+CEDRXS?',
    (0,6,1,'total'): 0,
    (0,6,1,'name'): 'Get eDRX / ptw Settings (AT+QPTWEDRXS)',      
    (0,6,1,'cli'): 'AT+QPTWEDRXS?',
    (0,6,2,'total'): 0,
    (0,6,2,'name'): 'Get e-I-DRX Dynamic Settings (AT+CEDRXRDP)',      
    (0,6,2,'cli'): 'AT+CEDRXRDP',

    (0,7,'total'): 3,
    (0,7,'name'): 'Get Latest Time Synchronized through Network (AT+QLTS) ...',    
    (0,7,0,'total'): 0,
    (0,7,0,'name'): 'Latest time that has been synchronized',
    (0,7,0,'cli'): 'AT+QLTS=0',
    (0,7,1,'total'): 0,
    (0,7,1,'name'): 'Current GMT time calculated from the latest time synch',
    (0,7,1,'cli'): 'AT+QLTS=1',
    (0,7,2,'total'): 0,
    (0,7,2,'name'): 'Current LOCAL time calculated from the latest time synch',
    (0,7,2,'cli'): 'AT+QLTS=2',

    (0,8,'total'): 0,
    (0,8,'name'): 'Get Network Information (AT+QNWINFO)',    
    (0,8,'cli'): 'AT+QNWINFO',

    (0,9,'total'): 0,
    (0,9,'name'): 'Get Signal Strength (AT+QCSQ)',    
    (0,9,'cli'): 'AT+QCSQ',

    (0,10,'total'): 0,
    (0,10,'name'): 'Get Clock (AT+CCLK)',    
    (0,10,'cli'): 'AT+CCLK?',

    (0,11,'total'): 0,
    (0,11,'name'): 'Get Temperature (AT+QTEMP)',    
    (0,11,'cli'): 'AT+QTEMP',
    
    (0,12,'total'): 0,
    (0,12,'name'): 'Get IMEI (AT+GSN)',    
    (0,12,'cli'): 'AT+GSN', 

    (0,13,'total'): 0,
    (0,13,'name'): 'Get Product Information (ATI)',    
    (0,13,'cli'): 'ATI',

    (0,14,'total'): 0,
    (0,14,'name'): 'Get ICCID Information (AT+QCCID)',    
    (0,14,'cli'): 'AT+QCCID',   


    
    
    (1,'total') : 14,
    (1,'name'): 'Set Modem Operation...',    
    
    (1,0,'total'): 7,
    (1,0,'name'): 'RAT Search sequence...',    
    (1,0,0,'total'): 0,
    (1,0,0,'name'): 'Automatic',
    (1,0,0,'cli'): 'AT+QCFG="nwscanseq",00',
    (1,0,1,'total'): 0,
    (1,0,1,'name'): 'GSM -> LTE-M -> LTE NB-IoT',
    (1,0,1,'cli'): 'AT+QCFG="nwscanseq",010203',
    (1,0,2,'total'): 0,
    (1,0,2,'name'): 'GSM -> LTE NB-IoT -> LTE-M',
    (1,0,2,'cli'): 'AT+QCFG="nwscanseq",010302',
    (1,0,3,'total'): 0,
    (1,0,3,'name'): 'LTE-M -> GSM -> LTE NB-IoT',
    (1,0,3,'cli'): 'AT+QCFG="nwscanseq",020103',
    (1,0,4,'total'): 0,
    (1,0,4,'name'): 'LTE-M -> LTE NB-IoT -> GSM ',
    (1,0,4,'cli'): 'AT+QCFG="nwscanseq",020301',
    (1,0,5,'total'): 0,
    (1,0,5,'name'): 'LTE NB-IoT -> GSM -> LTE-M',
    (1,0,5,'cli'): 'AT+QCFG="nwscanseq",030102',
    (1,0,6,'total'): 0,
    (1,0,6,'name'): 'LTE NB-IoT -> LTE-M -> GSM',
    (1,0,6,'cli'): 'AT+QCFG="nwscanseq",030201',
    
    (1,1,'total'): 3,
    (1,1,'name'): 'RATs to be searched...',    
    (1,1,0,'total'): 0,
    (1,1,0,'name'): 'Automatic',
    (1,1,0,'cli'): 'AT+QCFG="nwscanmode",0',
    (1,1,1,'total'): 0,
    (1,1,1,'name'): 'GSM Only',
    (1,1,1,'cli'): 'AT+QCFG="nwscanmode",1',
    (1,1,2,'total'): 0,
    (1,1,2,'name'): 'LTE Only',
    (1,1,2,'cli'): 'AT+QCFG="nwscanmode",3',    

    (1,2,'total'): 3,
    (1,2,'name'): 'RATs to be searched under LTE RAT...',    
    (1,2,0,'total'): 0,
    (1,2,0,'name'): 'LTE-M',
    (1,2,0,'cli'): 'AT+QCFG="iotopmode",0',
    (1,2,1,'total'): 0,
    (1,2,1,'name'): 'LTE NB-IoT',
    (1,2,1,'cli'): 'AT+QCFG="iotopmode",1',
    (1,2,2,'total'): 0,
    (1,2,2,'name'): 'LTE-M and LTE NB-IoT',
    (1,2,2,'cli'): 'AT+QCFG="iotopmode",2',  


    (1,3,'total'): 3,
    (1,3,'name'): 'Band...',    
    
    (1,3,0,'total'): 5,
    (1,3,0,'name'): 'GSM...',
    (1,3,0,0,'total'): 0,
    (1,3,0,0,'name'): 'Only GSM 900MHz',
    (1,3,0,0,'cli'): 'AT+QCFG="band",1,0,0',
    (1,3,0,1,'total'): 0,
    (1,3,0,1,'name'): 'Only GSM 1800MHz',
    (1,3,0,1,'cli'): 'AT+QCFG="band",2,0,0',
    (1,3,0,2,'total'): 0,
    (1,3,0,2,'name'): 'Only GSM 850MHz',
    (1,3,0,2,'cli'): 'AT+QCFG="band",4,0,0',
    (1,3,0,3,'total'): 0,
    (1,3,0,3,'name'): 'Only GSM 1900MHz',
    (1,3,0,3,'cli'): 'AT+QCFG="band",8,0,0',
    (1,3,0,4,'total'): 0,
    (1,3,0,4,'name'): 'Any Frequency band',
    (1,3,0,4,'cli'): 'AT+QCFG="band",F,0,0',

    (1,3,1,'total'): 16,
    (1,3,1,'name'): 'LTE-M...',
    (1,3,1,0,'total'): 0,
    (1,3,1,0,'name'): 'Only LTE B1',
    (1,3,1,0,'cli'): 'AT+QCFG="band",0,1,0',
    (1,3,1,1,'total'): 0,
    (1,3,1,1,'name'): 'Only LTE B2',
    (1,3,1,1,'cli'): 'AT+QCFG="band",0,2,0',
    (1,3,1,2,'total'): 0,
    (1,3,1,2,'name'): 'Only LTE B3',
    (1,3,1,2,'cli'): 'AT+QCFG="band",0,4,0',
    (1,3,1,3,'total'): 0,
    (1,3,1,3,'name'): 'Only LTE B4',
    (1,3,1,3,'cli'): 'AT+QCFG="band",0,8,0',
    (1,3,1,4,'total'): 0,
    (1,3,1,4,'name'): 'Only LTE B5',
    (1,3,1,4,'cli'): 'AT+QCFG="band",0,10,0',
    (1,3,1,5,'total'): 0,
    (1,3,1,5,'name'): 'Only LTE B8',
    (1,3,1,5,'cli'): 'AT+QCFG="band",0,80,0',
    (1,3,1,6,'total'): 0,
    (1,3,1,6,'name'): 'Only LTE B12',
    (1,3,1,6,'cli'): 'AT+QCFG="band",0,800,0',
    (1,3,1,7,'total'): 0,
    (1,3,1,7,'name'): 'Only LTE B13',
    (1,3,1,7,'cli'): 'AT+QCFG="band",0,1000,0',
    (1,3,1,8,'total'): 0,
    (1,3,1,8,'name'): 'Only LTE B18',
    (1,3,1,8,'cli'): 'AT+QCFG="band",0,20000,0',
    (1,3,1,9,'total'): 0,
    (1,3,1,9,'name'): 'Only LTE B19',
    (1,3,1,9,'cli'): 'AT+QCFG="band",0,40000,0',
    (1,3,1,10,'total'): 0,
    (1,3,1,10,'name'): 'Only LTE B20',
    (1,3,1,10,'cli'): 'AT+QCFG="band",0,80000,0',
    (1,3,1,11,'total'): 0,
    (1,3,1,11,'name'): 'Only LTE B26',
    (1,3,1,11,'cli'): 'AT+QCFG="band",0,2000000,0',
    (1,3,1,12,'total'): 0,
    (1,3,1,12,'name'): 'Only LTE B28',
    (1,3,1,12,'cli'): 'AT+QCFG="band",0,8000000,0',
    (1,3,1,13,'total'): 0,
    (1,3,1,13,'name'): 'Only LTE B39',
    (1,3,1,13,'cli'): 'AT+QCFG="band",0,4000000000,0',
    (1,3,1,14,'total'): 0,
    (1,3,1,14,'name'): 'Only Any Frequency band',
    (1,3,1,14,'cli'): 'AT+QCFG="band",0,400A0E189F,0',    
    (1,3,1,15,'total'): 0,
    (1,3,1,15,'name'): 'Choose multiple Frequency bands',
    (1,3,1,15,'cli'): (band_choice, 'LTEM'),    

    (1,3,2,'total'): 15,
    (1,3,2,'name'): 'LTE NB-IoT...',
    (1,3,2,0,'total'): 0,
    (1,3,2,0,'name'): 'Only LTE B1',
    (1,3,2,0,'cli'): 'AT+QCFG="band",0,0,1',
    (1,3,2,1,'total'): 0,            
    (1,3,2,1,'name'): 'Only LTE B2',      
    (1,3,2,1,'cli'): 'AT+QCFG="band",0,0,2',
    (1,3,2,2,'total'): 0,            
    (1,3,2,2,'name'): 'Only LTE B3',      
    (1,3,2,2,'cli'): 'AT+QCFG="band",0,0,4',
    (1,3,2,3,'total'): 0,            
    (1,3,2,3,'name'): 'Only LTE B4',      
    (1,3,2,3,'cli'): 'AT+QCFG="band",0,0,8',
    (1,3,2,4,'total'): 0,            
    (1,3,2,4,'name'): 'Only LTE B5',      
    (1,3,2,4,'cli'): 'AT+QCFG="band",0,0,10',
    (1,3,2,5,'total'): 0,            
    (1,3,2,5,'name'): 'Only LTE B8',      
    (1,3,2,5,'cli'): 'AT+QCFG="band",0,0,80',
    (1,3,2,6,'total'): 0,            
    (1,3,2,6,'name'): 'Only LTE B12',     
    (1,3,2,6,'cli'): 'AT+QCFG="band",0,0,800',
    (1,3,2,7,'total'): 0,            
    (1,3,2,7,'name'): 'Only LTE B13',     
    (1,3,2,7,'cli'): 'AT+QCFG="band",0,0,1000',
    (1,3,2,8,'total'): 0,            
    (1,3,2,8,'name'): 'Only LTE B18',     
    (1,3,2,8,'cli'): 'AT+QCFG="band",0,0,20000',
    (1,3,2,9,'total'): 0,
    (1,3,2,9,'name'): 'Only LTE B19',
    (1,3,2,9,'cli'): 'AT+QCFG="band",0,0,40000',
    (1,3,2,10,'total'): 0,
    (1,3,2,10,'name'): 'Only LTE B20',
    (1,3,2,10,'cli'): 'AT+QCFG="band",0,0,80000',
    (1,3,2,11,'total'): 0,
    (1,3,2,11,'name'): 'Only LTE B26',
    (1,3,2,11,'cli'): 'AT+QCFG="band",0,0,2000000',
    (1,3,2,12,'total'): 0,
    (1,3,2,12,'name'): 'Only LTE B28',
    (1,3,2,12,'cli'): 'AT+QCFG="band",0,0,8000000',
    (1,3,2,13,'total'): 0,
    (1,3,2,13,'name'): 'Any Frequency band',
    (1,3,2,13,'cli'): 'AT+QCFG="band",0,0,A0E189F',    
    (1,3,2,14,'total'): 0,
    (1,3,2,14,'name'): 'Choose multiple Frequency bands',
    (1,3,2,14,'cli'): (band_choice, 'NBIOT'),    



    (1,4,'total'): 2,
    (1,4,'name'): 'Service Domain...',    
    (1,4,0,'total'): 0,
    (1,4,0,'name'): 'PS Only',
    (1,4,0,'cli'): 'AT+QCFG="servicedomain",1',
    (1,4,1,'total'): 0,
    (1,4,1,'name'): 'CS & PS',
    (1,4,1,'cli'): 'AT+QCFG="servicedomain",2',
    
    (1,5,'total'): 2,
    (1,5,'name'): 'Enable/Disable PSM Entering Indication...',    
    (1,5,0,'total'): 0,
    (1,5,0,'name'): 'Disable',
    (1,5,0,'cli'): 'AT+QCFG="psm/urc",0',
    (1,5,1,'total'): 0,
    (1,5,1,'name'): 'Enable',
    (1,5,1,'cli'): 'AT+QCFG="psm/urc",1',

    (1,6,'total'): 12,
    (1,6,'name'): 'Configure Features of NB-IoT...',    
    (1,6,0,'total'): 0,
    (1,6,0,'name'): 'Reset bits',
    (1,6,0,'cli'): (nbiot_feature_bit,-1),
    (1,6,1,'total'): 0,
    (1,6,1,'name'): 'Enable EMM_CP_CIOT',
    (1,6,1,'cli'): (nbiot_feature_bit,0),
    (1,6,2,'total'): 0,
    (1,6,2,'name'): 'Enable EMM_UP_CIOT',
    (1,6,2,'cli'): (nbiot_feature_bit,1),
    (1,6,3,'total'): 0,
    (1,6,3,'name'): 'Enable EMM_S1_U',
    (1,6,3,'cli'): (nbiot_feature_bit,2),
    (1,6,4,'total'): 0,
    (1,6,4,'name'): 'Enable EMM_ER_WITHOUT_PDN',
    (1,6,4,'cli'): (nbiot_feature_bit,3),
    (1,6,5,'total'): 0,
    (1,6,5,'name'): 'Enable EMM_HC_CP_CIOT',
    (1,6,5,'cli'): (nbiot_feature_bit,4),
    (1,6,6,'total'): 0,
    (1,6,6,'name'): 'Enable EMM_SMS_ONLY',
    (1,6,6,'cli'): (nbiot_feature_bit,5),
    (1,6,7,'total'): 0,
    (1,6,7,'name'): 'Enable EMM_PNB_CP_CIOT',
    (1,6,7,'cli'): (nbiot_feature_bit,6),
    (1,6,8,'total'): 0,
    (1,6,8,'name'): 'Enable EMM_PNB_UP_CIOT',
    (1,6,8,'cli'): (nbiot_feature_bit,7),
    (1,6,9,'total'): 0,
    (1,6,9,'name'): 'Enable EMM_EPCO_CIOT',
    (1,6,9,'cli'): (nbiot_feature_bit,8),    
    (1,6,10,'total'): 0,
    (1,6,10,'name'): 'Update value in Modem (needed to activate changes)',
    (1,6,10,'cli'): (nbiot_feature_set,None),
    (1,6,11,'total'): 0,
    (1,6,11,'name'):'Show current NB-IoT Features application value',
    (1,6,11,'cli'): (nbiot_feature_show_values,None), 


    (1,7,'total'): 4,
    (1,7,'name'): 'Set Modem functionality (CFUN)...',    
    (1,7,0,'total'): 0,
    (1,7,0,'name'):'Disable (AT+CFUN=0)',
    (1,7,0,'cli'): 'AT+CFUN=0',    
    (1,7,1,'total'): 0,
    (1,7,1,'name'):'Enable (AT+CFUN=1)',
    (1,7,1,'cli'): 'AT+CFUN=1',  
    (1,7,2,'total'): 0,
    (1,7,2,'name'):'Disable the ME from both transmitting and receiving (AT+CFUN=4)',
    (1,7,2,'cli'): 'AT+CFUN=4', 
    (1,7,3,'total'): 0,
    (1,7,3,'name'):'Enable and Reset the ME (AT+CFUN=1,1). Connection with modem will be lost!',
    (1,7,3,'cli'): 'AT+CFUN=1,1',     

    (1,8,'total'): 3,
    (1,8,'name'): 'Set Result Codes...',    
    (1,8,0,'total'): 0,
    (1,8,0,'name'):'Disable result codes (AT+CMEE=0)',
    (1,8,0,'cli'): 'AT+CMEE=0',    
    (1,8,1,'total'): 0,
    (1,8,1,'name'):'Enable result codes and numeric values (AT+CMEE=1)',
    (1,8,1,'cli'): 'AT+CMEE=1',
    (1,8,2,'total'): 0,
    (1,8,2,'name'):'Enable result code and verbose values (AT+CMEE=2)',
    (1,8,2,'cli'): 'AT+CMEE=2',

    (1,9,'total'): 8,
    (1,9,'name'): 'Set PSM Timers...',    
    
    (1,9,0,'total'): 0,
    (1,9,0,'name'):'Reset timer values',
    (1,9,0,'cli'): (reset_psm_timer, None),    
    
    (1,9,1,'total'): 6,
    (1,9,1,'name'):'Set Periodic RAU...',
    (1,9,1,0,'total'): 0,
    (1,9,1,0,'name'): 'Increments in multiples of 10 minutes',
    (1,9,1,0,'cli'): (psm_enter_timer, ('RAU','000', '10 minutes')),    
    (1,9,1,1,'total'): 0,
    (1,9,1,1,'name'): 'Increments in multiples of 1 hour',
    (1,9,1,1,'cli'): (psm_enter_timer, ('RAU','001', '1 hour')), 
    (1,9,1,2,'total'): 0,
    (1,9,1,2,'name'): 'Increments in multiples of 10 hours',
    (1,9,1,2,'cli'): (psm_enter_timer, ('RAU','010', '10 hours')), 
    (1,9,1,3,'total'): 0,
    (1,9,1,3,'name'): 'Increments in multiples of 2 seconds',
    (1,9,1,3,'cli'): (psm_enter_timer, ('RAU','011', '2 seconds')), 
    (1,9,1,4,'total'): 0,
    (1,9,1,4,'name'): 'Increments in multiples of 30 seconds',
    (1,9,1,4,'cli'): (psm_enter_timer, ('RAU','100', '30 seconds')), 
    (1,9,1,5,'total'): 0,
    (1,9,1,5,'name'): 'Increments in multiples of 1 minute',
    (1,9,1,5,'cli'): (psm_enter_timer, ('RAU','101', '1 minute')),     
    
    
    (1,9,2,'total'): 4,
    (1,9,2,'name'):'Set GPRS Ready Timer...',
    (1,9,2,0,'total'): 0,
    (1,9,2,0,'name'): 'Increments in multiples of 2 seconds',
    (1,9,2,0,'cli'): (psm_enter_timer, ('READY','000', '2 seconds')),    
    (1,9,2,1,'total'): 0,
    (1,9,2,1,'name'): 'Increments in multiples of 1 minute',
    (1,9,2,1,'cli'): (psm_enter_timer, ('READY','001', '1 minute')), 
    (1,9,2,2,'total'): 0,
    (1,9,2,2,'name'): 'Increments in multiples of 6 minutes',
    (1,9,2,2,'cli'): (psm_enter_timer, ('READY','010', '6 minutes')), 
    (1,9,2,3,'total'): 0,
    (1,9,2,3,'name'): 'deactivated',
    (1,9,2,3,'cli'): (psm_enter_timer, ('READY','111', 'deactivated')),     
    
    (1,9,3,'total'): 6,
    (1,9,3,'name'):'Set Periodic TAU...',
    (1,9,3,0,'total'): 0,
    (1,9,3,0,'name'): 'Increments in multiples of 10 minutes',
    (1,9,3,0,'cli'): (psm_enter_timer, ('TAU','000', '10 minutes')),    
    (1,9,3,1,'total'): 0,
    (1,9,3,1,'name'): 'Increments in multiples of 1 hour',
    (1,9,3,1,'cli'): (psm_enter_timer, ('TAU','001', '1 hour')), 
    (1,9,3,2,'total'): 0,
    (1,9,3,2,'name'): 'Increments in multiples of 10 hours',
    (1,9,3,2,'cli'): (psm_enter_timer, ('TAU','010', '10 hours')), 
    (1,9,3,3,'total'): 0,
    (1,9,3,3,'name'): 'Increments in multiples of 2 seconds',
    (1,9,3,3,'cli'): (psm_enter_timer, ('TAU','011', '2 seconds')), 
    (1,9,3,4,'total'): 0,
    (1,9,3,4,'name'): 'Increments in multiples of 30 seconds',
    (1,9,3,4,'cli'): (psm_enter_timer, ('TAU','100', '30 seconds')), 
    (1,9,3,5,'total'): 0,
    (1,9,3,5,'name'): 'Increments in multiples of 1 minute',
    (1,9,3,5,'cli'): (psm_enter_timer, ('TAU','101', '1 minute')),

    
    (1,9,4,'total'): 4,
    (1,9,4,'name'):'Set Active Timer...',
    (1,9,4,0,'total'): 0,
    (1,9,4,0,'name'): 'Increments in multiples of 2 seconds',
    (1,9,4,0,'cli'): (psm_enter_timer, ('ACTIVE','000', '2 seconds')),    
    (1,9,4,1,'total'): 0,
    (1,9,4,1,'name'): 'Increments in multiples of 1 minute',
    (1,9,4,1,'cli'): (psm_enter_timer, ('ACTIVE','001', '1 minute')), 
    (1,9,4,2,'total'): 0,
    (1,9,4,2,'name'): 'Increments in multiples of 6 minutes',
    (1,9,4,2,'cli'): (psm_enter_timer, ('ACTIVE','010', '6 minutes')), 
    (1,9,4,3,'total'): 0,
    (1,9,4,3,'name'): 'deactivated',
    (1,9,4,3,'cli'): (psm_enter_timer, ('ACTIVE','111', 'deactivated')),  

    
    (1,9,5,'total'): 0,
    (1,9,5,'name'):'Enable PSM and update value in Modem (needed to activate changes)',
    (1,9,5,'cli'): (psm_timers_set,1),

    (1,9,6,'total'): 0,
    (1,9,6,'name'):'Disable PSM and update value in Modem (needed to activate changes)',
    (1,9,6,'cli'): (psm_timers_set,0),

    (1,9,7,'total'): 0,
    (1,9,7,'name'):'Show current PSM application values',
    (1,9,7,'cli'): (psm_show_values, None),

    (1,10,'total'): 3,
    (1,10,'name'): 'Set eDRX Timers...',    




    (1,10,0,'total'): 4,
    (1,10,0,'name'):'Set eDRX timers with AT+CEDRXS (only TeDRX)...',
       
    (1,10,0,0,'total'): 5,
    (1,10,0,0,'name'):'Set eDRX for GSM...',
    (1,10,0,0,0,'total'): 0,
    (1,10,0,0,0,'name'): 'Disable the use of e-I-DRX',
    (1,10,0,0,0,'cli'): 'AT+CEDRXS=0,2',    
    (1,10,0,0,1,'total'): 0,
    (1,10,0,0,1,'name'): 'Enable the use of e-I-DRX',
    (1,10,0,0,1,'cli'): (edrx_enter_cmd, (1,2)), 
    (1,10,0,0,2,'total'): 0,
    (1,10,0,0,2,'name'): 'Enable the use of e-I-DRX and enable the unsolicited result code',
    (1,10,0,0,2,'cli'): (edrx_enter_cmd, (2,2)), 
    (1,10,0,0,3,'total'): 0,
    (1,10,0,0,3,'name'): 'Disable the use of e-I-DRX and discard/reset all parameters doe e-I-DRX',
    (1,10,0,0,3,'cli'): 'AT+CEDRXS=3,2', 
    (1,10,0,0,4,'total'): 16,
    (1,10,0,0,4,'name'): 'Define eDRX Timer for GSM...',
    (1,10,0,0,4,0,'total'): 0,
    (1,10,0,0,4,0,'name'): '1.88 seconds',
    (1,10,0,0,4,0,'cli'): (edrx_set_timer, (2,'0000','1.88 seconds')),    
    (1,10,0,0,4,1,'total'): 0,
    (1,10,0,0,4,1,'name'): '3.76 seconds',
    (1,10,0,0,4,1,'cli'): (edrx_set_timer, (2,'0001','3.76 seconds')),   
    (1,10,0,0,4,2,'total'): 0,
    (1,10,0,0,4,2,'name'): '7.53 seconds',
    (1,10,0,0,4,2,'cli'): (edrx_set_timer, (2,'0010','7.53 seconds')),   
    (1,10,0,0,4,3,'total'): 0,
    (1,10,0,0,4,3,'name'): '12.24 seconds',
    (1,10,0,0,4,3,'cli'): (edrx_set_timer, (2,'0011','12.24 seconds')),   
    (1,10,0,0,4,4,'total'): 0,
    (1,10,0,0,4,4,'name'): '24.48 seconds',
    (1,10,0,0,4,4,'cli'): (edrx_set_timer, (2,'0100','24.48 seconds')),   
    (1,10,0,0,4,5,'total'): 0,
    (1,10,0,0,4,5,'name'): '48.96 seconds',
    (1,10,0,0,4,5,'cli'): (edrx_set_timer, (2,'0101','48.96 seconds')),   
    (1,10,0,0,4,6,'total'): 0,
    (1,10,0,0,4,6,'name'): '97.96 seconds',
    (1,10,0,0,4,6,'cli'): (edrx_set_timer, (2,'0110','97.96 seconds')),   
    (1,10,0,0,4,7,'total'): 0,
    (1,10,0,0,4,7,'name'): '195.84 seconds',
    (1,10,0,0,4,7,'cli'): (edrx_set_timer, (2,'0111','195.84 seconds')),   
    (1,10,0,0,4,8,'total'): 0,
    (1,10,0,0,4,8,'name'): '391.68 seconds',
    (1,10,0,0,4,8,'cli'): (edrx_set_timer, (2,'1000','391.68 seconds')),   
    (1,10,0,0,4,9,'total'): 0,
    (1,10,0,0,4,9,'name'): '783.36 seconds',
    (1,10,0,0,4,9,'cli'): (edrx_set_timer, (2,'1001','783.36 seconds')),   
    (1,10,0,0,4,10,'total'): 0,
    (1,10,0,0,4,10,'name'): '1566.72 seconds',
    (1,10,0,0,4,10,'cli'): (edrx_set_timer, (2,'1010','1566.72 seconds')),   
    (1,10,0,0,4,11,'total'): 0,
    (1,10,0,0,4,11,'name'): '3133.44 seconds',
    (1,10,0,0,4,11,'cli'): (edrx_set_timer, (2,'1011','3133.44 seconds')),   
    (1,10,0,0,4,12,'total'): 0,
    (1,10,0,0,4,12,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,0,0,4,12,'cli'): (edrx_set_timer, (2,'1100','1.88 seconds')),   
    (1,10,0,0,4,13,'total'): 0,
    (1,10,0,0,4,13,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,0,0,4,13,'cli'): (edrx_set_timer, (2,'1101','1.88 seconds')),   
    (1,10,0,0,4,14,'total'): 0,
    (1,10,0,0,4,14,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,0,0,4,14,'cli'): (edrx_set_timer, (2,'1110','1.88 seconds')),   
    (1,10,0,0,4,15,'total'): 0,
    (1,10,0,0,4,15,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,0,0,4,15,'cli'): (edrx_set_timer, (2,'1111','1.88 seconds')),       
    
    (1,10,0,1,'total'): 5,
    (1,10,0,1,'name'):'Set eDRX for UTRAN...',
    (1,10,0,1,0,'total'): 0,
    (1,10,0,1,0,'name'): 'Disable the use of e-I-DRX',
    (1,10,0,1,0,'cli'): 'AT+CEDRXS=0,3',    
    (1,10,0,1,1,'total'): 0,
    (1,10,0,1,1,'name'): 'Enable the use of e-I-DRX',
    (1,10,0,1,1,'cli'): (edrx_enter_cmd, (1,3)), 
    (1,10,0,1,2,'total'): 0,
    (1,10,0,1,2,'name'): 'Enable the use of e-I-DRX and enable the unsolicited result code',
    (1,10,0,1,2,'cli'): (edrx_enter_cmd, (2,3)), 
    (1,10,0,1,3,'total'): 0,
    (1,10,0,1,3,'name'): 'Disable the use of e-I-DRX and discard/reset all parameters doe e-I-DRX',
    (1,10,0,1,3,'cli'): 'AT+CEDRXS=3,3', 
    (1,10,0,1,4,'total'): 16,
    (1,10,0,1,4,'name'): 'Define eDRX Timer for UTRAN...',
    (1,10,0,1,4,0,'total'): 0,
    (1,10,0,1,4,0,'name'): '10.24 seconds',
    (1,10,0,1,4,0,'cli'): (edrx_set_timer, (3,'0000','10.24 seconds')),    
    (1,10,0,1,4,1,'total'): 0,
    (1,10,0,1,4,1,'name'): '20.48 seconds',
    (1,10,0,1,4,1,'cli'): (edrx_set_timer, (3,'0001','20.48 seconds')),   
    (1,10,0,1,4,2,'total'): 0,
    (1,10,0,1,4,2,'name'): '40.96 seconds',
    (1,10,0,1,4,2,'cli'): (edrx_set_timer, (3,'0010','40.96 seconds')),   
    (1,10,0,1,4,3,'total'): 0,
    (1,10,0,1,4,3,'name'): '81.92 seconds',
    (1,10,0,1,4,3,'cli'): (edrx_set_timer, (3,'0011','81.92 seconds')),   
    (1,10,0,1,4,4,'total'): 0,
    (1,10,0,1,4,4,'name'): '163.84 seconds',
    (1,10,0,1,4,4,'cli'): (edrx_set_timer, (3,'0100','163.84 seconds')),   
    (1,10,0,1,4,5,'total'): 0,
    (1,10,0,1,4,5,'name'): '327.68 seconds',
    (1,10,0,1,4,5,'cli'): (edrx_set_timer, (3,'0101','327.68 seconds')),   
    (1,10,0,1,4,6,'total'): 0,
    (1,10,0,1,4,6,'name'): '655.36 seconds',
    (1,10,0,1,4,6,'cli'): (edrx_set_timer, (3,'0110','655.36 seconds')),   
    (1,10,0,1,4,7,'total'): 0,
    (1,10,0,1,4,7,'name'): '1310.72 seconds',
    (1,10,0,1,4,7,'cli'): (edrx_set_timer, (3,'0111','1310.72 seconds')),   
    (1,10,0,1,4,8,'total'): 0,
    (1,10,0,1,4,8,'name'): '1966.08 seconds',
    (1,10,0,1,4,8,'cli'): (edrx_set_timer, (3,'1000','1966.08 seconds')),   
    (1,10,0,1,4,9,'total'): 0,
    (1,10,0,1,4,9,'name'): '2621.44 seconds',
    (1,10,0,1,4,9,'cli'): (edrx_set_timer, (3,'1001','2621.44 seconds')),   
    (1,10,0,1,4,10,'total'): 0,
    (1,10,0,1,4,10,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,0,1,4,10,'cli'): (edrx_set_timer, (3,'1010','10.24 seconds')),   
    (1,10,0,1,4,11,'total'): 0,
    (1,10,0,1,4,11,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,0,1,4,11,'cli'): (edrx_set_timer, (3,'1011','10.24 seconds')),   
    (1,10,0,1,4,12,'total'): 0,
    (1,10,0,1,4,12,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,0,1,4,12,'cli'): (edrx_set_timer, (3,'1100','10.24 seconds')),   
    (1,10,0,1,4,13,'total'): 0,
    (1,10,0,1,4,13,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,0,1,4,13,'cli'): (edrx_set_timer, (3,'1101','10.24 seconds')),   
    (1,10,0,1,4,14,'total'): 0,
    (1,10,0,1,4,14,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,0,1,4,14,'cli'): (edrx_set_timer, (3,'1110','10.24 seconds')),   
    (1,10,0,1,4,15,'total'): 0,
    (1,10,0,1,4,15,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,0,1,4,15,'cli'): (edrx_set_timer, (3,'1111','10.24 seconds')),     

    (1,10,0,2,'total'): 5,
    (1,10,0,2,'name'):'Set eDRX for LTE-M...',
    (1,10,0,2,0,'total'): 0,
    (1,10,0,2,0,'name'): 'Disable the use of e-I-DRX',
    (1,10,0,2,0,'cli'): 'AT+CEDRXS=0,4',    
    (1,10,0,2,1,'total'): 0,
    (1,10,0,2,1,'name'): 'Enable the use of e-I-DRX',
    (1,10,0,2,1,'cli'): (edrx_enter_cmd, (1,4)), 
    (1,10,0,2,2,'total'): 0,
    (1,10,0,2,2,'name'): 'Enable the use of e-I-DRX and enable the unsolicited result code',
    (1,10,0,2,2,'cli'): (edrx_enter_cmd, (2,4)), 
    (1,10,0,2,3,'total'): 0,
    (1,10,0,2,3,'name'): 'Disable the use of e-I-DRX and discard/reset all parameters doe e-I-DRX',
    (1,10,0,2,3,'cli'): 'AT+CEDRXS=3,4', 
    (1,10,0,2,4,'total'): 16,
    (1,10,0,2,4,'name'): 'Define eDRX Timer for LTE-M...',
    (1,10,0,2,4,0,'total'): 0,
    (1,10,0,2,4,0,'name'): '5.12 seconds',
    (1,10,0,2,4,0,'cli'): (edrx_set_timer, (4,'0000','5.12 seconds')),    
    (1,10,0,2,4,1,'total'): 0,
    (1,10,0,2,4,1,'name'): '10.24 seconds',
    (1,10,0,2,4,1,'cli'): (edrx_set_timer, (4,'0001','10.24 seconds')),   
    (1,10,0,2,4,2,'total'): 0,
    (1,10,0,2,4,2,'name'): '20.48 seconds',
    (1,10,0,2,4,2,'cli'): (edrx_set_timer, (4,'0010','20.48 seconds')),   
    (1,10,0,2,4,3,'total'): 0,
    (1,10,0,2,4,3,'name'): '40.96 seconds',
    (1,10,0,2,4,3,'cli'): (edrx_set_timer, (4,'0011','40.96 seconds')),   
    (1,10,0,2,4,4,'total'): 0,
    (1,10,0,2,4,4,'name'): '61.44 seconds',
    (1,10,0,2,4,4,'cli'): (edrx_set_timer, (4,'0100','61.44 seconds')),   
    (1,10,0,2,4,5,'total'): 0,
    (1,10,0,2,4,5,'name'): '81.92 seconds',
    (1,10,0,2,4,5,'cli'): (edrx_set_timer, (4,'0101','81.92 seconds')),   
    (1,10,0,2,4,6,'total'): 0,
    (1,10,0,2,4,6,'name'): '102.4 seconds',
    (1,10,0,2,4,6,'cli'): (edrx_set_timer, (4,'0110','102.4 seconds')),   
    (1,10,0,2,4,7,'total'): 0,
    (1,10,0,2,4,7,'name'): '122.88 seconds',
    (1,10,0,2,4,7,'cli'): (edrx_set_timer, (4,'0111','122.88 seconds')),   
    (1,10,0,2,4,8,'total'): 0,
    (1,10,0,2,4,8,'name'): '143.36 seconds',
    (1,10,0,2,4,8,'cli'): (edrx_set_timer, (4,'1000','143.36 seconds')),   
    (1,10,0,2,4,9,'total'): 0,
    (1,10,0,2,4,9,'name'): '163.84 seconds',
    (1,10,0,2,4,9,'cli'): (edrx_set_timer, (4,'1001','163.84 seconds')),   
    (1,10,0,2,4,10,'total'): 0,
    (1,10,0,2,4,10,'name'): '327.68 seconds',
    (1,10,0,2,4,10,'cli'): (edrx_set_timer, (4,'1010','327.68 seconds')),   
    (1,10,0,2,4,11,'total'): 0,
    (1,10,0,2,4,11,'name'): '655.36 seconds',
    (1,10,0,2,4,11,'cli'): (edrx_set_timer, (4,'1011','655.36 seconds')),   
    (1,10,0,2,4,12,'total'): 0,
    (1,10,0,2,4,12,'name'): '1310.72 seconds',
    (1,10,0,2,4,12,'cli'): (edrx_set_timer, (4,'1100','1310.72 seconds')),   
    (1,10,0,2,4,13,'total'): 0,
    (1,10,0,2,4,13,'name'): '2621.44 seconds',
    (1,10,0,2,4,13,'cli'): (edrx_set_timer, (4,'1101','2621.44 seconds')),   
    (1,10,0,2,4,14,'total'): 0,
    (1,10,0,2,4,14,'name'): '5242.88 seconds',
    (1,10,0,2,4,14,'cli'): (edrx_set_timer, (4,'1110','5242.88 seconds')),   
    (1,10,0,2,4,15,'total'): 0,
    (1,10,0,2,4,15,'name'): '10485.76 seconds',
    (1,10,0,2,4,15,'cli'): (edrx_set_timer, (4,'1111','10485.76 seconds')), 

    (1,10,0,3,'total'): 5,
    (1,10,0,3,'name'):'Set eDRX for NB-IoT...',
    (1,10,0,3,0,'total'): 0,
    (1,10,0,3,0,'name'): 'Disable the use of e-I-DRX',
    (1,10,0,3,0,'cli'): 'AT+CEDRXS=0,5',    
    (1,10,0,3,1,'total'): 0,
    (1,10,0,3,1,'name'): 'Enable the use of e-I-DRX',
    (1,10,0,3,1,'cli'): (edrx_enter_cmd, (1,5)), 
    (1,10,0,3,2,'total'): 0,
    (1,10,0,3,2,'name'): 'Enable the use of e-I-DRX and enable the unsolicited result code',
    (1,10,0,3,2,'cli'): (edrx_enter_cmd, (2,5)), 
    (1,10,0,3,3,'total'): 0,
    (1,10,0,3,3,'name'): 'Disable the use of e-I-DRX and discard/reset all parameters doe e-I-DRX',
    (1,10,0,3,3,'cli'): 'AT+CEDRXS=3,5', 
    (1,10,0,3,4,'total'): 16,
    (1,10,0,3,4,'name'): 'Define eDRX Timer for NB-IoT...',
    (1,10,0,3,4,0,'total'): 0,
    (1,10,0,3,4,0,'name'): '5.12 seconds',
    (1,10,0,3,4,0,'cli'): (edrx_set_timer, (5,'0000','5.12 seconds')),    
    (1,10,0,3,4,1,'total'): 0,
    (1,10,0,3,4,1,'name'): '10.24 seconds',
    (1,10,0,3,4,1,'cli'): (edrx_set_timer, (5,'0001','10.24 seconds')),   
    (1,10,0,3,4,2,'total'): 0,
    (1,10,0,3,4,2,'name'): '20.48 seconds',
    (1,10,0,3,4,2,'cli'): (edrx_set_timer, (5,'0010','20.48 seconds')),   
    (1,10,0,3,4,3,'total'): 0,
    (1,10,0,3,4,3,'name'): '40.96 seconds',
    (1,10,0,3,4,3,'cli'): (edrx_set_timer, (5,'0011','40.96 seconds')),   
    (1,10,0,3,4,4,'total'): 0,
    (1,10,0,3,4,4,'name'): '61.44 seconds',
    (1,10,0,3,4,4,'cli'): (edrx_set_timer, (5,'0100','61.44 seconds')),   
    (1,10,0,3,4,5,'total'): 0,
    (1,10,0,3,4,5,'name'): '81.92 seconds',
    (1,10,0,3,4,5,'cli'): (edrx_set_timer, (5,'0101','81.92 seconds')),   
    (1,10,0,3,4,6,'total'): 0,
    (1,10,0,3,4,6,'name'): '102.4 seconds',
    (1,10,0,3,4,6,'cli'): (edrx_set_timer, (5,'0110','102.4 seconds')),   
    (1,10,0,3,4,7,'total'): 0,
    (1,10,0,3,4,7,'name'): '122.88 seconds',
    (1,10,0,3,4,7,'cli'): (edrx_set_timer, (5,'0111','122.88 seconds')),   
    (1,10,0,3,4,8,'total'): 0,
    (1,10,0,3,4,8,'name'): '143.36 seconds',
    (1,10,0,3,4,8,'cli'): (edrx_set_timer, (5,'1000','143.36 seconds')),   
    (1,10,0,3,4,9,'total'): 0,
    (1,10,0,3,4,9,'name'): '163.84 seconds',
    (1,10,0,3,4,9,'cli'): (edrx_set_timer, (5,'1001','163.84 seconds')),   
    (1,10,0,3,4,10,'total'): 0,
    (1,10,0,3,4,10,'name'): '327.68 seconds',
    (1,10,0,3,4,10,'cli'): (edrx_set_timer, (5,'1010','327.68 seconds')),   
    (1,10,0,3,4,11,'total'): 0,
    (1,10,0,3,4,11,'name'): '655.36 seconds',
    (1,10,0,3,4,11,'cli'): (edrx_set_timer, (5,'1011','655.36 seconds')),   
    (1,10,0,3,4,12,'total'): 0,
    (1,10,0,3,4,12,'name'): '1310.72 seconds',
    (1,10,0,3,4,12,'cli'): (edrx_set_timer, (5,'1100','1310.72 seconds')),   
    (1,10,0,3,4,13,'total'): 0,
    (1,10,0,3,4,13,'name'): '2621.44 seconds',
    (1,10,0,3,4,13,'cli'): (edrx_set_timer, (5,'1101','2621.44 seconds')),   
    (1,10,0,3,4,14,'total'): 0,
    (1,10,0,3,4,14,'name'): '5242.88 seconds',
    (1,10,0,3,4,14,'cli'): (edrx_set_timer, (5,'1110','5242.88 seconds')),   
    (1,10,0,3,4,15,'total'): 0,
    (1,10,0,3,4,15,'name'): '10485.76 seconds',
    (1,10,0,3,4,15,'cli'): (edrx_set_timer, (5,'1111','10485.76 seconds')), 



####
    (1,10,1,'total'): 4,
    (1,10,1,'name'):'Set eDRX and ptw timers with AT+QPTWEDRXS (TeDRX+ ptw)...',

    (1,10,1,0,'total'): 6,
    (1,10,1,0,'name'):'Set eDRX and ptw for GSM...',
    (1,10,1,0,0,'total'): 0,
    (1,10,1,0,0,'name'): 'Disable the use of ptw and eDRX',
    (1,10,1,0,0,'cli'): 'AT+QPTWEDRXS=0,2',    
    (1,10,1,0,1,'total'): 0,
    (1,10,1,0,1,'name'): 'Enable the use of ptw and eDRX',
    (1,10,1,0,1,'cli'): (edrx_ptw_enter_cmd, (1,2)), 
    (1,10,1,0,2,'total'): 0,
    (1,10,1,0,2,'name'): 'Enable the use of ptw and eDRX and enable the unsolicited result code',
    (1,10,1,0,2,'cli'): (edrx_ptw_enter_cmd, (2,2)), 
    (1,10,1,0,3,'total'): 0,
    (1,10,1,0,3,'name'): 'Disable the use of ptw and eDRX and discard/reset all parameters',
    (1,10,1,0,3,'cli'): 'AT+QPTWEDRXS=3,2', 
    
    (1,10,1,0,4,'total'): 16,
    (1,10,1,0,4,'name'): 'Define eDRX Timer for GSM...',
    (1,10,1,0,4,0,'total'): 0,
    (1,10,1,0,4,0,'name'): '1.88 seconds',
    (1,10,1,0,4,0,'cli'): (edrx_set_timer, (2,'0000','1.88 seconds')),    
    (1,10,1,0,4,1,'total'): 0,
    (1,10,1,0,4,1,'name'): '3.76 seconds',
    (1,10,1,0,4,1,'cli'): (edrx_set_timer, (2,'0001','3.76 seconds')),   
    (1,10,1,0,4,2,'total'): 0,
    (1,10,1,0,4,2,'name'): '7.53 seconds',
    (1,10,1,0,4,2,'cli'): (edrx_set_timer, (2,'0010','7.53 seconds')),   
    (1,10,1,0,4,3,'total'): 0,
    (1,10,1,0,4,3,'name'): '12.24 seconds',
    (1,10,1,0,4,3,'cli'): (edrx_set_timer, (2,'0011','12.24 seconds')),   
    (1,10,1,0,4,4,'total'): 0,
    (1,10,1,0,4,4,'name'): '24.48 seconds',
    (1,10,1,0,4,4,'cli'): (edrx_set_timer, (2,'0100','24.48 seconds')),   
    (1,10,1,0,4,5,'total'): 0,
    (1,10,1,0,4,5,'name'): '48.96 seconds',
    (1,10,1,0,4,5,'cli'): (edrx_set_timer, (2,'0101','48.96 seconds')),   
    (1,10,1,0,4,6,'total'): 0,
    (1,10,1,0,4,6,'name'): '97.92 seconds',
    (1,10,1,0,4,6,'cli'): (edrx_set_timer, (2,'0110','97.92 seconds')),   
    (1,10,1,0,4,7,'total'): 0,
    (1,10,1,0,4,7,'name'): '195.84 seconds',
    (1,10,1,0,4,7,'cli'): (edrx_set_timer, (2,'0111','195.84 seconds')),   
    (1,10,1,0,4,8,'total'): 0,
    (1,10,1,0,4,8,'name'): '391.68 seconds',
    (1,10,1,0,4,8,'cli'): (edrx_set_timer, (2,'1000','391.68 seconds')),   
    (1,10,1,0,4,9,'total'): 0,
    (1,10,1,0,4,9,'name'): '783.36 seconds',
    (1,10,1,0,4,9,'cli'): (edrx_set_timer, (2,'1001','783.36 seconds')),   
    (1,10,1,0,4,10,'total'): 0,
    (1,10,1,0,4,10,'name'): '1566.72 seconds',
    (1,10,1,0,4,10,'cli'): (edrx_set_timer, (2,'1010','1566.72 seconds')),   
    (1,10,1,0,4,11,'total'): 0,
    (1,10,1,0,4,11,'name'): '3133.44 seconds',
    (1,10,1,0,4,11,'cli'): (edrx_set_timer, (2,'1011','3133.44 seconds')),   
    (1,10,1,0,4,12,'total'): 0,
    (1,10,1,0,4,12,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,1,0,4,12,'cli'): (edrx_set_timer, (2,'1100','1.88 seconds')),   
    (1,10,1,0,4,13,'total'): 0,
    (1,10,1,0,4,13,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,1,0,4,13,'cli'): (edrx_set_timer, (2,'1101','1.88 seconds')),   
    (1,10,1,0,4,14,'total'): 0,
    (1,10,1,0,4,14,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,1,0,4,14,'cli'): (edrx_set_timer, (2,'1110','1.88 seconds')),   
    (1,10,1,0,4,15,'total'): 0,
    (1,10,1,0,4,15,'name'): 'Same as 0000 (1.88 seconds)',
    (1,10,1,0,4,15,'cli'): (edrx_set_timer, (2,'1111','1.88 seconds')),      

    (1,10,1,0,5,'name'): 'Define ptw Timer for GSM...',
    (1,10,1,0,5,'total'): 16,    
    (1,10,1,0,5,0,'total'): 0,
    (1,10,1,0,5,0,'name'): '0 seconds (ptw not used)',
    (1,10,1,0,5,0,'cli'): (edrx_ptw_set_timer, (2,'0000','0 seconds')),    
    (1,10,1,0,5,1,'total'): 0,
    (1,10,1,0,5,1,'name'): '1 seconds',
    (1,10,1,0,5,1,'cli'): (edrx_ptw_set_timer, (2,'0001','1 seconds')),   
    (1,10,1,0,5,2,'total'): 0,
    (1,10,1,0,5,2,'name'): '2 seconds',
    (1,10,1,0,5,2,'cli'): (edrx_ptw_set_timer, (2,'0010','2 seconds')),   
    (1,10,1,0,5,3,'total'): 0,
    (1,10,1,0,5,3,'name'): '3 seconds',
    (1,10,1,0,5,3,'cli'): (edrx_ptw_set_timer, (2,'0011','3 seconds')),   
    (1,10,1,0,5,4,'total'): 0,
    (1,10,1,0,5,4,'name'): '4 seconds',
    (1,10,1,0,5,4,'cli'): (edrx_ptw_set_timer, (2,'0100','4 seconds')),   
    (1,10,1,0,5,5,'total'): 0,
    (1,10,1,0,5,5,'name'): '5 seconds',
    (1,10,1,0,5,5,'cli'): (edrx_ptw_set_timer, (2,'0101','5 seconds')),   
    (1,10,1,0,5,6,'total'): 0,
    (1,10,1,0,5,6,'name'): '6 seconds',
    (1,10,1,0,5,6,'cli'): (edrx_ptw_set_timer, (2,'0110','6 seconds')),   
    (1,10,1,0,5,7,'total'): 0,
    (1,10,1,0,5,7,'name'): '7 seconds',
    (1,10,1,0,5,7,'cli'): (edrx_ptw_set_timer, (2,'0111','7 seconds')),   
    (1,10,1,0,5,8,'total'): 0,
    (1,10,1,0,5,8,'name'): '8 seconds',
    (1,10,1,0,5,8,'cli'): (edrx_ptw_set_timer, (2,'1000','8 seconds')),   
    (1,10,1,0,5,9,'total'): 0,
    (1,10,1,0,5,9,'name'): '9 seconds',
    (1,10,1,0,5,9,'cli'): (edrx_ptw_set_timer, (2,'1001','9 seconds')),   
    (1,10,1,0,5,10,'total'): 0,
    (1,10,1,0,5,10,'name'): '10 seconds',
    (1,10,1,0,5,10,'cli'): (edrx_ptw_set_timer, (2,'1010','10 seconds')),   
    (1,10,1,0,5,11,'total'): 0,
    (1,10,1,0,5,11,'name'): '12 seconds',
    (1,10,1,0,5,11,'cli'): (edrx_ptw_set_timer, (2,'1011','12 seconds')),   
    (1,10,1,0,5,12,'total'): 0,
    (1,10,1,0,5,12,'name'): '14 seconds',
    (1,10,1,0,5,12,'cli'): (edrx_ptw_set_timer, (2,'1100','14 seconds')),   
    (1,10,1,0,5,13,'total'): 0,
    (1,10,1,0,5,13,'name'): '16 seconds',
    (1,10,1,0,5,13,'cli'): (edrx_ptw_set_timer, (2,'1101','16 seconds')),   
    (1,10,1,0,5,14,'total'): 0,
    (1,10,1,0,5,14,'name'): '18 seconds',
    (1,10,1,0,5,14,'cli'): (edrx_ptw_set_timer, (2,'1110','18 seconds')),   
    (1,10,1,0,5,15,'total'): 0,
    (1,10,1,0,5,15,'name'): '20 seconds',
    (1,10,1,0,5,15,'cli'): (edrx_ptw_set_timer, (2,'1111','20 seconds')), 


    (1,10,1,1,'total'): 6,
    (1,10,1,1,'name'):'Set eDRX and ptw for UTRAN...',
    (1,10,1,1,0,'total'): 0,
    (1,10,1,1,0,'name'): 'Disable the use of ptw and eDRX',
    (1,10,1,1,0,'cli'): 'AT+QPTWEDRXS=0,3',    
    (1,10,1,1,1,'total'): 0,
    (1,10,1,1,1,'name'): 'Enable the use of ptw and eDRX',
    (1,10,1,1,1,'cli'): (edrx_ptw_enter_cmd, (1,3)), 
    (1,10,1,1,2,'total'): 0,
    (1,10,1,1,2,'name'): 'Enable the use of ptw and eDRX and enable the unsolicited result code',
    (1,10,1,1,2,'cli'): (edrx_ptw_enter_cmd, (2,3)), 
    (1,10,1,1,3,'total'): 0,
    (1,10,1,1,3,'name'): 'Disable the use of ptw and eDRX and discard/reset all parameters',
    (1,10,1,1,3,'cli'): 'AT+QPTWEDRXS=3,3', 
            
    (1,10,1,1,4,'total'): 16,
    (1,10,1,1,4,'name'): 'Define eDRX Timer for UTRAN...',
    (1,10,1,1,4,0,'total'): 0,
    (1,10,1,1,4,0,'name'): '10.24 seconds',
    (1,10,1,1,4,0,'cli'): (edrx_set_timer, (3,'0000','10.24 seconds')),    
    (1,10,1,1,4,1,'total'): 0,
    (1,10,1,1,4,1,'name'): '20.48 seconds',
    (1,10,1,1,4,1,'cli'): (edrx_set_timer, (3,'0001','20.48 seconds')),   
    (1,10,1,1,4,2,'total'): 0,
    (1,10,1,1,4,2,'name'): '40.96 seconds',
    (1,10,1,1,4,2,'cli'): (edrx_set_timer, (3,'0010','40.96 seconds')),   
    (1,10,1,1,4,3,'total'): 0,
    (1,10,1,1,4,3,'name'): '81.92 seconds',
    (1,10,1,1,4,3,'cli'): (edrx_set_timer, (3,'0011','81.92 seconds')),   
    (1,10,1,1,4,4,'total'): 0,
    (1,10,1,1,4,4,'name'): '163.84 seconds',
    (1,10,1,1,4,4,'cli'): (edrx_set_timer, (3,'0100','163.84 seconds')),   
    (1,10,1,1,4,5,'total'): 0,
    (1,10,1,1,4,5,'name'): '327.68 seconds',
    (1,10,1,1,4,5,'cli'): (edrx_set_timer, (3,'0101','327.68 seconds')),   
    (1,10,1,1,4,6,'total'): 0,
    (1,10,1,1,4,6,'name'): '655.36 seconds',
    (1,10,1,1,4,6,'cli'): (edrx_set_timer, (3,'0110','655.36 seconds')),   
    (1,10,1,1,4,7,'total'): 0,
    (1,10,1,1,4,7,'name'): '1310.72 seconds',
    (1,10,1,1,4,7,'cli'): (edrx_set_timer, (3,'0111','1310.72 seconds')),   
    (1,10,1,1,4,8,'total'): 0,
    (1,10,1,1,4,8,'name'): '1966.08 seconds',
    (1,10,1,1,4,8,'cli'): (edrx_set_timer, (3,'1000','1966.08 seconds')),   
    (1,10,1,1,4,9,'total'): 0,
    (1,10,1,1,4,9,'name'): '2621.44 seconds',
    (1,10,1,1,4,9,'cli'): (edrx_set_timer, (3,'1001','2621.44 seconds')),   
    (1,10,1,1,4,10,'total'): 0,
    (1,10,1,1,4,10,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,1,1,4,10,'cli'): (edrx_set_timer, (3,'1010','10.24 seconds')),   
    (1,10,1,1,4,11,'total'): 0,
    (1,10,1,1,4,11,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,1,1,4,11,'cli'): (edrx_set_timer, (3,'1011','10.24 seconds')),   
    (1,10,1,1,4,12,'total'): 0,
    (1,10,1,1,4,12,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,1,1,4,12,'cli'): (edrx_set_timer, (3,'1100','10.24 seconds')),   
    (1,10,1,1,4,13,'total'): 0,
    (1,10,1,1,4,13,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,1,1,4,13,'cli'): (edrx_set_timer, (3,'1101','10.24 seconds')),   
    (1,10,1,1,4,14,'total'): 0,
    (1,10,1,1,4,14,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,1,1,4,14,'cli'): (edrx_set_timer, (3,'1110','10.24 seconds')),   
    (1,10,1,1,4,15,'total'): 0,
    (1,10,1,1,4,15,'name'): 'Same as 0000 (10.24 seconds)',
    (1,10,1,1,4,15,'cli'): (edrx_set_timer, (3,'1111','10.24 seconds')),      
            
    (1,10,1,1,5,'name'): 'Define ptw Timer for UTRAN...',
    (1,10,1,1,5,'total'): 16,    
    (1,10,1,1,5,0,'total'): 0,
    (1,10,1,1,5,0,'name'): '0 seconds (ptw not used)',
    (1,10,1,1,5,0,'cli'): (edrx_ptw_set_timer, (3,'0000','0 seconds')),    
    (1,10,1,1,5,1,'total'): 0,
    (1,10,1,1,5,1,'name'): '1 seconds',
    (1,10,1,1,5,1,'cli'): (edrx_ptw_set_timer, (3,'0001','1 seconds')),   
    (1,10,1,1,5,2,'total'): 0,
    (1,10,1,1,5,2,'name'): '2 seconds',
    (1,10,1,1,5,2,'cli'): (edrx_ptw_set_timer, (3,'0010','2 seconds')),   
    (1,10,1,1,5,3,'total'): 0,
    (1,10,1,1,5,3,'name'): '3 seconds',
    (1,10,1,1,5,3,'cli'): (edrx_ptw_set_timer, (3,'0011','3 seconds')),   
    (1,10,1,1,5,4,'total'): 0,
    (1,10,1,1,5,4,'name'): '4 seconds',
    (1,10,1,1,5,4,'cli'): (edrx_ptw_set_timer, (3,'0100','4 seconds')),   
    (1,10,1,1,5,5,'total'): 0,
    (1,10,1,1,5,5,'name'): '5 seconds',
    (1,10,1,1,5,5,'cli'): (edrx_ptw_set_timer, (3,'0101','5 seconds')),   
    (1,10,1,1,5,6,'total'): 0,
    (1,10,1,1,5,6,'name'): '6 seconds',
    (1,10,1,1,5,6,'cli'): (edrx_ptw_set_timer, (3,'0110','6 seconds')),   
    (1,10,1,1,5,7,'total'): 0,
    (1,10,1,1,5,7,'name'): '7 seconds',
    (1,10,1,1,5,7,'cli'): (edrx_ptw_set_timer, (3,'0111','7 seconds')),   
    (1,10,1,1,5,8,'total'): 0,
    (1,10,1,1,5,8,'name'): '8 seconds',
    (1,10,1,1,5,8,'cli'): (edrx_ptw_set_timer, (3,'1000','8 seconds')),   
    (1,10,1,1,5,9,'total'): 0,
    (1,10,1,1,5,9,'name'): '9 seconds',
    (1,10,1,1,5,9,'cli'): (edrx_ptw_set_timer, (3,'1001','9 seconds')),   
    (1,10,1,1,5,10,'total'): 0,
    (1,10,1,1,5,10,'name'): '10 seconds',
    (1,10,1,1,5,10,'cli'): (edrx_ptw_set_timer, (3,'1010','10 seconds')),   
    (1,10,1,1,5,11,'total'): 0,
    (1,10,1,1,5,11,'name'): '12 seconds',
    (1,10,1,1,5,11,'cli'): (edrx_ptw_set_timer, (3,'1011','12 seconds')),   
    (1,10,1,1,5,12,'total'): 0,
    (1,10,1,1,5,12,'name'): '14 seconds',
    (1,10,1,1,5,12,'cli'): (edrx_ptw_set_timer, (3,'1100','14 seconds')),   
    (1,10,1,1,5,13,'total'): 0,
    (1,10,1,1,5,13,'name'): '16 seconds',
    (1,10,1,1,5,13,'cli'): (edrx_ptw_set_timer, (3,'1101','16 seconds')),   
    (1,10,1,1,5,14,'total'): 0,
    (1,10,1,1,5,14,'name'): '18 seconds',
    (1,10,1,1,5,14,'cli'): (edrx_ptw_set_timer, (3,'1110','18 seconds')),   
    (1,10,1,1,5,15,'total'): 0,
    (1,10,1,1,5,15,'name'): '20 seconds',
    (1,10,1,1,5,15,'cli'): (edrx_ptw_set_timer, (3,'1111','20 seconds')), 
    
    
    
    (1,10,1,2,'total'): 6,
    (1,10,1,2,'name'):'Set eDRX and ptw for LTE-M...',
    (1,10,1,2,0,'total'): 0,
    (1,10,1,2,0,'name'): 'Disable the use of ptw and eDRX',
    (1,10,1,2,0,'cli'): 'AT+QPTWEDRXS=0,4',    
    (1,10,1,2,1,'total'): 0,
    (1,10,1,2,1,'name'): 'Enable the use of ptw and eDRX',
    (1,10,1,2,1,'cli'): (edrx_ptw_enter_cmd, (1,4)), 
    (1,10,1,2,2,'total'): 0,
    (1,10,1,2,2,'name'): 'Enable the use of ptw and eDRX and enable the unsolicited result code',
    (1,10,1,2,2,'cli'): (edrx_ptw_enter_cmd, (2,4)), 
    (1,10,1,2,3,'total'): 0,
    (1,10,1,2,3,'name'): 'Disable the use of ptw and eDRX and discard/reset all parameters',
    (1,10,1,2,3,'cli'): 'AT+QPTWEDRXS=3,4', 
            
    (1,10,1,2,4,'total'): 16,
    (1,10,1,2,4,'name'): 'Define eDRX Timer for LTE-M...',
    (1,10,1,2,4,0,'total'): 0,
    (1,10,1,2,4,0,'name'): '5.12 seconds',
    (1,10,1,2,4,0,'cli'): (edrx_set_timer, (4,'0000','5.12 seconds')),    
    (1,10,1,2,4,1,'total'): 0,
    (1,10,1,2,4,1,'name'): '10.24 seconds',
    (1,10,1,2,4,1,'cli'): (edrx_set_timer, (4,'0001','10.24 seconds')),   
    (1,10,1,2,4,2,'total'): 0,
    (1,10,1,2,4,2,'name'): '20.48 seconds',
    (1,10,1,2,4,2,'cli'): (edrx_set_timer, (4,'0010','20.48 seconds')),   
    (1,10,1,2,4,3,'total'): 0,
    (1,10,1,2,4,3,'name'): '40.96 seconds',
    (1,10,1,2,4,3,'cli'): (edrx_set_timer, (4,'0011','40.96 seconds')),   
    (1,10,1,2,4,4,'total'): 0,
    (1,10,1,2,4,4,'name'): '61.44 seconds',
    (1,10,1,2,4,4,'cli'): (edrx_set_timer, (4,'0100','61.44 seconds')),   
    (1,10,1,2,4,5,'total'): 0,
    (1,10,1,2,4,5,'name'): '81.92 seconds',
    (1,10,1,2,4,5,'cli'): (edrx_set_timer, (4,'0101','81.92 seconds')),   
    (1,10,1,2,4,6,'total'): 0,
    (1,10,1,2,4,6,'name'): '102.4 seconds',
    (1,10,1,2,4,6,'cli'): (edrx_set_timer, (4,'0110','102.4 seconds')),   
    (1,10,1,2,4,7,'total'): 0,
    (1,10,1,2,4,7,'name'): '122.88 seconds',
    (1,10,1,2,4,7,'cli'): (edrx_set_timer, (4,'0111','122.88 seconds')),   
    (1,10,1,2,4,8,'total'): 0,
    (1,10,1,2,4,8,'name'): '143.36 seconds',
    (1,10,1,2,4,8,'cli'): (edrx_set_timer, (4,'1000','143.36 seconds')),   
    (1,10,1,2,4,9,'total'): 0,
    (1,10,1,2,4,9,'name'): '163.84 seconds',
    (1,10,1,2,4,9,'cli'): (edrx_set_timer, (4,'1001','163.84 seconds')),   
    (1,10,1,2,4,10,'total'): 0,
    (1,10,1,2,4,10,'name'): '327.68 seconds',
    (1,10,1,2,4,10,'cli'): (edrx_set_timer, (4,'1010','327.68 seconds')),   
    (1,10,1,2,4,11,'total'): 0,
    (1,10,1,2,4,11,'name'): '655.36 seconds',
    (1,10,1,2,4,11,'cli'): (edrx_set_timer, (4,'1011','655.36 seconds')),   
    (1,10,1,2,4,12,'total'): 0,
    (1,10,1,2,4,12,'name'): '1310.72 seconds',
    (1,10,1,2,4,12,'cli'): (edrx_set_timer, (4,'1100','1310.72 seconds')),   
    (1,10,1,2,4,13,'total'): 0,
    (1,10,1,2,4,13,'name'): '2621.44 seconds',
    (1,10,1,2,4,13,'cli'): (edrx_set_timer, (4,'1101','2621.44 seconds')),   
    (1,10,1,2,4,14,'total'): 0,
    (1,10,1,2,4,14,'name'): '5242.88 seconds',
    (1,10,1,2,4,14,'cli'): (edrx_set_timer, (4,'1110','5242.88 seconds')),   
    (1,10,1,2,4,15,'total'): 0,
    (1,10,1,2,4,15,'name'): '10485.76 seconds',
    (1,10,1,2,4,15,'cli'): (edrx_set_timer, (4,'1111','10485.76 seconds')),      
            
    (1,10,1,2,5,'name'): 'Define ptw Timer for LTE-M...',
    (1,10,1,2,5,'total'): 16,    
    (1,10,1,2,5,0,'total'): 0,
    (1,10,1,2,5,0,'name'): '1.28 seconds',
    (1,10,1,2,5,0,'cli'): (edrx_ptw_set_timer, (4,'0000','1.28 seconds')),    
    (1,10,1,2,5,1,'total'): 0,
    (1,10,1,2,5,1,'name'): '2.56 seconds',
    (1,10,1,2,5,1,'cli'): (edrx_ptw_set_timer, (4,'0001','2.56 seconds')),   
    (1,10,1,2,5,2,'total'): 0,
    (1,10,1,2,5,2,'name'): '3.84 seconds',
    (1,10,1,2,5,2,'cli'): (edrx_ptw_set_timer, (4,'0010','3.84 seconds')),   
    (1,10,1,2,5,3,'total'): 0,
    (1,10,1,2,5,3,'name'): '5.12 seconds',
    (1,10,1,2,5,3,'cli'): (edrx_ptw_set_timer, (4,'0011','5.12 seconds')),   
    (1,10,1,2,5,4,'total'): 0,
    (1,10,1,2,5,4,'name'): '6.4 seconds',
    (1,10,1,2,5,4,'cli'): (edrx_ptw_set_timer, (4,'0100','6.4 seconds')),   
    (1,10,1,2,5,5,'total'): 0,
    (1,10,1,2,5,5,'name'): '7.68 seconds',
    (1,10,1,2,5,5,'cli'): (edrx_ptw_set_timer, (4,'0101','7.68 seconds')),   
    (1,10,1,2,5,6,'total'): 0,
    (1,10,1,2,5,6,'name'): '8.96 seconds',
    (1,10,1,2,5,6,'cli'): (edrx_ptw_set_timer, (4,'0110','8.96 seconds')),   
    (1,10,1,2,5,7,'total'): 0,
    (1,10,1,2,5,7,'name'): '10.24 seconds',
    (1,10,1,2,5,7,'cli'): (edrx_ptw_set_timer, (4,'0111','10.24 seconds')),   
    (1,10,1,2,5,8,'total'): 0,
    (1,10,1,2,5,8,'name'): '11.52 seconds',
    (1,10,1,2,5,8,'cli'): (edrx_ptw_set_timer, (4,'1000','11.56 seconds')),   
    (1,10,1,2,5,9,'total'): 0,
    (1,10,1,2,5,9,'name'): '12.8 seconds',
    (1,10,1,2,5,9,'cli'): (edrx_ptw_set_timer, (4,'1001','12.8 seconds')),   
    (1,10,1,2,5,10,'total'): 0,
    (1,10,1,2,5,10,'name'): '14.08 seconds',
    (1,10,1,2,5,10,'cli'): (edrx_ptw_set_timer, (4,'1010','14.08 seconds')),   
    (1,10,1,2,5,11,'total'): 0,
    (1,10,1,2,5,11,'name'): '15.36 seconds',
    (1,10,1,2,5,11,'cli'): (edrx_ptw_set_timer, (4,'1011','15.36 seconds')),   
    (1,10,1,2,5,12,'total'): 0,
    (1,10,1,2,5,12,'name'): '16.64 seconds',
    (1,10,1,2,5,12,'cli'): (edrx_ptw_set_timer, (4,'1100','16.64 seconds')),   
    (1,10,1,2,5,13,'total'): 0,
    (1,10,1,2,5,13,'name'): '17.92 seconds',
    (1,10,1,2,5,13,'cli'): (edrx_ptw_set_timer, (4,'1101','17.92 seconds')),   
    (1,10,1,2,5,14,'total'): 0,
    (1,10,1,2,5,14,'name'): '19.20 seconds',
    (1,10,1,2,5,14,'cli'): (edrx_ptw_set_timer, (4,'1110','19.20 seconds')),   
    (1,10,1,2,5,15,'total'): 0,
    (1,10,1,2,5,15,'name'): '20.48 seconds',
    (1,10,1,2,5,15,'cli'): (edrx_ptw_set_timer, (4,'1111','20.48 seconds')), 
    
    
    
    (1,10,1,3,'total'): 6,
    (1,10,1,3,'name'):'Set eDRX and ptw for NB-IoT...',
    (1,10,1,3,0,'total'): 0,
    (1,10,1,3,0,'name'): 'Disable the use of ptw and eDRX',
    (1,10,1,3,0,'cli'): 'AT+QPTWEDRXS=0,5',    
    (1,10,1,3,1,'total'): 0,
    (1,10,1,3,1,'name'): 'Enable the use of ptw and eDRX',
    (1,10,1,3,1,'cli'): (edrx_ptw_enter_cmd, (1,5)), 
    (1,10,1,3,2,'total'): 0,
    (1,10,1,3,2,'name'): 'Enable the use of ptw and eDRX and enable the unsolicited result code',
    (1,10,1,3,2,'cli'): (edrx_ptw_enter_cmd, (2,5)), 
    (1,10,1,3,3,'total'): 0,
    (1,10,1,3,3,'name'): 'Disable the use of ptw and eDRX and discard/reset all parameters',
    (1,10,1,3,3,'cli'): 'AT+QPTWEDRXS=3,5', 
            
    (1,10,1,3,4,'total'): 16,
    (1,10,1,3,4,'name'): 'Define eDRX Timer for NB-IoT...',
    (1,10,1,3,4,0,'total'): 0,
    (1,10,1,3,4,0,'name'): '5.12 seconds',
    (1,10,1,3,4,0,'cli'): (edrx_set_timer, (5,'0000','5.12 seconds')),    
    (1,10,1,3,4,1,'total'): 0,
    (1,10,1,3,4,1,'name'): '10.24 seconds',
    (1,10,1,3,4,1,'cli'): (edrx_set_timer, (5,'0001','10.24 seconds')),   
    (1,10,1,3,4,2,'total'): 0,
    (1,10,1,3,4,2,'name'): '20.48 seconds',
    (1,10,1,3,4,2,'cli'): (edrx_set_timer, (5,'0010','20.48 seconds')),   
    (1,10,1,3,4,3,'total'): 0,
    (1,10,1,3,4,3,'name'): '40.96 seconds',
    (1,10,1,3,4,3,'cli'): (edrx_set_timer, (5,'0011','40.96 seconds')),   
    (1,10,1,3,4,4,'total'): 0,
    (1,10,1,3,4,4,'name'): '61.44 seconds',
    (1,10,1,3,4,4,'cli'): (edrx_set_timer, (5,'0100','61.44 seconds')),   
    (1,10,1,3,4,5,'total'): 0,
    (1,10,1,3,4,5,'name'): '81.92 seconds',
    (1,10,1,3,4,5,'cli'): (edrx_set_timer, (5,'0101','81.92 seconds')),   
    (1,10,1,3,4,6,'total'): 0,
    (1,10,1,3,4,6,'name'): '102.4 seconds',
    (1,10,1,3,4,6,'cli'): (edrx_set_timer, (5,'0110','102.4 seconds')),   
    (1,10,1,3,4,7,'total'): 0,
    (1,10,1,3,4,7,'name'): '122.88 seconds',
    (1,10,1,3,4,7,'cli'): (edrx_set_timer, (5,'0111','122.88 seconds')),   
    (1,10,1,3,4,8,'total'): 0,
    (1,10,1,3,4,8,'name'): '143.36 seconds',
    (1,10,1,3,4,8,'cli'): (edrx_set_timer, (5,'1000','143.36 seconds')),   
    (1,10,1,3,4,9,'total'): 0,
    (1,10,1,3,4,9,'name'): '163.84 seconds',
    (1,10,1,3,4,9,'cli'): (edrx_set_timer, (5,'1001','163.84 seconds')),   
    (1,10,1,3,4,10,'total'): 0,
    (1,10,1,3,4,10,'name'): '327.68 seconds',
    (1,10,1,3,4,10,'cli'): (edrx_set_timer, (5,'1010','327.68 seconds')),   
    (1,10,1,3,4,11,'total'): 0,
    (1,10,1,3,4,11,'name'): '655.36 seconds',
    (1,10,1,3,4,11,'cli'): (edrx_set_timer, (5,'1011','655.36 seconds')),   
    (1,10,1,3,4,12,'total'): 0,
    (1,10,1,3,4,12,'name'): '1310.72 seconds',
    (1,10,1,3,4,12,'cli'): (edrx_set_timer, (5,'1100','1310.72 seconds')),   
    (1,10,1,3,4,13,'total'): 0,
    (1,10,1,3,4,13,'name'): '2621.44 seconds',
    (1,10,1,3,4,13,'cli'): (edrx_set_timer, (5,'1101','2621.44 seconds')),   
    (1,10,1,3,4,14,'total'): 0,
    (1,10,1,3,4,14,'name'): '5242.88 seconds',
    (1,10,1,3,4,14,'cli'): (edrx_set_timer, (5,'1110','5242.88 seconds')),   
    (1,10,1,3,4,15,'total'): 0,
    (1,10,1,3,4,15,'name'): '10485.76 seconds',
    (1,10,1,3,4,15,'cli'): (edrx_set_timer, (5,'1111','10485.76 seconds')),      
            
    (1,10,1,3,5,'name'): 'Define ptw Timer for NB-IoT...',
    (1,10,1,3,5,'total'): 16,    
    (1,10,1,3,5,0,'total'): 0,
    (1,10,1,3,5,0,'name'): '2.56 seconds',
    (1,10,1,3,5,0,'cli'): (edrx_ptw_set_timer, (5,'0000','2.56 seconds')),    
    (1,10,1,3,5,1,'total'): 0,
    (1,10,1,3,5,1,'name'): '5.12 seconds',
    (1,10,1,3,5,1,'cli'): (edrx_ptw_set_timer, (5,'0001','5.12 seconds')),   
    (1,10,1,3,5,2,'total'): 0,
    (1,10,1,3,5,2,'name'): '7.68 seconds',
    (1,10,1,3,5,2,'cli'): (edrx_ptw_set_timer, (5,'0010','7.68 seconds')),   
    (1,10,1,3,5,3,'total'): 0,
    (1,10,1,3,5,3,'name'): '10.24 seconds',
    (1,10,1,3,5,3,'cli'): (edrx_ptw_set_timer, (5,'0011','10.24 seconds')),   
    (1,10,1,3,5,4,'total'): 0,
    (1,10,1,3,5,4,'name'): '12.8 seconds',
    (1,10,1,3,5,4,'cli'): (edrx_ptw_set_timer, (5,'0100','12.8 seconds')),   
    (1,10,1,3,5,5,'total'): 0,
    (1,10,1,3,5,5,'name'): '15.36 seconds',
    (1,10,1,3,5,5,'cli'): (edrx_ptw_set_timer, (5,'0101','15.36 seconds')),   
    (1,10,1,3,5,6,'total'): 0,
    (1,10,1,3,5,6,'name'): '17.92 seconds',
    (1,10,1,3,5,6,'cli'): (edrx_ptw_set_timer, (5,'0110','17.92 seconds')),   
    (1,10,1,3,5,7,'total'): 0,
    (1,10,1,3,5,7,'name'): '20.48 seconds',
    (1,10,1,3,5,7,'cli'): (edrx_ptw_set_timer, (5,'0111','20.48 seconds')),   
    (1,10,1,3,5,8,'total'): 0,
    (1,10,1,3,5,8,'name'): '23.04 seconds',
    (1,10,1,3,5,8,'cli'): (edrx_ptw_set_timer, (5,'1000','23.04 seconds')),   
    (1,10,1,3,5,9,'total'): 0,
    (1,10,1,3,5,9,'name'): '25.6 seconds',
    (1,10,1,3,5,9,'cli'): (edrx_ptw_set_timer, (5,'1001','25.6 seconds')),   
    (1,10,1,3,5,10,'total'): 0,
    (1,10,1,3,5,10,'name'): '28.16 seconds',
    (1,10,1,3,5,10,'cli'): (edrx_ptw_set_timer, (5,'1010','28.16 seconds')),   
    (1,10,1,3,5,11,'total'): 0,
    (1,10,1,3,5,11,'name'): '30.72 seconds',
    (1,10,1,3,5,11,'cli'): (edrx_ptw_set_timer, (5,'1011','30.72 seconds')),   
    (1,10,1,3,5,12,'total'): 0,
    (1,10,1,3,5,12,'name'): '33.28 seconds',
    (1,10,1,3,5,12,'cli'): (edrx_ptw_set_timer, (5,'1100','33.28 seconds')),   
    (1,10,1,3,5,13,'total'): 0,
    (1,10,1,3,5,13,'name'): '35.84 seconds',
    (1,10,1,3,5,13,'cli'): (edrx_ptw_set_timer, (5,'1101','35.84 seconds')),   
    (1,10,1,3,5,14,'total'): 0,
    (1,10,1,3,5,14,'name'): '38.4 seconds',
    (1,10,1,3,5,14,'cli'): (edrx_ptw_set_timer, (5,'1110','38.4 seconds')),   
    (1,10,1,3,5,15,'total'): 0,
    (1,10,1,3,5,15,'name'): '40.96 seconds',
    (1,10,1,3,5,15,'cli'): (edrx_ptw_set_timer, (5,'1111','40.96 seconds')), 

    (1,10,2,'total'): 0,
    (1,10,2,'name'):'Show current eDRX application values',
    (1,10,2,'cli'): (edrx_show_values, None),

    (1,11,'total'): 3,
    (1,11,'name'):'Set Time Zone Reporting (AT+CTZR)...',
    (1,11,0,'total'): 0,
    (1,11,0,'name'): 'Disable time zone reporting of changed event',
    (1,11,0,'cli'): 'AT+CTZR=0',    
    (1,11,1,'total'): 0,
    (1,11,1,'name'): 'Enable timezone reporting by unsolicited result code',
    (1,11,1,'cli'): 'AT+CTZR=1', 
    (1,11,2,'total'): 0,
    (1,11,2,'name'): 'Enable extended timezone reporting by unsolicited result code',
    (1,11,2,'cli'): 'AT+CTZR=2', 
    

    (1,12,'total'): 3,
    (1,12,'name'):'Set Network Registration Status (AT+CREG/AT+CGREG/AT+CEREG)...',

    (1,12,0,'total'): 3,
    (1,12,0,'name'): 'Set Network Registration Status (AT+CREG)...',
    (1,12,0,0,'total'):0,
    (1,12,0,0,'name'): 'Disable network registration unsolicited result code',
    (1,12,0,0,'cli'): 'AT+CREG=0', 
    (1,12,0,1,'total'):0,
    (1,12,0,1,'name'): 'Enable network registration unsolicited result code',
    (1,12,0,1,'cli'): 'AT+CREG=1', 
    (1,12,0,2,'total'):0,
    (1,12,0,2,'name'): 'Enable network registration and location information unsolicited result code',
    (1,12,0,2,'cli'): 'AT+CREG=2', 
    
    (1,12,1,'total'): 4,
    (1,12,1,'name'): 'Set Network Registration Status (AT+CGREG)...',
    (1,12,1,0,'total'):0,
    (1,12,1,0,'name'): 'Disable network registration unsolicited result code',
    (1,12,1,0,'cli'): 'AT+CGREG=0', 
    (1,12,1,1,'total'):0,
    (1,12,1,1,'name'): 'Enable network registration unsolicited result code',
    (1,12,1,1,'cli'): 'AT+CGREG=1', 
    (1,12,1,2,'total'):0,
    (1,12,1,2,'name'): 'Enable network registration and location information unsolicited result code',
    (1,12,1,2,'cli'): 'AT+CGREG=2', 
    (1,12,1,3,'total'):0,
    (1,12,1,3,'name'): 'Enable network registration and location information unsolicited result code for PSM',
    (1,12,1,3,'cli'): 'AT+CGREG=4', 

    (1,12,2,'total'): 4,
    (1,12,2,'name'): 'Set EPS Network Registration Status (AT+CEREG)...',
    (1,12,2,0,'total'):0,
    (1,12,2,0,'name'): 'Disable network registration unsolicited result code',
    (1,12,2,0,'cli'): 'AT+CEREG=0', 
    (1,12,2,1,'total'):0,
    (1,12,2,1,'name'): 'Enable network registration unsolicited result code',
    (1,12,2,1,'cli'): 'AT+CEREG=1', 
    (1,12,2,2,'total'):0,
    (1,12,2,2,'name'): 'Enable network registration and location information unsolicited result code',
    (1,12,2,2,'cli'): 'AT+CEREG=2', 
    (1,12,2,3,'total'):0,
    (1,12,2,3,'name'): 'Enable network registration and location information unsolicited result code for PSM',
    (1,12,2,3,'cli'): 'AT+CEREG=4', 

    (1,13,'total'): 5,
    (1,13,'name'): 'Set Operator Selection ...',
    (1,13,0,'total'):0,
    (1,13,0,'name'): 'Automatic operator selection',
    (1,13,0,'cli'): 'AT+COPS=0', 
    (1,13,1,'total'):0,
    (1,13,1,'name'): 'Manual operator selection...',
    (1,13,1,'cli'): (cops_set, '1'), 
    (1,13,2,'total'):0,
    (1,13,2,'name'): 'Manual deregister from network',
    (1,13,2,'cli'): 'AT+COPS=2', 
    (1,13,3,'total'):0,
    (1,13,3,'name'): 'Set only format ...',
    (1,13,3,'cli'): (cops_set, '3'),     
    (1,13,4,'total'):0,
    (1,13,4,'name'): 'Manual/Automatic operator selection ...',    
    (1,13,4,'cli'): (cops_set, '4'),


    (2,'total') : 3,
    (2,'name'): 'Engineering Commands...',    
    
    (2,0,'total'): 0,
    (2,0,'name'): 'Neighbour Cell',    
    (2,0,'cli'): 'AT+QENG="neighbourcell"',
    
    (2,1,'total'): 0,
    (2,1,'name'): 'Serving Cell',    
    (2,1,'cli'): 'AT+QENG="servingcell"',
    
    (2,2,'total'): 8,
    (2,2,'name'): 'Scan network...',        
    
    (2,2,0,'total'): 0,
    (2,2,0,'name'): 'Restore the module to AUTO mode',    
    (2,2,0,'cli'): 'AT+QCOPS=0,1',
    (2,2,1,'total'): 0,
    (2,2,1,'name'): 'Scan only GSM Cells (may take too long to complete)',    
    (2,2,1,'cli'): 'AT+QCOPS=1,1',
    (2,2,2,'total'): 0,
    (2,2,2,'name'): 'Scan only LTE Cat M1 Cells (may take too long to complete)',    
    (2,2,2,'cli'): 'AT+QCOPS=2,1',
    (2,2,3,'total'): 0,
    (2,2,3,'name'): 'Scan GSM + LTE Cat M1 Cells (may take too long to complete)',    
    (2,2,3,'cli'): 'AT+QCOPS=3,1',
    (2,2,4,'total'): 0,
    (2,2,4,'name'): 'Scan only LTE Cat NB1 Cells (may take too long to complete)',    
    (2,2,4,'cli'): 'AT+QCOPS=4,1',
    (2,2,5,'total'): 0,
    (2,2,5,'name'): 'Scan GSM + LTE Cat NB1 Cells (may take too long to complete)',    
    (2,2,5,'cli'): 'AT+QCOPS=5,1',
    (2,2,6,'total'): 0,
    (2,2,6,'name'): 'Scan LTE Cat M1 + LTE Cat NB1 Cells (may take too long to complete)',    
    (2,2,6,'cli'): 'AT+QCOPS=6,1',    
    (2,2,7,'total'): 0,
    (2,2,7,'name'): 'Scan GSM + LTE Cat M1 + LTE Cat NB1 Cells (may take too long to complete)',    
    (2,2,7,'cli'): 'AT+QCOPS=7,1',  


    (3,'total') : 8,
    (3,'name') : 'PS Commands...',
 
    (3,0,'total') : 0,
    (3,0,'name'): 'Get Attachment/Detachment information (AT+CGATT)',
    (3,0,'cli'): 'AT+CGATT?', 
 
    (3,1,'total') : 2,
    (3,1,'name'): 'Get PDN definitions (AT+CGDCONT/AT+QICSGP)',
    (3,1,0,'total') : 0,
    (3,1,0,'name'): 'Get PDN definitions (AT+CGDCONT)',
    (3,1,0,'cli'): 'AT+CGDCONT?', 
    (3,1,1,'total') : 0,
    (3,1,1,'name'): 'Get PDN definitions (AT+QICSGP)',
    (3,1,1,'cli'): (qicsgp_info, None), 


    (3,2,'total') : 0,
    (3,2,'name'): 'Get PDN Addresses (AT+CGPADDR)',
    (3,2,'cli'): 'AT+CGPADDR',     

    (3,3,'total') : 2,
    (3,3,'name'): 'Get PDN Contexts Status (AT+CGACT/AT+QIACT) ...', 
    (3,3,0,'total') : 0,
    (3,3,0,'name'): 'Get PDN Contexts Status (AT+CGACT)',
    (3,3,0,'cli'): 'AT+CGACT?', 
    (3,3,1,'total') : 0,
    (3,3,1,'name'): 'Get PDN Contexts Status (AT+QIACT)',
    (3,3,1,'cli'): 'AT+QIACT?', 

    (3,4,'total') : 2,
    (3,4,'name'): 'Set Attach/Detach (AT+CGATT) ...',
    (3,4,0,'total'): 0,
    (3,4,0,'name'): 'Detach',
    (3,4,0,'cli'): 'AT+CGATT=0', 
    (3,4,1,'total'): 0,
    (3,4,1,'name'): 'Attach',
    (3,4,1,'cli'): 'AT+CGATT=1',
    
    (3,5,'total') : 2,
    (3,5,'name'): 'Set PDN definitions per ContextID (AT+CGDCONT/AT+QICSGP) ...',
    (3,5,0,'total') : 2,
    (3,5,0,'name'): 'Set PDN definitions per ContextID (AT+CGDCONT) ...',    
    (3,5,0,0,'total'):0,
    (3,5,0,0,'name'): 'Configure ContextID PDN definition ...',
    (3,5,0,0,'cli'): (cgdcont_definition, None),  
    (3,5,0,1,'total'):0,
    (3,5,0,1,'name'): 'Reset ContextID PDN definition ...',
    (3,5,0,1,'cli'): (cgdcont_reset, None),  
    (3,5,1,'total') : 0,
    (3,5,1,'name'): 'Set PDN definitions per ContextID (AT+QICSGP)',    
    (3,5,1,'cli'): (qicsgp_definition, None),  
    

    (3,6,'total') : 2,
    (3,6,'name'): 'Set PDN Activation/Deactivation (AT+CGACT/AT+QIACT/AT+QIDEACT) ...',
    (3,6,0,'total') : 2,
    (3,6,0,'name'): 'Set PDN Activation/Deactivation (AT+CGACT) ...',
    (3,6,0,0,'total'): 0,
    (3,6,0,0,'name'): 'Activate PDP ...',
    (3,6,0,0,'cli'): (cgact_set,1), 
    (3,6,0,1,'total'): 0,
    (3,6,0,1,'name'): 'Deactivate PDP ...',
    (3,6,0,1,'cli'): (cgact_set,0),
    (3,6,1,'total') : 2,
    (3,6,1,'name'): 'Set PDN Activation/Deactivation (AT+QIACT/AT+QIDEACT) ...',
    (3,6,1,0,'total'): 0,
    (3,6,1,0,'name'): 'Activate PDP ...',
    (3,6,1,0,'cli'): (qiact_qideact_set,1), 
    (3,6,1,1,'total'): 0,
    (3,6,1,1,'name'): 'Deactivate PDP ...',
    (3,6,1,1,'cli'): (qiact_qideact_set,0),



   
    (3,7,'total') : 2,
    (3,7,'name'): 'Set Activate/Deactivate Packet Domain Event Reporting (AT+CGEREP) ...',
    (3,7,0,'total'): 0,
    (3,7,0,'name'): 'Activate',
    (3,7,0,'cli'): 'AT+CGEREP=2,1', 
    (3,7,1,'total'): 0,
    (3,7,1,'name'): 'Deactivate',
    (3,7,1,'cli'): 'AT+CGEREP=0',
   
 
    (4,'total'): 6,
    (4,'name'): 'Connectivity AT commands ...',
    (4,0,'total'): 0,
    (4,0,'name'): 'Ping remote server ...',
    (4,0,'cli'): (qping_set, None),
    (4,1,'total'): 0,
    (4,1,'name'): 'Get addresses of DNS Servers ...',
    (4,1,'cli'): (qidnscfg_info, None),  
    (4,2,'total'): 0,
    (4,2,'name'): 'Configure address of DNS Server ...',
    (4,2,'cli'): (qidnscfg_set, None),      
    (4,3,'total'): 0,
    (4,3,'name'): 'Get IP address by Domain Name ...',
    (4,3,'cli'): (qidnsgip_info, None), 
    
    (4,4,'total'): 5,
    (4,4,'name'): 'TCP/IP options ...',
    (4,4,0,'total'): 0,
    (4,4,0,'name'): 'Open a socket service ...',    
    (4,4,0,'cli'): (socket_open, None),      
    
    (4,4,1,'total'): 0,
    (4,4,1,'name'): 'Close a socket service ...',    
    (4,4,1,'cli'): (socket_close, None),   

    (4,4,2,'total'): 2,
    (4,4,2,'name'): 'Query socket status ...',    
    (4,4,2,'cli'): 'AT+QISTATE?',   
    (4,4,2,0,'total'): 0,
    (4,4,2,0,'name'): 'Query all socket status',    
    (4,4,2,0,'cli'): 'AT+QISTATE?', 
    (4,4,2,1,'total'): 0,
    (4,4,2,1,'name'): 'Query all socket status per ContextID',    
    (4,4,2,1,'cli'): (socket_status, None), 
    
    (4,4,3,'total'): 2,
    (4,4,3,'name'): 'Send Data ...', 
    
    (4,4,3,0,'total'): 0,
    (4,4,3,0,'name'): 'Send Data for TCP/TCP SERVER/UDP Service Type ...',    
    (4,4,3,0,'cli'): (socket_send, 0), 
    (4,4,3,1,'total'): 0,
    (4,4,3,1,'name'): 'Send Data for UDP SERVER Service Type ...',    
    (4,4,3,1,'cli'): (socket_send, 1),     
       
    
    (4,4,4,'total'): 0,
    (4,4,4,'name'): 'Retrieve received Data ...',     
    (4,4,4,'cli'): (socket_receive, None),       
 
    (4,5,'total'): 2,
    (4,5,'name'): 'NTP options ...',
    (4,5,0,'total'): 0,
    (4,5,0,'name'): 'Synchronize local time with NTP ...',    
    (4,5,0,'cli'): (ntp_set, None),      
    
    (4,5,1,'total'): 0,
    (4,5,1,'name'): 'Get Clock (AT+CCLK)',    
    (4,5,1,'cli'): 'AT+CCLK?',  
 
 
    (5,'total'): 0,
    (5,'name'): 'Execute AT command ...',
    (5,'cli'): (execute_at_command, None),


    (6,'total') : 0,
    (6,'name'): 'Show menu tree',  
    (6,'cli'): (dummy_menu_tree, None),
    
    }
    
    return menu_dict

# print menu tree     
def dummy_menu_tree(dummy1, dummy2):
    return 1000    
###################################################### ###################################################### 
###################################################### ###################################################### 
###################################################### ###################################################### 
###################################################### ###################################################### 
###################################################### ######################################################     
    

def process_at_output(buffer, log_file):
    
    if 'ERROR' in buffer or 'OK' in buffer:
        return
    elif '+' not in buffer or ':' not in buffer:
        return
    else:
        aux = buffer.split('\r\n')
        if True:
        #try:   
        
            cmd = aux[0].split('+')[1].split(':')[0]
            param = aux[0].split('+')[1].split(':')[1].strip().split(',')
            decoded_at_command_output(cmd,param,log_file)
        #except:
        #    pass
                    
    
def decoded_at_command_output(cmd,param,log_file):
    cmd_func = {
        'QENG': cmd_qeng,
        'COPS': cmd_cops,
        'QCFG': cmd_qcfg,
        'CREG': cmd_creg,
        'CGREG': cmd_creg, 
        'CEREG': cmd_creg,         
        'CPSMS': cmd_cpsms,
        'QPSMEXTCFG': cmd_qpsmextcfg,
        'QCSCON': cmd_qcscon,
        'CEDRXS': cmd_cedrxs,
        'CEDRXP': cmd_cedrxs,
        'CEDRXRDP': cmd_cedrxs,
        'QNWINFO': cmd_qnwinfo,
        'QCSQ': cmd_qcsq,
        'QPTWEDRXS': cmd_qptwedrxs,   
        'QPTWEDRXP': cmd_qptwedrxs,
        'CGATT': cmd_cgatt,
        'CGACT': cmd_cgact,
        'CGDCONT': cmd_cgdcont,
        'CGPADDR': cmd_cgpaddr,
        'QPING': cmd_qping,
        'QIACT': cmd_qiact,
        'QIURC': cmd_qiurp,
        'QIOPEN': cmd_qiopen,
        'QISTATE': cmd_qistate,
        'QIRD': cmd_qird,
        'QCOPS': cmd_qcops        
    }
    func = cmd_func.get(cmd, unsupported_cmd)     
    func(param,log_file)
    
    
def unsupported_cmd(param,log_file):
    #print(param)
    return
    
def unsupported_option():
    return
    
def print_output(key,value,log_file):
    for i in range(len(value)):
        print(key[i],':',value[i])
        print_log(key[i] + ' : ' + value[i],log_file)
            
    print('-----------------------------------------------------------------------')         

         

def generic_print_output(param, param_list, dict_list, log_file):
    key = ()
    value = []
    
    try:
        for i in range(len(param_list)):
            key += (param_list[i],)
            if dict_list[i] is not None:
                value.append(dict_list[i].get(param[i],param[i]) + ' (' +  param[i] + ')')
            else:
                value.append(param[i])
    except:
        pass
    print_output(key, value, log_file)


###################################################### ###################################################### 
###################################################### ###################################################### 
###################################################### ###################################################### 
###################################################### ###################################################### 
###################################################### ###################################################### 


def cmd_qcops(param, log_file):
    gprs_support = {
        '0': 'Not support for GPRS',
        '1': 'Support for GPRS'
    }
    if param[0] == 'GSM':    
        param_list = ['RAT','PLMN NAME','PLMN','BAND','CHANNEL','LAC','CELL ID','BSIC','RX LEVEL','C1','GPRS SUPPORT']
        dict_list = [None,None,None,None,None,None,None,None,None,None,gprs_support]       
    else:
        param_list = ['RAT','PLMN NAME','PLMN','BAND','CHANNEL','TAC','PC ID','RRSI','RSRP','RSRQ']
        dict_list = [None,None,None,None,None,None,None,None,None,None]     

    generic_print_output(param,param_list,dict_list,log_file)


def cmd_qird(param,log_file):
    
    param_list = ['READ ACTUAL LENGTH','REMOTE IP ADDRESS','REMOTE PORT']
    dict_list = [None,None,None]       

    generic_print_output(param,param_list,dict_list,log_file)

def cmd_qistate(param,log_file):
    state = {
        '0': 'Initial',
        '1': 'Opening',
        '2': 'Connected',
        '3': 'Listening',
        '4': 'Closing'
    }
    access_mode = {
        '0': 'Buffer access mode',
        '1': 'Direct push mode',
        '2': 'Transparent access mode'
    }     
    at_port = {
        '"usbmodem"': 'USB MODEM PORT',
        '"usbat"': 'USB AT PORT',
        '"uart1"': 'UART PORT1'
    }     
    param_list = ['CONNECT ID','SERVICE TYPE', 'IP ADDRESS', 'REMOTE PORT','LOCAL PORT','SOCKET STATE','CONTEXT ID','SERVER ID','ACCESS MODE','AT PORT']
    dict_list = [None,None,None,None,None,state,None,None,access_mode,at_port]       

    generic_print_output(param,param_list,dict_list,log_file)


def cmd_qiopen(param,log_file):
    global error_code
    param_list = ['CONNECT ID','RESULT']
    dict_list = [None,error_code]       

    generic_print_output(param,param_list,dict_list,log_file)



def cmd_qiact(param,log_file):
    state = {
        '0': 'Deactivated',
        '1': 'Activated'
    }
    context_type = {
        '1': 'IPV4',
        '2': 'IPV6'
    }    
    param_list = ['CONTEXT ID','CONTEXT STATE','CONTEXT TYPE','PDP ADDRESS']
    dict_list = [None,state,context_type,None]
    generic_print_output(param,param_list,dict_list,log_file)


   
    
def cmd_qping(param,log_file):
    global error_code
    if len(param) == 5:
        param_list = ['RESULT','IP ADDRESS','BYTES','TIME','TTL']
        dict_list = [error_code,None,None,None,None]       
    else:
        param_list = ['FINAL RESULT','SENT','RCVD','LOST','MIN','MAX','AVG']
        dict_list = [error_code,None,None,None,None,None,None]
    generic_print_output(param,param_list,dict_list,log_file)

    
def cmd_qpsmextcfg(param,log_file):
    param_list = ['PSM OPT MASK','MAX OOS FULL SCAN','PSM DURATION DUE TO OOS','PSM RANDOMIZATION WINDOW','MAX OOS TIME','EARLY WAKE UP TIME']
    dict_list = [None,None,None,None,None,None]
    generic_print_output(param,param_list,dict_list,log_file)


def cmd_cgpaddr(param,log_file):
    param_list = ['CID','PDP ADDRESS']
    dict_list = [None,None]
    generic_print_output(param,param_list,dict_list,log_file)
    

def cmd_cgatt(param,log_file):
    state = {
        '0': 'Detached',
        '1': 'Attached'
    }
    param_list = ['STATE']
    dict_list = [state]
    generic_print_output(param,param_list,dict_list,log_file)


def cmd_cgdcont(param,log_file):
    param_list = ['CONTEXT ID','PDP TYPE','APN','PDP ADDRESS','DATA COMPRESSION','HEADER COMPRESSION']
    dict_list = [None,None,None,None,None,None]
    generic_print_output(param,param_list,dict_list,log_file)

def cmd_cgact(param,log_file):
    state = {
        '0': 'Deactivated',
        '1': 'Activated'
    }
    param_list = ['CONTEXT ID','STATE']
    dict_list = [None,state]
    generic_print_output(param,param_list,dict_list,log_file)


def cmd_qcsq(param,log_file):
    param_list = ['SYS-MODE','RSSI','RSRP','SINR','RSRQ']
    dict_list = [None,None, None,None,None]
    generic_print_output(param,param_list,dict_list,log_file)

def cmd_qnwinfo(param,log_file):
    param_list = ['ACT-TYPE','OPERATOR','BAND','CHANNEL']
    dict_list = [None,None, None,None]
    generic_print_output(param,param_list,dict_list,log_file)       
    
    
def cmd_qeng(param,log_file):
    output_options = {
        '"neighbourcell"': ("GSM","MNC","MCC","LAC","CELLID","BSIC","ARFCN","RXLEV","C1","C2","C31","C32"),
        '"neighbourcell intra"': ("RAT","EARFCN","PCID","RSRQ","RSRP","RSSI","SINR","SRXLEV","CELL_RESEL_PRIORITY","S_NON_INTRA_SEARCH","THRESH_SERVING_LOW","S_INTRA_SEARCH"),
        '"neighbourcell intra"': ("RAT","EARFCN","PCID","RSRQ","RSRP","RSSI","SINR","SRXLEV","CELL_RESEL_PRIORITY","S_NON_INTRA_SEARCH","THRESH_SERVING_LOW","S_INTRA_SEARCH"),
        '"neighbourcell inter"': ("RAT","EARFCN","PCID","RSRQ","RSRP","RSSI","SINR","SRXLEV","THRESH_SERVING_LOW","THRESH_SERVING_HIGH","CELL_RESEL_PRIORITY"),
        '"servingcell"GSM': ("STATE","GSM","MCC","MNC","LAC","CELLID","BSIC","ARFCN","BAND","RXLEV","TXP","RLA","DRX","C1","C2","GPRS","TCH","TS","TA","MAIO","HSN","RXLEVSUB","RXLEVFULL","RXQUALSUB","RXQUALFULL","VOICECODEC") ,
        '"servingcell"': ("STATE","RAT","IS_TDD","MCC","MNC","CELLID","PCID","EARFCN","FREQ_BAND_IND","UL_BANDWIDTH","DL_BANDWIDTH","TAC","RSRP","RSRQ","RSSI","SINR","SRXLEV")
    }

    output = output_options.get(param[0]+param[2], None)
    if output is not None:
        print_output(output,param[1:],log_file)
        return
    output = output_options.get(param[0], None)
    if output is not None:
        print_output(output,param[1:],log_file)
        return




def cmd_cedrxs(param,log_file):

    act_type = {
        '2': 'GSM',
        '3': 'UTRAN',
        '4': 'LTE Cat M1',
        '5': 'LTE Cat NB1'
    }

    param_list = ['ACT-TYPE','REQUESTED eDRX VALUE','NW-PROVIDED eDRX VALUE','PAGING TIME WINDOW (ptw)']
    dict_list = [act_type,None, None,None]
    generic_print_output(param,param_list,dict_list,log_file) 
   
   
def cmd_qptwedrxs(param,log_file):

    act_type = {
        '2': 'GSM',
        '3': 'UTRAN',
        '4': 'LTE Cat M1',
        '5': 'LTE Cat NB1'
    }

    param_list = ['ACT-TYPE','REQUESTED PAGING TIME WINDOW (ptw) VALUE','REQUESTED eDRX VALUE','NW-PROVIDED eDRX VALUE','NW-PROVIDED PAGING TIME WINDOW (ptw) VALUE']
    dict_list = [act_type,None,None, None,None]
    generic_print_output(param,param_list,dict_list,log_file)  
   

def cmd_qcscon(param,log_file):
    n = {
        '0': 'Disable unsolicited result code',
        '1': 'Enable unsolicited result code'
    }
    mode = {
        '0': 'Idle',
        '1': 'Connected'
    }

    param_list = ['N','MODE']
    dict_list = [n,mode]
    generic_print_output(param,param_list,dict_list,log_file)




def cmd_cops(param,log_file):
    if param[0][0] == '(':
        cmd_cops_all(param,log_file)
    else:
        cmd_cops_current(param,log_file)

def cmd_cops_all(param,log_file):
    join_param = ','.join(param)
    param_operators = join_param.split(',,')[0].replace('(','').replace('),','|').replace(')','').split('|')
    stat = {
        '0': 'Unknown',
        '1': 'Operator available',
        '2': 'Current operator',
        '3': 'operator forbidden'
    }
    act = {
        '0': 'GSM',
        '8': 'LTE Cat M1',
        '9': 'LTE Cat NB1'
    }
    param_list = ['STAT','LONG ALPHANUMERIC OPERATOR NAME','SHORT ALPHANUMERIC OPERATOR NAME','NUMERIC OPERATOR','ACT']
    dict_list = [stat,None,None,None,act]
    for i in param_operators:
        generic_print_output(i.split(','),param_list,dict_list,log_file)    
    
    
def cmd_cops_current(param,log_file):
    mode = {
        '0': 'Automatic mode',
        '1': 'Manual operator selection',
        '2': 'Manual deregister from network'
    }
    format = {
        '0': 'Long format alphanumeric',
        '1': 'Short format alphanumeric',
        '2': 'Numeric'
    }
    act = {
        '0': 'GSM',
        '8': 'LTE Cat M1',
        '9': 'LTE Cat NB1'
    }
    param_list = ['MODE', 'FORMAT','OPERATOR','ACT']
    dict_list = [mode,format,None,act]
    generic_print_output(param,param_list,dict_list,log_file)
    
    
    
def cmd_qcfg(param,log_file):
    output_options = {
        '"nwscanseq"': ("SCANSEQ (00-AUTO, 01-GSM, 02-LTE Cat M1, 03-LTE Cat NB1)",),
        '"nwscanmode"': ("SCANMODE (0-AUTO, 1-GSM Only, 3-LTE Only)",),
        '"iotopmode"': ("MODE (0-LTE Cat M1, 1-LTE Cat NB1, 2-LTE Cat M1 and Cat NB1)",),
        '"roamservice"': ("ROAMMODE (1-Disable Roam Service, 2-Enable Roam Service, 255-AUTO)",),
        '"band"': ("GSMBANDVAL","CATM1BANDVAL","CATNB1BANDVAL") ,
        '"celevel"': ("LEVEL",),
        '"servicedomain"':("SERVICE (1-PS Only, 2-CS & PS)",),
        '"nb1/bandprior"':("BAND_VALUE",),
        '"psm/urc"':("ENABLE/DISABLE (0-Disabled, 1-Enabled",),
        '"sgsn"':("SGSNNR (0-R97, 1-R99, 2-Dynamic)",),
        '"msc"':("MSCR (0-R97, 1-R99, 2-Dynamic)",),
        '"pdp/duplicatechk"':("ENABLE (0-Refused, 1-Allowed)",),
        '"ledmode"':("MODE (0-Flicker Mode, 1-Output High LEvel when Attached to Network)",),
        '"ims"':("VALUE (0-Set by MBN File, 1-Enable IMS Function, 2-Disable IMS Function)", "VOLTE_STATE (0-VoLTE not ready, 1-VoLTE ready)"),
        '"urc/ri/ring"':("TYPERI","PULSEDURATION", "ACTIVEDURATION","INACTIVEDURATION","RINGNODISTURBING","PULSECOUNT"),
        '"urc/ri/smsincoming"':("TYPERI","PULSEDURATION","PULSECOUNT"),
        '"urc/ri/other"':("TYPERI","PULSEDURATION","PULSECOUNT"),
        '"risignaltype"':("RISIGNALTYPE",),
        '"urc/delay"':("ENABLE",),
        '"cmux/urcport"':("URC_PORT",),
        '"apready"':("ENABLE/DISABLE (0-Disabled, 1-Enabled)","LEVEL","INTERVAL"),
        '"psm/enter"':("MODE (0-PSM after T3324 Expired, 1-PSM immediately after RRC release)",),
        '"rrcabort"':("MODE",),
        '"nccconf"':("CAP_VAL",)
    }

    output = output_options.get(param[0], None)
    #print(output,param[1:])
    if output is not None:
        print_output(output,param[1:],log_file)
        if param[0] == '"nccconf"':
            decode_nccconf(param[1])    
        elif param[0] == '"band"':
            decode_band('GSM',param[1])
            decode_band('LTE-M',param[2])
            decode_band('NB-IoT',param[3])
    
    
def decode_nccconf(value):
    emm_bits = ['EMM_CP_CIOT','EMM_UP_CIOT','EMM_S1_U','EMM_ER_WITHOUT_PDN','EMM_HC_CP_CIOT','EMM_SMS_ONLY','EMM_PNB_CP_CIOT','EMM_PNB_UP_CIOT','EMM_EPCO_CIOT']
    
    binary = str(bin(int(value, 16))[2:].zfill(9))[::-1] #to reverse string
    for i in range(len(binary)):
        print(emm_bits[i],':',binary[i])



def decode_band(type,value):
    print(type,':\n')
    if type == 'GSM':
        gsm = ['GSM 900 MHz','GSM 1800 MHz','GSM 850MHz','GSM 1900 MHz']
        binary = str(bin(int(value, 16))[2:].zfill(4))[::-1] #to reverse string
        for i in range(len(binary)):
            print(gsm[i],':',binary[i])
    else:
        binary = str(bin(int(value, 16))[2:].zfill(40))[::-1] #to reverse string
        for i in range(len(binary)//4):
            print('LTE B' + str(i+1),':',binary[i],'\t','LTE B' + str(i+11),':',binary[i+10],'\t','LTE B' + str(i+21),':',binary[i+20],'\t','LTE B' + str(i+31),':',binary[i+30])
    print('-----------------------------------------------------------------------')
    
    
def cmd_creg(param,log_file):
    n = {
        '0': 'Disable Network registration unsolicited result code',
        '1': 'Enable Network registration unsolicited result code',
        '2': 'Enable Network registrations and Location information unsolicited result code',
        '4': 'Enable Network registrations and Location information unsolicited result code for PSM'
    }
    stat = {
        '0': 'Not Registered',
        '1': 'Registered, Home Network',
        '2': 'Not Registered, but MT is trying to attach or searching an operator to register to',
        '3': 'Registration denied',
        '4': 'Unknown',
        '5': 'Registered, Roaming'
    }
    rat = {
        '0': 'GSM',
        '8': 'LTE Cat M1',
        '9': 'LTE Cat NB1'
    }
    if len(param) == 10:
        param_list = ['N', 'STAT','LAC', 'CI','RAT','RAC','CAUSE TYPE','REJECT CAUSE','ACTIVE TIMER','PERIODIC TAU']
        dict_list = [n,stat,None,None,rat,None,None,None,None,None]
    else:
        param_list = ['N', 'STAT','LAC', 'CI','RAT','CAUSE TYPE','REJECT CAUSE','ACTIVE TIMER','PERIODIC TAU']
        dict_list = [n,stat,None,None,rat,None,None,None,None]    
    key = ()
    value = []
    
    try:
        for i in range(len(param_list)):
            key += (param_list[i],)
            if dict_list[i] is not None:
                value.append(dict_list[i].get(param[i],param[i]) + ' (' +  param[i] + ')')
            else:
                if (i == 9 and len(param)==10) or (i == 8 and len(param)==9):
                    value.append(param[i] + ' (' + decode_tau_rau(param[i])  + ')')
                elif (i == 8 and len(param)==10) or (i == 7 and len(param)==9) :
                    value.append(param[i] + ' (' + decode_ready_active(param[i])  + ')')
                else:
                    value.append(param[i])
    except:
        pass

    print_output(key, value,log_file)

  
  
def cmd_cpsms(param,log_file):
    mode = {
        '0': 'Disable the use of PSM',
        '1': 'Enable the use of PSM'
    }

    param_list = ['MODE', 'NETWORK_PERIODIC-RAU','NETWORK_GPRS-READY-timer', 'NETWORK_PERIODIC-TAU','NETWORK_ACTIVE-Time']
    dict_list = [mode,None,None,None,None]
    key = ()
    value = []

    try:
        for i in range(len(param_list)):
            key += (param_list[i],)
            if dict_list[i] is not None:
                value.append(dict_list[i].get(param[i],param[i]) + ' (' +  param[i] + ')')
            else:
                if param[i] == '':
                    value.append(param[i])
                elif i == 1 or i == 3:
                    value.append(param[i] + ' (' + decode_tau_rau(param[i])  + ')')
                elif i == 2 or i == 4:
                    value.append(param[i] + ' (' + decode_ready_active(param[i])  + ')')
    except:
        pass
    print_output(key, value,log_file)
    
    
def decode_tau_rau(timer):
    unit = {
        '000': (10, 'minutes'),
        '001': (1, 'hour'),
        '010': (10, 'hour'),
        '011': (2, 'seconds'),
        '100': (30, 'seconds'),
        '101': (1, 'minute')
    } 
    timer_unit = unit.get(timer[1:4], None)
    timer_value = int(timer[4:-1],2)
    if timer_unit is not None:
        return str(timer_unit[0]*timer_value) + ' ' + timer_unit[1]
    else:
        return 'unknown value'

def decode_ready_active(timer):
    unit = {
        '000': (2, 'seconds'),
        '001': (1, 'minute'),
        '010': (6, 'minutes'),
        '111': (0, 'deactivated')
    } 
    timer_unit = unit.get(timer[1:4], None)
    timer_value = int(timer[4:-1],2)
    if timer_unit is not None:
        return str(timer_unit[0]*timer_value) + ' ' + timer_unit[1]
    else:
        return 'unknown value'
        
        
def reset_psm_timer(dummy1,dummy2):
    global psm_requested_periodic_rau, psm_requested_gprs_ready_timer, psm_requested_periodic_tau, psm_requested_active_timer
    psm_requested_periodic_rau = ('00000000','')
    psm_requested_gprs_ready_timer = ('00000000','')
    psm_requested_periodic_tau = ('00000000','')
    psm_requested_active_timer = ('00000000','')
    
def psm_timers_set(ser,mode):
    if mode == 1:
        at_cmd(ser,'AT+CPSMS=1,"' + psm_requested_periodic_rau[0] + '","' + psm_requested_gprs_ready_timer[0] + '","' + psm_requested_periodic_tau[0] + '","' + psm_requested_active_timer[0] + '"')
    else:
        at_cmd(ser,'AT+CPSMS=0,"' + psm_requested_periodic_rau[0] + '","' + psm_requested_gprs_ready_timer[0] + '","' + psm_requested_periodic_tau[0] + '","' + psm_requested_active_timer[0] + '"')    


##### QIURP - Multiple output #####
def cmd_qiurp(param,log_file):
    if param[0] == '"dnsgip"':
        cmd_qiurp_dnsgip(param,log_file)
    elif param[0] == '"closed"':
        cmd_qiurp_closed(param,log_file)
    elif param[0] == '"recv"':
        cmd_qiurp_recv(param,log_file)
    elif param[0] == '"incoming"':
        cmd_qiurp_incoming(param,log_file)
    elif param[0] == '"incoming full"':
        cmd_qiurp_incoming_full(param,log_file)        
    elif param[0] == '"pdpdeact"':
        cmd_qiurp_pdpdeact(param,log_file)

def cmd_qiurp_dnsgip(param,log_file):
    global error_code
    if len(param) == 2:
        param_list = ['DNSGIP','HOST IP ADDRESS']
        dict_list = [None,None]    
    else:
        param_list = ['DNSGIP','RESULT','IP COUNT','DNS TTL']
        dict_list = [None,error_code,None,None]
    generic_print_output(param,param_list,dict_list,log_file) 

def cmd_qiurp_closed(param,log_file):
    param_list = ['SOCKET CLOSED','CONNECT ID']
    dict_list = [None,None]    
    generic_print_output(param,param_list,dict_list,log_file) 

def cmd_qiurp_recv(param,log_file):
    param_list = ['DATA RECEIVED','CONNECT ID','LENGTH OF DATA','REMOTE IP','REMOTE PORT','DATA']
    dict_list = [None,None,None,None,None,None]    
    generic_print_output(param,param_list,dict_list,log_file) 

def cmd_qiurp_incoming(param,log_file):
    param_list = ['INCOMING CONNECTION','CONNECT ID','SERVER ID','REMOTE IP','REMOTE PORT']
    dict_list = [None,None,None,None,None]    
    generic_print_output(param,param_list,dict_list,log_file) 

def cmd_qiurp_incoming_full(param,log_file):
    param_list = ['INCOMING CONNECTIONS LIMIT REACHED']
    dict_list = [None]    
    generic_print_output(param,param_list,dict_list,log_file) 

def cmd_qiurp_pdpdeact(param,log_file):
    param_list = ['PDP DEACTIVATION','CONTEXT ID']
    dict_list = [None,None]    
    generic_print_output(param,param_list,dict_list,log_file) 

##################################################################
##################################################################
##################################################################



def psm_enter_timer(dummy, timer_type_timer_unit):
    global psm_requested_periodic_rau, psm_requested_gprs_ready_timer, psm_requested_periodic_tau, psm_requested_active_timer
    timer_type = timer_type_timer_unit[0]
    timer_unit = timer_type_timer_unit[1]
    timer_unit_text = timer_type_timer_unit[2]    
    input_text = 'Input value [1-31] for ' + timer_type + ' timer (timer unit: ' + timer_unit_text + '): \n99 - return\n\n'
    clear()
    print(input_text)
    while True:        
        msg = sys.stdin.readline()
        clear()
        if msg[:-1].isdigit() == True:
            value = int(msg[:-1])
            if value == 99:
                return 99
            elif 0 < value < 32:
                timer_value = str(bin(value)[2:].zfill(5))    
                if timer_type == 'RAU':
                    psm_requested_periodic_rau = (timer_unit + timer_value, str(value) + '*' + timer_unit_text)
                elif timer_type == 'READY':
                    psm_requested_gprs_ready_timer = (timer_unit + timer_value, str(value) + '*' + timer_unit_text)
                elif timer_type == 'TAU':
                    psm_requested_periodic_tau = (timer_unit + timer_value, str(value) + '*' + timer_unit_text)
                elif timer_type == 'ACTIVE':
                    psm_requested_active_timer = (timer_unit + timer_value, str(value) + '*' + timer_unit_text)
                
                break
            else:
                print('Values should be between 1 and 31.')
                print(input_text)
        else:
            print('Values should be numbers between 1 and 31.')
            print(input_text)
            
    return 99
   


def psm_show_values(dummy1,dummy2):
    global psm_requested_periodic_rau, psm_requested_gprs_ready_timer, psm_requested_periodic_tau, psm_requested_active_timer
    param_list = ['PSM REQUESTED PERIODIC RAU','PSM REQUESTED GPRS READY TIMER','PSM REQUESTED PERIODIC TAU','PSM REQUESTED ACTIVE TIMER']
    dict_list = [psm_requested_periodic_rau, psm_requested_gprs_ready_timer, psm_requested_periodic_tau, psm_requested_active_timer]
    for i in range(len(param_list)):
        print(param_list[i],':',dict_list[i][0],'(' + dict_list[i][1] + ')')   
   
 
def nbiot_feature_show_values(dummy1, dummy2):
    global nbiot_features 
    decode_nccconf(nbiot_features) 
 
 
def nbiot_feature_bit(dummy,bit):
    global nbiot_features             
    global nbiot_features_list
    if bit == -1:
        nbiot_features_list = NB_IOT_NUM_BITS*[0]
        nbiot_features = '0'
        
    else:
        nbiot_features_list[bit] = 1
        nbiot_features = format(sum(nbiot_features_list[i] * 2**i for i in range(len(nbiot_features_list))), 'x')
        


def nbiot_feature_set(ser,dummy):
    global nbiot_features  
    at_cmd(ser,'AT+QCFG="nccconf",' + nbiot_features)    




def edrx_show_values(dummy1,dummy2):
    global edrx_gsm, edrx_utran, edrx_lte_m, edrx_lte_nbiot, edrx_ptw_gsm, edrx_ptw_utran, edrx_ptw_lte_m, edrx_ptw_lte_nbiot
    param_list = ['EDRX GSM','EDRX UTRAN','EDRX LTE-M','EDRX NB-IoT','EDRX ptw GSM','EDRX ptw UTRAN','EDRX ptw LTE-M','EDRX ptw NB-IoT']
    dict_list = [edrx_gsm, edrx_utran, edrx_lte_m, edrx_lte_nbiot, edrx_ptw_gsm, edrx_ptw_utran, edrx_ptw_lte_m, edrx_ptw_lte_nbiot]
    for i in range(len(param_list)):
        print(param_list[i],':',dict_list[i][0],'(' + dict_list[i][1] + ')')    
       


def edrx_enter_cmd(ser,mode_act_type):
    global edrx_gsm, edrx_utran, edrx_lte_m, edrx_lte_nbiot
    mode = str(mode_act_type[0])
    act_type = str(mode_act_type[1])
    if act_type == '2':
        at_cmd(ser,'AT+CEDRXS=' + mode + ',' + act_type + ',"' + edrx_gsm[0] + '"') 
    elif act_type == '3':
        at_cmd(ser,'AT+CEDRXS=' + mode + ',' + act_type + ',"' + edrx_utran[0] + '"') 
    elif act_type == '4':
        at_cmd(ser,'AT+CEDRXS=' + mode + ',' + act_type + ',"' + edrx_lte_m[0] + '"') 
    elif act_type == '5':
        at_cmd(ser,'AT+CEDRXS=' + mode + ',' + act_type + ',"' + edrx_lte_nbiot[0] + '"')       


def edrx_ptw_enter_cmd(ser,mode_act_type):
    global edrx_gsm, edrx_utran, edrx_lte_m, edrx_lte_nbiot, edrx_ptw_gsm, edrx_ptw_utran, edrx_ptw_lte_m, edrx_ptw_lte_nbiot
    mode = str(mode_act_type[0])
    act_type = str(mode_act_type[1])
    if act_type == '2':
        at_cmd(ser,'AT+QPTWEDRXS=' + mode + ',' + act_type + ',"' + edrx_ptw_gsm[0] + '","' + edrx_gsm[0] + '"') 
    elif act_type == '3':
        at_cmd(ser,'AT+QPTWEDRXS=' + mode + ',' + act_type + ',"' + edrx_ptw_utran[0] + '","' + edrx_utran[0] + '"') 
    elif act_type == '4':
        at_cmd(ser,'AT+QPTWEDRXS=' + mode + ',' + act_type + ',"' + edrx_ptw_lte_m[0] + '","' + edrx_lte_m[0] + '"') 
    elif act_type == '5':
        at_cmd(ser,'AT+QPTWEDRXS=' + mode + ',' + act_type + ',"' + edrx_ptw_lte_nbiot[0] + '","' + edrx_lte_nbiot[0] + '"') 


def edrx_set_timer(dummy, act_type_timer_text):
    global edrx_gsm, edrx_utran, edrx_lte_m, edrx_lte_nbiot
    act_type = act_type_timer_text[0]
    timer = act_type_timer_text[1]
    timer_text = act_type_timer_text[2]
    if act_type == 2:
        edrx_gsm = (timer, timer_text)
    elif act_type == 3:
        edrx_utran = (timer, timer_text)
    elif act_type == 4:
        edrx_lte_m = (timer, timer_text)
    elif act_type == 5:
        edrx_lte_nbiot = (timer, timer_text)
       
    clear()       
    return 99
    
      
def edrx_ptw_set_timer(dummy, act_type_timer_text):
    global edrx_ptw_gsm, edrx_ptw_utran, edrx_ptw_lte_m, edrx_ptw_lte_nbiot
    act_type = act_type_timer_text[0]
    timer = act_type_timer_text[1]
    timer_text = act_type_timer_text[2]
    if act_type == 2:
        edrx_ptw_gsm = (timer, timer_text)
    elif act_type == 3:
        edrx_ptw_utran = (timer, timer_text)
    elif act_type == 4:
        edrx_ptw_lte_m = (timer, timer_text)
    elif act_type == 5:
        edrx_ptw_lte_nbiot = (timer, timer_text)        
       
    clear()       
    return 99      


def execute_at_command(ser, dummy):
  
    input_text = 'Enter the AT command to execute:\n99 - return\n\n'
    clear()
    #print(input_text)
    while True:        
        print(input_text)
        msg = sys.stdin.readline()
        if msg[:-1].isdigit() == True:
            value = int(msg[:-1])
            if value == 99:
                clear()
                return 99        
        clear()
        
        at_cmd(ser,msg[:-1]) 
            
    return 99    
   

def qicsgp_definition(ser,dummy):   

    input_list = [
        ['Enter the Context ID to configure [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None],
        ['Choose the PDP Type:\n1 - IPV4\n2 - IPV6\n3 - IPV4V6\n\n99 - return\n\n',{str(i) for i in range(1,4)},None],
        ['Enter the APN name:\n\n99 -return\n\n',{None},None],
        ['Enter the username:\n\n99 -return\n\n',{None},None],
        ['Enter the password:\n\n99 -return\n\n',{None},None],
        ['Choose the Authetication method:\n0 - None\n1 - PAP\n2 - CHAP\n3 - PAP or CHAP\n\n99 - return\n\n',{str(i) for i in range(0,4)},None],
        ['Enter Y/y to configure...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QICSGP='+ input_list[0][2] + ',' + input_list[1][2] + ',"' + input_list[2][2] + '","' + input_list[3][2] + '","' + input_list[4][2] + '",' + input_list[5][2]) 

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1        


    
def cgdcont_definition(ser, dummy):
    
    pdp_type = {
        '1': '"IP"',
        '2': '"IPV6"',
        '3': '"IPV4V6"',
        '4': '"PPP"'
    }     
    input_list = [
        ['Enter the Context ID to configure [1-24]:\n99 - return\n\n',{str(i) for i in range(25)},None],
        ['Choose the PDP Type:\n1 - IPV4\n2 - IPV6\n3 - IPV4V6\n4 - PPP\n\n99 - return\n\n',{str(i) for i in range(1,5)},None],
        ['Enter the APN name:\n\n99 -return\n\n',{None},None],
        ['Enter Y/y to configure...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+CGDCONT='+ input_list[0][2] + ',' + pdp_type.get(input_list[1][2]) + ',"' + input_list[2][2] + '"') 

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1        


def qiact_qideact_set(ser,type):
    input_list = ['Enter the Context ID to configure [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            if type == 1: #activate
                at_cmd(ser,'AT+QIACT=' + input_list[2]) 
            elif type == 0: #deactivate
                at_cmd(ser,'AT+QIDEACT=' + input_list[2])
            return 98
        else:
            continue

def cgact_set(ser,type):    
    input_list = ['Enter the Context ID to configure [1-24]:\n99 - return\n\n',{str(i) for i in range(25)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            at_cmd(ser,'AT+CGACT='+ str(type) + ',' + input_list[2]) 
            return 98
        else:
            continue

def cgdcont_reset(ser,dummy):    
    input_list = ['Enter the Context ID to reset [1-24]:\n99 - return\n\n',{str(i) for i in range(25)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            at_cmd(ser,'AT+CGDCONT=' + input_list[2]) 
            return 98
        else:
            continue


def qicsgp_info(ser,dummy):
    input_list = ['Enter the Context ID to get information [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            at_cmd(ser,'AT+QICSGP=' + input_list[2]) 
            return 98
        else:
            continue
            
            
def qping_set(ser, dummy):
     
    input_list = [
        ['Enter the Context ID to use [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None],
        ['Enter the server IP address/domain:\n\n99 - return\n\n',{None},None],
        ['Enter the timeout [1-255 seconds]:\n\n99 -return\n\n',{str(i) for i in range(256)},None],
        ['Enter the number of Pings to send [1-10]:\n\n99 -return\n\n',{str(i) for i in range(1,11)},None],
        ['Enter Y/y to send Ping...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QPING='+ input_list[0][2] + ',"' + input_list[1][2] + '",' + input_list[2][2] + ',' + input_list[3][2]) 

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1 
            
def qidnscfg_set(ser, dummy):

    input_list = [
        ['Enter the Context ID to use [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None],
        ['Enter the primary server IP address:\n\n99 - return\n\n',{None},None],
        ['Enter the secondary server IP address:\n\n99 - return\n\n',{None},None],
        ['Enter Y/y to set DNS addresses...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QIDNSCFG='+ input_list[0][2] + ',"' + input_list[1][2] + '","' + input_list[2][2] + '"') 

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1 
            
def qidnscfg_info(ser,dummy):
    input_list = ['Enter the Context ID to get information [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            at_cmd(ser,'AT+QIDNSCFG=' + input_list[2]) 
            return 98
        else:
            continue


def qidnsgip_info(ser,dummy):            
    input_list = [
        ['Enter the Context ID to use [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None],
        ['Enter the domain to resolve:\n99 - return\n\n',{None},None],
        ['Enter Y/y to get IP addresses...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QIDNSGIP='+ input_list[0][2] + ',"' + input_list[1][2] + '"') 

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1 



def socket_open(ser, dummy):
    service_type = {
        '1': '"TCP"',
        '2': '"TCP LISTENER"',
        '3': '"UDP"',
        '4': '"UDP SERVICE"'
    }     
    access_mode = {
        '1': '0',
        '2': '1',
        '3': '2'
    }      
    input_list = [
        ['Enter the Context ID to use [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None],
        ['Enter the Connect ID to use [0-11]:\n99 - return\n\n',{str(i) for i in range(12)},None],        
        ['Enter the Service Type:\n1 - TCP\n2 - TCP Server\n3 - UDP\n4 - UDP server\n\n99 - return\n\n',{str(i) for i in range(1,5)},None],
        ['Enter the Server IP Address/Domain Name (put 127.0.0.1 if Server mode):\n99 -return\n\n',{None},None],
        ['Enter the Remote Port (put 0 if server mode): [0-65535]:\n99 -return\n\n',{str(i) for i in range(0,65536)},None],
        ['Enter the Local Port (if 0 port will be assigned automatically): [0-65535]:\n99 -return\n\n',{str(i) for i in range(0,65536)},None],
        ['Enter the Access Mode to use [1-3]:\n1 - Buffer Access Mode\n2 - Direct Push mode\n3 - Transparent access Mode\n\n99 - return\n\n',{str(i) for i in range(1,4)},None],        
        ['Enter Y/y to open socket...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 99
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QIOPEN='+ input_list[0][2] + ',' + input_list[1][2] + ',' + service_type.get(input_list[2][2]) + ',"' + input_list[3][2] + '",' + input_list[4][2] + ',' + input_list[5][2] + ',' + access_mode.get(input_list[6][2])) 

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1             
            
def socket_close(ser, dummy):            
    input_list = ['Enter the Connect ID to close [0-11]:\n99 - return\n\n',{str(i) for i in range(12)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            at_cmd(ser,'AT+QICLOSE=' + input_list[2] + ',2') #timeout= 2 seconds 
            return 98
        else:
            continue
    
def socket_status(ser, dummy):            
    input_list = ['Enter the Context ID to get information [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            at_cmd(ser,'AT+QISTATE=0,' + input_list[2]) 
            return 98
        else:
            continue
            
def socket_send(ser, type):    
    if type == 0:
        return socket_send_0(ser)
    elif type == 1:
        return socket_send_1(ser)
       
def socket_send_0(ser):
    input_list = [
        ['Enter the Connect ID to use [0-11]:\n99 - return\n\n',{str(i) for i in range(12)},None],
        ['Enter the data to send:\n99 - return\n\n',{None},None],
        ['Enter Y/y to send Data...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QISEND='+ input_list[0][2])
                    at_cmd(ser,input_list[1][2] + chr(26))                    

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1 

            
def socket_send_1(ser):
    input_list = [
        ['Enter the Connect ID to use [0-11]:\n99 - return\n\n',{str(i) for i in range(12)},None],
        ['Enter the remote IP address:\n\n99 - return\n\n',{None},None],
        ['Enter the remote UDP port [0-65535]:\n\n99 - return\n\n',{str(i) for i in range(0,65536)},None],        
        ['Enter the data to send:\n99 - return\n\n',{None},None],
        ['Enter Y/y to send Data...\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QISEND='+ input_list[0][2] + ',' + str(len(input_list[3][2])) + ',"' + input_list[1][2] + '",' + input_list[2][2])
                    #time.sleep(0.5)
                    at_cmd(ser,input_list[3][2])                    

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1
      
    
def socket_receive(ser, dummy):    
    input_list = ['Enter the Connect ID to retrieve data [0-11]:\n99 - return\n\n',{str(i) for i in range(12)},None]
    while True:   
        clear()    
        print(input_list[0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98

        if msg[:-1] in input_list[1]:
            input_list[2] = msg[:-1]
            clear()
            at_cmd(ser,'AT+QIRD=' + input_list[2]) 
            return 98
        else:
            continue
            
            
def ntp_set(ser, dummy):    
    input_list = [
        ['Enter the Context ID to use [1-16]:\n99 - return\n\n',{str(i) for i in range(17)},None],
        ['Enter the NTP server IP address/domain:\n99 - return\n\n',{None},None],
        ['Enter the port (NTP default port: 123):\n99 - return\n\n',{str(i) for i in range(65536)},None],        
        ['Enter Y/y to synchronize NTP local time\n99 - return\n\n',{'y','Y'},None]
    ]
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    at_cmd(ser,'AT+QNTP='+ input_list[0][2] + ',"' + input_list[1][2] + '",' + input_list[2][2]) 

                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1         
            

def band_choice_to_hex(band_list):
    value = 0
    for i in band_list:
        if i[1] == 1: value += 2 ** (i[0]-1)
    return str(hex(value)[2:])

            
def band_choice_current(band_list):
    for i in range(len(band_list)):
        if band_list[i][1] == 1:
            print(str(i),'- BAND LTE' + str(band_list[i][0]),': [X]')
        else:
            print(str(i),'- BAND LTE' + str(band_list[i][0]),': [ ]')
            
def band_choice(ser,type):
    input_list = 'Choose the bands to add:\n99 - return\n\nY/y to configure in modem\n\n'
    if type == 'LTEM':
        band_list = [(1,0),(2,0),(3,0),(4,0),(5,0),(8,0),(12,0),(13,0),(18,0),(19,0),(20,0),(26,0),(28,0),(39,0)]
    else:
        band_list = [(1,0),(2,0),(3,0),(4,0),(5,0),(8,0),(12,0),(13,0),(18,0),(19,0),(20,0),(26,0),(28,0)]    
    band_list_input = [str(x) for x in range(len(band_list))]        
    
    while True:
        clear()
        print(input_list)
        band_choice_current(band_list)
        print()
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        if msg[:-1] in band_list_input:
            print("banana")
            print(band_list[int(msg[:-1])])
            band_list[int(msg[:-1])] = ( band_list[int(msg[:-1])][0], (band_list[int(msg[:-1])][1]+1)%2)
            continue
        
        if msg[:-1] == 'Y' or msg[:-1] == 'y':
            clear()
            if type == 'LTEM':
                at_cmd(ser,'AT+QCFG="band",0,' + band_choice_to_hex(band_list) + ',0')
            else:
                at_cmd(ser,'AT+QCFG="band",0,0,' + band_choice_to_hex(band_list))               

            return 98
            
            
            
def cops_set(ser,type):
    if type == '3':
        input_list = [
            ['Enter the format to use [0-2]:\n99 - return\n\n0 - Long\n1 - Short\n2 - Numeric\n\n',{str(i) for i in range(3)},None],          
            ['Enter Y/y to confirm\n99 - return\n\n',{'y','Y'},None]
        ]
    else:
        input_list = [
            ['Enter the format to use [0-2]:\n99 - return\n\n0 - Long\n1 - Short\n2 - Numeric\n\n',{str(i) for i in range(3)},None],  
            ['Enter the Operator (according to format chosen before):\n99 - return\n\n',{None},None],     
            ['Enter the Access Technology:\n99 - return\n\n0 - GSM\n7 - LTE\n8 - LTE-M\n9 - NB-IoT\n\n',{'0','7','8','9'},None],              
            ['Enter Y/y to confirm\n99 - return\n\n',{'y','Y'},None]
        ]    
    i = 0
    while True:   
        clear()    
        print(input_list[i][0])
        msg = sys.stdin.readline()
        if msg[:-1] == '99': 
            clear()
            return 98
        
        if None not in input_list[i][1]:
            if msg[:-1] in input_list[i][1]:
                input_list[i][2] = msg[:-1]
                i += 1
                if i == len(input_list): #exit
                    clear()
                    if type == '3':
                        at_cmd(ser,'AT+COPS=3,' + input_list[0][2]) 
                    else:
                        at_cmd(ser,'AT+COPS=' + type + ',' + input_list[0][2] + ',"' + input_list[1][2] + '",' + input_list[2][2])                     
                    return 98
            else:
                continue
        else:
            input_list[i][2] = msg[:-1]
            i += 1              
