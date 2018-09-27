## Calculus-3
**Not intended for cryptography**


### Distance from a line to point Q

We define a point P on the line, and take the line segment of PQ = Q-P. Vector v is used to describe a line being parallel to it

```
d = (| v x PQ |) / |v|
```

### Equation of plane in 3-dimensions
Likewise v, n is a vector which is always orthogonal / normal to the plane. Po(x0,y0,z0) and n = <a,b,c>
```
a(x-x0)+b(y-y0)+c(z-z0) = 0
```

### Equation of Tangent Plane if surface is given
```
z = f(x,y)
a = fx(x,y) = differentiation wrt x
b = fy(x,y) = differentiation wrt y
c = -1

Plug into the equation of plane and that's it
```

### 3 points lie in the same plane
Then a,b and c are coplanar

bxc it will produce a vector z which is always perpendicular to `b` and `c` . Hence, a should always be perpendicular to new vector z. Hence, the dot product rule say it two vectors are orthogonal then a.z = 0
```
a.(bxc) = 0 
```

### Parallel & Orthogonal Planes
Two planes are orthogonal, if normal vectors of both plane's dot product is 0
Two planes are paralle, if normal vectors are multiple of each other

### Line of Intersection between two planes
You need to find 
1.) Point of the line
2.) Vector

### Curves
Parameterized Curve: Tangent vectors indicate positive orientation
Unparameterized Curve: Tangent vectors in either of two directions

### Tangent Vector & Derivate Vector
r(t) = f(t)i+g(t)j+h(t)k

r'(t) is derivative vector
and if `r'(t) != 0` , `r'(t)` is a tangent vector

### Unit Tangent Vector
```
T(t) = r'(t)/|r'(t)| = v(t)/|v(t)|
```

### Differentiation by Parts
```
d/dx(a(x).b(x)) = a(x)b'(x) + a'(x)b(x)
```

### Integration by Parts
```
∫f(x)g'(x) = f(x).g(x) - ∫f'(x).g(x)dx
```

### Arc Length of a Curve

Vector valued function `r(t) = <f(t), g(t), h(t)>`
```
L = ∫ b sqrt(f'(t)^2+g'(t)^2+h'(t)^2)
    a
```

### Curvature
Let r be smooth parameterized curve. s denotes arc length, and T = r'/|r'|
```
k(s) = |dT/ds|
```

### Curvature Formula
```
k(t) = (1/|v|)* |dT/dt|
```

```
k = | v x a | / |v|^3
```

### Principle Unit Normal Vector
```
N(t) = dT/dt
       ______
       |dT/dt|
```

