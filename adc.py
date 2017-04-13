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
        t_digital = signals[2]
        digital_signal = signals[3]
        adc = signals[4]
        fig, ax1 = plt.subplots()
        ax1.set_ylabel('Voltage',color='b')
        ax1.tick_params('y',colors='b')
        ax1.plot(t_analog,analog_signal,'-b',zorder=10)
        ax1.set_xlabel('Time')
        ax1.set_ylim([adc.lower_ref_voltage,adc.upper_ref_voltage])
        ax2 = ax1.twinx()
        ax2.set_ylim([0,2**adc.no_of_bits-1])

        ax2.step(t_digital,digital_signal,'r',zorder=10)
        ax2.set_ylabel('ADC value',color='r')
        ax2.tick_params('y',colors='r')
        ax2.grid(True, zorder=5)
        plt.title(adc.get_config())
        plt.show()
 
        
class System(object):
    """This class create signals and do the AD conversion using ADC class
    """
    analog_sampling_rate=500
    adc=Adc()
    def __init__(self,analog_sampling_rate=analog_sampling_rate,adc=adc):
        self.analog_sampling_rate=analog_sampling_rate
        self.adc=adc
    def get_signal(self,analog_signal):
        t_analog=np.linspace(0, 1, self.analog_sampling_rate)
        under_sampling_step =int(np.ceil(self.analog_sampling_rate/self.adc.sampling_rate))
        
        digital_signal=self.adc.get_adc_val(analog_signal[1::under_sampling_step])
        t_digital=t_analog[1::under_sampling_step]
        
        return [t_analog, analog_signal,t_digital,digital_signal,self.adc]

a=Adc(4)
s=System(500,a)

x = np.linspace(0, 1, s.analog_sampling_rate)
x = np.abs(np.sin(4*np.pi*x)*np.exp(-5*x))*8
y = a.get_adc_val(x);
v=Visualize_adc();
v.plot(s.get_signal(x))    
