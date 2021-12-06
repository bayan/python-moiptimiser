from moiptimiser.ozlen_2014_moiptimiser import Ozlen2014MOIPtimiser

def test_2AP05():
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/2AP05.lp')
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
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/3AP05.lp')
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
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/4AP05.lp')
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
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/ozlen_2014_paper.lp')
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
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/ozlen_2014_paper.as.max.lp')
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
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/tamby_vanderpooten_2020.lp')
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
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/2KP50.lp')
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
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/3KP10.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 6
    assert (474, 336, 344) in nds
    assert (427, 307, 353) in nds
    assert (423, 292, 358) in nds
    assert (408, 270, 364) in nds
    assert (404, 255, 369) in nds
    assert (361, 316, 410) in nds


def test_4KP10():
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/4KP10.lp')
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


def test_3AP_15_1():
    optimiser = Ozlen2014MOIPtimiser.from_lp_file('tests/examples/3AP-15-1.lp')
    nds = optimiser.find_non_dominated_objective_vectors()
    assert len(nds) == 506
    assert (100, 34, 102) in nds
    assert (100, 35, 97) in nds
    assert (100, 64, 50) in nds
    assert (100, 92, 36) in nds
    assert (101, 32, 100) in nds
    assert (101, 59, 59) in nds
    assert (102, 25, 122) in nds
    assert (102, 76, 45) in nds
    assert (103, 24, 133) in nds
    assert (103, 35, 95) in nds
    assert (103, 42, 85) in nds
    assert (103, 45, 75) in nds
    assert (103, 83, 40) in nds
    assert (104, 52, 66) in nds
    assert (104, 61, 57) in nds
    assert (104, 74, 45) in nds
    assert (105, 110, 30) in nds
    assert (105, 41, 87) in nds
    assert (105, 60, 58) in nds
    assert (105, 73, 46) in nds
    assert (105, 95, 35) in nds
    assert (106, 30, 109) in nds
    assert (106, 33, 99) in nds
    assert (106, 36, 93) in nds
    assert (106, 37, 90) in nds
    assert (106, 41, 81) in nds
    assert (107, 60, 55) in nds
    assert (107, 90, 34) in nds
    assert (108, 43, 77) in nds
    assert (108, 47, 72) in nds
    assert (108, 78, 43) in nds
    assert (109, 31, 102) in nds
    assert (109, 38, 83) in nds
    assert (109, 62, 54) in nds
    assert (110, 107, 32) in nds
    assert (110, 53, 65) in nds
    assert (110, 88, 33) in nds
    assert (112, 29, 108) in nds
    assert (112, 52, 62) in nds
    assert (112, 71, 48) in nds
    assert (113, 36, 92) in nds
    assert (114, 27, 118) in nds
    assert (114, 46, 70) in nds
    assert (115, 101, 32) in nds
    assert (115, 23, 139) in nds
    assert (115, 29, 106) in nds
    assert (115, 50, 67) in nds
    assert (115, 61, 52) in nds
    assert (115, 81, 40) in nds
    assert (116, 22, 150) in nds
    assert (116, 34, 95) in nds
    assert (117, 22, 142) in nds
    assert (117, 27, 117) in nds
    assert (117, 52, 59) in nds
    assert (117, 80, 42) in nds
    assert (118, 42, 77) in nds
    assert (118, 43, 76) in nds
    assert (118, 46, 67) in nds
    assert (118, 79, 39) in nds
    assert (118, 99, 31) in nds
    assert (119, 118, 26) in nds
    assert (119, 59, 58) in nds
    assert (120, 117, 27) in nds
    assert (120, 28, 110) in nds
    assert (120, 35, 91) in nds
    assert (120, 37, 88) in nds
    assert (120, 50, 64) in nds
    assert (120, 59, 57) in nds
    assert (120, 70, 48) in nds
    assert (120, 75, 44) in nds
    assert (121, 32, 94) in nds
    assert (122, 42, 76) in nds
    assert (122, 56, 56) in nds
    assert (123, 24, 127) in nds
    assert (123, 26, 116) in nds
    assert (123, 41, 78) in nds
    assert (123, 45, 73) in nds
    assert (123, 64, 48) in nds
    assert (124, 43, 75) in nds
    assert (125, 31, 100) in nds
    assert (126, 21, 127) in nds
    assert (126, 26, 114) in nds
    assert (126, 30, 104) in nds
    assert (126, 36, 88) in nds
    assert (126, 88, 32) in nds
    assert (127, 107, 27) in nds
    assert (127, 42, 73) in nds
    assert (127, 50, 63) in nds
    assert (127, 73, 45) in nds
    assert (128, 45, 70) in nds
    assert (128, 72, 47) in nds
    assert (128, 73, 44) in nds
    assert (129, 27, 113) in nds
    assert (129, 29, 104) in nds
    assert (129, 31, 97) in nds
    assert (129, 86, 31) in nds
    assert (130, 105, 26) in nds
    assert (130, 20, 159) in nds
    assert (130, 24, 122) in nds
    assert (130, 58, 55) in nds
    assert (130, 71, 44) in nds
    assert (131, 24, 119) in nds
    assert (131, 40, 82) in nds
    assert (131, 50, 60) in nds
    assert (132, 24, 113) in nds
    assert (132, 29, 102) in nds
    assert (132, 34, 93) in nds
    assert (132, 36, 86) in nds
    assert (133, 39, 81) in nds
    assert (133, 40, 78) in nds
    assert (133, 44, 68) in nds
    assert (134, 23, 124) in nds
    assert (134, 68, 47) in nds
    assert (134, 84, 38) in nds
    assert (135, 35, 89) in nds
    assert (135, 48, 65) in nds
    assert (136, 30, 99) in nds
    assert (136, 32, 93) in nds
    assert (136, 34, 90) in nds
    assert (136, 50, 57) in nds
    assert (136, 58, 54) in nds
    assert (136, 75, 43) in nds
    assert (137, 18, 135) in nds
    assert (139, 36, 84) in nds
    assert (139, 57, 55) in nds
    assert (139, 73, 42) in nds
    assert (140, 26, 112) in nds
    assert (140, 28, 108) in nds
    assert (141, 33, 92) in nds
    assert (141, 59, 53) in nds
    assert (142, 47, 65) in nds
    assert (143, 21, 121) in nds
    assert (143, 26, 110) in nds
    assert (143, 35, 86) in nds
    assert (143, 43, 71) in nds
    assert (143, 49, 62) in nds
    assert (144, 55, 56) in nds
    assert (146, 31, 94) in nds
    assert (146, 48, 61) in nds
    assert (146, 71, 43) in nds
    assert (147, 27, 107) in nds
    assert (147, 29, 99) in nds
    assert (148, 34, 88) in nds
    assert (148, 38, 81) in nds
    assert (149, 20, 131) in nds
    assert (149, 25, 111) in nds
    assert (149, 28, 105) in nds
    assert (149, 56, 53) in nds
    assert (149, 69, 42) in nds
    assert (150, 27, 106) in nds
    assert (151, 48, 58) in nds
    assert (152, 30, 97) in nds
    assert (152, 36, 80) in nds
    assert (153, 25, 108) in nds
    assert (153, 32, 90) in nds
    assert (155, 23, 117) in nds
    assert (155, 56, 52) in nds
    assert (156, 17, 160) in nds
    assert (156, 30, 94) in nds
    assert (157, 63, 48) in nds
    assert (158, 25, 105) in nds
    assert (159, 47, 64) in nds
    assert (160, 19, 129) in nds
    assert (160, 26, 104) in nds
    assert (160, 28, 103) in nds
    assert (162, 22, 118) in nds
    assert (163, 28, 99) in nds
    assert (163, 31, 90) in nds
    assert (163, 45, 66) in nds
    assert (165, 26, 101) in nds
    assert (165, 39, 77) in nds
    assert (165, 40, 73) in nds
    assert (165, 70, 41) in nds
    assert (166, 33, 87) in nds
    assert (168, 34, 86) in nds
    assert (169, 29, 96) in nds
    assert (170, 23, 115) in nds
    assert (170, 40, 70) in nds
    assert (173, 23, 111) in nds
    assert (173, 34, 83) in nds
    assert (178, 39, 76) in nds
    assert (180, 28, 96) in nds
    assert (20, 111, 129) in nds
    assert (21, 100, 180) in nds
    assert (22, 103, 176) in nds
    assert (22, 105, 152) in nds
    assert (22, 107, 136) in nds
    assert (22, 113, 127) in nds
    assert (22, 115, 126) in nds
    assert (23, 77, 130) in nds
    assert (23, 88, 105) in nds
    assert (24, 70, 125) in nds
    assert (24, 72, 123) in nds
    assert (24, 82, 109) in nds
    assert (25, 75, 104) in nds
    assert (25, 77, 102) in nds
    assert (26, 90, 95) in nds
    assert (27, 72, 111) in nds
    assert (29, 66, 128) in nds
    assert (29, 77, 95) in nds
    assert (29, 79, 93) in nds
    assert (30, 65, 160) in nds
    assert (30, 70, 124) in nds
    assert (30, 71, 107) in nds
    assert (30, 74, 101) in nds
    assert (30, 92, 86) in nds
    assert (31, 68, 126) in nds
    assert (32, 104, 85) in nds
    assert (32, 67, 124) in nds
    assert (32, 73, 105) in nds
    assert (33, 61, 142) in nds
    assert (33, 63, 138) in nds
    assert (33, 65, 136) in nds
    assert (33, 68, 119) in nds
    assert (33, 86, 90) in nds
    assert (33, 88, 88) in nds
    assert (34, 100, 83) in nds
    assert (34, 101, 81) in nds
    assert (34, 108, 80) in nds
    assert (34, 66, 121) in nds
    assert (34, 68, 117) in nds
    assert (34, 70, 115) in nds
    assert (34, 73, 98) in nds
    assert (34, 76, 92) in nds
    assert (35, 58, 161) in nds
    assert (35, 60, 127) in nds
    assert (35, 63, 106) in nds
    assert (35, 71, 102) in nds
    assert (35, 74, 96) in nds
    assert (35, 81, 91) in nds
    assert (35, 90, 85) in nds
    assert (36, 106, 76) in nds
    assert (36, 68, 100) in nds
    assert (36, 79, 90) in nds
    assert (36, 81, 88) in nds
    assert (36, 87, 87) in nds
    assert (37, 53, 131) in nds
    assert (37, 60, 125) in nds
    assert (37, 62, 118) in nds
    assert (37, 70, 98) in nds
    assert (37, 72, 96) in nds
    assert (37, 73, 84) in nds
    assert (37, 75, 82) in nds
    assert (37, 90, 79) in nds
    assert (38, 102, 74) in nds
    assert (38, 103, 72) in nds
    assert (38, 61, 123) in nds
    assert (38, 88, 75) in nds
    assert (39, 55, 108) in nds
    assert (39, 58, 102) in nds
    assert (39, 65, 97) in nds
    assert (39, 70, 90) in nds
    assert (40, 115, 71) in nds
    assert (41, 99, 74) in nds
    assert (42, 104, 69) in nds
    assert (42, 112, 67) in nds
    assert (42, 60, 92) in nds
    assert (42, 69, 87) in nds
    assert (42, 72, 81) in nds
    assert (42, 83, 80) in nds
    assert (42, 87, 78) in nds
    assert (43, 77, 80) in nds
    assert (43, 86, 74) in nds
    assert (43, 96, 73) in nds
    assert (44, 102, 65) in nds
    assert (45, 52, 171) in nds
    assert (45, 53, 128) in nds
    assert (45, 86, 68) in nds
    assert (46, 113, 60) in nds
    assert (46, 46, 144) in nds
    assert (46, 54, 111) in nds
    assert (46, 57, 105) in nds
    assert (46, 80, 78) in nds
    assert (46, 98, 63) in nds
    assert (46, 99, 61) in nds
    assert (47, 51, 135) in nds
    assert (47, 52, 127) in nds
    assert (47, 53, 121) in nds
    assert (47, 61, 86) in nds
    assert (48, 48, 120) in nds
    assert (48, 51, 114) in nds
    assert (48, 78, 75) in nds
    assert (49, 47, 109) in nds
    assert (49, 50, 103) in nds
    assert (49, 57, 100) in nds
    assert (49, 59, 95) in nds
    assert (49, 75, 79) in nds
    assert (49, 77, 77) in nds
    assert (49, 83, 71) in nds
    assert (50, 122, 55) in nds
    assert (50, 71, 72) in nds
    assert (50, 83, 67) in nds
    assert (51, 101, 60) in nds
    assert (51, 115, 59) in nds
    assert (51, 118, 57) in nds
    assert (51, 67, 83) in nds
    assert (51, 97, 66) in nds
    assert (52, 52, 93) in nds
    assert (52, 62, 84) in nds
    assert (52, 82, 70) in nds
    assert (53, 121, 54) in nds
    assert (53, 43, 129) in nds
    assert (53, 68, 82) in nds
    assert (53, 97, 65) in nds
    assert (53, 98, 58) in nds
    assert (54, 109, 49) in nds
    assert (54, 57, 92) in nds
    assert (54, 59, 90) in nds
    assert (54, 70, 81) in nds
    assert (54, 81, 68) in nds
    assert (54, 82, 65) in nds
    assert (55, 69, 80) in nds
    assert (55, 79, 70) in nds
    assert (55, 94, 61) in nds
    assert (55, 95, 60) in nds
    assert (56, 39, 116) in nds
    assert (56, 42, 110) in nds
    assert (56, 46, 109) in nds
    assert (56, 49, 105) in nds
    assert (56, 63, 78) in nds
    assert (56, 66, 72) in nds
    assert (56, 88, 62) in nds
    assert (56, 89, 61) in nds
    assert (56, 93, 60) in nds
    assert (57, 75, 65) in nds
    assert (57, 82, 64) in nds
    assert (58, 36, 134) in nds
    assert (58, 82, 58) in nds
    assert (58, 86, 57) in nds
    assert (58, 98, 56) in nds
    assert (59, 111, 48) in nds
    assert (59, 128, 45) in nds
    assert (59, 44, 100) in nds
    assert (59, 56, 89) in nds
    assert (59, 61, 81) in nds
    assert (59, 68, 62) in nds
    assert (60, 60, 87) in nds
    assert (61, 103, 53) in nds
    assert (61, 91, 56) in nds
    assert (62, 101, 53) in nds
    assert (62, 106, 51) in nds
    assert (62, 49, 98) in nds
    assert (62, 91, 54) in nds
    assert (63, 104, 49) in nds
    assert (63, 106, 46) in nds
    assert (63, 38, 119) in nds
    assert (63, 41, 113) in nds
    assert (63, 54, 89) in nds
    assert (63, 84, 53) in nds
    assert (64, 110, 44) in nds
    assert (64, 45, 94) in nds
    assert (64, 58, 86) in nds
    assert (64, 77, 58) in nds
    assert (64, 84, 51) in nds
    assert (64, 99, 48) in nds
    assert (65, 108, 45) in nds
    assert (65, 43, 107) in nds
    assert (65, 51, 88) in nds
    assert (65, 61, 79) in nds
    assert (65, 76, 61) in nds
    assert (66, 105, 45) in nds
    assert (66, 35, 119) in nds
    assert (66, 43, 103) in nds
    assert (66, 50, 85) in nds
    assert (66, 59, 83) in nds
    assert (66, 60, 76) in nds
    assert (67, 55, 80) in nds
    assert (68, 107, 44) in nds
    assert (68, 125, 42) in nds
    assert (69, 129, 40) in nds
    assert (69, 73, 56) in nds
    assert (69, 92, 49) in nds
    assert (70, 102, 40) in nds
    assert (70, 107, 39) in nds
    assert (70, 41, 108) in nds
    assert (71, 100, 46) in nds
    assert (71, 34, 151) in nds
    assert (71, 38, 111) in nds
    assert (71, 59, 79) in nds
    assert (71, 62, 73) in nds
    assert (71, 90, 50) in nds
    assert (72, 42, 107) in nds
    assert (72, 47, 93) in nds
    assert (72, 54, 81) in nds
    assert (72, 72, 55) in nds
    assert (72, 95, 37) in nds
    assert (73, 42, 105) in nds
    assert (73, 47, 86) in nds
    assert (73, 50, 80) in nds
    assert (73, 94, 48) in nds
    assert (74, 40, 104) in nds
    assert (74, 43, 98) in nds
    assert (74, 55, 79) in nds
    assert (74, 59, 73) in nds
    assert (74, 64, 63) in nds
    assert (74, 84, 50) in nds
    assert (75, 126, 35) in nds
    assert (75, 42, 102) in nds
    assert (75, 87, 45) in nds
    assert (75, 93, 36) in nds
    assert (76, 39, 105) in nds
    assert (76, 45, 89) in nds
    assert (76, 48, 85) in nds
    assert (76, 52, 70) in nds
    assert (76, 86, 46) in nds
    assert (77, 114, 33) in nds
    assert (77, 32, 127) in nds
    assert (77, 45, 88) in nds
    assert (77, 72, 52) in nds
    assert (77, 80, 51) in nds
    assert (78, 36, 116) in nds
    assert (78, 37, 110) in nds
    assert (78, 42, 100) in nds
    assert (79, 36, 115) in nds
    assert (79, 43, 94) in nds
    assert (79, 50, 75) in nds
    assert (79, 84, 47) in nds
    assert (80, 112, 32) in nds
    assert (80, 68, 61) in nds
    assert (80, 79, 50) in nds
    assert (81, 32, 111) in nds
    assert (81, 35, 105) in nds
    assert (81, 39, 104) in nds
    assert (81, 42, 94) in nds
    assert (81, 61, 66) in nds
    assert (81, 68, 59) in nds
    assert (82, 31, 122) in nds
    assert (82, 41, 99) in nds
    assert (82, 60, 69) in nds
    assert (82, 64, 61) in nds
    assert (82, 81, 48) in nds
    assert (83, 29, 129) in nds
    assert (83, 40, 103) in nds
    assert (83, 44, 91) in nds
    assert (83, 55, 69) in nds
    assert (83, 60, 67) in nds
    assert (84, 28, 140) in nds
    assert (84, 37, 95) in nds
    assert (84, 47, 84) in nds
    assert (85, 66, 59) in nds
    assert (86, 43, 88) in nds
    assert (86, 57, 64) in nds
    assert (86, 69, 58) in nds
    assert (86, 86, 45) in nds
    assert (86, 91, 39) in nds
    assert (87, 42, 93) in nds
    assert (87, 49, 78) in nds
    assert (87, 56, 68) in nds
    assert (87, 58, 62) in nds
    assert (87, 62, 57) in nds
    assert (87, 85, 46) in nds
    assert (88, 31, 114) in nds
    assert (88, 34, 108) in nds
    assert (88, 46, 81) in nds
    assert (88, 48, 79) in nds
    assert (88, 62, 55) in nds
    assert (88, 78, 49) in nds
    assert (89, 134, 31) in nds
    assert (89, 30, 125) in nds
    assert (89, 38, 89) in nds
    assert (89, 56, 63) in nds
    assert (89, 77, 50) in nds
    assert (89, 79, 45) in nds
    assert (89, 89, 38) in nds
    assert (90, 36, 102) in nds
    assert (90, 44, 83) in nds
    assert (90, 74, 50) in nds
    assert (91, 110, 35) in nds
    assert (91, 132, 31) in nds
    assert (91, 28, 114) in nds
    assert (91, 36, 98) in nds
    assert (91, 43, 80) in nds
    assert (92, 27, 125) in nds
    assert (92, 35, 103) in nds
    assert (92, 54, 68) in nds
    assert (92, 71, 53) in nds
    assert (92, 77, 44) in nds
    assert (93, 113, 31) in nds
    assert (93, 49, 77) in nds
    assert (93, 70, 54) in nds
    assert (94, 108, 34) in nds
    assert (94, 41, 88) in nds
    assert (94, 48, 76) in nds
    assert (94, 56, 60) in nds
    assert (94, 87, 43) in nds
    assert (95, 34, 103) in nds
    assert (95, 68, 54) in nds
    assert (96, 103, 34) in nds
    assert (96, 111, 30) in nds
    assert (96, 31, 106) in nds
    assert (96, 69, 50) in nds
    assert (96, 83, 42) in nds
    assert (97, 26, 157) in nds
    assert (97, 36, 97) in nds
    assert (97, 40, 88) in nds
    assert (97, 49, 72) in nds
    assert (97, 54, 65) in nds
    assert (98, 26, 149) in nds
    assert (98, 35, 100) in nds
    assert (98, 64, 54) in nds
    assert (99, 101, 33) in nds
    assert (99, 119, 27) in nds
    assert (99, 33, 103) in nds
    assert (99, 48, 69) in nds
    assert (99, 65, 49) in nds
    assert (99, 81, 41) in nds
