# -*- coding: utf-8 -*-
"""Design Check of the Beam wrt IS 800:2007

"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
from google.colab import files



"""**Design Check For Beams **"""

import math

# Constants and design factors from IS:800:2007
E = 200000  # Modulus of elasticity in MPa (for steel)
gamma_mo = 1.1  # Partial safety factor for material strength

def read_input(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()

    # Process data to handle multiple test cases
    inputs_list = []
    inputs = {}

    for line in data:
        if "Test Case" in line:
            if inputs:
                inputs_list.append(inputs)
                inputs = {}
        elif line.strip():
            key, value = line.strip().split(':')
            # Remove any units from the value
            value = ''.join(filter(lambda x: x.isdigit() or x == '.', value.strip()))  # Keep digits and decimal points
            inputs[key.strip()] = float(value)  # Convert to float after stripping units

    if inputs:  # Add the last case if any
        inputs_list.append(inputs)

    return inputs_list

def moment_capacity_check(Z, fy, P):
    # Calculate design bending strength (Md)
    Md = Z * fy * (1 + P / gamma_mo)  # Moment capacity in kN·m
    return Md

def shear_capacity_check(shear_force, area, fy):
    Vd = 0.6 * area * fy / gamma_mo  # Shear capacity in kN
    return Vd, Vd >= shear_force

def deflection_check(span, moment, I):
    delta = (5 * moment * span**2) / (48 * E * I)  # Deflection in mm
    max_deflection = span / 250  # Typical permissible limit (span/250) in mm
    return delta, delta <= max_deflection

def design_flexural_member(inputs):
    span = inputs["Span"]  # mm
    moment = inputs["Moment"]  # kN·m
    shear_force = inputs["Shear Force"]  # kN
    fy = inputs["Yield Strength"]  # MPa
    Z = inputs["Section Modulus (Z)"]  # mm³
    I = inputs["Moment of Inertia (I)"]  # mm⁴
    area = inputs["Cross-sectional Area (A)"]  # mm²

    # Assuming P is determined based on section type
    P = 1.0  # Adjust based on the section type (plastic/compact or semi-compact)

    results = {}

    # Moment capacity check
    Md = moment_capacity_check(Z, fy, P)
    moment_limit = 1.2 * Z * fy / gamma_mo  # Limit for simply supported beams
    moment_status = Md <= moment and Md < moment_limit  # Check both conditions

    results['Moment Capacity Check'] = {
        'Applied Moment (kN·m)': moment,
        'Moment Capacity (kN·m)': Md,
        'Status': 'Pass' if moment_status else 'Fail'
    }

    # Shear capacity check
    Vd, shear_status = shear_capacity_check(shear_force, area, fy)
    results['Shear Capacity Check'] = {
        'Applied Shear Force (kN)': shear_force,
        'Shear Capacity (kN)': Vd,
        'Status': 'Pass' if shear_status else 'Fail'
    }

    # Deflection check
    delta, deflection_status = deflection_check(span, moment, I)
    results['Deflection Check'] = {
        'Calculated Deflection (mm)': delta,
        'Permissible Deflection (mm)': span / 250,
        'Status': 'Pass' if deflection_status else 'Fail'
    }

    return results

def write_output(results_list, file_path):
    with open(file_path, 'w') as f:
        for i, results in enumerate(results_list, 1):
            f.write(f"Results for Test Case {i}:\n")
            for check, details in results.items():
                f.write(f"{check}:\n")
                for key, value in details.items():
                    f.write(f"  {key}: {value}\n")
                f.write("\n")
            f.write("\n")  # Separate test cases with a blank line

if __name__ == "__main__":
    try:
        inputs_list = read_input('beam_design_input.txt')
        results_list = [design_flexural_member(inputs) for inputs in inputs_list]
        write_output(results_list, 'beam_design_output.txt')
        print("Output file 'beam_design_output.txt' has been created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
from google.colab import files
files.download('beam_design_output.txt')