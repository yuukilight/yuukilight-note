`include "nand.v"
`include "not.v"

module moduleName;
    reg a;
    wire out;
    Not obj(a, out);

    initial begin
        a = 0;
        #10 a = 1;
    end

    initial begin
        $monitor("a=%d out=%d \n", a, out);
    end
    
endmodule