

#include <Servo.h>

Servo servo1; 
Servo servo2;


int i = 0;
int j = 0;



int prev_i,prev_j;

void setup()
{
  Serial.begin(19200);
  servo1.attach(9,500,2500);
  servo2.attach(10,500,2500); 
   
}

void loop() 
{
   while(Serial.available()== 0){};

   Serial.setTimeout(50000);

   
  
   i=Serial.parseInt();
   j=Serial.parseInt();
   Serial.println("i=");
   Serial.println(i);
   Serial.println("j=");
   Serial.println(j);

   
    delay(500);
   if(i==0 && j==0)
   {
    i=prev_i;
    j=prev_j;
   }

 
   
   Serial.println("i=");
   Serial.println(i);
   Serial.println("j=");
   Serial.println(j);
   servo1.write(i);
   servo2.write(j);

   prev_i=i;
   prev_j=j;

  
}
