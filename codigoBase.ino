#include <MFRC522.h>  // Biblioteca para el lector RFID
#include <SPI.h>
#include <Wire.h>
#include <RTClib.h>   // Biblioteca para el RTC
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Crear instancia del lector RFID
RTC_DS1307 rtc;  // Crear instancia del RTC

const int buzzerPin = 8;  // Pin al que está conectado el buzzer
void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();

  
}

void loop() {
  // put your main code here, to run repeatedly:
  DateTime now = rtc.now();

}

bool checkRFID() {
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    return true;
  }
  return false;
}

int getUserInfo() {
  
}
