#define red 8
#define green 9
#define yellow 10
#define pushButton 11

int next_color = red;
int buttonPushed = 0;

void setup()
{
    pinMode(red, OUTPUT);
    pinMode(green, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(pushButton, INPUT);
}

void loop()
{
    buttonPushed = digitalRead(pushButton);

    if (buttonPushed == 1)
    {
        turnLEDOn(next_color);
    }
    else
    {
        turnLEDsOff();
    }
}

void turnLEDsOff()
{
    digitalWrite(red, 0);
    digitalWrite(green, 0);
    digitalWrite(yellow, 0);
}

void turnLEDOn(int color)
{
    int red_state = 0, green_state = 0, yellow_state = 0;

    switch (color)
    {
    case red:
        red_state = 1;
        next_color = green;
        break;
    case green:
        green_state = 1;
        next_color = yellow;
        break;
    case yellow:
        yellow_state = 1;
        next_color = red;
        break;
    }

    digitalWrite(red, red_state);
    digitalWrite(green, green_state);
    digitalWrite(yellow, yellow_state);
    delay(1000);
    turnLEDsOff();
}