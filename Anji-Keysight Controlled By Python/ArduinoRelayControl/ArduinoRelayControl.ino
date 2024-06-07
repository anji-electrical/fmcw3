void setup() 
{
  pinMode(4,OUTPUT);
  Serial.begin(9600);
  Serial.println("READY!");
}

char command_byte;

void loop() 
{
  if(Serial.available())
  {
    command_byte = Serial.read();
    switch(command_byte)
    {
    case 'f':
      Serial.println("TURN OFF");
      digitalWrite(4,LOW);
      break;
    case 'n':
      Serial.println("TURN ON");
      digitalWrite(4,HIGH);
      break;
    default:
      Serial.println("INVALID");
      break;
    }
  }
}
