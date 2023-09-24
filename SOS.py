import pandas as pd
from plyer import notification
from datetime import datetime
import time

csv_file_path='pollutiondata_Final.csv'

dangerous_level={
    'CO': 90,
    'NH3': 40,
    'NO2': 110,
    'PM10': 260,
    'PM2.5': 40,
    'OZONE': 6,
    'SO2': 120,
    'PM2.5_AQI': 45,
    'AQI': 550,
}


def check_csv_for_dangerous_values():
    try:
        df = pd.read_csv('pollutiondata_Final.csv',low_memory=False)

        # Iterate through rows and columns to check for dangerous values
        for index, row in df.iterrows():
            for pollutant, threshold in dangerous_level.items():
                value = row[pollutant]
                if float(value) > threshold:
                    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + row['Station']
                    print(timestamp)
                    # aqi = calculate_aqi(value, pollutant)
                    
                    notification_title = f"Dangerous {pollutant} Level Alert"
                    notification_text = f"High {pollutant} value of {value} detected at {timestamp}."
                    aqi_text = f"{pollutant}"
                    
                    notification_message = f"{notification_text}\n{aqi_text}"
                    
                    notification.notify(
                        title=notification_title,
                        message=notification_message,
                        app_name="CSV Monitor",
                    )
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Set the monitoring interval (in seconds)
monitoring_interval = 540  # Check every 60 seconds

while True:
    check_csv_for_dangerous_values()
    time.sleep(monitoring_interval)