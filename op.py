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

# div
print("=== div res ===")
print(a)
print(b)

print(a/b)
print(a.div(b))
print(torch.div(a, b))

print(a)

print(a.div_(b))

print(a)

# matmul
print("=== matmul res ===")

a = torch.ones(2, 1)
b = torch.ones(1, 2)
print(a)
print(b)

print(a @ b)
print(a.matmul(b))
print(a.mm(b))
print(torch.matmul(a, b))
print(torch.mm(a, b))

# high dimension tensor
print("=== high dimension res ===")

a = torch.ones(1, 2, 3, 4)
b = torch.ones(1, 2, 4, 3)
print(a)
print(b)

print(a @ b)
print(a.matmul(b))
print(torch.matmul(a, b))

print(torch.matmul(a, b).shape)

# pow
print("=== pow res ===")

a = torch.tensor([1, 2])
print(a)

print(a**3)
print(a.pow(3))
print(torch.pow(a, 3))

print(a)

print(a.pow_(3))

print(a)
