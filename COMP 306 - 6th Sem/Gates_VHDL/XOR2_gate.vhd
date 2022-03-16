LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

---- XOR gate for two inputs ----
ENTITY XOR2_gate IS
    PORT (
        A, B : IN STD_LOGIC;
        Y : OUT STD_LOGIC
    );
END ENTITY;

ARCHITECTURE xorLogic OF XOR2_gate IS
BEGIN
    Y <= A XOR B;
END ARCHITECTURE;