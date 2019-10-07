#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pkg_resources

def get_abs_path(filename):
    return pkg_resources.resource_filename(__name__, filename)

PCTRL_MAIN = get_abs_path('main.py')
PCTRL_UI = get_abs_path('ui/main.ui')
