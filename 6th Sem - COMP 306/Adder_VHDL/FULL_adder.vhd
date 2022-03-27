LIBRARY library IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY FULL_ADDER IS
    PORT (
        A, B, CARRY_IN : IN STD_LOGIC;
        SUM, CARRY_OUT : OUT STD_LOGIC
    );
END ENTITY;

