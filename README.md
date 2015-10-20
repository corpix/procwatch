### procwatch
---------------------

Show info about process and all it childs.

Usage:
```
procwatch.py <pid> <format_string>
```

It provides some object that you sould use in `<format_string>`:
  - `datetime` Python core library
  - `os` Python core library
  - `sys` Python core library
  - `time` Python core library
  - `psutil` https://github.com/giampaolo/psutil
  - `proc` psutil.Process instance of parent or some child

#### Example

Any valid Python expression could be passed in `<format_string>`.

Example:
```bash
$ ./procwatch.py 1 "time.strftime('%Y/%m/%d %H:%M:%S %z') + '\tpid:{pid}'.format(pid=proc.pid) + '\tvsize:{vms}\trss:{rss}'.format(**proc.memory_info().__dict__)"
2015/10/20 02:26:06 +0000       pid:1   vsize:47255552  rss:8200192
2015/10/20 02:26:06 +0000       pid:432 vsize:55074816  rss:16019456
2015/10/20 02:26:06 +0000       pid:450 vsize:132390912 rss:5877760
2015/10/20 02:26:06 +0000       pid:463 vsize:47259648  rss:6594560
2015/10/20 02:26:06 +0000       pid:518 vsize:50241536  rss:3219456
2015/10/20 02:26:06 +0000       pid:547 vsize:24821760  rss:3010560
2015/10/20 02:26:06 +0000       pid:549 vsize:329523200 rss:29253632
2015/10/20 02:26:06 +0000       pid:551 vsize:116793344 rss:3510272
2015/10/20 02:26:06 +0000       pid:553 vsize:61988864  rss:4317184
2015/10/20 02:26:06 +0000       pid:561 vsize:128798720 rss:3231744
2015/10/20 02:26:06 +0000       pid:566 vsize:90845184  rss:4284416
2015/10/20 02:26:06 +0000       pid:622 vsize:443355136 rss:11968512
2015/10/20 02:26:06 +0000       pid:634 vsize:82870272  rss:6205440
2015/10/20 02:26:06 +0000       pid:648 vsize:542081024 rss:13369344
2015/10/20 02:26:06 +0000       pid:1032        vsize:45940736  rss:4784128
2015/10/20 02:26:06 +0000       pid:1065        vsize:54689792  rss:585728
2015/10/20 02:26:06 +0000       pid:1125        vsize:134172672 rss:6864896
2015/10/20 02:26:06 +0000       pid:1037        vsize:145707008 rss:5349376
2015/10/20 02:26:06 +0000       pid:983 vsize:123412480 rss:20332544
2015/10/20 02:26:06 +0000       pid:1076        vsize:142659584 rss:7954432
2015/10/20 02:26:06 +0000       pid:1035        vsize:83705856  rss:2633728
2015/10/20 02:26:06 +0000       pid:1126        vsize:150364160 rss:5885952
2015/10/20 02:26:06 +0000       pid:2017        vsize:150376448 rss:6184960
2015/10/20 02:26:06 +0000       pid:2089        vsize:145809408 rss:5505024
2015/10/20 02:26:06 +0000       pid:2328        vsize:145813504 rss:5574656
2015/10/20 02:26:06 +0000       pid:1081        vsize:142659584 rss:4055040
2015/10/20 02:26:06 +0000       pid:1204        vsize:322068480 rss:47226880
2015/10/20 02:26:06 +0000       pid:3080        vsize:196960256 rss:12496896
2015/10/20 02:26:06 +0000       pid:2197        vsize:131051520 rss:3596288
2015/10/20 02:26:06 +0000       pid:1082        vsize:145801216 rss:5435392
2015/10/20 02:26:06 +0000       pid:1123        vsize:128196608 rss:3022848
```

For `psutil < 2.0.0` you could use this commandline:
```bash
$ ./procwatch.py 1 "time.strftime('%Y/%m/%d %H:%M:%S %z') + '\tpid:{pid}'.format(pid=proc.pid) + '\tvsize:{vms}\trss:{rss}'.format(**proc.get_memory_info()._asdict())"
```
