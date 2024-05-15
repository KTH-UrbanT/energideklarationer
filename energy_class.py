from data import CURRENT_BBR_STANDARD, ENERGY_CLASS_THRESHOLDS, ENERGY_CLASS_REQUIREMENTS

def calculate_energy_class(building_type,
                           pet,
                           atemp = None,
                           bbr_standard = CURRENT_BBR_STANDARD):
    
    building_type_requirements = ENERGY_CLASS_REQUIREMENTS[bbr_standard][building_type]
    requirement = fetch_requirement(building_type_requirements, atemp)

    if not requirement:
        return "No specific requirement"

    pet_requirement = requirement['pet_requirement']
    rate = (pet / pet_requirement) * 100 if pet_requirement else float('inf')

    return classify(rate)

def fetch_requirement(requirements, atemp):
    # Handle a single dictionary directly without list wrapping
    if isinstance(requirements, dict) and 'pet_requirement' in requirements:
        return requirements  # Assume the entire dict is the requirement if not in list form

    # Check if atemp is provided and if it fits the category's area constraints
    if atemp is not None:
        for category in requirements:
            if (category['max_area'] is None or atemp <= category['max_area']) and \
            (category['min_area'] is None or atemp > category['min_area']):
                return category
    else:
        # Find the category that corresponds to the largest buildings for the given building type and return it
        largest_category = None
        for category in requirements:
            # If atemp is None, track the category with the largest area range
            if category['max_area'] is None:
                # Assuming None for max_area implies the largest possible area
                largest_category = category
            elif largest_category is None or \
                (largest_category['max_area'] is not None and 
                category['max_area'] is not None and 
                category['max_area'] > largest_category['max_area']):
                largest_category = category

        # Return the largest category if atemp was not provided or no specific category matched
        return largest_category or 'No specific energy requirement found for the given building type and area.'

def classify(rate):
    for energy_class, threshold in ENERGY_CLASS_THRESHOLDS.items():
        if rate <= threshold:
            return energy_class
    return 'Unknown'  # In case no classification fits

