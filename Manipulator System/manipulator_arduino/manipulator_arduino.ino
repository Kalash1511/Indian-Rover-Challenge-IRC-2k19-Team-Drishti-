#include <avr/wdt.h>

int motor_1,motor_2,motor_3;
int motor_4,motor_5;//camera
int actuator_1,actuator_2,actuator_3;
int d;
 

int pwm_ac1=2,pwm_ac2=3,pwm_ac3=4;
int pwm_mo1=7,pwm_mo2=5,pwm_mo3=9,pwm_mo4=11,pwm_mo5=13;

int dir_a11=23,dir_a12=25;
int dir_a21=27,dir_a22=29;
int dir_a31=31,dir_a32=33;
int dir_m1=8,dir_m2=6,dir_m3=43,dir_m4=12,dir_m5=10;

int analog_pin1=13;
int analog_pin2=14;
int analog_pin3=15;

int pwm_a1,pwm_a2,pwm_a3;
int pwm_m1,pwm_m2,pwm_m3,pwm_m4,pwm_m5;

int a=0;
int b=0;
int c=0;

int base_speed_1=50;
int base_speed_2=100;
int base_speed_3=100;

float kp1=0.9,kd1=0.21;
float kp2=0.15,kd2=0.10;
float kp3=0.15,kd3=0.10;

int previous_error_1,previous_error_2,previous_error_3;
int d_error_1,d_error_2,d_error_3;

void(*resetFunc) (void) = 0;//declare the reset function @ address 0


void setup() 
{
    Serial.begin(9600);
    
    pinMode(dir_a11, OUTPUT);
    pinMode(dir_a21, OUTPUT);
    pinMode(dir_a31, OUTPUT);
    pinMode(dir_a12, OUTPUT);
    pinMode(dir_a22, OUTPUT);
    pinMode(dir_a32, OUTPUT);

    pinMode(dir_m1, OUTPUT);
    pinMode(dir_m2, OUTPUT);
    pinMode(dir_m3, OUTPUT);
    pinMode(dir_m4, OUTPUT);
    pinMode(dir_m5, OUTPUT);

    pinMode(pwm_ac1, OUTPUT);
    pinMode(pwm_ac2, OUTPUT);
    pinMode(pwm_ac3, OUTPUT);

    pinMode(pwm_mo1, OUTPUT);
    pinMode(pwm_mo2, OUTPUT);
    pinMode(pwm_mo3, OUTPUT);
    pinMode(pwm_mo4, OUTPUT);
    pinMode(pwm_mo5, OUTPUT);

    pinMode(analog_pin1,OUTPUT);
    pinMode(analog_pin2,OUTPUT);
    pinMode(analog_pin3,OUTPUT);

    digitalWrite(pwm_ac1,0);
    digitalWrite(pwm_ac2,0);
    digitalWrite(pwm_ac3,0);
    digitalWrite(pwm_mo1,0);
    digitalWrite(pwm_mo2,0);
    digitalWrite(pwm_mo3,0);
    digitalWrite(pwm_mo4,0);
    digitalWrite(pwm_mo5,0);

    wdt_reset();
    wdt_disable();

    Serial.println("CODE STARTED");
}


void actuator_1_set(int desired_value_1)
{
    
    int error_1=0,total_error_1=0,distance_1=0;
  
    int digital_value_1;
    Serial.println(desired_value_1);
    do
    {

            digital_value_1=analogRead(analog_pin1);
            error_1=(desired_value_1-digital_value_1);
            d_error_1=(error_1- previous_error_1);
            total_error_1=kp1*(error_1)+kd1*(d_error_1);
            previous_error_1=error_1;
            if(error_1<-3)
           {
              
              digitalWrite(dir_a11,1);
              digitalWrite(dir_a12,0);
              
              a=base_speed_1+total_error_1;
              analogWrite(pwm_ac1,a);
            }
            else if(error_1>3)
            {    
                digitalWrite(dir_a11,0);
                digitalWrite(dir_a12,1);
                a=base_speed_1-total_error_1;
               
                analogWrite(pwm_ac1,a);
            }
            else
            {
                digitalWrite(pwm_ac1,0);
            }
            Serial.println("digital_value1=" +String(digital_value_1));
            distance_1=map(digital_value_1,25,983,17,115);
    }while(error_1>3 || error_1<-3);
}






void actuator_2_set(int desired_value_2)
{                                                       
    int digital_value_2;
    int error_2=0,total_error_2=0,distance_2=0;
    Serial.println(desired_value_2);
    do
    {
    
          digital_value_2=analogRead(analog_pin2);
          error_2=(digital_value_2-desired_value_2);
          d_error_2=(error_2 - previous_error_2);
          total_error_2=kp2*error_2+kd2*d_error_2;
          previous_error_2=error_2;
      
           if(error_2<-3)
           {
                digitalWrite(dir_a21,0);
                digitalWrite(dir_a22,1);
                b=base_speed_2-total_error_2;
                analogWrite(pwm_ac2,b);
            }
            
            else if(error_2>3)
            {    
                digitalWrite(dir_a21,1);
                digitalWrite(dir_a22,0);
                b=base_speed_2+total_error_2;
                analogWrite(pwm_ac2,b);
           }
           
           else
           {
                analogWrite(pwm_ac2,0);
           }
           distance_2=map(digital_value_2,25,942,20,320);
           Serial.println("digital_value2=" +String(digital_value_2));
    }while(error_2>3 || error_2<-3);
}

       
void actuator_3_set(int desired_value_3)
{
      int digital_value_3;
      
      int error_3=0,total_error_3=0,distance_3=0;
      Serial.println(desired_value_3);
      do 
      {
  
              digital_value_3=analogRead(analog_pin3);
              error_3=(digital_value_3-desired_value_3);
              d_error_3=(error_3- previous_error_3);
              total_error_3=kp3*error_3+kd3*d_error_3;
              
              
              if(error_3<-3)
              {
                 digitalWrite(dir_a31,0);
                 digitalWrite(dir_a32,1);
                            
                 c=base_speed_3-total_error_3;
                 analogWrite(pwm_ac3,c);
              }
              else if(error_3>3)
              {    
                  digitalWrite(dir_a31,1);
                  digitalWrite(dir_a32,0);
                  c=base_speed_3+total_error_3;
                 
                  analogWrite(pwm_ac3,c);
              }
              else
              {
                  digitalWrite(pwm_ac3,0);
              }
              
              distance_3=map(digital_value_3,25,942,20,320);
              Serial.println("digital_value3=" +String(digital_value_3));
              previous_error_3=error_3;
              
    }while((error_3 >3)||(error_3 <-3));
    Serial.println("DEFAULT POSITION SET");
}

void Reset()
{
  wdt_reset();
  wdt_enable(WDTO_15MS);   
  
}


void loop()
{

   while(Serial.available()== 0){};
  
   actuator_1=Serial.parseInt();
   actuator_2=Serial.parseInt();
   actuator_3=Serial.parseInt();
   
   motor_1=Serial.parseInt();
   motor_2=Serial.parseInt();
   motor_3=Serial.parseInt();
   motor_4=Serial.parseInt();
   motor_5=Serial.parseInt();

   d=Serial.parseInt();

   Serial.setTimeout(5000000);

  

  if(d == 10)
  {
    Serial.println("CODE RESETED");
    Reset();
  }


 
   //actuator_1
   if(actuator_1==2)
   {
      pwm_a1=127;
      digitalWrite(dir_a11,1);
      digitalWrite(dir_a12,0);
      analogWrite(pwm_ac1,pwm_a1);
   }
   
   else if(actuator_1==1)
   {
      
      pwm_a1=127;
      digitalWrite(dir_a11,0);
      digitalWrite(dir_a12,1);
      analogWrite(pwm_ac1,pwm_a1);
   }
   
   else
   {
      pwm_a1=0;
      digitalWrite(dir_a11,0);
      digitalWrite(dir_a12,0);
      analogWrite(pwm_ac1,pwm_a1);
   }
   

   //actuator_2
   if(actuator_2==2)
   {
      pwm_a2=97;
      digitalWrite(dir_a21,1);
      digitalWrite(dir_a22,0);
      analogWrite(pwm_ac2,pwm_a2);
   }
   
   else if(actuator_2==1)
   {
      pwm_a2=97;
      digitalWrite(dir_a21,0);
      digitalWrite(dir_a22,1);
      analogWrite(pwm_ac2,pwm_a2);
   }
   
   else
   {
      pwm_a2=0;
      digitalWrite(dir_a21,0);
      digitalWrite(dir_a22,0);
      analogWrite(pwm_ac2,pwm_a2);
   }

   
   //actuator_3
   if(actuator_3==2)
   {
      digitalWrite(dir_a31,1);
      digitalWrite(dir_a32,0);
      pwm_a3=127;
      analogWrite(pwm_ac3,pwm_a3);
   }
   
   else if(actuator_3==1)
   {
      digitalWrite(dir_a31,0);
      digitalWrite(dir_a32,1);
      pwm_a3=127;
      analogWrite(pwm_ac3,pwm_a3);
   }
   
   else
   {
      digitalWrite(dir_a31,0);
      digitalWrite(dir_a32,0);
      pwm_a3=0;
      analogWrite(pwm_ac3,pwm_a3);
   }

   
    //motor_1
   if(motor_1==1)
   {
      digitalWrite(dir_m1,LOW);
      pwm_m1=100;
      analogWrite(pwm_mo1,pwm_m1);
   }
   
   else if(motor_1==2)
   {
      digitalWrite(dir_m1,HIGH);
      pwm_m1=100;
      analogWrite(pwm_mo1,pwm_m1);
   }
   
   else
   {
      digitalWrite(dir_m1,LOW);
      pwm_m1=0;
      analogWrite(pwm_mo1,pwm_m1);
   }

   
   //motor_2
   if(motor_2==1)
   {
      digitalWrite(dir_m2,LOW);
      pwm_m2=255;
      analogWrite(pwm_mo2,pwm_m2);
   }
   
   else if(motor_2==2)
   {
      digitalWrite(dir_m2,HIGH);
      pwm_m2=255;
      analogWrite(pwm_mo2,pwm_m2);
   }
   
   else
   {
      digitalWrite(dir_m2,LOW);
      pwm_m2=0;
      analogWrite(pwm_mo2,pwm_m2);
   }

   
   //motor_3
   if(motor_3==1)
   {
      digitalWrite(dir_m3,LOW);
      pwm_m3=175;
      analogWrite(pwm_mo3,pwm_m3);
   }
   
   else if(motor_3==2)
   {
      digitalWrite(dir_m3,HIGH);
      pwm_m3=175;
      analogWrite(pwm_mo3,pwm_m3);
   }
   
   else
   {
      digitalWrite(dir_m3,LOW);
      pwm_m3=0;
      analogWrite(pwm_mo3,pwm_m3);
   }

   //motor_4
   if(motor_4==1)
   {
      digitalWrite(dir_m4,LOW);
      pwm_m4=200;
      analogWrite(pwm_mo4,pwm_m4);
   }
   
   else if(motor_4==2)
   {
      digitalWrite(dir_m4,HIGH);
      pwm_m4=200;
      analogWrite(pwm_mo4,pwm_m4);
   }
   
   else
   {
      digitalWrite(dir_m4,LOW);
      pwm_m4=0;
      analogWrite(pwm_mo4,pwm_m4);
   }

   //motor_5
   if(motor_5==1)
   {
      digitalWrite(dir_m5,LOW);
      pwm_m5=200;
      analogWrite(pwm_mo5,pwm_m5);
   }
   
   else if(motor_5==2)
   {
      digitalWrite(dir_m5,HIGH);
      pwm_m5=200;
      analogWrite(pwm_mo5,pwm_m5);
   }
   
   else
   {
      digitalWrite(dir_m5,LOW);
      pwm_m5=0;
      analogWrite(pwm_mo5,pwm_m5);
   }
      Serial.println(d);
   
}
