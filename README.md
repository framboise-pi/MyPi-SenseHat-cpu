# MyPi-SenseHat-cpu
Display CPU usage on Pi Sense Hat, with a nice dot line


# How ?
Using psutil to get cpu usage in percent,
each second, it will display a dot base on the usage percent.
From line 0 to 7, where 0 is the upper line and equal to 100% cpu usage;
and 7 the bottom line for <12.5% of cpu usage

# Anything special ?
As psutil wasn't returning a value each second request,
it was displaying dots and often a space between dots, 'caused by a null value.
I just had to code : "display a dot only if you have a value, so wait for it". Which is logical.
Resulting in a complete dot line with no space. Wonderful.

# Pictures
