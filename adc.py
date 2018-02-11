#############
#!/usr/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt
import sys
from math import floor,ceil
class Adc(object):
    """This class simulates function of the ADC

    """
    no_of_bits=4
    lower_ref_voltage=0
    upper_ref_voltage=5
    def __init__(self,no_of_bits=4):
        self.no_of_bits=no_of_bits
    def get_config(self):
        return 'Number of bits {} Lower Ref {} Upper Ref {}'.format(self.no_of_bits,self.lower_ref_voltage,self.upper_ref_voltage)
    def get_adc_val(self,val):
        val=np.clip(val,self.lower_ref_voltage,self.upper_ref_voltage)
        adc_val= np.floor(val*(2**self.no_of_bits-1)/(self.upper_ref_voltage-self.lower_ref_voltage))
        return adc_val

class Visualize_adc(object):
    def __init__(self):
        pass

    def plot(self,signals):
        t_analog = signals[0]
        analog_signal = signals[1]
        analog_signal_for_adc = signals[7]
        t_digital = signals[2]
        t_digital_shift = signals[6]
        digital_signal = signals[3]
        digital_sampling_rate=signals[4]
        adc = signals[5]

        fig, ax1 = plt.subplots()
        ax1.set_ylabel('Voltage',color='b')
        ax1.tick_params('y',colors='b')
        ax1.plot(t_analog,analog_signal,'-b',zorder=10)
        ax1.plot(t_digital[1:],analog_signal_for_adc,'ro')
        ax1.set_xlabel('Time')
        ax1.set_ylim([adc.lower_ref_voltage,adc.upper_ref_voltage])
        ax2 = ax1.twinx()
        ax2.set_ylim([0,2**adc.no_of_bits-1])

        ax2.step(t_digital+t_digital_shift,digital_signal,'r',zorder=10)
        ax2.plot(t_digital[1:],digital_signal[1:],'*g',zorder=10)
        ax2.set_ylabel('ADC value',color='r')
        ax2.tick_params('y',colors='r')
        ax2.grid(True, zorder=5)
        plt.title(adc.get_config())
        #plt.ion()
        #sample_rate_input = input("Enter sampling rate:")  # Python 3
        #plt.title(sample_rate_input) 
        #plt.ioff()
        plt.show()

class System(object):
    """This class create signals and do the AD conversion using ADC class
    """
    analog_sampling_rate=500
    digital_sampling_rate=10
    adc=Adc()
    def __init__(self,analog_sampling_rate=analog_sampling_rate,adc=adc):
        self.analog_sampling_rate=analog_sampling_rate
        self.adc=adc
    def get_signal(self,analog_signal):
        t_analog=np.linspace(0, 1, self.analog_sampling_rate)
        under_sampling_step =int(np.ceil(self.analog_sampling_rate/self.digital_sampling_rate))
        
        analog_signal_for_adc=analog_signal[1::under_sampling_step]
        digital_signal=self.adc.get_adc_val(analog_signal_for_adc)
        digital_signal = np.concatenate((digital_signal[0:1],digital_signal))
        t_digital_shift = (t_analog[under_sampling_step+1]-t_analog[1])/2        
        t_digital=(t_analog[1::under_sampling_step]) #+ t_digital_shift;
        t_digital = np.concatenate((t_digital[0:1]-t_digital_shift,t_digital))

        return [t_analog, analog_signal,t_digital,digital_signal,self.digital_sampling_rate,self.adc,t_digital_shift,analog_signal_for_adc]

adc_no_of_bits=4
if len(sys.argv) >1:
    adc_no_of_bits=int(sys.argv[1])

a=Adc(adc_no_of_bits)
s=System(500,a)

x = np.linspace(0, 1, s.analog_sampling_rate)
#x = np.abs(np.sin(4*np.pi*x)*np.exp(-5*x))*8
x = np.sin(4*np.pi*x)*np.exp(-5*x)*6.5+1.1


v = Visualize_adc();
v.plot(s.get_signal(x))    
#s.digital_sampling_rate=500
#v.plot(s.get_signal(x))    

