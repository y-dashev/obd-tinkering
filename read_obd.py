import obd

connection = obd.OBD("socket://192.168.0.10:35000")  # auto-connects to USB or RF port

if not connection.is_connected():
    print("Failed to connect to OBD-II adapter. Please check your connection.")
else:
    print("Successfully connected to OBD-II adapter!")

obd_commands = [
    obd.commands.ENGINE_LOAD,
    obd.commands.COOLANT_TEMP,
    obd.commands.FUEL_PRESSURE,
    obd.commands.INTAKE_PRESSURE,
    obd.commands.RPM,
    obd.commands.SPEED,
    obd.commands.TIMING_ADVANCE,
    obd.commands.INTAKE_TEMP,
    obd.commands.MAF,
    obd.commands.THROTTLE_POS,
    obd.commands.RUN_TIME,
    obd.commands.FUEL_LEVEL,
    obd.commands.WARMUPS_SINCE_DTC_CLEAR,
    obd.commands.BAROMETRIC_PRESSURE,
    obd.commands.AMBIANT_AIR_TEMP,
    obd.commands.THROTTLE_ACTUATOR,
    obd.commands.TIME_SINCE_DTC_CLEARED,
    obd.commands.HYBRID_BATTERY_REMAINING,
    obd.commands.VIN
]


for cmd in obd_commands:
    response = connection.query(cmd)
    if response.is_null():
        print("Error retrieving {}".format(cmd.name))
    else:
        print("{}: {}".format(cmd.name, response.value))

# Close the connection
connection.close()
