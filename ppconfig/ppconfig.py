# -*- coding: utf-8 -*-
"""Configuration helper

Author: Peter Pakos <peter.pakos@wandisco.com>

Copyright (C) 2018 WANdisco

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import, print_function

import os
import logging

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

log = logging.getLogger(__name__)


class Config(object):
    def __init__(self, config_file, config_dir=None):

        if config_dir:
            self._config_dir = config_dir
        else:
            self._config_dir = os.path.expanduser(os.environ.get('XDG_CONFIG_HOME', '~/.config'))

        self._config_path = os.path.join(self._config_dir, config_file)

        if not os.path.isfile(self._config_path):
            msg = 'Config file not found: %s' % self._config_path
            log.error(msg)
            raise IOError(msg)

        log.debug('Loading configuration from: %s' % self._config_path)
        self._config = configparser.ConfigParser()
        self._config.read(self._config_path)

    def get(self, name, section='default'):
        if not self._config.has_section(section):
            msg = 'Config file %s has no section: %s' % (self._config_path, section)
            log.error(msg)
            raise NameError(msg)
        if self._config.has_option(section, name):
            log.debug('Read: %s.%s' % (section, name))
            return self._config.get(section, name)
        else:
            msg = 'Config file %s has no entry: %s.%s' % (self._config_path, section, name)
            log.error(msg)
            raise NameError(msg)
