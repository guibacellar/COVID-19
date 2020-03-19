# Data Download Functions

import cv19_constants
import requests


def download_timeline_data() -> bool:
    """
    Download and Save all Timeline Data. Save data at data/alltimeline.json

    :return: True if Succeeded, otherwise False
    """

    print('[+} Download Timeline: ', end='')

    # Request Remote Data
    timeline_api_response: requests.request = requests.get(
        url=cv19_constants.TARGET_API,
        allow_redirects=True
    )

    # Decode
    decoded_content: str = timeline_api_response.content.decode(encoding='utf-8')

    # Basic Integrity Check
    if len(decoded_content) <= 100:
        print('FAILED. Invalid Response')
        print('****************************************')
        print(decoded_content)
        print('****************************************')
        return False

    # Save Data to Disk
    with open(cv19_constants.TARGET_TIMELINE_RAW_DATA, 'w') as file:
        file.write(decoded_content)
        file.flush()
        file.close()

    print('Completed')
    return True

