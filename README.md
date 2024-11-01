# Design-Check-of-the-Beam-wrt-IS-800-2007
This program performs a design check for beams based on IS 800:2007. The checks include moment capacity, shear capacity, and deflection to determine if the beam meets the required structural standards.

**Features**
Calculates design bending strength, shear capacity, and deflection.
Pass/Fail status for each check based on input values and the specifications from IS 800:2007.
Supports multiple test cases and generates results in a structured output file.


**Prerequisites**
Python 3.x

**Installation**
**Copy code**
git clone https://github.com/shubarya2912/design-check-beam-IS800-2007.git

**Usage**

Prepare Input File: The program reads input values from a file, e.g., beam_design_input.txt. You can either:
Use an existing file with the required input values.
Use the **[Beam Analysis Tool](https://github.com/shubarya2912/Beam-Analysis-Tool)** to generate an input file.

**Run the Program:**
Execute the program in Python.

**Copy code**
python beam_design_check.py

**Output**
Results are written to an output file (beam_design_output.txt), detailing the pass/fail status for each check per test case.

**Input Specifications**
The input file should include the following parameters for each test case:

Span (mm): The length of the beam.
Moment (kN·m): The applied moment on the beam.
Shear Force (kN): The applied shear force on the beam.
Yield Strength (fy) (MPa): The yield strength of the material.
Section Modulus (Z) (mm³): The section modulus.
Moment of Inertia (I) (mm⁴): The moment of inertia of the section.
Cross-sectional Area (A) (mm²): The cross-sectional area.

**Note**
The values of **gamma_m0** and **P** can be adjusted based on the specific beam section type.
File names** (beam_design_input.txt and beam_design_output.txt)** are named considering the use of the **Beam Analysis Tool** to generate the input file.


**Example Input**
The input file should be formatted as follows:
Copy code
Test Case 1:
Span: 5000
Moment: 20
Shear Force: 5
Yield Strength: 250
Section Modulus (Z): 500
Moment of Inertia (I): 2000
Cross-sectional Area (A): 300

**Example Output**
The output file will contain results in the following format:
Copy code
**Results for Test Case 1:**
Moment Capacity Check:
  Applied Moment (kN·m): 20
  Moment Capacity (kN·m): 30
  Status: Pass
**
Shear Capacity Check:**
  Applied Shear Force (kN): 5
  Shear Capacity (kN): 6
  Status: Pass

**Deflection Check:**
  Calculated Deflection (mm): 4
  Permissible Deflection (mm): 20
  Status: Pass


License
None






