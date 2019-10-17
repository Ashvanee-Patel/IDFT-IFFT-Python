#----------------------------Now start IDFT  implimentation------------------------------>

import math
import threading
#D = [6, -1.5 + 0.866j, -1.5 - 0.866j]
D = [45, -4.5+12.36364j, -4.5+5.36289j, -4.5+2.598j,-4.5+0.79347j, -4.5-0.79347j,-4.5-2.59807j,-4.5-5.36289j,-4.5-12.36364j]
def idft(D):
    N = len(D)
    pi = 180
    IDFT = []#for output
    n = 0    
    def f1(n,u,N):
        W = 0
        while(n < u):
            k = 0
            Op = 0
            while(k < N):
                sr = math.cos(math.radians(2*pi*k*n/N))
                si = math.sin(math.radians(2*pi*k*n/N))*(1j)
                W = sr + si
                Op = Op + (1/N)*(D[k])*W
                k = k + 1
            IDFT.insert(n,round(Op.real,1))
            n = n + 1 #"""

    t1 = threading.Thread(target=f1, args=(0,int(N/2),N))
    t2 = threading.Thread(target=f1, args=(int(N/2),int((N)),N))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(IDFT)
