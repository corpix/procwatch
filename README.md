### procwatch
---------------------

Simple library of functions that helps me keep track of the process `stat` metrics in the system(`/proc/[pid]/stat`).

Basicaly this library is just a "thin client" for `/proc/[pid]/stat`.

It could be a good idea to go and read [this](http://man7.org/linux/man-pages/man5/proc.5.html) manpage about `/proc/[pid]/stat` and other files in `/proc` file system.

#### API

  - `get_stat(pid)` Get /proc/[pid]/stat contents and repack it into dict
  - `get_pids()` Findout all processes PIDs
  - `get_stats(pids)` Read stat's of all pids
  - `get_childs(pid, stats)` Build stats for all childs of the pid

#### Example:
```python
import procwatch
stats = procwatch.get_stats(procwatch.get_pids())
for stat in procwatch.get_childs(1, stats):
    print(stat["pid"], stat["state"])
```

#### External usage

This script sould be called from outside with string representing output format for stat's.

Usage:
```
procwatch.py <pid> <format_string>
```

Any valid Python expression could be passed `<format_string>`.

Example:
```bash
$ python procwatch.py 1 'datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\tpid:{stat[pid]}\trss:{stat[rss]}%s" % ({stat[rss]} * {system[page_size]})'
29.03.2015 03:09:42     pid:107         rss:10309632
29.03.2015 03:09:42     pid:143         rss:3399680
29.03.2015 03:09:42     pid:180         rss:2953216
29.03.2015 03:09:42     pid:182         rss:2576384
29.03.2015 03:09:42     pid:185         rss:1720320
29.03.2015 03:09:42     pid:239         rss:192512
29.03.2015 03:09:42     pid:247         rss:5251072
29.03.2015 03:09:42     pid:1597        rss:6266880
29.03.2015 03:09:42     pid:1602        rss:4751360
29.03.2015 03:09:42     pid:1603        rss:5738496
29.03.2015 03:09:42     pid:1866        rss:3063808
29.03.2015 03:09:42     pid:1599        rss:4399104
29.03.2015 03:09:42     pid:1600        rss:1503232
29.03.2015 03:09:42     pid:1868        rss:7819264
29.03.2015 03:09:42     pid:1869        rss:7393280
29.03.2015 03:09:42     pid:2343        rss:43180032
29.03.2015 03:09:42     pid:2347        rss:790528
29.03.2015 03:09:42     pid:3706        rss:42254336
29.03.2015 03:09:42     pid:3709        rss:819200
29.03.2015 03:09:42     pid:3722        rss:37392384
29.03.2015 03:09:42     pid:3732        rss:10846208
29.03.2015 03:09:42     pid:3735        rss:5742592
29.03.2015 03:09:42     pid:6019        rss:9531392
```

String just evaled inside, so it's pretty simple.

There are some things that can be substituted:

  - `stat` all fields from `/proc/[pid]/stat` structure
  - `system` some system specific variables(memory page size, etc)

There are some modules that already in global scope:

  - `datetime`
  - `time`
  - `os`
  - `sys`
