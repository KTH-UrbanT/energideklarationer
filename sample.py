# Import the calculate_energy_class function from the module where it is defined
from energy_class import calculate_energy_class

# Example function calls to calculate energy classes with various inputs

# Example 1: Medium Small House (specified BBR and area)
print(calculate_energy_class('Småhus', 100, 120, 'BBR25'))  # Specific BBR standard and area

# Example 2: Large Office (specified BBR and area)
print(calculate_energy_class('Lokal', 75, 60, 'BBR29'))  # Specific BBR standard and area

# Example 3: Small Multi-Dwelling House (specified BBR, large area irrelevant)
print(calculate_energy_class('Flerbostadshus', 82, 200, 'BBR25'))  # Area provided but generally irrelevant for type

# Example 4: Very Small House (specified BBR, very small area)
print(calculate_energy_class('Småhus', 30, 40, 'BBR29'))  # Area less than the minimum defined, no specific requirement expected

# Example 5: Office with no area specified (uses default area handling, if any)
print(calculate_energy_class('Lokal', 80))  # No area or BBR standard provided, defaults should handle

# Example 6: Small House with no BBR specified (assumes default BBR)
print(calculate_energy_class('Småhus', 95, 85))  # No BBR standard provided, should use default
