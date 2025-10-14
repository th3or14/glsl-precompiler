import filecmp


def test_input():
    assert not filecmp.cmp('in.glsl', 'expected-out.glsl')


def test_output():
    assert filecmp.cmp('out.glsl', 'expected-out.glsl')
