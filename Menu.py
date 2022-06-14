#!/usr/bin/env python3

import os.path
import sys
import pkg
import argparse
import re


# Linux OS Regex to check users input, on match return true, on false will exit program
def regular_expression(path, key, output):

    if re.search(r'^[/]+', path) and re.search(r'[a-zA-Z0-9]{64}', key) and re.search(r'(/)+[a-zA-Z0-9\\-_/ ]*(.txt)',
                                                                                      output):
        if os.path.isdir(path):
            return True

    print('wrong input')
    sys.exit()


# takes in user input and if match regex will proces further
def argument_parser():
    try:
        parser = argparse.ArgumentParser(description="""This program will walk through all file in given path. 
                                                     After all files find it will extrack MD5 hash value and
                                                     filter in NSLR database. The hash values which was not found
                                                     in NSLR will be processed with Virus Total and will output
                                                     full report into the file.""")

        parser.add_argument('-p', '--path', required=True, help="require path of the folder to scanned")
        parser.add_argument('-k', '--key', required=True, help="takes in Virus Total api key")
        parser.add_argument('-o', '--output', required=True, help="path to file.txt where report will be output")

        args = parser.parse_args()

    except argparse.ArgumentParser as error:
        print('error in argument parsing: ', error)

    if regular_expression(args.path, args.key, args.output):
        return args.path, args.key, args.output


path, api_key, output_path = argument_parser()

print('Scanning...')

# Will search for all files in given path and will return dictionary with file, path to the file and MD5 value
files = pkg.scan_file_system(path)

# Filter files in NSRL, removes files from dictionary which were found and returns filtered dictionary
filtered_nslr = pkg.query_nsrl(files)

# Returns report from vt for each file after nsrl check
vt_report = pkg.query_vt(filtered_nslr, api_key)

# Generate report
pkg.report(vt_report, filtered_nslr, output_path)

print(str(len(vt_report)), 'suspicious files was found. Report is available at', output_path)
