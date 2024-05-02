import re
import time
from tqdm import tqdm
from black_duck_api import *


def get_component_versions(component):
    # extract UUID from url
    pattern = '/components/([0-9a-f-]+)/versions/([0-9a-f-]+)'
    return re.findall(pattern, component['componentVersion'])[0]


def fill_black_duck_form(modules: dict, headers: dict, form_values: dict):
    for module_name, module_info in modules.items():
        resp = get_project_components(
            api_headers=headers, project_id=module_info['id'], version_id=module_info['versionId'])
        if 'errorMessage' in resp:
            print(
                f"Error on get components for {module_name}: {resp['errorMessage']}")
        else:
            for index, component in enumerate(tqdm(
                    resp["items"],
                    desc=module_name.ljust(15),
                    bar_format="{l_bar}{bar:50}{r_bar}{bar:-50b}", 
                    ascii=True)):
                component_id, component_version_id = get_component_versions(component)

                resp = set_black_duck_custom_fields(headers, module_info['id'], module_info['versionId'], component_id, component_version_id, form_values)
                if 'errorMessage' in resp:
                    print(
                        f"Error on set custom field for component {component['componentName']}: {resp['errorMessage']}")
                time.sleep(0.5)
