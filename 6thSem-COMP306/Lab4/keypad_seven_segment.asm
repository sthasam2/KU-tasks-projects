start:
	MOV R0, #0
	
    ; scan row with * 0 #
    SETB P0.3
	CLR P0.0
	CALL colScan
	JB F0, finish

    ; scan row with 1 2 3
	SETB P0.0
	CLR P0.1
	CALL colScan
	JB F0, finish
    
    ; scan row with 4 5 6
	SETB P0.1
	CLR P0.2
	CALL ColScan
	JB F0, finish 
    
    ; scan row with 7 8 9
    SETB P0.2
	CLR P0.3
	CALL ColScan
	JB F0, finish
	JMP start
	
finish:
    ; display Okay

	SETB P3.4
	SETB P3.3
	MOV P1, #11000000B
	CALL delay
	
    SETB P3.4
	CLR P3.3
	MOV P1, #10001001B
	CALL delay
    
	CLR P3.4
    SETB P3.3
	MOV P1, #10100000B
	CALL delay
	
    CLR P3.4
    CLR P3.3
	MOV P1, #10010001B
	CALL delay
	
colScan:
	JNB P0.4, gotKey
	INC R0
	JNB P0.5, gotKey
	INC R0
	JNB P0.6, gotKey
	INC R0
	RET
	
gotKey:
	CJNE R0, #7, NTEQUAL
	SETB F0
	
NTEQUAL:
	RET

delay:
	MOV R0, #1
	DJNZ R0, $
    MOV P1, #11111111B
	RET
