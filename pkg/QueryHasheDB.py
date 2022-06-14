import sys
import urllib.error
from urllib import request


def query_nsrl(files):
    try:
        for i in range(len(files)):
            resp = request.urlopen(
                'http://nsrl.hashsets.com/national_software_reference_library_list.php?q=(MD5~equals~%s)' % files[i][
                    'MD5'])
            html = resp.read().decode('utf-8')
            found = str.__contains__(html, 'No results found.')

            # removes index from file dictionary if MD5 have been found in NSRL
            if not found:
                del files[i]

    except urllib.error.HTTPError as error:
        print('HTTP error: ', error)
    except urllib.error.URLError as error:
        print('URL error:', error)

    if files:
        return files
    else:
        print('all files matched in NSRL and no future process is needed')
        sys.exit(0)
