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
        allow_redirects=True,
        headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'cache-control': 'no-cache',
            'cookie': '__cfduid=dea9414996e53d713147114d4af7bb3be1584655525; __dtsu=6BB6E9D959C316AE53856BC7FEB0E602; __gads=ID=1c335eede1f36aac:T=1584660837:S=ALNI_MbURH8rnVeYCxRfHtQZNv_SV46Ffg; PHPSESSID=748893f11c2a679f9e7d31f619c30d68; sc_is_visitor_unique=rx12206630.1584994887.3F35EC07CC304FC088CB944FF518149F.4.4.3.3.3.3.3.2.1'
        }
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

