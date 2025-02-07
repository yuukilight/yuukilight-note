module Not (
    input a,
    output out
);
    Nand nand1(a, a, out);
    
endmodule