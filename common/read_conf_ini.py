import configparser
import os
current = os.path.dirname(__file__)
config_path = os.path.join(current,'../conf/conf.ini')
class ReadConf:
    def __init__(self,config_path):
        self.config_path = config_path
    def read_conf_url(self):
        config = configparser.ConfigParser()
        config.read(self.config_path,encoding='utf-8')
        return config.get('url','url')

    def read_conf_username(self):
        config = configparser.ConfigParser()
        config.read(self.config_path,encoding='utf-8')
        return config.get('username','username')

    def read_conf_password(self):
        config = configparser.ConfigParser()
        config.read(self.config_path,encoding='utf-8')
        return config.get('password','password')

    def read_conf_jira(self):
        config = configparser.ConfigParser()
        config.read(self.config_path,encoding='utf-8')
        return config.get('url','jira')

    def read_conf_jirausername(self):
        config = configparser.ConfigParser()
        config.read(self.config_path,encoding='utf-8')
        return config.get('username','jirausername')

    def read_conf_jirapassword(self):
        config = configparser.ConfigParser()
        config.read(self.config_path,encoding='utf-8')
        return config.get('password','jirapassword')