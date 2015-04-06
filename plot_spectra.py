# Collects all the BC03 spectra, and plots them according to a specified redshift.

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import *


dict={"0":"data/tau01_age01.spec",
      "1":"data/tau01_age03.spec",
      "2":"data/tau01_age07.spec",
      "3":"data/tau01_age11.spec",
      "4":"data/tau01_age20.spec",
      "5":"data/tau01_age30.spec",
      "6":"data/tau03_age01.spec",
      "7":"data/tau03_age03.spec",
      "8":"data/tau03_age07.spec",
      "9":"data/tau03_age11.spec",
      "10":"data/tau03_age20.spec",
      "11":"data/tau03_age30.spec",
      "12":"data/tau1_age01.spec",
      "13":"data/tau1_age03.spec",
      "14":"data/tau1_age07.spec",
      "15":"data/tau1_age11.spec",
      "16":"data/tau1_age20.spec",
      "17":"data/tau1_age30.spec"}
dict_col={"0":'r-',
          "1":'y-',
          "2":'g-',
          "3":'c-',
          "4":'b-',
          "5":'m-'}
dict_age={"0":"age=0.1Gyr",
          "1":"age=0.3Gyr",
          "2":"age=0.7Gyr",
          "3":"age=1.1Gyr",
          "4":"age=2.0Gyr",
          "5":"age=3.0Gyr"}
tick_list=[100,300,600,1000,3000,6000,10000,30000,60000,100000,200000,300000]
grid_list=[i for i in range(100,1000,100)]+[i for i in range(1000,10000,1000)]+[i for i in range(10000,100000,10000)]+[100000,200000,300000]
tick_label=[str(i) for i in tick_list]


#Input redshift and Lyman/Balmer break options
while True:
    try:
        z=raw_input("Please enter redshift: ")
        z=float(z)
        if z<0:
            print "*** ERROR: Redshift must be non-negative. ***"
        if z>25:
            print "*** ERROR: Redshift is too large. ***"
        else:
            break
    except ValueError:
        print "*** ERROR: Input is not a number. ***"
while True:
    swt=raw_input("Show Lyman break and Balmer break? (y/N) ")
    if swt=='y' or swt=='Y' or swt=="\'y\'" or swt=="\"y\"" or swt=="\'Y\'" or swt=="\"Y\"" or swt=="yes" or swt=="Yes" or swt=="YES":
        swt=1
    else:
        swt=0
    break


spec_sto=[]
for j in range(18):
    #Read spectra
    fil=open(dict[str(j)],"r")
    dat=[]
    for lin in fil:
        dat.append(filter(None,lin.strip().split(' ')))
    fil.close()
    spec=[]
    record=False
    prev=0.
    for i in dat:
        if record:
            if float(i[0])-prev<0.:
                break
            spec.append(i)
            prev=float(i[0])
        if i[0]=='8.00000':
            record=True
        if i[0][0:3]=='0.2':
            record=True
            spec.append(i)
            prev=float(i[0])
    spec_sto.append(spec)


#Read filter.in
try:
    fil=open("filter.in","r")
    filt=[]
    for lin in fil:
        if lin[0]=='#':
            continue
        lin_raw=filter(None,lin.strip().split(' '))
        filt.append(lin_raw)
        if len(lin_raw)<3:
            sys.exit("*** ERROR: Cannot read filter.in, please check for mistakes. ***")
    fil.close()
except:
    sys.exit("*** ERROR: Cannot open filter.in ***")


#Prepare canvas
f,(ax1,ax2,ax3)=plt.subplots(1,3,sharex=True,sharey=True)
ax1.semilogx()
ax2.semilogx()
ax3.semilogx()

tit="z="+str(z)+", no extinction"
plt.suptitle(tit,size=20)
ax1.set_title("tau=0.1Gyr",size=20)
ax2.set_title("tau=0.3Gyr",size=20)
ax3.set_title("tau=1.0Gyr",size=20)
ax1.set_xlabel("Wavelength (Angstroms)",size=20)
ax2.set_xlabel("Wavelength (Angstroms)",size=20)
ax3.set_xlabel("Wavelength (Angstroms)",size=20)
ax1.set_ylabel("Magnitude (AB)",size=20)

#Set x-axes
ax1.xaxis.set_major_locator(FixedLocator(tick_list))
ax1.xaxis.set_minor_locator(FixedLocator(grid_list))
for tic in ax1.xaxis.get_minor_ticks():
    tic.tick1On = tic.tick2On = False
ax1.xaxis.set_tick_params(width=3)
ax1.xaxis.set_major_formatter(FixedFormatter(tick_label))
plt.setp(ax1.get_xticklabels(),rotation=-30,ha='left')
ax1.xaxis.grid(b=True,which='minor',linestyle='-',alpha=0.2)

ax2.xaxis.set_major_locator(FixedLocator(tick_list))
ax2.xaxis.set_minor_locator(FixedLocator(grid_list))
for tic in ax2.xaxis.get_minor_ticks():
    tic.tick1On = tic.tick2On = False
ax2.xaxis.set_tick_params(width=3)
ax2.xaxis.set_major_formatter(FixedFormatter(tick_label))
plt.setp(ax2.get_xticklabels(),rotation=-30,ha='left')
ax2.xaxis.grid(b=True,which='minor',linestyle='-',alpha=0.2)

ax3.xaxis.set_major_locator(FixedLocator(tick_list))
ax3.xaxis.set_minor_locator(FixedLocator(grid_list))
for tic in ax3.xaxis.get_minor_ticks():
    tic.tick1On = tic.tick2On = False
ax3.xaxis.set_tick_params(width=3)
ax3.xaxis.set_major_formatter(FixedFormatter(tick_label))
plt.setp(ax3.get_xticklabels(),rotation=-30,ha='left')
ax3.xaxis.grid(b=True,which='minor',linestyle='-',alpha=0.2)

#Set y-axis
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
ax1.yaxis.set_tick_params(width=2)
ax1.yaxis.grid(b=True,which='major',linestyle='-',alpha=0.2)
ax2.yaxis.set_tick_params(width=2)
ax2.yaxis.grid(b=True,which='major',linestyle='-',alpha=0.2)
ax3.yaxis.set_tick_params(width=2)
ax3.yaxis.grid(b=True,which='major',linestyle='-',alpha=0.2)


#Plot filters
try:
    for i in filt:
        x=(float(i[1])+float(i[2]))/2
        xerr=(float(i[1])-float(i[2]))/2
        y=float(i[3])
        ax1.errorbar(x,y,xerr=xerr,fmt='k-',linewidth=2.0,capsize=4,capthick=1.5,zorder=32)
        ax1.annotate(i[0],xy=(x,y),xytext=(0,5),textcoords='offset points',ha='center',va='bottom',zorder=32)
        ax2.errorbar(x,y,xerr=xerr,fmt='k-',linewidth=2.0,capsize=4,capthick=1.5,zorder=32)
        ax2.annotate(i[0],xy=(x,y),xytext=(0,5),textcoords='offset points',ha='center',va='bottom',zorder=32)
        ax3.errorbar(x,y,xerr=xerr,fmt='k-',linewidth=2.0,capsize=4,capthick=1.5,zorder=32)
        ax3.annotate(i[0],xy=(x,y),xytext=(0,5),textcoords='offset points',ha='center',va='bottom',zorder=32)
except:
    sys.exit("*** ERROR: Cannot read filter.in, please check for mistakes. ***")


for i in filt:
    if float(i[1])>float(i[2]):
        sys.exit("*** ERROR: freq_min larger than freq_max in "+i[0]+" band ***")
    if float(i[1])<300:
        sys.exit("*** ERROR: freq_min too small in "+i[0]+" band ***")
    if float(i[2])>1000000:
        sys.exit("*** ERROR: freq_max too large in "+i[0]+" band ***")


#Set reference filter
mag_adj=[0 for i in range(18)]
freq_low=0
for i in filt:
    swt=i[-1]
    if swt=='y' or swt=='Y' or swt=="\'y\'" or swt=="\"y\"" or swt=="\'Y\'" or swt=="\"Y\"" or swt=="yes" or swt=="Yes" or swt=="YES":
        freq_low=float(i[1])
        freq_high=float(i[2])
        sensitivity=float(i[3])
        break
if (freq_high-freq_low<500):
    sys.exit("*** ERROR: Reference bandpass must be at least 500A wide. ***")
if (freq_high<100*(1+z)):
    sys.exit("*** ERROR: Wavelength of the reference filter is too short. ***")
if freq_low:
    for j in range(18):
        xs=[]
        ys=[]
        for i in spec_sto[j]:
            if float(i[0])/3*(1+z)>freq_high:
                break
            if float(i[0])/3*(1+z)>freq_low:
                xs.append(float(i[0])/3*(1+z))
                ys.append(10.**(-2./5*float(i[1])))
        #ys_div=[y/x for y,x in zip(ys,xs)]
        #xs_div=[1./x for x in xs]
        #mag_ref=-5./2*np.log10(np.trapz(ys_div,xs)/mp.trapz(xs_div,xs))
        mag_ref=-5./2*np.log10(np.trapz([y/x for y,x in zip(ys,xs)],xs)/np.trapz([1./x for x in xs],xs))
        mag_adj[j]=float(sensitivity-mag_ref)
    ax1.add_patch(Rectangle(xy=(freq_low,sensitivity-0.4),width=freq_high-freq_low,height=0.6,color='w',alpha=0.6,zorder=30))
    ax2.add_patch(Rectangle(xy=(freq_low,sensitivity-0.4),width=freq_high-freq_low,height=0.6,color='w',alpha=0.6,zorder=30))
    ax3.add_patch(Rectangle(xy=(freq_low,sensitivity-0.4),width=freq_high-freq_low,height=0.6,color='w',alpha=0.6,zorder=30))

#Plot spectra
xs=[]
ys=[]
for j in range(0,6):
    xs=[]
    ys=[]
    for i in spec_sto[j]:
        i[0]=float(i[0])
        i[1]=float(i[1])
        xs.append(i[0]/3*(1+z))
        ys.append(i[1]+mag_adj[j])
    ax1.plot(xs,ys,dict_col[str(j%6)],linewidth=2.0,label=dict_age[str(j%6)])
l1=ax1.legend(bbox_to_anchor=(1.03,0.28))
l1.get_frame().set_linewidth(0.0)
l1.get_frame().set_alpha(0.4)
l1.set_zorder(36)
for j in range(6,12):
    xs=[]
    ys=[]
    for i in spec_sto[j]:
        i[0]=float(i[0])
        i[1]=float(i[1])
        xs.append(i[0]/3*(1+z))
        ys.append(i[1]+mag_adj[j])
    ax2.plot(xs,ys,dict_col[str(j%6)],linewidth=2.0,label=dict_age[str(j%6)])
l2=ax2.legend(bbox_to_anchor=(1.03,0.28))
l2.get_frame().set_linewidth(0.0)
l2.get_frame().set_alpha(0.4)
l2.set_zorder(36)
for j in range(12,18):
    xs=[]
    ys=[]
    for i in spec_sto[j]:
        i[0]=float(i[0])
        i[1]=float(i[1])
        xs.append(i[0]/3*(1+z))
        ys.append(i[1]+mag_adj[j])
    ax3.plot(xs,ys,dict_col[str(j%6)],linewidth=2.0,label=dict_age[str(j%6)])
l3=ax3.legend(bbox_to_anchor=(1.03,0.28))
l3.get_frame().set_linewidth(0.0)
l3.get_frame().set_alpha(0.4)
l3.set_zorder(36)


#Set axes range
xmin=600*(1+z)
xmax=15000*(1+z)
if freq_low:
    if freq_high > xmax:
        xmax=freq_high*1.2
    if freq_low < xmin:
        xmin=freq_low/1.2
plt.xlim(xmin,xmax)
ymin=spec_sto[5][0][1]
for i in range(len(spec_sto[5])):
    if spec_sto[5][i][1]<ymin:
        ymin=spec_sto[5][i][1]
ymin=ymin+mag_adj[5]-1
ymax=ymin+14.5
if freq_low:
    if sensitivity > ymax:
        ymax=sensitivity+1
plt.ylim(ymax,ymin)


#Plot Lyman/Balmer break
if (swt):
    ax1.plot([912*(1+z),912*(1+z)],[-100,100],'k--',linewidth=1)
    ax1.plot([1216*(1+z),1216*(1+z)],[-100,100],'k--',linewidth=1)
    ax1.plot([3646*(1+z),3646*(1+z)],[-100,100],'k--',linewidth=1)
    ax1.annotate("Lyman\nlimit",xy=(912*(1+z),ymin+1),xytext=(-1,0),textcoords='offset points',ha='right',va='top')
    ax1.annotate("Lyman\nalpha",xy=(1216*(1+z),ymin+1),xytext=(4,0),textcoords='offset points',va='top')
    ax1.annotate("Balmer",xy=(3646*(1+z),ymin+1),xytext=(4,0),textcoords='offset points',va='top')
    ax2.plot([912*(1+z),912*(1+z)],[-100,100],'k--',linewidth=1)
    ax2.plot([1216*(1+z),1216*(1+z)],[-100,100],'k--',linewidth=1)
    ax2.plot([3646*(1+z),3646*(1+z)],[-100,100],'k--',linewidth=1)
    ax2.annotate("Lyman\nlimit",xy=(912*(1+z),ymin+1),xytext=(-1,0),textcoords='offset points',ha='right',va='top')
    ax2.annotate("Lyman\nalpha",xy=(1216*(1+z),ymin+1),xytext=(4,0),textcoords='offset points',va='top')
    ax2.annotate("Balmer",xy=(3646*(1+z),ymin+1),xytext=(4,0),textcoords='offset points',va='top')
    ax3.plot([912*(1+z),912*(1+z)],[-100,100],'k--',linewidth=1)
    ax3.plot([1216*(1+z),1216*(1+z)],[-100,100],'k--',linewidth=1)
    ax3.plot([3646*(1+z),3646*(1+z)],[-100,100],'k--',linewidth=1)
    ax3.annotate("Lyman\nlimit",xy=(912*(1+z),ymin+1),xytext=(-1,0),textcoords='offset points',ha='right',va='top')
    ax3.annotate("Lyman\nalpha",xy=(1216*(1+z),ymin+1),xytext=(4,0),textcoords='offset points',va='top')
    ax3.annotate("Balmer",xy=(3646*(1+z),ymin+1),xytext=(4,0),textcoords='offset points',va='top')


#Show
plt.show()