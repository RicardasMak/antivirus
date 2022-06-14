import sys
import requests
import time


def query_vt(filtered_nslr, api_key):
    report = {}
    url_vt = 'https://www.virustotal.com/vtapi/v2/file/report'

    try:
        for i in range(len(filtered_nslr)):

            params = {
                'apikey': api_key,
                'resource': filtered_nslr[i]['MD5']
            }

            response = requests.get(url_vt, params=params)

            if response.status_code == 200:
                report[i] = response.json()
                time.sleep(15)


    except requests.exceptions.ConnectionError as error:
        print('Connection error: ', error)
    except requests.exceptions.HTTPError as error:
        print('HTTP error: ', error)
    except requests.exceptions.RequestException as error:
        print('Error: ', error)

    if report:
        return report
    else:
        print('something went wrong with Virus Total output')
        sys.exit(0)
