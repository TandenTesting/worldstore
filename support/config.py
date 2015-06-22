import json

def logfile(configfile):
    with open(configfile) as json_file:
        test_conf = json.load(json_file)
        return test_conf['logfilename']