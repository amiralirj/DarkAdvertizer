#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" STEP TWO """

import requests


def login_step_get_stel_cookie(
        input_phone_number,
        tg_random_hash,
        tg_cloud_password,
        Proxy
):
    """Logins to my.telegram.org and returns the cookie,
    or False in case of failure"""
    request_url = "https://my.telegram.org/auth/login"
    request_data = {
        "phone": input_phone_number,
        "random_hash": tg_random_hash,
        "password": tg_cloud_password
    }
    response_c = requests.post(request_url, data=request_data,proxies=Proxy)
    #
    re_val = None
    re_status_id = None
    if response_c.text == "true":
        re_val = response_c.headers.get("Set-Cookie")
        re_status_id = True
    else:
        re_val = response_c.text
        re_status_id = False
    return re_status_id, re_val
