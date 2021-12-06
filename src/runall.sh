#!/bin/zsh

rm -rf runs/ozout runs/tbout
mkdir -p runs/ozout runs/tbout

export TIMEFMT='%E'

{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/2AP05.lp | sort > runs/ozout/2AP05.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/2AP05.lp | sort > runs/tbout/2AP05.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/2KP50.lp | sort > runs/ozout/2KP50.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/2KP50.lp | sort > runs/tbout/2KP50.txt ) ; } 2>> runs/tbout/times.txt

{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP05.lp | sort > runs/ozout/3AP05.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP05.lp | sort > runs/tbout/3AP05.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3KP10.lp | sort > runs/ozout/3KP10.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3KP10.lp | sort > runs/tbout/3KP10.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/4AP05.lp | sort > runs/ozout/4AP05.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/4AP05.lp | sort > runs/tbout/4AP05.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/4KP10.lp | sort > runs/ozout/4KP10.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/4KP10.lp | sort > runs/tbout/4KP10.txt ) ; } 2>> runs/tbout/times.txt

{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/ozlen_2014_paper.as.max.lp | sort > runs/ozout/ozlen_2014_paper.as.max.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/ozlen_2014_paper.as.max.lp | sort > runs/tbout/ozlen_2014_paper.as.max.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/ozlen_2014_paper.lp | sort > runs/ozout/ozlen_2014_paper.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/ozlen_2014_paper.lp | sort > runs/tbout/ozlen_2014_paper.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/tamby_vanderpooten_2020.lp | sort > runs/ozout/tamby_vanderpooten_2020.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/tamby_vanderpooten_2020.lp | sort > runs/tbout/tamby_vanderpooten_2020.txt ) ; } 2>> runs/tbout/times.txt

{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-10-1.lp | sort > runs/ozout/3AP-10-1.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-10-1.lp | sort > runs/tbout/3AP-10-1.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-10-2.lp | sort > runs/ozout/3AP-10-2.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-10-2.lp | sort > runs/tbout/3AP-10-2.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-10-3.lp | sort > runs/ozout/3AP-10-3.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-10-3.lp | sort > runs/tbout/3AP-10-3.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-10-4.lp | sort > runs/ozout/3AP-10-4.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-10-4.lp | sort > runs/tbout/3AP-10-4.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-10-5.lp | sort > runs/ozout/3AP-10-5.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-10-5.lp | sort > runs/tbout/3AP-10-5.txt ) ; } 2>> runs/tbout/times.txt

{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-15-1.lp | sort > runs/ozout/3AP-15-1.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-15-1.lp | sort > runs/tbout/3AP-15-1.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-15-2.lp | sort > runs/ozout/3AP-15-2.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-15-2.lp | sort > runs/tbout/3AP-15-2.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-15-3.lp | sort > runs/ozout/3AP-15-3.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-15-3.lp | sort > runs/tbout/3AP-15-3.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-15-4.lp | sort > runs/ozout/3AP-15-4.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-15-4.lp | sort > runs/tbout/3AP-15-4.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-15-5.lp | sort > runs/ozout/3AP-15-5.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-15-5.lp | sort > runs/tbout/3AP-15-5.txt ) ; } 2>> runs/tbout/times.txt

{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-20-1.lp | sort > runs/ozout/3AP-20-1.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-20-1.lp | sort > runs/tbout/3AP-20-1.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-20-2.lp | sort > runs/ozout/3AP-20-2.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-20-2.lp | sort > runs/tbout/3AP-20-2.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-20-3.lp | sort > runs/ozout/3AP-20-3.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-20-3.lp | sort > runs/tbout/3AP-20-3.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-20-4.lp | sort > runs/ozout/3AP-20-4.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-20-4.lp | sort > runs/tbout/3AP-20-4.txt ) ; } 2>> runs/tbout/times.txt
{ time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-20-5.lp | sort > runs/ozout/3AP-20-5.txt ) ; } 2>> runs/ozout/times.txt
{ time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-20-5.lp | sort > runs/tbout/3AP-20-5.txt ) ; } 2>> runs/tbout/times.txt

# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-25-1.lp | sort > runs/ozout/3AP-25-1.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-25-1.lp | sort > runs/tbout/3AP-25-1.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-25-2.lp | sort > runs/ozout/3AP-25-2.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-25-2.lp | sort > runs/tbout/3AP-25-2.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-25-3.lp | sort > runs/ozout/3AP-25-3.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-25-3.lp | sort > runs/tbout/3AP-25-3.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-25-4.lp | sort > runs/ozout/3AP-25-4.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-25-4.lp | sort > runs/tbout/3AP-25-4.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-25-5.lp | sort > runs/ozout/3AP-25-5.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-25-5.lp | sort > runs/tbout/3AP-25-5.txt ) ; } 2>> runs/tbout/times.txt

# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-30-1.lp | sort > runs/ozout/3AP-30-1.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-30-1.lp | sort > runs/tbout/3AP-30-1.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-30-2.lp | sort > runs/ozout/3AP-30-2.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-30-2.lp | sort > runs/tbout/3AP-30-2.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-30-3.lp | sort > runs/ozout/3AP-30-3.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-30-3.lp | sort > runs/tbout/3AP-30-3.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-30-4.lp | sort > runs/ozout/3AP-30-4.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-30-4.lp | sort > runs/tbout/3AP-30-4.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-30-5.lp | sort > runs/ozout/3AP-30-5.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-30-5.lp | sort > runs/tbout/3AP-30-5.txt ) ; } 2>> runs/tbout/times.txt

# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-40-1.lp | sort > runs/ozout/3AP-40-1.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-40-1.lp | sort > runs/tbout/3AP-40-1.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-40-2.lp | sort > runs/ozout/3AP-40-2.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-40-2.lp | sort > runs/tbout/3AP-40-2.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-40-3.lp | sort > runs/ozout/3AP-40-3.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-40-3.lp | sort > runs/tbout/3AP-40-3.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-40-4.lp | sort > runs/ozout/3AP-40-4.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-40-4.lp | sort > runs/tbout/3AP-40-4.txt ) ; } 2>> runs/tbout/times.txt
# { time ( python3 -m moiptimiser -a ozlen2014 ../tests/examples/3AP-40-5.lp | sort > runs/ozout/3AP-40-5.txt ) ; } 2>> runs/ozout/times.txt
# { time ( python3 -m moiptimiser -a tamby2020 ../tests/examples/3AP-40-5.lp | sort > runs/tbout/3AP-40-5.txt ) ; } 2>> runs/tbout/times.txt
