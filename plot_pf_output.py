from pylab import *

import pandas

def read_tecfile(filename):
    f=open(filename,'r')
    headerline=f.readline()
    header=[x[:x.find('[')].strip(' "') for x in headerline.split(',')]
    lines=f.readlines()

    f.close()

    # This converter stuff is necessary because pflotran doesn't produce the right text format when exponent is <= E-100
    def convertfunc(strval):
        if '-' in strval and 'E' not in strval:
            return 0.0
        else:
            return float(strval)

    converters=dict(((n,convertfunc) for n in range(len(header))))
    return pandas.read_table(filename,skiprows=1,names=header,header=None,delim_whitespace=True,index_col=0,converters=converters)

if __name__=='__main__':
    # data=read_tecfile('CLM-CN-obs-0.tec')*100**3
    #
    # figure(1);clf()
    # subplot(211)
    # plot(data['C'],'k--',label='CO2')
    # plot(data['SOM1'])
    # plot(data['SOM2'])
    # plot(data['SOM3'])
    # plot(data['SOM4'])
    # plot(data['Lit1C'])
    # plot(data['Lit2C'])
    # plot(data['Lit3C'])
    # title('C pools')
    # legend()
    # xlabel('Time (days)')
    # ylabel('Concentration (mol cm$^{-3}$)')
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

    read_tecfile('test3d-obs-0.tec').plot()

    show()
