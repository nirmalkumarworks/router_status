'''
Helper For man file
'''
# IMPORTS
import json
import os

# Store Path
config_path = "./store/data.json"

# Default Value in config
default_store_value = {
    "isActive" : 0 ,
    "connectedCount" : 0,
    "connectedData" : []
}

# Create Empty store file
def create_config():
    '''
    create a store config and update with default value
    :return: boolean
    '''
    try :
        with open(config_path , "w+") as store_file:
            json.dump(default_store_value, store_file)
        return True
    except Exception as e:
        print('ERR @create_config',e)
        return False

# Change Active
def get_data():
    '''
    Get the Data in the store
    :return: dictionary
    '''
    try:
        with open(config_path, "r") as store_fie:
            data = json.load(store_fie)

        return data

    except Exception as e:
        print('ERR @get_data',e)
        return None

# write to the store
def update_config(data : dict):
    '''
    Update the config
    :param data: All keys in config
    :return: boolean
    '''
    try :
        with open(config_path , "w") as store_file:
            json.dump(data, store_file)
        return True
    except Exception as e:
        print('ERR @update_config', e)
        return False

# Update the active status
def update_device_status(is_active : bool):
    '''
    Update the status of device
    :param is_active: true or false
    :return: boolean
    '''
    try:
        default_data = default_store_value.copy()
        if(is_active):
            default_data["isActive"] = 1
        update_config(default_data)
        return True
    except Exception as e:
        print('ERR @make_device_active', e)
        return False

# Update the connectedData
def update_device_connected_data(data : list):
    try:
        default_data = default_store_value.copy()
        default_data["isActive"] = 1
        default_data["connectedCount"] = len(data)
        default_data["connectedData"] = [dict(each_data) for each_data in data]
        update_config(default_data)
        return True
    except Exception as e:
        print('ERR @update_device_connected_data', e)
        return False

# Rename the connection file
def rename_store_file(file_store_name : str):
    try:
        if os.path.exists(config_path):
            os.rename(config_path, "data_"+str(file_store_name)+".json")
            print(f"Renamed")
        return True
    except Exception as e:
        print('ERR @rename_store_file', e)
        return False