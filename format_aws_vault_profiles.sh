#!/bin/bash

set -e

function fetch(){
    local aws_vault_path=${aws_vault_path:-/usr/local/bin/aws-vault}
    result=$(${aws_vault_path} list)
    if [[ $? -ne 0 ]]; then
        echo "error on running aws-vault list"
        echo "${result}" >&2
        exit 1
    fi
    echo "${result}"
}

function parse(){
    local aws_vault_result="$1"
    echo "${aws_vault_result}" | tail +3 | cut -f 1 -d' ' | grep -Ev '^-$'
}

function format_alfred(){
    local profiles="$1"
    local profiles_max_lines=$(echo -n "${profiles}" | grep -c '^')
    local i=0

    echo '{"items": ['
    for profile in ${profiles}; do
        cat << EOS
    {
        "uid": "${profile}",
        "title": "${profile}",
        "arg": "${profile}",
        "icon": {"path": "icon.png"},
        "autocomplete": "${profile}"
EOS
        i=$(( i+1 ))
        if [[ $i -eq $profiles_max_lines ]]; then
            echo '    }'
        else
            echo '    },'
        fi
    done
    echo ']}'

}

aws_vault_result=$(fetch)
profiles=$(parse "${aws_vault_result}")
format_alfred "${profiles}"