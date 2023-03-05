start:
	; display 1 in LED 11
	SETB P3.4
	SETB P3.3
	MOV P1, #11111001B
	CALL delay
	
	; display 2 in LED 10
	SETB P3.4
	CLR P3.3
	MOV P1, #10100100B
	CALL delay
	
	; display 3 in LED 01
	CLR P3.4
    SETB P3.3
	MOV P1, #10110000B
	CALL delay
	
	; display 4 in LED 00
	CLR P3.4
    CLR P3.3
	MOV P1, #10011001B
	CALL delay

	; display 5 in LED 11
	SETB P3.4
	SETB P3.3
	MOV P1, #10010010B
	CALL delay
	
	; display 6 in LED 10
	SETB P3.4
	CLR P3.3
	MOV P1, #10000010B
	CALL delay
	
	; display 7 in LED 01
	CLR P3.4
    SETB P3.3
	MOV P1, #11111000B
	CALL delay
	
	; display 8 in LED 00
	CLR P3.4
    CLR P3.3
	MOV P1, #00000000B
	CALL delay

	; display 9 in LED 11
	SETB P3.4
	SETB P3.3
	MOV P1, #10010000B
	CALL delay
	
    JMP start
	
delay:
	MOV R0, #1
	DJNZ R0, $
    MOV P1, #11111111B
	RET
