from getgauge.python import before_spec, after_spec
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

@before_spec
def init():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
