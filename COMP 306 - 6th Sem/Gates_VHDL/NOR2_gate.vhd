LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

---- NOR gate for two inputs ----
ENTITY NOR2_gate IS
    PORT (
        A, B : IN STD_LOGIC;
        Y : OUT STD_LOGIC
    );
END ENTITY;

ARCHITECTURE norLogic OF NOR2_gate IS
BEGIN
    Y <= NOT(A OR B);
END ARCHITECTURE;