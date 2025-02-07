module Not (
    input a,
    output out
);
    // Nand nand1(a, a, out);
    pmos p1(out, 1, a);
    nmos n1(out, 0, a);
    
endmodule