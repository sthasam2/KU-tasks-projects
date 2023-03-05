#define red 8
#define green 9
#define yellow 10

void setup()
{
    pinMode(red, OUTPUT);
    pinMode(green, OUTPUT);
    pinMode(yellow, OUTPUT);
}

void loop()
{
    turnLED(red);
    turnLED(green);
    turnLED(yellow);
}

void turnLED(int color)
{
    int red_state = 0, green_state = 0, yellow_state = 0;

    switch (color)
    {
    case red:
        red_state = 1;
        break;
    case green:
        green_state = 1;
        break;
    case yellow:
        yellow_state = 1;
        break;
    }

    digitalWrite(red, red_state);
    digitalWrite(green, green_state);
    digitalWrite(yellow, yellow_state);

    delay(2000);

    digitalWrite(red, 0);
    digitalWrite(green, 0);
    digitalWrite(yellow, 0);
}