from pylab import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_tecfile(filename):
    f=open(filename,'r')
    headerline=f.readline()
    header=[x[:x.find('[')].strip(' "') for x in headerline.split(',')]
    lines=f.readlines()

    f.close()

#     This converter stuff is necessary because pflotran doesn't produce the right text format when exponent is <= E-100
    def convertfunc(strval):
        if '-' in strval and 'E' not in strval:
            return 0.0
        else:
            return float(strval)

    converters=dict(((n,convertfunc) for n in range(len(header))))
    return pandas.read_table(filename,skiprows=1,names=header,header=None,delim_whitespace=True,index_col=0,converters=converters)

if __name__=='__main__':
     with open('tide-010.tec') as docfile:
        data = docfile.read()
    
     plt.figure(1);clf()
    # subplot(211)
     plt.plot(data['Free Ca++ [M]'],'Z[m]')
    # plot(data['SOM1'])
    # plot(data['SOM2'])
    # plot(data['SOM3'])
    # plot(data['SOM4'])
    # plot(data['Lit1C'])
    # plot(data['Lit2C'])
    # plot(data['Lit3C'])
     title('C pools')
     legend()
     xlabel('Depth')
     ylabel('Concentration')
    #
    #
    # subplot(212)
    # plot(data['N'],'k--',label='Mineral N')
    # plot(data['Lit1N'])
    # plot(data['Lit2N'])
    # plot(data['Lit3N'])
    # legend()
    # title('N pools')
    # xlabel('Time (days)')
    # ylabel('Concentration (mol cm$^{-3}$)')
    #
    #
    # tight_layout()

    #read_tecfile('ttide-010.tec').plot()

    #show()
