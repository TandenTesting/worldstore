import json

class environment:
    def __init__(self, env):
        with open(env) as json_file:
            self.environment_info = json.load(json_file)

    def get_testenv(self):
        return self.environment_info['environment']

    def thinktime(self, waitfor = None):
        self.time_waited=0.0
        if self.environment_info['thinktime']['status'].lower == "on":
            if waitfor == None or 0 > waitfor<=30:
                waitfor = self.environment_info['thinktime']['delay']
            print (waitfor)
        else:
            logging.info('Skipping thinktime: disabled in config')
        return self.time_waited