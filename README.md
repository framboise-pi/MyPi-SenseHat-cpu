# MyPi-SenseHat-cpu
Display CPU usage on Pi Sense Hat, with a nice dot line


# How ?
Using psutil to get cpu usage in percent,
each second, it will display a dot base on the usage percent.
## Lines
From line 0 to 7, where 0 is the upper line and equal to 100% cpu usage;
and 7 the bottom line for <12.5% of cpu usage
## Columns
Logically, one column equal one second (see "Anything special" below)
## Brightness
The brightness of the LED follows the percent value.
So 100% cpu usage will be on the top line and at max bright,
and low usage will be on bottom with low light.

# Anything special ?
As psutil wasn't returning a value each second request,
it was displaying dots and often a space between dots, 'caused by a null value.
I just had to code : "display a dot only if you have a value, so wait for it". Which is logical.
Resulting in a complete dot line with no space. Wonderful.

# Pictures


-------------------------------------
### Give support ! ( a chocolat viennois break | help me get sensors and Raspberry hardware)
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=E79JA29LBLTAE&source=url)
