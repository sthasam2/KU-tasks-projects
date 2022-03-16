LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

---- AND gate for two inputs ----
ENTITY AND2_gate IS
    PORT (
        A, B : IN STD_LOGIC;
        Y : OUT STD_LOGIC
    );
END ENTITY;

ARCHITECTURE andLogic OF AND2_gate IS
BEGIN
    Y <= A AND B;
END ARCHITECTURE;