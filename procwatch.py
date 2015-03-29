#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import datetime
import time

# /proc/[pid]/stat fields as specified in https://github.com/torvalds/linux/blob/a0c2e07d6d4fe6f67b057d0f1c961e70ff581eda/fs/proc/array.c#L445
# MAN proc(5) http://man7.org/linux/man-pages/man5/proc.5.html
# Please, read manual page before reporting any bugs.

NAMES = (
    "pid",           "comm",
    "state",         "ppid",
    "pgrp",          "session",
    "tty_nr",        "tpgid",
    "flags",         "minflt",
    "cminflt",       "majflt",
    "cmajflt",       "utime",
    "stime",         "cutime",
    "cstime",        "priority",
    "nice",          "num_threads",
    "itrealvalue",   "starttime",
    "vsize",         "rss",
    "rsslim",        "startcode",
    "endcode",       "startstack",
    "kstkesp",       "kstkeip",
    "signal",        "blocked",
    "sigignore",     "sigcatch",
    "wchan",         "nswap",
    "cnswap",        "exit_signal",
    "processor",     "rt_priority",
    "policy",        "delayacct_blkio_ticks",
    "guest_time",    "cguest_time",
    "start_data",    "end_data",
    "start_brk",     "arg_start",
    "arg_end",       "env_start",
    "env_end",       "exit_code",
)

def get_stat(pid):
    """Get /proc/[pid]/stat contents and repack it into dict"""
    try:
        with open("/proc/" + str(pid) + "/stat", "rt") as fd:
            return dict(zip(NAMES, fd.readline().split()))
    except Exception as e:
        return None

def get_pids():
    """Findout all processes PIDs"""
    _, dirnames, _ = list(os.walk("/proc"))[0]
    return filter(lambda x: re.match('^\d+$', x) is not None, dirnames)

def get_stats(pids):
    """Read stat's of all pids"""
    return filter(lambda x: x is not None, [get_stat(pid) for pid in pids])

def get_childs(pid, stats):
    """Build stats for all childs of the pid"""
    pid_str = str(pid)
    childs = []
    for stat in stats:
        if pid_str == stat["ppid"]:
            childs.append(stat)
            childs += get_childs(stat["pid"], stats)

    return childs

SYSTEM = {
    "page_size": int(os.sysconf("SC_PAGE_SIZE"))
}

if __name__ == "__main__":
    stats = get_stats(get_pids())
    if len(sys.argv) < 3 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        sys.stderr.write("Usage:\nprocwatch.py <pid> <format_string>\n")
        sys.exit(1)

    pid = sys.argv[1]
    template = sys.argv[2]
    for stat in list(get_stats([pid])) + get_childs(pid, stats):
        data = {
            "stat": stat,
            "system": SYSTEM
        }
        sys.stdout.write(
            str(eval(
                template.format(**data),
                {"datetime": datetime, "os": os, "sys": sys, "time": time}
            )) + "\n"
        )
