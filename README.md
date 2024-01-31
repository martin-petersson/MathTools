# MathTools
A math library I made to learn and explore math.

### Usage

Open up a terminal and go to the directory where you want to put Math Tools.

<br>

Clone the repo:

```bash
git clone https://github.com/martin-petersson/MathTools.git
```
Inside the same directory run the interactive Python interpreter:

```bash
$ python
```

```text
>>> import mathtools as mt
```

### Define a vector
```python
a = mt.Vector([x, y])
```
### Adding two vectors
```python
a + b
```
### Multiply vector by scalar
```python
a * 0.78
```
### Divide vector by scalar
```python
a / 2
```
### Normalize/unitize vector
```python
a.unit
```
### Dot product of two vectors
```python
a.dot(b)
```
### Cross product of two 3d vectors
```python
a.cross(b)
```

### Linear interpolation between two vectors
```python
t = 0.5
a.lerp(b, t)
```

### Define a matrix
```python
m = mt.Matrix([[a, b], [c, d]])
```