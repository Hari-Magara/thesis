import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
t1 = pd.read_csv('t1.csv')
t2 = pd.read_csv('t2.csv')
t3 = pd.read_csv('t3.csv')
t4 = pd.read_csv('t4.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t1['Time in Minutes'],t1['Average-Pb1'], label='T1-Pb1', color='red',  markevery=10, ms=4, marker='o')
plt.plot(t2['Time in Minutes'],t2['Average-Pb1'], linestyle='-.', label='T2-Pb1', color='red',  markevery=10, ms=4, marker='v')
plt.plot(t3['Time in Minutes'],t3['Average-Pb1'], linestyle='--', label='T3-Pb1', color='red',  markevery=10, ms=4, marker='s')
plt.plot(t4['Time in Minutes'],t4['Average-Pb1'], linestyle=':', label='T4-Pb1', color='red',  markevery=10, ms=4, marker='^')
plt.plot(t1['Time in Minutes'],t1['Average-Pb1-Pb2'], label='T1-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='d')
plt.plot(t2['Time in Minutes'],t2['Average-Pb1-Pb2'], linestyle='-.', label='T2-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='>')
plt.plot(t3['Time in Minutes'],t3['Average-Pb1-Pb2'], linestyle='--', label='T3-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='+')
plt.plot(t4['Time in Minutes'],t4['Average-Pb1-Pb2'], linestyle=':', label='T4-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='>')
plt.plot(t1['Time in Minutes'],t1['Average-Pb2'], label='T1-Pb2', color='C1',  markevery=10, ms=4, marker='1')
plt.plot(t2['Time in Minutes'],t2['Average-Pb2'], linestyle='-.', label='T2-Pb2', color='C1',  markevery=10, ms=4, marker='h')
plt.plot(t3['Time in Minutes'],t3['Average-Pb2'], linestyle='--', label='T3-Pb2', color='C1',  markevery=10, ms=4, marker='p')
plt.plot(t4['Time in Minutes'],t4['Average-Pb2'], linestyle=':', label='T4-Pb2', color='C1',  markevery=10, ms=4, marker='<')
plt.plot(t1['Time in Minutes'],t1['Average-Pb3'], label='T1-Pb3', color='C2',  markevery=10, ms=4, marker='P')
plt.plot(t2['Time in Minutes'],t2['Average-Pb3'], linestyle='-.', label='T2-Pb3', color='C2',  markevery=10, ms=4, marker='x')
plt.plot(t3['Time in Minutes'],t3['Average-Pb3'], linestyle='--', label='T3-Pb3', color='C2',  markevery=10, ms=4, marker='X')
plt.plot(t4['Time in Minutes'],t4['Average-Pb3'], linestyle=':', label='T4-Pb3', color='C2',  markevery=10, ms=4, marker='2')
plt.plot(t1['Time in Minutes'],t1['Average-Pb3-Pb4'], label='T1-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='*')
plt.plot(t2['Time in Minutes'],t2['Average-Pb3-Pb4'], linestyle='-.', label='T2-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='|')
plt.plot(t3['Time in Minutes'],t3['Average-Pb3-Pb4'], linestyle='--', label='T3-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker=4)
plt.plot(t4['Time in Minutes'],t4['Average-Pb3-Pb4'], linestyle=':', label='T3-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker=8)
plt.plot(t1['Time in Minutes'],t1['Average-Pb4'], label='T1-Pb4', color='C6',  markevery=10, ms=4, marker=5)
plt.plot(t2['Time in Minutes'],t2['Average-Pb4'], linestyle='-.', label='T2-Pb4', color='C6',  markevery=10, ms=4, marker='D')
plt.plot(t3['Time in Minutes'],t3['Average-Pb4'], linestyle='--', label='T3-Pb4', color='C6',  markevery=10, ms=4, marker='H')
plt.plot(t4['Time in Minutes'],t4['Average-Pb4'], linestyle=':', label='T4-Pb4', color='C6',  markevery=10, ms=4, marker='_')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.gcf()
plt.savefig('T1vsT2vsT3vsT4-Avg-Pb.pdf', bbox_inches='tight')
plt.show()


#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Fire-HF'], label='T1-Stud3-Fire-HF', color='red')
#plt.plot(t2['Time in Minutes'],t2['Stud3-Top-Fire-HF'], linestyle='--', label='T2-Stud3-Fire-HF', color='red')
#plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Fire-CF'], label='T1-Stud3-Fire-CF', color='C0')
#plt.plot(t2['Time in Minutes'],t2['Stud3-Top-Fire-CF'], linestyle='--', label='T2-Stud3-Fire-CF', color='C0')
#plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Amb-HF'], label='T1-Stud3-Amb-HF', color='C1')
#plt.plot(t2['Time in Minutes'],t2['Stud3-Top-Amb-HF'], linestyle='--', label='T2-Stud3-Amb-HF', color='C1')
#plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Amb-CF'], label='T1-Stud3-Amb-CF', color='C2')
#plt.plot(t2['Time in Minutes'],t2['Stud3-Top-Amb-CF'], linestyle='--', label='T2-Stud3-Amb-CF', color='C2')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T1vsT2-Studs.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t1['Time in Minutes'],t1['Stud3-Axial'], label='T1-Stud3-Axial', color='C0')
#plt.plot(t2['Time in Minutes'],t2['Stud3-Axial'], linestyle='--', label='T2-Stud3-Axial', color='C0')
#plt.plot(t1['Time in Minutes'],t1['Stud4-Axial'], label='T1-Stud4-Axial', color='C3')
#plt.plot(t2['Time in Minutes'],t2['Stud4-Axial'], linestyle='--', label='T2-Stud4-Axial', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Axial Displacement(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T1vsT2-Axial.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t1['Time in Minutes'],t1['Stud3-Axial'], label='T1-Stud3-Axial', color='C0')
#plt.plot(t2['Time in Minutes'],t2['Stud3-Axial'], linestyle='--', label='T2-Stud3-Axial', color='C0')
#plt.plot(t1['Time in Minutes'],t1['Stud5-Axial'], label='T1-Stud5-Axial', color='C3')
#plt.plot(t2['Time in Minutes'],t2['Stud5-Axial'], linestyle='--', label='T2-Stud5-Axial', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Axial Displacement(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T1vsT2-Axial2.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t1['Time in Minutes'],t1['Stud3-Mid'], label='T1-Stud3-Lateral', color='C0')
#plt.plot(t2['Time in Minutes'],t2['Stud3-Mid'], linestyle='--', label='T2-Stud3-Lateral', color='C0')
#plt.plot(t1['Time in Minutes'],t1['Stud4-Mid'], label='T1-Stud4-Lateral', color='C3')
#plt.plot(t2['Time in Minutes'],t2['Stud4-Mid'], linestyle='--', label='T2-Stud4-Lateral', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Lateral Deflection(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T1vsT2-Lateral.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t1['Time in Minutes'],t1['Load in kN'], label='T1-Load', color='C0')
#plt.plot(t2['Time in Minutes'],t2['Load in kN'], linestyle='--', label='T2-Load', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Applied Axial Load(kN)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T1vsT2-Load.pdf', bbox_inches='tight')
#plt.show()