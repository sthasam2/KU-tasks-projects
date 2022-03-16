LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

---- OR gate for two inputs ----
ENTITY OR2_gate IS
    PORT (
        A, B : IN STD_LOGIC;
        Y : OUT STD_LOGIC
    );
END ENTITY;

ARCHITECTURE orLogic OF OR2_gate IS
BEGIN
    Y <= A OR B;
END ARCHITECTURE;