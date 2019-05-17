"""
It's a simple case of linear regession

There is a .pdf file with case description written in Portugese;
it's on this GitHub repository:
https://github.com/SamuelJansen/Linear-Regression

This code was written in Python3 using numpy,
for a Mathematics graduating class assignment.
"""

import numpy as np
A = np.matrix('1 1; 1 2; 1 4; 1 0')

B = (A.T*A).I*A.T*np.matrix('0.5; 1; 2; 0')

Area = np.matrix('1 56; 1 84; 1 118; 1 144 ; 1 173; 1 182; 1 210; 1 238; 1 243')
Aluguel = np.matrix('891; 1189; 1464; 1761; 2048; 2317; 2611; 2875; 3362')

B = (Area.T*Area).I*Area.T*np.matrix(Aluguel)

print(B)
