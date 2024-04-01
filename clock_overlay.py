import datetime
import time

# Specify the output file paths
output_file = "clock_overlay.txt"


while True:
    # Get the current time in Morrilton
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Calculate the time of totality in Morrilton
    totality_time = datetime.datetime(2024, 4, 1, 14, 58, 00)
    totality_time_str = totality_time.strftime("%H:%M:%S")

    # Calculate the time left until totality
    time_left = totality_time - current_time
    if time_left > datetime.timedelta(0):
        time_left_str = str(time_left).split(".")[0]  # Extract the time left without milliseconds
        time_left_str = time_left_str[:-3] + ":" + time_left_str[-2:]  # Add a colon between minutes and seconds

    # Create totality countdown
    totality_countdown = 253

    if current_time >= totality_time:
        totality_countdown = totality_countdown - (current_time - totality_time).total_seconds()

    if totality_countdown > 0:
        totality_countdown_str = "{:02d}:{:02d}".format(int(totality_countdown // 60), int(totality_countdown % 60))
    else:
        totality_countdown_str = "Totality has ended."


    # Write the current time, totality time, and time left to the output file
    with open(output_file, "w") as file:
        file.write(f"Current Time: {current_time_str}\n")
        file.write(f"Totality Time at Petit Jean State Park: {totality_time_str}\n")
        if time_left > datetime.timedelta(0):
            file.write(f"Time Left Until Totality: {time_left_str}\n")
        file.write(f"Time Left in Totality: {totality_countdown_str}\n")

    print("Current time, totality time, and time left have been written to the output file.")

    # Wait for 1 second before updating the time again
    time.sleep(1)
