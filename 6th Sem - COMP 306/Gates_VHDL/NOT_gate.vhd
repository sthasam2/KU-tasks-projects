LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

---- NOT gate for single input ----
ENTITY NOT_gate IS
    PORT (
        A : IN STD_LOGIC;
        Y : OUT STD_LOGIC
    );
END ENTITY;

ARCHITECTURE notLogic OF NOT_gate IS
BEGIN
    Y <= NOT(A);
END ARCHITECTURE;