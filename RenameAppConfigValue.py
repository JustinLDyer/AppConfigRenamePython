import xml.etree.ElementTree as ET
from pathlib import Path

def change_config_value(file_path, key_name, new_value):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        app_settings_section = root.find('appSettings')
        if app_settings_section is not None:
            key_name_found = False
            for add_tag in app_settings_section.findall('add'):
                if add_tag.get('key') == key_name:
                    add_tag.set('value', new_value)
                    key_name_found = True
                    break

            if key_name_found:
                tree.write(file_path)
                print(f"Successfully set {key_name} to {new_value} in {file_path}")
            else:
                print(f"{key_name} not found in appSettings section of {file_path}")
        else:
            print(f"Fatal error. appSettings section not found in {file_path}.")
    except Exception as ex:
        print(f"The following exception occurred: {ex}")
    
if __name__ == "__main__":
    while True:
        file_path = input("Enter the name/path of the config file you want to modify. ")
        if Path(file_path).exists():
            break
        else:
            print("Specified file does not exist.")

    while True:
        key_name = input("Enter the key name of the appSetting you want to modify. ")
        if (key_name.isalnum()):
            break
        else:
            print("Key name must be alphanumeric.")

    while True:
        key_value = input(f"Enter the value you want for the appSetting {key_name}. ")
        if (key_value.isalnum()):
            break
        else:
            print("Key value must be alphanumeric.")

    change_config_value(file_path, key_name, key_value)