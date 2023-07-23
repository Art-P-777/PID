import numpy as np
import matplotlib.pyplot as plt
from DinamicModel import MassSpringDamper
from pid import PID

delta_t = 0.001
reg = PID(15, 8, 0.01, delta_t, -50, 50)
model = MassSpringDamper(1, 1, 1, delta_t)
T = 20
t = np.arange(0, T, delta_t)
F = 0

x_des = np.ones(len(t))

model_x = []

F_hist = []

P_hist, D_hist, I_hist = [], [], []
for i in range(len(t)):
    model_x.append(model.update(F))
    F = -reg.update(model_x[-1], x_des[i])
    F_hist.append(F)
    P_hist.append(reg._prop)
    D_hist.append(reg._dif)
    I_hist.append(reg._integ)

fig, (ax1, ax2,ax3) = plt.subplots(ncols=3, figsize=[10, 7])
ax1.plot(t, model_x, label="real x")
ax1.plot(t, x_des, label="x desired")
ax2.plot(t, P_hist, label="P")
ax2.plot(t, D_hist, label="D")
ax2.plot(t, I_hist, label="I")
ax3.plot(t ,F_hist, label="F_hist")


ax1.legend()
ax1.plot()
ax2.legend()
ax3.legend()
ax2.plot()
plt.show()