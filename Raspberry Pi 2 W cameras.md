# Raspberry Pi 2 W cameras

[![pi_hardware](https://user-images.githubusercontent.com/110564012/236584678-bbba299f-493c-4603-8ee0-4370afe01251.png)](https://user-images.githubusercontent.com/110564012/236584678-bbba299f-493c-4603-8ee0-4370afe01251.png)
### Cameras:
Note: If the camera is inside a window do not use the night IR camera, it will reflect off the window. I've had one outside in a non watertight 3d case for months and has been fine so far.

Arducam 1080P Day & Night Vision USB Camera: https://www.amazon.com/Arducam-Computer-Automatic-Switching-All-Day/dp/B0829HZ3Q7
Arducam 5MP Wide Angle USB Camera: https://www.amazon.com/Arducam-Camera-Computer-Without-Microphone/dp/B0972KK7BC

### Software:
MotionEye is a linux distro for single board computers (ie. the Raspberry Pi) to create a simple video surveillence network. More cameras can be added to the MotionEye interface if desired, just repeat this setup then add them all as network cameras to one of the web interfaces to act as a central server.

### Step 1: Get the image file
I'm using a branched version of MotionEye made specifically for the Pi Zero 2W board. download the MotionEye ISO file for the Pi Zero 2 W: [https://github.com/jawsper/motioneyeos/releases/tag/20220119-dev](https://github.com/jawsper/motioneyeos/releases/tag/20220119-dev)

### Step 2 write the image to SD card
Write the ISO file to your microSD card. I used a program called Win32DiskImager which can be downloaded here: [https://sourceforge.net/projects/win32diskimager/](https://sourceforge.net/projects/win32diskimager/) Once you have finished installing Win32DiskImager, launch it and insert the microSD card into your computer.

[![image](https://user-images.githubusercontent.com/110564012/235790174-e06137ae-43d0-4eb0-b190-9765d28c2335.png)](https://user-images.githubusercontent.com/110564012/235790174-e06137ae-43d0-4eb0-b190-9765d28c2335.png)

### Step 3: Configure Wifi settings
Before ejecting the card there is one more step we need to take care of so that we will have wifi connectivity after initialization has been complete on our raspberry pi.

Navigate to the SD card's directory and create a new text file named "wpa_supplicant.conf" and edit it with notepad++. Set up the configuration file like the example below and place your wifi SSID and password in the appropriate lines of the file, then change the line endings to linux with the following options in the top menu _Edit>EOL Conversion>Unix (LF)_. 

#### IMPORTANT NOTE: 
this must be done after imaging the SD card but before MotionEye has been initialized on the raspberry pi.

[![image](https://user-images.githubusercontent.com/110564012/235792381-70a690d5-7b17-4f43-91e8-e47846494abe.png)](https://user-images.githubusercontent.com/110564012/235792381-70a690d5-7b17-4f43-91e8-e47846494abe.png)
Save the wpa_supplicant.conf file and eject the SD card.

### Step 4 initialize MotionEye
Insert the SD card in your Pi Zero 2W and attach the power supply. This has been set up for a headless installation but I included a screenshot of the video output anyway because there are multiple ways to proceed with the initial configuration. When first powering on the Pi it will need a few moments to install. Once complete access the device by navigating to the MotionEye web portal hosted by the device. The address can be found on the initialization prompt displayed by the raspberry pi (http[:]//meye-4af22670 in the example below). Alternatively, if you are performing a completely headless you can find the IP address of your device in your router's administration page, or in your DHCP reservations.

[![image](https://user-images.githubusercontent.com/110564012/235792492-9c87b22b-df60-4e49-bf6f-58b954f0dfca.png)](https://user-images.githubusercontent.com/110564012/235792492-9c87b22b-df60-4e49-bf6f-58b954f0dfca.png)

### Step 5: Accessing the MotionEye web portal
When first logging into the MotionEye webpage use the default credentials. The username is admin, leave the password blank. Click the menu icon in the top right and under general settings change the usernames and passwords. Might also want to add a standard user account if you're going to give other people access, and change the port. If you want to give it a static IP go make a reservation by MAC first, then change the address in the Motioneye portal, then reboot.

[![image](https://user-images.githubusercontent.com/110564012/235792568-f27d5af6-a159-44c1-911f-63c298fb34c9.png)](https://user-images.githubusercontent.com/110564012/235792568-f27d5af6-a159-44c1-911f-63c298fb34c9.png)

### Step 6: Configuring a camera
Log back into the web portal with the new admin username and password that you changed in the previous step. Click the link on the home page "You have not configured any camera yet. Click here to add one…" If you don't see your camera you might need to power off the PI, plug the camera in first, then power on the PI. Your camera options may not be the same as this example depending on which one you're using.

[![image](https://user-images.githubusercontent.com/110564012/235792640-9c050ab1-4e53-46e3-8172-5fdedaeb2182.png)](https://user-images.githubusercontent.com/110564012/235792640-9c050ab1-4e53-46e3-8172-5fdedaeb2182.png)

After clicking okay the camera will be available in the menu under Video Device and will be visible on the home page. Now that your camera is configured many more menus become available.

### Step 7: Printed parts
I have these files if you have a printer and want to make them yourself.

I've been using this case for the PI
https://www.thingiverse.com/thing:1595429
[![image](https://user-images.githubusercontent.com/110564012/236585341-1eb222af-aba4-4b00-bc6e-d2cfa7bb68f9.png)](https://user-images.githubusercontent.com/110564012/236585341-1eb222af-aba4-4b00-bc6e-d2cfa7bb68f9.png)

And this case for the camera. The 5MP day camera doesnt quite fit, I'm working on a redesign.
[![image](https://user-images.githubusercontent.com/110564012/236586575-7bc67fa9-2325-449b-9123-7895821f928e.png)](https://user-images.githubusercontent.com/110564012/236586575-7bc67fa9-2325-449b-9123-7895821f928e.png)
