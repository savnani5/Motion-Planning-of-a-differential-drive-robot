#include "WiFi.h"


// Setting SSID and password of the network
const char* ssid = "PARAS";
const char* password =  "123456789";
 
WiFiServer wifiServer(80);

// Motor 1 Pins definition
int motor1Pin1 = 27; 
int motor1Pin2 = 26; 
int enable1Pin = 14; 

// Motor 2 Pins definition
int motor2Pin1 = 18; 
int motor2Pin2 = 19; 
int enable2Pin = 15; 

// Setting PWM properties
const int freq = 30000;
const int pwmChannel = 0;
const int resolution = 8;
int dutyCycle = 200;

void setup() 
{
  // sets the pins as outputs:
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(enable1Pin, OUTPUT);

  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);
  pinMode(enable2Pin, OUTPUT);
  
  // configure LED PWM functionalitites
  ledcSetup(pwmChannel, freq, resolution);
  
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(enable1Pin, pwmChannel);
  ledcAttachPin(enable2Pin, pwmChannel);

  Serial.begin(115200);
 
 //Connecting to the wifi network
 
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
 
  wifiServer.begin();

  // testing
  Serial.print("Testing DC Motor...");
}

void loop() 
{

   WiFiClient client = wifiServer.available();
 
  if (client) 
  {
 
    while (client.connected()) 
    {
 
      while (client.available()>0) 
      {
        char c = client.read();
        Serial.println(c);
        
          if (c == 'w')
          {
             // Move the Robot forward at maximum speed
              Serial.println("Moving Forward");
              digitalWrite(motor1Pin1, LOW);
              digitalWrite(motor1Pin2, HIGH); 
              digitalWrite(motor2Pin1, LOW);
              digitalWrite(motor2Pin2, HIGH); 
              delay(50);
             
          }
          if (c == 's')
          {
            
            // Move the Robot backwards at maximum speed
            Serial.println("Moving Backwards");
            digitalWrite(motor1Pin1, HIGH);
            digitalWrite(motor1Pin2, LOW); 
            digitalWrite(motor2Pin1, HIGH);
            digitalWrite(motor2Pin2, LOW); 
            delay(50);
          }
          if (c == 'a')
          {
            
            // Rotate the robot anticlockwise
            Serial.println("Rotating anticlockwise");
            digitalWrite(motor1Pin1, LOW);
            digitalWrite(motor1Pin2, HIGH); 
            digitalWrite(motor2Pin1, HIGH);
            digitalWrite(motor2Pin2, LOW); 
            delay(10);
          }

         if (c == 'd')
         {
          // Rotate the robot clockwise
            Serial.println("Rotating clockwise");
            digitalWrite(motor1Pin1, HIGH);
            digitalWrite(motor1Pin2, LOW); 
            digitalWrite(motor2Pin1, LOW);
            digitalWrite(motor2Pin2, HIGH); 
            delay(10);
         }       
        if (c == 'k')
        {
         // Stop the robot 
            Serial.println("Stopping the robot");
            digitalWrite(motor1Pin1, LOW);
            digitalWrite(motor1Pin2, LOW); 
            digitalWrite(motor2Pin1, LOW);
            digitalWrite(motor2Pin2, LOW); 
            delay(50);  
        }
          
          
          
      }
 
      delay(10);
    }
 
    client.stop();
    Serial.println("Client disconnected");
 
  }
}
  /*
  

  // Move the robot forward with increasing speed
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);
  while (dutyCycle <= 255){
    ledcWrite(pwmChannel, dutyCycle);   
    Serial.print("Forward with duty cycle: ");
    Serial.println(dutyCycle);
    dutyCycle = dutyCycle + 5;
    delay(500);
  }
  dutyCycle = 200;
}
*/
