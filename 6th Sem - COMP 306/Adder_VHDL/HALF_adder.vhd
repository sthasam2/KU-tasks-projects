LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY HALF_ADDER IS
    PORT (
        A, B : IN STD_LOGIC;
        SUM, CARRY_OUT : OUT STD_LOGIC
    );
END HALF_ADDER;

ARCHITECTURE halfAdderLogic OF HALF_ADDER IS
BEGIN
    SUM <= A XOR B;
    CARRY_OUT <= A AND B;
END halfAdderLogic;