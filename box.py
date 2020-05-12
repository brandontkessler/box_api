import json
import os
from boxsdk import JWTAuth, Client

class BoxAPI:
    """Class for working with the Box API

    Usage:
    Within flask, this should be initiated upon booting up the server, maybe in the
        config file:

    >>> from box_api import box
    >>> box = box.BoxAPI()

    Using within a file would be like:

    >>> from config import box
    >>> folder = box.client.folder(folder_id='112116079195').get_items()
    >>> item = box.client.file('660573631005').get()
    >>> item_content = item.content()
    >>> print(item_content)

    """

    def __init__(self):
        self.client = None
        self.setup()

    ############## HIDDEN METHODS ################
    @staticmethod
    def get_config():
        prod_config_path = './creds/box_api_config.json'
        if os.path.exists(prod_config_path):
            config_path = prod_config_path
        else:
            config_path = 'config/box_creds.json'

        with open(config_path) as f:
            config_data = json.load(f)
            return config_data

    def setup(self):
        config_dict = self.get_config()
        config = JWTAuth.from_settings_dictionary(config_dict)
        self.client = Client(config)


    ############### USER METHODS #################
    def check_folder(self, folder_id='0'):
        """Allows seeing items inside of folder with provided ID
        Root folder is default with ID of '0'
        ID is a string, not an integer
        """
        folder = self.client.folder(folder_id).get_items()
        for item in folder:
            print(item.name, item.id, item.object_type)
        return
