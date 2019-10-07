#!/bin/bash
import os
import platform
import logging
import pkg_resources
import urllib.request

logger = logging.getLogger()


def get_abs_path(relative):
    """
    relative = relative path with base at python/
    """
    return pkg_resources.resource_filename(__name__, relative)

FILE = get_abs_path('Redes e Beaglebones.xlsx')

url = 'http://10.0.38.42/streamdevice-ioc/Redes%20e%20Beaglebones.xlsx'
try:
    urllib.request.urlretrieve(url, FILE)
    logger.info('File {} updated.'.format(FILE))
except:
    logger.exception('Failed to update the spreadsheet from http://10.0.38.42/streamdevice-ioc/Redes%20e%20Beaglebones.xlsx ! Using old data ...')

IS_LINUX = (os.name == 'posix' or platform.system() == 'Linux')

ARCHIVER_URL = 'https://10.0.6.57/mgmt/ui/index.html'

ARGS_HIDE_ALL = ['--hide-nav-bar', '--hide-menu-bar', '--hide-status-bar']


DRAW_ALARMS_NO_INVALID_QSS = ''
with open(get_abs_path('css/draw_no-invalid.qss')) as f:
    DRAW_ALARMS_NO_INVALID_QSS = ''.join(f.readlines())

TABLE_ALARMS_QSS = ''
with open(get_abs_path('css/table-alarm.qss')) as f:
    TABLE_ALARMS_QSS = ''.join(f.readlines())

OVERVIEW_UI = get_abs_path('ui/overview.ui')


# Images
CNPEM_IMG = get_abs_path('images/CNPEM.jpg')
LNLS_IMG = get_abs_path('images/LNLS.png')
LTB_IMG = get_abs_path('images/ltb.png')
BOOSTER_IMG = get_abs_path('images/booster.png')
BTS_IMG = get_abs_path('images/btts.png')
STORAGE_RING_IMG = get_abs_path('images/storage_ring.png')
RINGB1A_IMG = get_abs_path('images/ringB1A.png')
RINGB2A_IMG = get_abs_path('images/ringB2A.png')