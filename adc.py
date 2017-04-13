import numpy as np
import matplotlib.pyplot as plt
from math import floor
class Adc(object):
    no_of_bits=4
    lower_ref_voltage=0
    upper_ref_voltage=5
    sampling_rate=10
    saturate=np.array([0]);
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
    a=Adc()   
    def __init__(self,a=Adc()):
        self.a=a
    def plot(self,ang,dig,a=a):
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
        plt.show()
        
class Signal(object):
    input=0;
    output=0;
    def __init__(self):
        print("signal")
    def get_signal():
        return np.arange(0,5,.1)

a=Adc(4)
analog_sampling_rate=500

x = np.linspace(0, 1, analog_sampling_rate)
x = np.abs(np.sin(4*np.pi*x)*np.exp(-5*x))*8
y = a.get_adc_val(x);

v=Visualize_adc(a);
v.plot(x,y,a)    
