from radiotherm import radiotherm #based on location in RaspberryPI

#code to init thermostat identification and finding temperature
tstat = radiotherm.get_thermostat()
tstat.temp

#For thermostat function status, defined in class CommonThermostat in thermostat.py
#attributes yet to be tested
