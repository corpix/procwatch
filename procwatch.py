#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import datetime
import time
import psutil

if len(sys.argv) < 3 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    sys.stderr.write("Usage:\nprocwatch.py <pid> <format_string>\n")
    sys.exit(1)

pid = int(sys.argv[1])
format_string = sys.argv[2]
process = psutil.Process(pid=pid)

def children(process, *args, **kwargs):
    if psutil.version_info < (2, 0, 0,):
        return process.get_children(*args, **kwargs)
    else:
        return process.children(*args, **kwargs)

for proc in [process] + children(process, recursive=True):
    try:
        sys.stdout.write(
            str(eval(
                format_string,
                {
                    "datetime": datetime,
                    "os": os,
                    "sys": sys,
                    "time": time,
                    "psutil": psutil,
                    "proc": proc,
                }
            )) + "\n"
        )
    except psutil.NoSuchProcess:
        pass
