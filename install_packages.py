#!/usr/bin/env

import os
import json
import sys

#Load the given json file
#Run as: <python install_packages.py ip_packages.json>

failed = []
with open(sys.argv[1]) as dependency_file:
    data = json.load(dependency_file)
dependency = data.get('dependencies')

#Function to install relevant packages using pip utility
def install_packages(dependencies):
    failed_pkgs = []
    for pkg in dependencies:
        return_code = os.system('pip install ' + pkg)
        if return_code != 0:
            failed_pkgs.append(pkg)
        else:
            print("Success: " + pkg)
    return failed_pkgs


#If dependency is a valid package dependencies
if (dependency):
    print("Trying to install dependencies")
    failed += install_packages(dependency)

#Check for the failed packages
if (failed):
    print("Failed to install these packages")
    for pkg in failed:
        print(pkg)