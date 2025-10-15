import filecmp
import subprocess


def test_usage():
    args = ['python',
            '../precompiler.py',
            '-D',
            'A=1',
            '-D',
            'B=2',
            '-i',
            'in.glsl',
            '-o',
            'out.glsl']
    assert subprocess.run(args=args).returncode == 0
    assert filecmp.cmp('out.glsl', 'expected-out.glsl')
