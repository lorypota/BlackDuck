import requests
import json

BASE_URL = 'https://abb.app.blackduck.com'
QUERY_PARAMS = '?limit=9999&offset=0&sort=projectName%20ASC'
CUSTUM_FIELD_VALUE_URL = BASE_URL + '/api/custom-fields/objects/bom-entry/fields'


def generate_payload(url: str, values: dict) -> dict:
    payload = {"fields": []}
    for field, enum in values.items():
        num_value = enum.value
        custom_field = f'{url}/{field}'
        custom_field_values = f'{CUSTUM_FIELD_VALUE_URL}/{field}/options/{num_value}'
        payload["fields"].append({
            "customField": custom_field,
            "values": [custom_field_values]
        })
    return payload


def get_project_components(api_headers: dict, project_id: str, version_id: str) -> dict:
    api = f'/api/projects/{project_id}/versions/{version_id}/components'
    url = BASE_URL + api + QUERY_PARAMS
    resp = requests.get(url=url, headers=api_headers)
    return json.loads(resp.content)


def set_black_duck_custom_fields(api_headers: dict, project_id: str, project_version_id: str, component_id: str, component_version_id: str, values: dict):
    headers = api_headers.copy()  # by value and not by reference
    headers["Content-type"] = "application/json"
    headers["Accept"] = "application/json"
    api = f'/api/projects/{project_id}/versions/{project_version_id}/components/{component_id}/versions/{component_version_id}/custom-fields'
    url = BASE_URL + api
    payload = generate_payload(url, values)
    resp = requests.put(url=url, headers=api_headers, json=payload)
    return json.loads(resp.content)

# Function below is to test more depth, maybe blackDuck doesn't allow for the deletion of custom_fields
def delete_black_duck_custom_fields(api_headers: dict, project_id: str, project_version_id: str, component_id: str, component_version_id: str):
    headers = api_headers.copy()  # by value and not by reference
    headers["Content-type"] = "application/json"
    headers["Accept"] = "application/json"
    api = f'/api/projects/{project_id}/versions/{project_version_id}/components/{component_id}/versions/{component_version_id}/custom-fields'
    url = BASE_URL + api
    resp = requests.delete(url=url, headers=api_headers)
    return json.loads(resp.content)