#!/bin/python3.6
import subprocess,sys, datetime
import json
from etcdget import etcdget as get
from ast import literal_eval as mtuple
from socket import gethostname as hostname
from sendhost import sendhost
def sendlog(*args):
 z=[]
 knowns=[]
 myhost=hostname()
 z=['/TopStor/Evacuatelocal.py']
 with open('/root/evacuate','w') as f:
  f.write('bargs'+str(args)+'\n')
 for arg in args:
  z.append(arg)
 leaderinfo=get('leader','--prefix')
 knowninfo=get('known','--prefix')
 leaderip=leaderinfo[0][1]
 for k in knowninfo:
  knowns.append(k[1])
 print('leader',leaderip) 
 print('knowns',knowns) 
 msg={'req': 'Evacuate', 'reply':z}
 print('sending', leaderip, str(msg),'recevreply',myhost)
 sendhost(leaderip, str(msg),'recvreply',myhost)
 for k in knowninfo:
  sendhost(k[1], str(msg),'recvreply',myhost)
  knowns.append(k[1])

if __name__=='__main__':
 sendlog(*sys.argv[1:])
