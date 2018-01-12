from javax.swing import *
from java.awt import BorderLayout
from java.awt import *
import java.awt.event.ActionListener   
import java.awt.event.ActionEvent 	
import java.lang.Runtime
import os
import subprocess


frame = JFrame("Electripy-Circuit Solver and Simulator")
btnPnl = JPanel(FlowLayout(FlowLayout.CENTER))
components = []
temp_res = {}
pane=JPanel()
rcount=0
icount=0
ccount=0
vaccount=0
vdccount=0
parameters=[]

#components consists of all components in circuit where each each element is an array [component addded(resistor/capacitor),magnitude,node1,node2,frequency,phase]
class Example:

    def add_res(self,event):
    	pane.removeAll()
    	self.disp1=JLabel("Enter Value of Resistance")
    	self.val1 = JTextField(15)
    	self.node1 = JLabel("Enter node 1")
    	self.val2=JTextField(15)
    	self.node2=JLabel("Enter node 2")
    	self.val3= JTextField(15)
    	self.submit=JButton('Submit',actionPerformed=self.removing)
    	self.comp='r'
    	self.freq=0
    	self.phase=0
    	pane.add(self.disp1)
    	pane.add(self.val1)
    	pane.add(self.node1)
    	pane.add(self.val2)
    	pane.add(self.node2)
    	pane.add(self.val3)
    	pane.add(self.submit)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.add(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)


    def add_capac(self,event):
    	pane.removeAll()
    	self.disp1=JLabel("Enter value of Capacitance")
    	self.val1 = JTextField(15)
    	self.node1 = JLabel("Enter node 1")
    	self.val2=JTextField(15)
    	self.node2=JLabel("Enter node 2")
    	self.val3= JTextField(15)
    	self.submit=JButton('Submit',actionPerformed=self.removing)
    	self.comp='c'
    	self.freq=0
    	self.phase=0
    	pane.add(self.disp1)
    	pane.add(self.val1)
    	pane.add(self.node1)
    	pane.add(self.val2)
    	pane.add(self.node2)
    	pane.add(self.val3)
    	pane.add(self.submit)
    	frame.add(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)


    def add_ind(self,event):
    	pane.removeAll()
    	self.disp1=JLabel("Enter value of inductor")
    	self.val1=JTextField(15)
    	self.node1=JLabel("Enter node 1")
    	self.val2=JTextField(15)
    	self.node2=JLabel("Enter node 2")
    	self.val3=JTextField(15)
    	self.submit=JButton('Submit',actionPerformed=self.removing)
    	self.comp='i'
    	self.freq=0
    	self.phase=0
    	pane.add(self.disp1)	
    	pane.add(self.val1)
    	pane.add(self.node1)
    	pane.add(self.val2)
    	pane.add(self.node2)
    	pane.add(self.val3)
    	pane.add(self.submit)
    	frame.add(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)

    def v_dc(self,event):
    	pane.removeAll()
    	self.disp1=JLabel("Enter Magnitude of DC Voltage")
    	self.val1=JTextField(15)
    	self.node1=JLabel("Enter node 1")
    	self.val2=JTextField(15)
    	self.node2=JLabel("Enter node 2")
    	self.val3=JTextField(15)
    	self.submit=JButton('Submit',actionPerformed=self.removing)
    	self.comp='vdc'
    	self.freq=0
    	self.phase=0
    	pane.add(self.disp1)	
    	pane.add(self.val1)
    	pane.add(self.node1)
    	pane.add(self.val2)
    	pane.add(self.node2)
    	pane.add(self.val3)
    	pane.add(self.submit)
    	frame.add(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)

    def v_ac(self,event):
    	pane.removeAll()
    	self.disp1=JLabel("Enter Magnitude of AC Voltage")
    	self.val1=JTextField(15)
    	self.node1=JLabel("Enter node 1")
    	self.val2=JTextField(15)
    	self.node2=JLabel("Enter node 2")
    	self.val3=JTextField(15)
    	self.frequency=JLabel("Enter Frequency")
    	self.a=JTextField(15)
    	self.theta1=JLabel("Enter Phase Value")
    	self.b=JTextField(15)
    	self.submit=JButton('Submit',actionPerformed=self.removing)
    	self.comp='vac'
    	pane.add(self.disp1)	
    	pane.add(self.val1)
    	pane.add(self.node1)
    	pane.add(self.val2)
    	pane.add(self.node2)
    	pane.add(self.val3)
    	pane.add(self.frequency)
    	pane.add(self.a)
    	pane.add(self.theta1)
    	pane.add(self.b)
    	pane.add(self.submit)
    	frame.add(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)


    def __init__(self):
    	frame.setExtendedState(JFrame.MAXIMIZED_BOTH)
        frame.setLayout(BorderLayout())
        res = JButton('resisitor',actionPerformed=self.add_res)
        capac = JButton('capacitor',actionPerformed=self.add_capac)
        button = JButton('Analysis',actionPerformed=self.circuitanalysis)
        ind = JButton('inductor',actionPerformed=self.add_ind)
        source1 = JButton('DC source',actionPerformed=self.v_dc)
        source2 = JButton('AC source',actionPerformed=self.v_ac)
        #drawing=JButton("Show Circuit")

        btnPnl.add(source1);
        btnPnl.add(source2);	
        btnPnl.add(res);
        btnPnl.add(capac);
        btnPnl.add(ind);
        #btnPnl.add(drawing)
        btnPnl.add(button)
        frame.add(btnPnl, BorderLayout.SOUTH);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        frame.setVisible(True)
        self.rcount=0
        self.icount=0
        self.ccount=0
        self.vaccount=0
        self.vdccount=0


    def circuitanalysis(self,event):
    	pane.removeAll()
    	self.disp1=JLabel("Enter component ")
    	self.val=JTextField(15)
    	self.disp2=JLabel("Parameter")
    	self.val2=JTextField(15)
    	self.submit=JButton("Submit",actionPerformed=self.Submit1)
    	pane.add(self.disp1)
    	pane.add(self.val)
    	pane.add(self.disp2)
    	pane.add(self.val2)
    	pane.add(self.submit)
    	frame.add(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)

    def Submit1(self,event):
    	parameters.append(str(self.val.getText()))
    	parameters.append(str(self.val2.getText()))
    	print(parameters)
    	pane.removeAll()
    	frame.remove(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)
        newfile = open('temp.txt', 'w')
        newfile2 = open('temp2.txt', 'w')
        for item in components:
            newfile.write("%s\n" % item)
        for item in parameters:
            newfile2.write("%s\n" % item)
        newfile.close()
        newfile2.close() 
    	subprocess.Popen("bash m.sh",shell=True)
    	
    def removing(self,event):
    	if self.comp=='vac':
    		self.vaccount +=1
    		r=['V' + str(self.comp + str(self.vaccount)),float(self.val1.getText()),str(self.val2.getText()),str(self.val3.getText()),float(self.a.getText()),float(self.b.getText())]
    	elif self.comp=='vdc':
    		self.vdccount +=1
    		r=['V' + str(self.comp + str(self.vdccount)),float(self.val1.getText()),str(self.val2.getText()),str(self.val3.getText()),self.freq,self.phase]
    	elif self.comp=='r' :
    		self.rcount +=1
    		r=[str(self.comp + str(self.rcount)),float(self.val1.getText()),str(self.val2.getText()),str(self.val3.getText()),self.freq,self.phase]
    	elif self.comp=='c':
    		self.ccount +=1
    		r=[str(self.comp + str(self.ccount)),float(self.val1.getText()),str(self.val2.getText()),str(self.val3.getText()),self.freq,self.phase]
    	elif self.comp=='i' :
    		self.icount +=1
    		r=[str(self.comp + str(self.icount)),float(self.val1.getText()),str(self.val2.getText()),str(self.val3.getText()),self.freq,self.phase]
    	components.append(r)
    	pane.removeAll()
    	frame.remove(pane)
    	SwingUtilities.updateComponentTreeUI(frame)
    	frame.setVisible(True)


   
if __name__ == '__main__':
    Example()
