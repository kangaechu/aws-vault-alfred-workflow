#!/usr/bin/env python3

import subprocess
import sys
import json
import os


def fetch():
    if 'aws_vault_path' in os.environ:
        aws_vault_path = os.environ['aws_vault_path']
    else:
        aws_vault_path = "/usr/local/bin/aws-vault"

    try:
        result = subprocess.run([aws_vault_path, "list"], stdout=subprocess.PIPE)
    except:
        print("error on running aws-vault list")
        sys.stderr.buffer.write(result.stdout)
        exit(1)

    return result.stdout.decode()


def parse(aws_vault_result):
    # skip first 2 lines (header)
    profiles = []
    for profile in aws_vault_result.splitlines()[2:]:
        if profile.split()[0] == '-':
            continue
        profiles.append(profile.split()[0])
    return profiles

def format_alfred(profiles):
    formatted_profiles = []
    for profile in profiles:
        formatted_profiles.append({
            "uid": profile,
            "title": profile,
            "arg": profile,
            "icon": {"path": "icon.png"},
            "autocomplete": profile
        })

    return json.dumps({"items" : formatted_profiles}, indent=2)

def run():
    aws_vault_result = fetch()
    profiles = parse(aws_vault_result)
    alfred_json = format_alfred(profiles)
    return alfred_json


if __name__ == '__main__':
    print(run())
