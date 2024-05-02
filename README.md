# Black Duck - Licenses Analysis

Script useful for Black Duck OSS Analysis. 2 main purposes:

- Create an Excel file containing all the licenses used with their rule_set (post scan analysis step)
- Autofill custom fields on Black Duck (post analysis step)

## Getting started

- Download from this _link redacted_ the Excel in which rule_set are defined and place it in the [oss](/oss/) folder
- Create and activate virtualenv (venv) with Python 3.9
- Install requirements: `(venv)$ pip install -r requirements.txt`
- In `__main__.py` fill in:
  - BEARER_TOKEN &rarr; get it from Black Duck
  - MODULES &rarr; insert project name, project id and verion id of the Black Duck projects that you want to analyze
  - FORM_VALUE &rarr; insert the values with which you want to fill-in Black Duck custom fields
- Run the project: `(venv)$ python __main__.py`
  - set SCAN_LICENSES = True to generate Excel file
  - set SCAN_LICENSES = False to autofill custom field

## Map for custom fields

- "22" : Obligation
- "17" : DistributionType
- "16" : ComponentModified
- "13" : Hosting
- "12" : HostControl
- "15" : ComponentInteraction
