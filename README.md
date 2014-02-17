pi-radio
========

##A barebones Raspberry Pi internet radio

This is a Python script for what I think is the simplest functional internet radio you can make with a Raspberry Pi. 

You will need:

- A RaspberryPi with a fresh headless install of Raspbian – this means you set it not to boot into a graphical environment when it starts up.
- To install the Music Player Daemon and Client mpd & mpc and configure some online radio stations.
- A push button.
- A 10k and a 1k ohm resistor, and some way of wiring them together (such as a breadboard) and some way of connecting 3 wires to pins on the RaspberryPi.
- Headphones or some powered speakers.
- Optional: USB wifi dongle to make your radio, er, wireless.

First, log into your Pi at the command line. Ensure it’s connected to the internet and update it by typing
```
sudo apt-get update
```

Then install mpd (music player daemon) and mpc (client) by typing the following:
```
sudo apt-get install mpc mpd
```

Add some internet radio stations by typing this at the command line to add BBC Radio 1:
```
mpc add http://bbcmedia.ic.llnwd.net/stream/bbcmedia_intl_lc_radio1_p?s=1365376033&e=1365390433&h=a0fef58c2149248d6bff1f7b7b438931
```

There are more stations BBC listed here: http://thenated0g.wordpress.com/2013/06/06/raspberry-pi-add-bbc1-6-radio-streams-and-mpc-play-command/

I added BBC radios 1-6, and also added US public radio NWPR and the French station Fip, leaving me with 8 stations in total. Here’s how I added Fip (it’s a super-cool French music station):
```
mpc add http://mp3.live.tv-radio.com/fip/all/fip-32k.mp3
```

And for NPR try:
```
mpc add http://69.166.45.47:8000
```

Do try and add the stations in the order you want them to cycle through – you can re-order them using mpc at the command line, but it’s much easier to get them right first time. (I didn’t).

Test mpc is working by typing
```
mpc play 1
```
at the command line, and you should hear Radio 1 (or whichever station you added first) coming out of the Pi’s headphone jack. You can adjust the volume of your sound device by typing
```
alsamixer
```
at the command line. You get a graphical mixer in the command line which is pretty intuitive.

You can also adjust volume in mpc by typing:
```
mpc volume +5
```
or + or – any number you fancy.

Then type
```
mpc stop
```
to make the horrible noise go away.

<a href="http://www.flickr.com/photos/gilesbooth/12596494545/" title="Pi-Radio schematic by gilesbooth, on Flickr"><img src="http://farm4.staticflickr.com/3750/12596494545_93777dbea0.jpg" width="500" height="329" alt="Pi-Radio schematic"></a>

Using a little breadboard, connect one side of your push button to the 3.3v pin on the RaspberryPi. The other side of the switch is connected via a 1K resistor to RaspberryPi GPIO pin 23, and via a 10K resistor to a GND pin on the Pi. You can find a good diagram of the pins here: http://elinux.org/RPi_Low-level_peripherals

Now save **radio.py** in the home directory /home/pi. The script assumes you have 8 stations set up – if you have a different number, change the 8 to your number of radio stations.

Then test it by typing
```
sudo python radio.py
```
at the command line. The radio should play, and when you press the button it should change up through the channels, cycling back to 1 when it passes 8.

Next, to make it run automatically at start up, type
```
sudo nano /etc/rc.local
```
and add the following line before the exit command:
```
(sleep 65; python /home/pi/radio.py)&
```
The 'sleep 65' is needed because my Pi has a USB wifi dongle which takes an eternity (well, a minute) to get on the network. If your Pi is connected to the internet by ethernet, you could probably make the sleep time an awful lot shorter.
Save it by typing ctrl-x. Reboot your Pi, and **enjoy**!



