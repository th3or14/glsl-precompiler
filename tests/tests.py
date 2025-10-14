import filecmp


def test_output():
    assert filecmp.cmp('out.glsl', 'expected-out.glsl')
