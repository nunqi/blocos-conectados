import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import r2_score
from statistics import mean

d = 1

weights = [59.9, 109.5, 119.5, 129.5, 139.6]
measurements = [
    mean([0.867, 0.880, 0.871, 0.873, 0.872]),
    mean([0.698, 0.700, 0.698, 0.705, 0.705]),
    mean([0.681, 0.680, 0.676, 0.677, 0.685]),
    mean([0.665, 0.664, 0.664, 0.664, 0.666]),
    mean([0.650, 0.649, 0.648, 0.649, 0.649])
]

x = [ 1/w for w in weights ]
y = [ t**2 for t in measurements ]

slope, intercept, r, p, std_err = linregress(x, y)

print(f'm = {slope}')
print(f'b = {intercept}')

model_y = [ slope * i + intercept for i in x ]

print(f'R² = {r2_score(y, model_y)}')

g = (2 * d) / intercept
print(f"g = {g}")

mc = (slope * 9.8) / (2 * d)
print(f"Mc = {mc}")

plt.scatter(x, y, label="Dados coletados")
plt.plot(x, model_y, label=f"Resultado regressão linear (R² = {r2_score(y, model_y)})")
plt.xlabel("Peso (1/g)")
plt.ylabel("Tempo (s²)")
plt.legend()
#plt.show()
