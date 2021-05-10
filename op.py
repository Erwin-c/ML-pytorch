"""
  op.py

    Created on: May 10, 2021
        Author: Erwin
"""

import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)

# add
print("=== add res ===")
print(a)
print(b)

print(a + b)
print(a.add(b))
print(torch.add(a, b))

print(a)

print(a.add_(b))

print(a)

# sub
print("=== sub res ===")
print(a)
print(b)

print(a - b)
print(a.sub(b))
print(torch.sub(a, b))

print(a)

print(a.sub_(b))

print(a)

# mul
print("=== mul res ===")
print(a)
print(b)

print(a * b)
print(a.mul(b))
print(torch.mul(a, b))

print(a)

print(a.mul_(b))

print(a)
