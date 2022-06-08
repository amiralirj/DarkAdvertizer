#!/usr/bin/env python

""" STEP ONE """

import requests


def request_tg_code_get_random_hash(input_phone_number,Proxy):
    """ requests Login Code
    and returns a random_hash
    which is used in STEP TWO """
    request_url = "https://my.telegram.org/auth/send_password"
    request_data = {
        "phone": input_phone_number
    }
    response_c = requests.post(request_url, data=request_data,proxies=Proxy)
    json_response = response_c.json()
    return json_response["random_hash"]
