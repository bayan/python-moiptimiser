from click.testing import CliRunner

from moiptimiser.impl import MOIPtimiser

def test_2AP05():
    optimiser = MOIPtimiser.from_lp_file('tests/examples/2AP05.lp')
    nds = optimiser.find_non_dominated_objective_vectors()

    assert len(nds) == 9
    assert (50,24) in nds
    assert (39,28) in nds
    assert (34,29) in nds
    assert (31,30) in nds
    assert (30,31) in nds
    assert (27,36) in nds
    assert (24,45) in nds
    assert (23,46) in nds
    assert (21,55) in nds
