import obd

# Connect to the WiFi OBD-II adapter
connection = obd.OBD("socket://192.168.0.10:35000")

if not connection.is_connected():
    print("❌ Failed to connect to OBD-II adapter.")
else:
    print("✅ Connected to OBD-II adapter!")

    supported_cmds = connection.supported_commands
    print("\n📋 Supported Commands from ECU:")
    for cmd in supported_cmds:
        print(f"- {cmd.name}")

    connection.close()
