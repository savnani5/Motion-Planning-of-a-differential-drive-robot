#include "BluetoothSerial.h"
BluetoothSerial ESP_BT;

int incoming;

void setup() 
{
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  ESP_BT.begin("ESP32_LED_Control"); //Name of your Bluetooth Signal
  Serial.println("Bluetooth Device is Ready to Pair");
  pinMode(2, OUTPUT); //make the LED pin (2) as output
  digitalWrite (2, LOW);
}

void loop() 
{
  if (ESP_BT.available()) //Check if we receive anything from Bluetooth
  {
    incoming = ESP_BT.read(); //Read what we recevive
      Serial.print("Received:"); 
      Serial.println(incoming);
}
if (incoming == 49)
        {
        digitalWrite(2, HIGH);
        ESP_BT.println("LED turned ON");
        }
       
    if (incoming == 48)
        {
        digitalWrite(2, LOW);
        ESP_BT.println("LED turned OFF");
        }
delay(20);

}
