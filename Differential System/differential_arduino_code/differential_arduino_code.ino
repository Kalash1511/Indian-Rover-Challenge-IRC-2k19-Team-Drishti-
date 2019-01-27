 
double left_motor_1, lft1_pwm , prev_l1;
double right_motor_1, rght1_pwm, prev_r1;
double left_motor_2, lft2_pwm, prev_l2;
double right_motor_2, rght2_pwm, prev_r2;


int l1_pwm=5;
int l2_pwm=7;
int r1_pwm=2;
int r2_pwm=4;

int l1_dir=25;
int l2_dir=6;
int r1_dir=23;
int r2_dir=3;



void setup() 
{
    Serial.begin(9600);
    
    pinMode(l1_pwm, OUTPUT);
    pinMode(r1_pwm, OUTPUT);
    pinMode(l2_pwm, OUTPUT);
    pinMode(r2_pwm, OUTPUT);
  
    pinMode(l1_dir, OUTPUT);
    pinMode(r1_dir, OUTPUT);
    pinMode(l2_dir, OUTPUT);
    pinMode(r2_dir, OUTPUT);

    digitalWrite(l1_pwm,0);
    digitalWrite(l2_pwm,0);
    digitalWrite(r1_pwm,0);
    digitalWrite(r2_pwm,0);
}


void loop() 
{ 
             while(Serial.available()== 0){};
          
             Serial.setTimeout(5000000);
            
             left_motor_1=Serial.parseInt();
             right_motor_1=Serial.parseInt();
             left_motor_2=Serial.parseInt();
             right_motor_2=Serial.parseInt();
             
          
             Serial.println(left_motor_1);
             Serial.println(left_motor_2);
             Serial.println(right_motor_1);
             Serial.println(right_motor_2);
          
          //left motor 1
          
             if(left_motor_1<0)
             {
                digitalWrite(l1_dir,HIGH);
                analogWrite(l1_pwm,(-1*left_motor_1));
             }
             
             else
             {
                digitalWrite(l1_dir,LOW);
                analogWrite(l1_pwm,(left_motor_1));  
             }
          
          //right motor 1
          
             if(right_motor_1<0)
             {
                digitalWrite(r1_dir,HIGH);
                analogWrite(r1_pwm,(-1*right_motor_1));
             }
          
             else
             {
                digitalWrite(r1_dir,LOW);
                analogWrite(r1_pwm,(right_motor_1));
             }
          
          //left motor 2
          
             if(left_motor_2<0)
             {
                digitalWrite(l2_dir,HIGH);
                analogWrite(l2_pwm,(-1*left_motor_2));
             }

             else
             {
                digitalWrite(l2_dir,LOW);
                analogWrite(l2_pwm,(left_motor_2));
             }
          
          //right motor 2
          
             if(right_motor_2<0)
             {
                digitalWrite(r2_dir,HIGH);
                analogWrite(r2_pwm,(-1*right_motor_2));
             }

             else
             {
                digitalWrite(r2_dir,LOW);
                analogWrite(r2_pwm,(right_motor_2));
             }

  

             Serial.flush();
   

   
}







  
