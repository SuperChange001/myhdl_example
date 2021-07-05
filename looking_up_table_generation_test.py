from myhdl import *

@block
def VhdlRomGen(addr, data):

    # Create the ROM container
    rom = [Signal(intbv(0)[8:]) for ii in range(2**4)]

    # Initialize ROM, any value, any complex python can
    # be in this initialization code.
    for ii in range(len(rom)):
        rom[ii] = ii

    rom = tuple(rom)

    @always_comb
    def rtl_rom():
        data.next = rom[int(addr)]


    return rtl_rom

if __name__ == "__main__":
    addr = Signal(intbv(0)[4:])
    data = Signal(intbv(0)[8:])

    # toVHDL(VhdlRomGen, addr, data)
    vhdlRomGen1 = VhdlRomGen(addr, data)
    vhdlRomGen1.convert('VHDL')