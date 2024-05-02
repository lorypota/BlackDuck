import os
from enums import *
from license_analysis import perform_license_analysis
from components_analysis import perform_components_analysis
from fill_forms import fill_black_duck_form

SCAN_COMPONENTS: bool = bool(os.getenv('SCAN_COMPONENTS', False))
SCAN_LICENSES: bool = bool(os.getenv('SCAN_LICENSES', False))
BEARER_TOKEN: str = os.getenv('BEARER_TOKEN', '')
HEADERS = {"Authorization": "Bearer " + BEARER_TOKEN}
FORM_VALUE = {
    "22": Obligation.AGREE,
    "17": DistributionType.INTERNAL,
    "16": ComponentModified.NO,
    "13": Hosting.YES,
    "12": HostControl.ABB,
    "15": ComponentInteraction.DYNAMICALLY
}
SCAN_INFOS = {
    "Internal" : True,
    "Modification" : False,
    "Hosted" : True,
    "Host_control_ABB" : True, 
    # type of interaction is easy to get from blackduck
}
# dev version for all modules
MODULES = {
    "Matomo": {
        "id": "",
        "versionId": ""
    }
}

if __name__ == "__main__":
    if SCAN_COMPONENTS:
        print("Analyzing components...")
        perform_components_analysis(MODULES, HEADERS, SCAN_INFOS)
    else:
        if SCAN_LICENSES:
            print("Analyzing licenses...")
            perform_license_analysis(MODULES, HEADERS)
        else:
            print("Filling custom fields...")
            fill_black_duck_form(MODULES, HEADERS, FORM_VALUE)
