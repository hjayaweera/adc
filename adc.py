#############
import numpy as np
import matplotlib.pyplot as plt
from math import floor
class Adc(object):
    """This class simulates function of the ADC

    """
    no_of_bits=4
    lower_ref_voltage=0
    upper_ref_voltage=5
    sampling_rate=10
    def __init__(self,no_of_bits=4):
        self.no_of_bits=no_of_bits
    def get_config(self):
        print('Number of bits {} Lower Ref {} Upper Ref {}'.format(self.no_of_bits,self.lower_ref_voltage,self.upper_ref_voltage))
        return [self.no_of_bits,self.lower_ref_voltage,self.upper_ref_voltage] 
    def get_adc_val(self,val):
        val=np.clip(val,self.lower_ref_voltage,self.upper_ref_voltage)
        adc_val= np.floor(val*(2**self.no_of_bits-1)/(self.upper_ref_voltage-self.lower_ref_voltage))
        return adc_val

class Visualize_adc(object):
    adc=Adc()   
    def __init__(self,adc=Adc()):
        self.adc=adc
    def plot(self,ang,dig,adc=adc):
        t=range(0,len(ang))
        fig, ax1 = plt.subplots()
        ax1.set_ylabel('Voltage',color='b')
        ax1.tick_params('y',colors='b')
        ax1.plot(t,ang,'-b',zorder=10)
        ax1.set_xlabel('Time')

        ax2 = ax1.twinx()
        ax2.step(t[1::10],dig[1::10],'r',zorder=10)
        ax2.set_ylabel('ADC value',color='r')
        ax2.tick_params('y',colors='r')
        ax2.grid(True, zorder=5)
        plt.title("ADC parameters: V_l={} V_u={} No of bits={}".format(self.adc.lower_ref_voltage,self.adc.upper_ref_voltage,self.adc.no_of_bits));
        plt.show()
        
class System(object):
    """This class create signals and do the AD conversion using ADC class
    """
    analog_signal=0;
    digital_signal=0;
    analog_sampling_rate=500
    adc=Adc()
    def __init__(self,analog_sampling_rate=analog_sampling_rate,adc=adc):
        self.analog_sampling_rate=analog_sampling_rate
        self.adc=adc
    def get_signal():
        return np.arange(0,5,.1)

a=Adc(10)
s=System(500,a)

x = np.linspace(0, 1, s.analog_sampling_rate)
x = np.abs(np.sin(4*np.pi*x)*np.exp(-5*x))*8
y = a.get_adc_val(x);

v=Visualize_adc(a);
v.plot(x,y,a)    
