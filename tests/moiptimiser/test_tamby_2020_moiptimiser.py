from moiptimiser.tamby_2020_moiptimiser import Tamby2020MOIPtimiser

def test_2AP05():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/2AP05.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 9
    assert (50, 24) in nds
    assert (39, 28) in nds
    assert (34, 29) in nds
    assert (31, 30) in nds
    assert (30, 31) in nds
    assert (27, 36) in nds
    assert (24, 45) in nds
    assert (23, 46) in nds
    assert (21, 55) in nds


def test_3AP05():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/3AP05.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 12
    assert (50, 24, 44) in nds
    assert (41, 37, 31) in nds
    assert (39, 28, 53) in nds
    assert (34, 29, 44) in nds
    assert (31, 30, 34) in nds
    assert (30, 31, 39) in nds
    assert (28, 48, 35) in nds
    assert (28, 40, 43) in nds
    assert (27, 36, 58) in nds
    assert (24, 45, 38) in nds
    assert (23, 46, 43) in nds
    assert (21, 55, 47) in nds


def test_4AP05():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/4AP05.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 33
    assert (60, 39, 35, 32) in nds
    assert (56, 40, 53, 22) in nds
    assert (56, 33, 36, 31) in nds
    assert (50, 32, 38, 60) in nds
    assert (50, 24, 44, 48) in nds
    assert (49, 34, 55, 26) in nds
    assert (47, 34, 55, 27) in nds
    assert (47, 34, 53, 40) in nds
    assert (46, 41, 41, 27) in nds
    assert (46, 36, 40, 40) in nds
    assert (44, 35, 46, 25) in nds
    assert (43, 44, 40, 21) in nds
    assert (41, 37, 31, 39) in nds
    assert (40, 37, 41, 36) in nds
    assert (40, 32, 49, 44) in nds
    assert (39, 28, 53, 53) in nds
    assert (37, 46, 43, 41) in nds
    assert (37, 44, 37, 49) in nds
    assert (37, 42, 58, 36) in nds
    assert (36, 42, 56, 45) in nds
    assert (34, 44, 45, 37) in nds
    assert (34, 29, 44, 52) in nds
    assert (33, 47, 44, 30) in nds
    assert (32, 39, 54, 61) in nds
    assert (31, 30, 34, 67) in nds
    assert (30, 31, 39, 63) in nds
    assert (28, 48, 35, 29) in nds
    assert (28, 40, 45, 46) in nds
    assert (28, 40, 43, 59) in nds
    assert (27, 36, 58, 50) in nds
    assert (24, 45, 38, 48) in nds
    assert (23, 46, 43, 44) in nds
    assert (21, 55, 47, 40) in nds


def test_ozlen_2014_paper():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/ozlen_2014_paper.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 14
    assert (19, 15, 14, 11) in nds
    assert (18, 15, 15, 9) in nds
    assert (17, 16, 13, 11) in nds
    assert (17, 13, 15, 11) in nds
    assert (16, 18, 15, 9) in nds
    assert (16, 15, 10, 13) in nds
    assert (15, 17, 11, 10) in nds
    assert (15, 16, 7, 12) in nds
    assert (14, 11, 16, 9) in nds
    assert (14, 8, 23, 13) in nds
    assert (13, 19, 17, 10) in nds
    assert (13, 9, 16, 11) in nds
    assert (12, 11, 11, 13) in nds
    assert (11, 19, 12, 14) in nds


def test_ozlen_2014_paper_as_max():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/ozlen_2014_paper.as.max.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 14
    assert (-19, -15, -14, -11) in nds
    assert (-18, -15, -15, -9) in nds
    assert (-17, -16, -13, -11) in nds
    assert (-17, -13, -15, -11) in nds
    assert (-16, -18, -15, -9) in nds
    assert (-16, -15, -10, -13) in nds
    assert (-15, -17, -11, -10) in nds
    assert (-15, -16, -7, -12) in nds
    assert (-14, -11, -16, -9) in nds
    assert (-14, -8, -23, -13) in nds
    assert (-13, -19, -17, -10) in nds
    assert (-13, -9, -16, -11) in nds
    assert (-12, -11, -11, -13) in nds
    assert (-11, -19, -12, -14) in nds


def test_tamby_vanderpooten_paper():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/tamby_vanderpooten_2020.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 7
    # Add 5000 to each element to match up with expected values from example in paper
    plus_5000 = lambda values: tuple([x + 5000 for x in values])
    expected_nds = set([plus_5000(nd) for nd in nds])
    assert (1606, 1183, 1592) in expected_nds
    assert (2146, 1430, 1286) in expected_nds
    assert (2146, 364, 1924)  in expected_nds
    assert (1958, 373, 1811)  in expected_nds
    assert (2294, 1143, 1696) in expected_nds
    assert (2482, 1134, 1809) in expected_nds
    assert (2003, 1461, 1491) in expected_nds


def test_2KP50():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/2KP50.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 43
    assert (2414, 2229) in nds
    assert (2411, 2266) in nds
    assert (2404, 2267) in nds
    assert (2402, 2283) in nds
    assert (2401, 2286) in nds
    assert (2398, 2287) in nds
    assert (2397, 2290) in nds
    assert (2396, 2301) in nds
    assert (2394, 2306) in nds
    assert (2393, 2309) in nds
    assert (2391, 2311) in nds
    assert (2388, 2319) in nds
    assert (2386, 2325) in nds
    assert (2384, 2338) in nds
    assert (2382, 2340) in nds
    assert (2381, 2343) in nds
    assert (2378, 2344) in nds
    assert (2374, 2347) in nds
    assert (2369, 2357) in nds
    assert (2366, 2358) in nds
    assert (2365, 2362) in nds
    assert (2359, 2371) in nds
    assert (2356, 2373) in nds
    assert (2350, 2383) in nds
    assert (2346, 2385) in nds
    assert (2344, 2386) in nds
    assert (2337, 2388) in nds
    assert (2335, 2398) in nds
    assert (2333, 2400) in nds
    assert (2325, 2410) in nds
    assert (2318, 2415) in nds
    assert (2309, 2422) in nds
    assert (2304, 2423) in nds
    assert (2289, 2432) in nds
    assert (2284, 2434) in nds
    assert (2283, 2435) in nds
    assert (2256, 2438) in nds
    assert (2254, 2441) in nds
    assert (2244, 2442) in nds
    assert (2242, 2445) in nds
    assert (2212, 2448) in nds
    assert (2210, 2449) in nds
    assert (2209, 2450) in nds


def test_3KP10():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/3KP10.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 6
    assert (474, 336, 344) in nds
    assert (427, 307, 353) in nds
    assert (423, 292, 358) in nds
    assert (408, 270, 364) in nds
    assert (404, 255, 369) in nds
    assert (361, 316, 410) in nds


def test_4KP10():
    optimiser = Tamby2020MOIPtimiser.from_lp_file('tests/examples/4KP10.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 11
    assert (474, 336, 344, 501) in nds
    assert (458, 285, 343, 504) in nds
    assert (427, 307, 353, 433) in nds
    assert (423, 292, 358, 437) in nds
    assert (408, 270, 364, 476) in nds
    assert (404, 255, 369, 480) in nds
    assert (399, 288, 332, 521) in nds
    assert (388, 204, 368, 483) in nds
    assert (383, 237, 331, 524) in nds
    assert (361, 316, 410, 374) in nds
    assert (357, 226, 378, 412) in nds


def test_ideal_point():
    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/2AP05.lp')._ideal_point) == (21, 24)
    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/3AP05.lp')._ideal_point) == (21, 24, 31)
    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/4AP05.lp')._ideal_point) == (21, 24, 31, 21)

    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/ozlen_2014_paper.lp')._ideal_point) == (11, 8, 7, 9)
    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/ozlen_2014_paper.as.max.lp')._ideal_point) == (11, 8, 7, 9)

    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/2KP50.lp')._ideal_point) == (-2414, -2450)
    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/3KP10.lp')._ideal_point) == (-474, -336, -410)
    assert(Tamby2020MOIPtimiser.from_lp_file('tests/examples/4KP10.lp')._ideal_point) == (-474, -336, -410, -524)
