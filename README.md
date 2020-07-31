<img src="https://www.newpaltz.edu/media/identity/logos/newpaltzlogo.jpg" width="280" height="87">


**Spring 2020 Embedded Linux Class. -- Final**
---------------------------------------------------------------------------

This repository documents my class work and projects done for **CPS342**

This branch contains the content for the CPS 342 Final.

Here I am aiming to create a live gauge of various data from my car using the **obd** Python library and a bluetooth obdII scanner. Further plans include a website that will log important data such as speeding, trouble codes, overheating, and so on. The current issue with that is I do not have the means of having internet connection in my car as of right now. 

Current status of the project is I am able to have the gauges work separately, but still am working on the means of having them all work together on the same page.

**Materials**

1\. **ELM327 OBDII Scanner**
  
  Please be mindful that this is infact an OBDII scanner with the ELM327 microcontroller, other OBDII scanners may not work. Does not have to necessarily be Bluetooth but it does make things a bit cleaner.
  
2\. **Raspberry Pi 3B / 4**
  
  You can get away with older, but in my case I am using the 4 and the built in Bluetooth makes things easier. I am also using the raspbian desktop environment as opposed to the console for this project as it makes it a bit easier to work with the gui. 
  
3\. **A screen for the Pi**

<img src="https://www.miuzeipro.com/wp-content/uploads/2019/01/MC21-35-1-600x600.jpg" width="300" height="300">

I am using a 4inch LCD Touchscreen from Miuzel for this project. Having a small screen with touch function makes things easier to debug and work with but not necessary.
  
4\. **12 volt power converter** so you can run the pi from the car
  
<br />
<br />

**Setup Steps**

1\. Download python and the needed libraries. 
	sudo apt install python3-pip
	sudo pip3 install obd
	sudo pip3 install guizero

2\. Plugin and download the drivers for the touch screen.
	The Miuzel case I use isn't the niecst looking but is relatively straight forward to build and comes with a nice little plug to go from the mini hdmi of the Pi to the hdmi port of the screen. The steps to download the drivers is as follows,
	
	1. git clone https://github.com/waveshare/LCD-show.git 
	
	2. cd /LCD-show
	
	3. ./LCD4-800x480-show
	
	4. From here your pi should appear on the small screen with touchscreen functionality. The touchscreen however only works with the Raspbian desktop.


3\. Download bluetooth in console
	I have found that the bluetooth on the taskbar in the standard raspberry pi desktop does not allow you to full connect as you need to trust the device. It is less of a headache to do it in the console.
	
	1. bluetoothctl
	
	2. power on
	
	3. agent on
	
	4. scan on
	From here you should be able to pick the obd2 scanner out from the crowd as it usually has OBD in the name
	
	5. Using the MAC address you just found run 'pair xx-xx-xx-xx-xx-xx' and then 'trust xx-xx-xx-xx-xx-xx'
	
	6. And finally outside of the bluetooth command line run 'sudo rfcomm bind rfcomm0 xx-xx-xx-xx-xx-xx' 
		This should have your obd2 bluetooth adapter ready to go
4\. I have the obd package's debug running in the program so if you do have trouble connecting this will give you some error messages that will give you some insight into why.

5\. Download this repository to the pi, using 'git clone https://github.com/RichterBeau/obd2App.git' command in a folder of your choosing. 

6\. And finally run the program using 'python obd.py' 
		
	
<br />
<br />

&nbsp; 1\. **Personal Information**:
	   
&nbsp; &nbsp; &nbsp; Name: *Beau Richter*

&nbsp; &nbsp; &nbsp; Major: *Computer Science*
	
&nbsp; &nbsp; &nbsp; ID: [*N03743050*](https://github.com/RichterBeau/EL2020)
	
&nbsp; &nbsp; &nbsp; Year: *Senior*
	
&nbsp; 2\. **Class Start Date**: Jan 21, 2020 
	
&nbsp; 3\. **Class End Date**: May 15, 2020
