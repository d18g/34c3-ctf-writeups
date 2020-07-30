># hardotp 
>
> This is a hard challenge :)
> 
> I intercepted a message: **2FED5B7FEB81D3C44E39E4AEA346010240E0CBBB** 
> 
> I know the hardware used. See [schematic](schematic.png) for an overview. Someone sent me this [PRNG](prng.bin)
# Solution - TL;DR

1. Look at the schematics, find out about [IceStorm](http://www.clifford.at/icestorm/) an opensource project for iCE40 FPGAs.
2. Get a verilog representation of the bitstream using IceStorm.
3. Notice that there are only 256 internal states.
4. Profit.
