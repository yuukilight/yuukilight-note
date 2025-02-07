module Nor(input a, b, output out);
    Not not1(a, na);
    Not not2(b, nb);

    Nand nand1(na, nb, o1);
    Not not3(o1, out);
endmodule