LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

---- NAND gate for two inputs ----
ENTITY NAND2_gate IS
    PORT (
        A, B : IN STD_LOGIC;
        Y : OUT STD_LOGIC
    );
END ENTITY;

ARCHITECTURE nandLogic OF NAND2_gate IS
BEGIN
    Y <= NOT(A AND B);
END ARCHITECTURE;