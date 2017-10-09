#!/usr/bin/env python
# -*- coding:utf-8 -*-

from task.search.cracker.gsxt_hebei_worker import GsxtHeBeiWorker


class GsxtSearchListHeBeiWorker(GsxtHeBeiWorker):
    def __init__(self, **kwargs):
        GsxtHeBeiWorker.__init__(self, **kwargs)

    def get_detail_html_list(self, seed, session, param_list):
        return len(param_list), []