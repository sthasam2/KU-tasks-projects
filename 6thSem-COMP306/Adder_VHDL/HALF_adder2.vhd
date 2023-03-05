LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY HALF_ADDER IS
    PORT (
        A, B : IN STD_LOGIC;
        SUM, CARRY_OUT : OUT STD_LOGIC);
END HALF_ADDER;

ARCHITECTURE behavoural OF HALF_ADDER IS
BEGIN
    HA : PROCESS (A, B)
    BEGIN
        IF A = '1' THEN
            SUM <= NOT B;
            CARRY_OUT <= B;
        ELSE
            SUM <= B;
            CARRY_OUT <= '0';
        END IF;
    END PROCESS HA;

END behavoural;