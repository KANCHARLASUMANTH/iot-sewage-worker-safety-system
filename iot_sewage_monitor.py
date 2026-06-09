import paho.mqtt.client as mqtt
import requests
import warnings

# Simulated sensor thresholds
depth = 110  # Example depth in cm
gas_level = 900  # Example PPM
temperature = 38  # Celsius
humidity = 90  # Percent

# Thresholds
DEPTH_THRESHOLD = 100
GAS_THRESHOLD = 800
TEMP_THRESHOLD = 35
HUMIDITY_THRESHOLD = 85

# Alert messages
if depth > DEPTH_THRESHOLD:
    print("ALERT: Depth threshold exceeded")

if gas_level > GAS_THRESHOLD:
    print("ALERT: Gas concentration threshold exceeded")

if temperature > TEMP_THRESHOLD or humidity > HUMIDITY_THRESHOLD:
    print("ALERT: Environmental condition threshold exceeded")

# HTTP POST example (returns 405 if POST not allowed on the endpoint)
try:
    response = requests.post("https://example.com/api/data", json={"depth": depth})
    print("HTTP Response:", response.status_code)
except Exception as e:
    print("HTTP Request failed:", e)

# MQTT setup (warning: API version 1 is deprecated)
warnings.warn("Callback API version 1 is deprecated, update to latest version", DeprecationWarning)

def send_data_mqtt():
    mqtt_client = mqtt.Client()  # This triggers the DeprecationWarning in older versions
    mqtt_client.connect("mqtt.example.com", 1883, 60)  # Replace with actual broker
    mqtt_client.publish("iot/sewage", payload="Sensor Alert", qos=1)
    mqtt_client.disconnect()

# Call function
send_data_mqtt()
