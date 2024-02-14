#include <DHT.h>
#define DHTPIN 12   
#define DHTTYPE DHT11
int buzzerPin = 13;    
float temperatureLimit = 32.0; 

DHT dht(DHTPIN, DHTTYPE);
#define led1 2
#define led2 4
#define led3 7
#define led4 8

void setup() {
  Serial.begin(9600);
  pinMode(led1,OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  dht.begin();
}
int a=1;
void loop() {
  // if(Serial.available()>0){
    String keyword = Serial.readStringUntil('\n');
    keyword.trim();

    if (keyword.equals("on led 1")) {
      digitalWrite(led1,HIGH);
    }
    else if(keyword.equals("on led 2")){
      digitalWrite(led2,HIGH);
    }
    else if(keyword.equals("on led 3")){
      digitalWrite(led3,HIGH);
    }
    else if(keyword.equals("on led 4")){
      digitalWrite(led4,HIGH);
    }
    else if(keyword.equals("on all led")){
      digitalWrite(led1,HIGH);
      digitalWrite(led2,HIGH);
      digitalWrite(led3,HIGH);
      digitalWrite(led4,HIGH);
    }
    else if(keyword.equals("off led 1")){
      digitalWrite(led1,LOW);
    }
    else if(keyword.equals("off led 2")){
      digitalWrite(led2,LOW);
    }
    else if(keyword.equals("off led 3")){
      digitalWrite(led3,LOW);
    }
    else if(keyword.equals("off led 4")){
      digitalWrite(led4,LOW);
    }
    else if(keyword.equals("off all led")){
      digitalWrite(led1,LOW);
      digitalWrite(led2,LOW);
      digitalWrite(led3,LOW);
      digitalWrite(led4,LOW);
    }
    else if(keyword.equals("Thank")){
      for (int frequency = 2000; frequency >= 0; frequency -= 50) {
        tone(buzzerPin, frequency);
        delay(50);
      }
      noTone(buzzerPin);
    }
    else if(keyword.equals("off buzzer")){
      noTone(buzzerPin);
      a=0;
    }
  // }
  float temperature = dht.readTemperature();
  if (!isnan(temperature)) {
    Serial.print("Temperature: ");
    Serial.print(temperature);
    // Serial.println(" °C");
    if (temperature > temperatureLimit && a==1) {
      digitalWrite(buzzerPin, HIGH);
      digitalWrite(led1,HIGH);
      digitalWrite(led2,HIGH);
      digitalWrite(led3,HIGH);
      digitalWrite(led4,HIGH);
      delay(100);
      digitalWrite(led1,LOW);
      digitalWrite(led2,LOW);
      digitalWrite(led3,LOW);
      digitalWrite(led4,LOW);
      delay(100);
    } 
    else {
      digitalWrite(buzzerPin, LOW);
    }
  }
  else {
    Serial.println("Error reading temperature!");
  }
}
