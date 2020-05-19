from moiptimiser.impl import MOIPtimiser


def test_2AP05():
    optimiser = MOIPtimiser.from_lp_file('tests/examples/2AP05.lp')
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
    optimiser = MOIPtimiser.from_lp_file('tests/examples/3AP05.lp')
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
    optimiser = MOIPtimiser.from_lp_file('tests/examples/4AP05.lp')
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


def test_paper():
    optimiser = MOIPtimiser.from_lp_file('tests/examples/paper.lp')
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


def test_paper_as_max():
    optimiser = MOIPtimiser.from_lp_file('tests/examples/paper.as.max.lp')
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
