#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import requests
from requests.exceptions import RequestException


def requestor(result):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    HOST = result.Host
    START = result.start
    END = result.end
    LOGIN = result.login
    PASSWORD = result.password

    for i in range(start, end):
        # Sample CURL
        ## curl curl -k -X PUT -u 'firemon:firemon' S--header 'Content-Type: application/json' --header 'Accept: application/json' 'https://IP.ADDRESS/securitymanager/api/rev/1/nd/restart'
        try:
            requests.put('https://{}/securitymanager/api/rev/{}/nd/restart'.format(HOST, i),
                                headers=headers,
                                verify=False,
                                auth=(LOGIN, PASSWORD))
        except RequestException as e:
            print('Connection error: {}'.format(e))
            sys.exit(1)

    # Sample CURL
    ## curl curl -k -X PUT -u 'firemon:firemon' --header 'Content-Type: application/json' --header 'Accept: application/json' 'https://IP.ADDRESS/securitymanager/api/rev/interrupted/requeue'
    try:
        requests.put('https://{}/securitymanager/api/rev/interrupted/requeue'.format(host),
                            headers=headers,
                            verify=False,
                            auth=(LOGIN, PASSWORD))
    except RequestException as e:
        print('Connection error: {}'.format(e))
        sys.exit(1)


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--Host", type=str,
                        help="Host",
                        required=True)
    parser.add_argument("-l", "--login", type=str,
                        help="login",
                        required=True)
    parser.add_argument("-p", "--password", type=str,
                        help="password",
                        required=True)
    parser.add_argument("-s", "--start", type=int,
                        help="start",
                        required=True)
    parser.add_argument("-e", "--end", type=int,
                        help="end",
                        required=True)

    result = parser.parse_args()

    return result


if __name__ == "__main__":

    requestor(args())