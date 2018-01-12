from ahkab import run, new_dc, new_tran, diode
from ahkab.circuit import Circuit
from ahkab.plotting import plot_results
from ahkab import circuit, printing, time_functions
import numpy as np
import pylab as plt


cir=Circuit("NEW CIRCUIT")
gnd = cir.get_ground_node()
def CircuitAnalysis(components,parameters):
	for i in components:
		if 'r' in i[0]:	
			if(i[2]=='0'):
				cir.add_resistor(i[0],gnd,i[3],i[1])
			elif(i[3]=='0'):
				cir.add_resistor(i[0],i[2],gnd,i[1])
			else:
				cir.add_resistor(i[0],i[2],i[3],i[1])
		elif 'c' in i[0]:
			if(i[2]=='0'):
				cir.add_capacitor(i[0],gnd,i[3],i[1])
			elif(i[3]=='0'):
				cir.add_capacitor(i[0],i[2],gnd,i[1])
			else:
				cir.add_capacitor(i[0],i[2],i[3],i[1])
		elif 'i' in i[0]:
			if(i[2]=='0'):
				cir.add_inductor(i[0],gnd,i[3],i[1])
			elif(i[3]=='0'):
				cir.add_inductor(i[0],i[2],gnd,i[1])
			else:
				cir.add_inductor(i[0],i[2],i[3],i[1])
		elif 'vdc' in i[0]:
			if(i[2]=='0'):
				cir.add_vsource(i[0],gnd,i[3],i[1])
			elif(i[3]=='0'):
				cir.add_vsource(i[0],i[2],gnd,i[1])
			else:
				cir.add_vsource(i[0],i[2],i[3],i[1])
		elif 'vac' in i[0]:
			mys = lambda t: 1 if not t else i[1]*math.sin(math.pi*i[4]/180 + 2*math.pi*i[5]*t) 
			if(i[2]=='0'):
				cir.add_vsource(i[0],gnd,i[3],1,function=mys)
			elif(i[3]=='0'):
				cir.add_vsource(i[0],gnd,i[3],1,function=mys)
			else:
				cir.add_vsource(i[0],gnd,i[3],1,function=mys)

	if parameters[1]=='V':
		node1=''
		node2=''
		for i in components:
			if parameters[0]==i[0]:
				node1=components[2]
				node2=components[3]
				if node1=='0':
					node1=gnd
				elif node2=='0':
					node2=gnd
				break
		tran_analysis=new_tran(0,100,10000,x0=None)
		r=run(cir,tran_analysis)
		fig = plt.figure() 
		plt.plot(r['tran']['T'], (r['tran']['V'+node1]-r['tran']['V'+node2]), label="Voltage across component")
		plt.legend()
		plt.plot()
		plt.grid(True)
		plt.ylabel('Voltage')
		plt.xlabel('Time [s]')
		fig.savefig('Volatge.png')

	elif parameters[1]=='I':
		node1=''
		node2=''
		r=0
		i=0
		c=0
		for i in components:
			if parameters[0]==i[0]:
				node1=components[2]
				node2=components[3]
				if node1=='0':
					node1=gnd
				elif node2=='0':
					node2=gnd
				if 'r' in parameters[0]:
					r=components[1]
				elif 'c' in parameters[0]:
					c=components[1]
				elif 'i' in parameters[0]:
					i=components[1]
				break
		tran_analysis=new_tran(0,100,10000,x0=None)
		r=run(cir,tran_analysis)
		fig = plt.figure() 
		plt.plot(r['tran']['T'], I(parameters[0]), label="Current across component")
		plt.legend()
		plt.plot()
		plt.grid(True)
		plt.ylabel('Current')
		plt.xlabel('Time [s]')
		fig.savefig('Current.png')

if __name__ == "__main__":
	components = []
	parameters = []
	with open('temp.txt') as f1:
		for line in f1:
			line = line.strip()
			components.append(line)
	with open('temp2.txt') as f2:
		for line in f2:
			parameters.append(line)
	CircuitAnalysis(components, parameters)