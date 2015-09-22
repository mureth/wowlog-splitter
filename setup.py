#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import distutils
import cx_Freeze

base = None
pkg_name    = 'WowlogSpliter'
pkg_version = '0.1.0'
pkg_url = 'https://github.com/mureth/wowlog-splitter'
upgrade_code = '2774175E-9188-4C33-9960-0948C66A9718'
programfiles_dir = 'ProgramFiles64Folder' if distutils.util.get_platform() == 'win-amd64' else 'ProgramFilesFolder'
icon = 'images/icon.ico'

pkg_includes = ['re']

build_exe_options = {
    'packages': ['os'],
    'includes': pkg_includes,
    'compressed'   : True
}

bdist_msi_options = {
    'upgrade_code': upgrade_code,
    'add_to_path': False,
    'initial_target_dir': '[%s]\%s' % (programfiles_dir, pkg_name)
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options,
}

splitter_exe = cx_Freeze.Executable(
    'splitter.py',
    base = base,
    icon = icon,
    copyDependentFiles = True,
    shortcutName="WowlogSplitter",
    shortcutDir="DesktopFolder"
)


cx_Freeze.setup(
    name=pkg_name,
    version=pkg_version,
    url=pkg_url,
    options=options,
    executables=[splitter_exe]
)

