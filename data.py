import yaml

def load_boverket_requirements():
    with open('bbr/energy_requirements.yml', 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    
    # Convert string "float('inf')" to float('inf')
    for key, threshold in data['energy_class_thresholds'].items():
        if threshold == "float('inf')":
            data['energy_class_thresholds'][key] = float('inf')
    
    return data

REQUIREMENTS = load_boverket_requirements()
CURRENT_BBR_STANDARD = REQUIREMENTS['current_bbr']
ENERGY_CLASS_THRESHOLDS = REQUIREMENTS['energy_class_thresholds']
ENERGY_CLASS_REQUIREMENTS = REQUIREMENTS['energy_requirements']