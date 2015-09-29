This is a system to automatically generate certificates for the Local Hack Day when given a CSV with names of the participiants from the Organizer.

### How to:
Replace the ```data.csv``` with your attendance file. To do so download the file from the organizer(organizer.mlh.io) and rename it to be called ```data.csv```. Put it into the root directory and run the command as shown below.

To run this project from the root directory type the following into your command line: 

```python main.py```

If you want to change the background image replace base.jpg with a desired background. To change the data modify the data.csv file. 

Output samples can be viewed in https://github.com/LLHD/certificate-generator/tree/master/output . 

You will need to have the Python Imaging Libary (PIL) installed. See https://python-pillow.github.io for information about installing PIL.

Adapted from https://github.com/MLH/flyer_generator/
