#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import time
import datetime

class Splitter:
    MAX_INTERVAL = 2 * 60 * 60
    
    def __init__(self, io):
        self.__io = io
        self.__date_ptn = re.compile('^(\d+/\d+ \d{2}:\d{2}:\d{2})\.\d{3}  ')

    def split(self, outdir=os.getcwd()):
        dt_now = datetime.datetime.now()
        prev_ts = None
        fd = None
        
        for line in self.__io:
            matched = self.__date_ptn.search(line)
            if matched is None: continue # not matched log format

            # parse date/time
            str_dt = '{0}/{1}'.format(dt_now.timetuple().tm_year,
                                      matched.group(1))
            dt = datetime.datetime.strptime(str_dt, '%Y/%m/%d %H:%M:%S')
            ts = time.mktime(dt.timetuple())

            # create a new file if not yet open a file or interval is too long
            if not prev_ts or prev_ts + Splitter.MAX_INTERVAL < ts:
                out_fname = dt.strftime('WoWCombatLog_%m%d_%H%M%S.txt')
                out_fpath = os.path.join(outdir, out_fname)
                fd = open(out_fpath, 'w')
                print('Created a new file: {0}'.format(out_fpath))

            prev_ts = ts
                
            if fd: fd.write(line)
                

if __name__ == '__main__':
    log_path = sys.argv[1]
    sp = Splitter(open(log_path, 'r'))
    sp.split(os.path.dirname(log_path))
