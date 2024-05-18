#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Define la dirección de la LCD
#define I2C_ADDR 0x27

// Define las dimensiones de la LCD
#define LCD_COLS 16
#define LCD_ROWS 2

// Crea un objeto LCD
LiquidCrystal_I2C lcd(I2C_ADDR, LCD_COLS, LCD_ROWS);

const int F = 4;
const int C = 4;
bool arduinoFound = false;

int filas[] = {12,11,10,9};
int columnas[] = {5,6,7,8};

int matriz[F][C];
int matrizAnterior[F][C] = {0};

// Definir los pines para los botones adicionales
const int buttonPins[] = {2, A0, 3, 4};
const int numButtons = sizeof(buttonPins) / sizeof(int);
int buttonStates[numButtons];
int lastButtonStates[numButtons];

// Variables para almacenar los valores actuales
int volume = 10;
bool effect = false;
int scale = 4;

void setup() {
    
    pinMode(13, INPUT);  // Desactivar el LED del pin 13

    for (int i = 0; i < F; i++){
        pinMode(filas[i],INPUT);
    }
    for (int i = 0; i < C; i++){
        pinMode(columnas[i],INPUT);
    }

    // Configurar los pines de los botones como entradas
    for (int i = 0; i < numButtons; i++) {
        pinMode(buttonPins[i], INPUT_PULLUP);
        buttonStates[i] = digitalRead(buttonPins[i]);
        lastButtonStates[i] = buttonStates[i];
    }

    Serial.begin(9600);
    while (!Serial) {
        ; // espera a que el puerto serie esté disponible
    }

    // Envía el mensaje "Arduino Piano" cada segundo hasta que sea reconocido
    while (!arduinoFound) {
        Serial.println("Midithara");
        delay(1000);  // espera un segundo

        // Comprueba si se ha recibido un mensaje de confirmación
        if (Serial.available() > 0) {
            String message = Serial.readString();
            if (message == "Midithara found") {
                arduinoFound = true;
            }
        }
    }

    // Inicializa la LCD
    lcd.init();

    // Enciende la luz de fondo
    lcd.backlight();

    // Muestra los valores iniciales en la LCD
    updateLCD();
}

void leerMatriz(){
    for (int i = 0; i < F; i++){
        pinMode(filas[i],OUTPUT);
        digitalWrite(filas[i],LOW);
        for (int j = 0; j < C; j++){
            pinMode(columnas[j],INPUT_PULLUP);
            int estadoActual = digitalRead(columnas[j]);
            if (estadoActual == LOW && matrizAnterior[i][j] == HIGH) {
                Serial.println(i * C + j);
            }
            matrizAnterior[i][j] = estadoActual;
            pinMode(columnas[j],INPUT);
        }
        pinMode(filas[i],INPUT);
    }
}

void loop() {
    leerMatriz();

    // Leer el estado de los botones
    for (int i = 0; i < numButtons; i++) {
        buttonStates[i] = digitalRead(buttonPins[i]);

        // Detectar flanco de subida
        if (buttonStates[i] == HIGH && lastButtonStates[i] == LOW) {
            // El botón i ha sido presionado
            switch (i) {
                case 0:  // Botón 0 (pin 4): -1 en volumen
                    if (volume > 0) {
                        volume--;
                        Serial.println(18);
                    }
                    break;
                case 1:  // Botón 1 (pin 3): +1 en volumen
                    if (volume < 10) {
                        volume++;
                        Serial.println(19);
                    }
                    break;
                case 2:  // Botón 2 (pin 2): +1 en escala
                    scale++;
                    if (scale > 5) {
                        scale = 3;
                    }
                    Serial.println(17);
                    break;
                case 3:  // Botón 3 (pin A0): cambiar efecto
                    effect = !effect;
                    Serial.println(16);
                    break;
            }

            // Actualizar la LCD con los nuevos valores
            updateLCD();
        }

        // Actualizar el estado anterior del botón
        lastButtonStates[i] = buttonStates[i];
    }

    delay(45);
}

void updateLCD() {
    lcd.clear();

    lcd.setCursor(0, 0);
    lcd.print("Vol: ");
    lcd.print(volume);

    lcd.setCursor(0, 1);
    lcd.print("Effect: ");
    lcd.print(effect ? "Reverb" : "None");

    lcd.setCursor(8, 0);
    lcd.print("Oct: ");
    lcd.print(scale);
}