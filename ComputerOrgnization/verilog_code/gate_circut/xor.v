module Xor(input a, b, output out);
    Nand nand1(a, b, o1);

    Nand nand2(o1, a, o1_a);
    Nand nand3(o1, b, o1_b);

    Nand nand4(o1_a, o1_b, out);
endmodule