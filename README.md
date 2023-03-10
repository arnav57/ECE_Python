## ECE_Python / Circuits
_Contains useful methods and classes to make analyzing circuits easier_

CHANGELIST:  
- **1.0** - Initial commit
- **1.01** - Added `Amplifier` class definition. Method creates an equivalent voltage amplifier out of any of the 4 model types: "voltage", "current", "transresistance", "transconductance". `output()` method returns a tuple containing a (voltage_source, output_resistance) to be cascaded or voltage divided upon.
- **1.02** - Added `toNorton()` and `toThevenin()` methods to convert one equivalent type to another using the concept of source transformations.
- **1.03** - Added `gain_vi()` and `gain_power()` methods to return unit/unit gain, or decibel gain if given db=True in the method argument.
---
