import obd

# Connect to the OBD-II WiFi adapter
connection = obd.OBD("socket://192.168.0.10:35000")  

if not connection.is_connected():
    print("❌ Failed to connect to OBD-II adapter. Check WiFi settings.")
else:
    print("✅ Successfully connected to OBD-II adapter!\n")

    # Get diagnostic trouble codes (DTCs)
    dtc_response = connection.query(obd.commands.GET_DTC)

    if dtc_response.is_null():
        print("✅ No trouble codes found. Your car seems fine! 🎉")
    else:
        print("🚨 Trouble Codes Found:")
        for code in dtc_response.value:
            print(f"- {code}")

    connection.close()
