"""
  boadcast.py

    Created on: May 22, 2021
        Author: Erwin
"""

import torch

a = torch.rand(2, 1, 1, 3)
b = torch.rand(4, 2, 3)
c = a + b

print(a)
print(b)
print(c)
print(c.shape)
