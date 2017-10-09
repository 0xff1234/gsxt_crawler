#!/usr/bin/env python
# encoding: utf-8
"""
@author: youfeng
@email: youfeng243@163.com
@license: Apache Licence
@file: http_proxy.py
@time: 2017/7/23 10:41
"""

# -*- coding: utf-8 -*-
from contextlib import closing

import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.before_request
def before_request():
    url = request.url
    method = request.method
    data = request.data or request.form or None
    headers = dict()
    for name, value in request.headers:
        if not value or name == 'Cache-Control':
            continue
        headers[name] = value

    with closing(requests.request(method, url, headers=headers, data=data, stream=True)) as r:
        resp_headers = []
        for name, value in r.headers.items():
            if name.lower() in ('content-length', 'connection',
                                'content-encoding'):
                continue
            resp_headers.append((name, value))
        return Response(r, status=r.status_code, headers=resp_headers)


app.run(port=8007, debug=True)
