[![Python application](https://github.com/th3or14/glsl-precompiler/actions/workflows/python-app.yml/badge.svg)](https://github.com/th3or14/glsl-precompiler/actions/workflows/python-app.yml)

# Description

Automates adding `#define` directives to GLSL shader files for conditional compilation.

# Usage

Let's say you have a GLSL shader file `in.glsl`

```
// some comments

#version 460 core

// other code
```

and you would like to add `#define A 1` and `#define B 2` to it before compiling. Then running

```
python precompiler.py -D A=1 -D B=2 -i in.glsl -o out.glsl
```

produces `out.glsl`

```
// some comments

#version 460 core
#define A 1
#define B 2

// other code
```

with the desired defines inserted after the line with `#version` directive.

`core` (profile name) is optional, of course. `#version` directive could be just

```
#version 460
```

# Requirements

- Python (minimal tested version is 3.8)

# Restrictions

While comments before `#version` directive are allowed, the parser doesn't distinguish between commented and uncommented code. So please do not use `#version` directive in comments before uncommented `#version` directive like this

```
// #version 450 core

#version 460 core
```

or this

```
/*
#version 450 core
*/

#version 460 core
```

or this

```
/* #version 450 core */ #version 460 core
```

And please do not use comments inside `#version` directive like this

```
#version /* 450 */ 460 core
```
