# TempCSV

This project saves the temperature value of the Sense HAT in to a CSV file

## Add to crontab

Add following line to crontab with `sudo nano /etc/crontab` to store every 5 minutes a temperature value:
`*/5 *  * * *   root    /absolute/file/path/to/repo/storeTempCSV.py` 

Temperature values will be saved into file tempValues.csv inside Repository-Folder

Example of tempValue.csv :

> Time,Temp from Hum-Sensor,Temp from Preas-Sensor 
>
> 2016-03-30 19:06:02,35.651,34.912 
>
> 2016-03-30 19:07:02,35.614,34.908 

All values are in °C
