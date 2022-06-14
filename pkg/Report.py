# writes report of VT findings
def report(vt_report, nsrl_report, output_path):
    count = 0
    not_found_vt = {}

    try:
        write_file = open(output_path, 'w')

        write_file.write('File was detected by Virus Total')

        for n in range(len(nsrl_report)):
            for i in range(len(vt_report)):

                if 'md5' in vt_report[i]:
                    if vt_report[i]['md5'] == nsrl_report[n]['MD5']:
                        write_file.write('\n')
                        write_file.write('\nName: ' + nsrl_report[n]['name'])
                        write_file.write('\nPath: ' + nsrl_report[n]['path'])
                        write_file.write('\nMD5: ' + nsrl_report[n]['MD5'])
                        write_file.write('\n')
                        write_file.write('\nVirus Total Report:')
                        write_file.write('\n')
                        write_file.write('\nVendors Identified as Malware'
                                         ': ' + str(vt_report[i]['positives']))
                        write_file.write('\nFull Report: ' + vt_report[i]['permalink'])
                        write_file.write('\nScan Date: ' + vt_report[i]['scan_date'])
                        write_file.write('\n')

                elif 'resource' in vt_report[i]:
                    if vt_report[i]['resource'] == nsrl_report[n]['MD5']:

                        not_found_vt[count] = {'name': nsrl_report[n]['name'],
                                               'path': nsrl_report[n]['path'],
                                               'MD5': nsrl_report[n]['MD5']
                                               }

                        count += 1

        write_file.close()

        if not_found_vt:
            not_found(not_found_vt, output_path)

    except IOError as error:
        print('Error on writing: ', error)


# write report of files which was filed by VT
def not_found(not_found_vt, output):

    try:
        write_file = open(output, 'a')

        write_file.write('\nFiles that was not found by VT and might need further investigation:')

        for i in range(len(not_found_vt)):

            write_file.write('\n')
            write_file.write('\nName: ' + not_found_vt[i]['name'])
            write_file.write('\nPath: ' + not_found_vt[i]['path'])
            write_file.write('\nMD5: ' + not_found_vt[i]['MD5'])

        write_file.close()

    except IOError as error:
        print('error on writing: ', error)
