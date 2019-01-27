#include <Adafruit_Sensor.h>
#include <SFE_BMP180.h>
#include <EEPROM.h>
#include <Wire.h>
#include <Servo.h>
SoftwareSerial portOne(10,11);

Servo servo1; 
Servo servo2;

int i = 0;
int j = 0;
int k = 0;
int prev_i,prev_j;

#define DHTTYPE DHT22  
int soil_moist= A0;    //fc-28
int air_quality = A1;  //mq135
int DHT_pin = A2;      //dht22
//int temp_press= A3;    //bmp180
float x,y,m = 0;
float Temp,Hum;
//byte A,B,C,D,E,F,G;


//DHT dht(DHT_pin, DHTTYPE);
SFE_BMP180 pressure;

#define ALTITUDE 100.0 //write your base altitude


void setup() 
{
   Serial.begin(9600);
//  dht.begin();
  pressure.begin();
  servo1.attach(9,500,2500);
  servo2.attach(10,500,2500); 
  //Serial.print('a');
  portOne.begin(9600);

}

void sensor()
{
  x=analogRead(soil_moist);
   m=x*100/1023;
   portOne.print(x);
   portOne.print("\t");
   delay(10);

    y=analogRead(air_quality);
    portOne.print(y);
    portOne.print("\t");
    delay(10);

     char status;
  double T, P, p0, a;


  status = pressure.startTemperature();
  if (status != 0)
  {
    delay(status);

    status = pressure.getTemperature(T);
    if (status != 0)
    {1/
      portOne.print(T, 2);
      portOne.print("\t");
      

      status = pressure.startPressure(3);
      if (status != 0)
      {
        delay(status);

        status = pressure.getPressure(P, T);
        if (status != 0)
        {
          portOne.print(P, 2);
          portOne.print("\t");
        }
        else portOne.println("error retrieving pressure measurement\n");
      }
      else portOne.println("error starting pressure measurement\n");
    }
    else portOne.println("error retrieving temperature measurement\n");
  }
  else portOne.println("error starting temperature measurement\n");  

    portOne.println(" ");
}

void servo_control_1(int i)
{
   servo1.write(i);
}

void servo_control_2(int j)
{
   servo1.write(j);
}


void loop() 
{
   while(Serial.available()== 0){};

   Serial.setTimeout(5000000);

   k=Serial.parseInt();

   if(k==1)
   {
      sensor();
   }

   if(k==2)
   {
      servo_control_1(180);
   }
   if(k==3)
   {
      servo_control_2(180);
   }


 //SERVO CODE

    
}
