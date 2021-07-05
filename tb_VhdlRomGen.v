module tb_VhdlRomGen;

reg [3:0] addr;
wire [7:0] data;

initial begin
    $from_myhdl(
        addr
    );
    $to_myhdl(
        data
    );
end

VhdlRomGen dut(
    addr,
    data
);

endmodule
