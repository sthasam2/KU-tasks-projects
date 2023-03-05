LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY HALF_ADDER IS
    PORT (
        A, B : IN STD_LOGIC;
        SUM, CARRY_OUT : OUT STD_LOGIC);
END HALF_ADDER;

ARCHITECTURE structure OF HALF_ADDER IS

    COMPONENT XOR_gate IS
        PORT (
            I1, I2 : IN STD_LOGIC;
            O1 : OUT STD_LOGIC);
    END COMPONENT;

    COMPONENT AND_gate IS
        PORT (
            I1, I2 : IN STD_LOGIC;
            O1 : OUT STD_LOGIC);
    END COMPONENT;

BEGIN
    u1 : XOR_gate PORT MAP(I1 => A, I2 => B, O1 => SUM);
    u2 : AND_gate PORT MAP(I1 => A, I2 => B, O1 => CARRY_OUT);
END structure;