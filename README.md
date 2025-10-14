[![Python application](https://github.com/th3or14/glsl-precompiler/actions/workflows/python-app.yml/badge.svg)](https://github.com/th3or14/glsl-precompiler/actions/workflows/python-app.yml)

# Description

Automates adding `#define` directives to GLSL shader files for conditional compilation.

# Usage

Let's say you have a GLSL shader file `in.glsl`

```
// some comments

#version 460

// other code
```

and you would like to add `#define A 1` and `#define B 2` to it before compiling. Then running

```
python3 precompiler.py -D A=1 -D B=2 -i in.glsl -o out.glsl
```

produces `out.glsl`

```
// some comments

#version 460
#define A 1
#define B 2

// other code
```

with the desired defines inserted after the line with `#version` directive.

# Requirements

- Python 3
