#!/bin/zsh

rm -rf runs/out
mkdir -p runs/out

for example in\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-10-1.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-10-2.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-10-3.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-10-4.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-10-5.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-15-1.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-15-2.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-15-3.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-15-4.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-15-5.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-20-1.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-20-2.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-20-3.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-20-4.lp\
                pettersson_ozlen_2017_examples/AP3_Tests/3AP-20-5.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-05-1.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-05-2.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-05-3.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-05-4.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-05-5.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-08-1.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-08-2.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-08-3.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-08-4.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-08-5.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-10-1.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-10-2.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-10-3.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-10-4.lp\
                pettersson_ozlen_2017_examples/AP4_Tests/4AP-10-5.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_050-1.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_050-2.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_050-3.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_050-4.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_050-5.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_075-1.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_075-2.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_075-3.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_075-4.lp\
                pettersson_ozlen_2017_examples/KP3_Tests/KP3D_075-5.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-020-1.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-020-2.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-020-3.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-020-4.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-020-5.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-040-1.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-040-2.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-040-3.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-040-4.lp\
                pettersson_ozlen_2017_examples/KP4_Tests/KP4D-040-5.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-10-1.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-10-2.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-10-3.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-10-4.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-10-5.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-12-1.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-12-2.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-12-3.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-12-4.lp\
                pettersson_ozlen_2017_examples/TSP3_Tests/TSP3-12-5.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-06-1.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-06-2.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-06-3.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-06-4.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-06-5.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-08-1.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-08-2.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-08-3.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-08-4.lp\
                pettersson_ozlen_2017_examples/TSP4_Tests/TSP4-08-5.lp
do
    for algorithm in ozlen2014 tamby2020-direct tamby2020-two-stage
    do
        echo Running $algorithm for $example ...
        python3 -m moiptimiser -a $algorithm ../tests/examples/$example >> runs/out/$algorithm.txt
        echo '' >> runs/out/$algorithm.txt
        echo Applied $algorithm to $example.
    done
done
