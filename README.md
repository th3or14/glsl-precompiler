Automates adding `#define` directives to GLSL shader files for conditional compilation.

# Usage

If you have a GLSL shader file `in.glsl` and you would like to add `#define A 1` and `#define B 2` to it before compiling, then calling

```
python3 precompiler.py -D A=1 -D B=2 -i in.glsl -o out.glsl
```

produces `out.glsl` with the desired defines pasted after the line with `#version` directive.

# Requirements

- Python 3
