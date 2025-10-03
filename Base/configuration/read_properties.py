import configparser
import os

# aeye
BASE_DIR = str(os.path.dirname(os.path.dirname(__file__)))
config = configparser.RawConfigParser()
properties = configparser.RawConfigParser()
# base_path = str(BASE_DIR)
config.read(BASE_DIR + "//configuration//configs.ini")


class ReadConfig:

    @staticmethod
    def get_url(section, opt):
        url = config.get(section, opt)
        return url

    @staticmethod
    def get_username(section, opt):
        username = config.get(section, opt)
        return username

    @staticmethod
    def get_password(section, opt):
        password = config.get(section, opt)
        return password

    @staticmethod
    def get_expected_result(section, opt):
        expected_result = config.get(section, opt)
        return expected_result

    @staticmethod
    def get_invalid_email(section, opt):
        invalid_email = config.get(section, opt)
        return invalid_email

    @staticmethod
    def get_invalid_password(section, opt):
        invalid_password = config.get(section, opt)
        return invalid_password

    @staticmethod
    def get_unregistered_email(section, opt):
        unregistered_email = config.get(section, opt)
        return unregistered_email
