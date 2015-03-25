# -*- coding: utf-8 -*-
import os
import re

PAGE_SIZE = int(os.sysconf("SC_PAGE_SIZE") / 1024)

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
    with open("/proc/" + str(pid) + "/stat", "rt") as fd:
        return dict(zip(NAMES, fd.readline().split()))

def get_pids():
    """Findout all processes PIDs"""
    _, dirnames, _ = list(os.walk("/proc"))[0]
    return filter(lambda x: re.match('^\d+$', x) is not None, dirnames)

def get_stats(pids):
    """Reads stat's of all processes in the system"""
    return [get_stat(pid) for pid in pids]

def get_childs(pid, stats):
    """Build stats for all childs of the process"""
    pid_str = str(pid)
    childs = []
    for stat in stats:
        if pid_str == stat["ppid"]:
            childs.append(stat)
            childs += get_childs(stat["pid"], stats)

    return childs

if __name__ == "__main__":
    stats = get_stats(get_pids())
    print(["pid:{0} rss:{1}".format(process["pid"], int(process["rss"]) * PAGE_SIZE) for process in get_childs(1, stats)])
