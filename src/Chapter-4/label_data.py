import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import scipy.interpolate as interpolate
import scipy.signal as signal
from scipy.signal import argrelmax, argrelmin
import peakutils
import argparse


def analysis(filename):

	df = pd.read_csv( filename, sep="\t",header=None, index_col= False)
	M01 = np.array(df[1])
	M07 = np.array(df[7])
	n, filter_M01 = filter_signal(M01)
	m, filter_M07 = filter_signal_1(M07)
	a = np.empty(len(df[1]), dtype=object)
	l = [x+1 for x in n]
	k= [y+1 for y in m]
	a[l] = 'Stance'
	a[k] = 'Swing'
	df[11] = a
	f1 = plt.figure()
	f2 = plt.figure()
	ax1 = f1.add_subplot(111)
	ax1.plot(M01, '-gD', markevery=n,linewidth=1.5)
	ax1.set_xlabel('Time [ms]',fontsize=16)
	ax1.set_ylabel('Plantar Pressure',fontsize=16)
	ax1.grid(linestyle='--', linewidth=1.0)



	ax2 = f2.add_subplot(111)
	ax2.plot(M07, '-bD',markevery=m, linewidth=1.5)
	ax2.set_xlabel('Time [ms]',fontsize=16)
	ax2.set_ylabel('Plantar Pressure',fontsize=16)
	ax2.grid(linestyle='--', linewidth=1.0)
	plt.show()
	df.to_csv('output'+ filename, sep = "\t", header=False, index = False)







def filter_signal(data):

	N = 1
	Wn = [0.01 ,0.4]
	B,A = signal.butter(N,Wn,btype='band',output='ba')
	filter_signal = signal.filtfilt(B,A,data)
	ind_max = signal.argrelmax(filter_signal)
	ind_min = signal.argrelmin(filter_signal)

	l = []
	for i in range(int(len(ind_max[0][:]))):
		if (data[ind_max[0][i]] > 1.45):
			j = ind_max[0][i]
			l.append(j)

	n = []
	for i in range(len(l)):

		a = np.where(ind_min[0][:]<l[i])
		if (len(a[0][:]) > 0):
			if(data[ind_min[0][a[0][-1]]] < 1.2):
				n.append(ind_min[0][a[0][-1]])
		
		#
		# 	
	print ("Valleys Extracted :", len(n))

	return n, filter_signal

def filter_signal_1(data):

	N=1
	Wn = [0.01,0.4]
	B,A = signal.butter(N,Wn , btype='band',output='ba')
	filter_signal = signal.filtfilt(B,A,data)
	ind_max = signal.argrelmax(filter_signal)
	ind_min = signal.argrelmin(filter_signal)

	p = []

	for i in range(int(len(ind_max[0][:]))):
		if (data[ind_max[0][i]] > 1.4):

			j = ind_max[0][i]
			p.append(j)
	print("Peaks Extracted :",len(p))
	return p , filter_signal




if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Dataset dir')
	parser.add_argument('filename', type=str, default='', help = 'Name of the Dataset',)
	args = parser.parse_args()
	analysis(args.filename)

	