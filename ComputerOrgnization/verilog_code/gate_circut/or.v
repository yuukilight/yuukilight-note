module Or(input a, b, output out);
    Not not1(a, na);
    Not not2(b, nb);

    Nand nand1(na, nb, out);
endmodule