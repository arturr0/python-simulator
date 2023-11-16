import numpy as np 
from numpy.linalg import inv
from matplotlib import pyplot as plt
from scipy.fftpack import fft

m = 2.0
k = 2.0
c = 0.2   

omega = 1.0	 # czestosc sily wymuszajacej
F0 = 1.0 # amplituda sily wymuszajacej
delta_t = 0.001 # krok czasowy
time = np.arange(0.0, 100.0, delta_t) # czas symulacji 

# warunki poczatkowe
x = np.array([0,0])   # [predkosc, przesuniecie]
A = np.array([[m,0],[0,1]]) # macierz A
B = np.array([[c,k],[-1,0]]) # macierz B
F = np.array([0.0,0.0]) # wektor F

X = [] # lista przechowujaca przesuniecie
force = [] # lista przechowujaca sile F

# petla liczaca sile wymuszajaca i przesuniecie wg kroku czasowego
for t in time:
	if t <= 15:
		F[0] = F0 * np.cos(omega*t)
	else:
		F[0] = 0.0 # po uplywie 15 sekund odejmujemy sile wymuszajaca

	x = x + delta_t * inv(A).dot( F - B.dot(x) )
	X.append(x[1])
	force.append(F[0])
	
Y = fft(X)
# wykresy
t = [i for i in time] 
plt.subplot(2,1,1)
plt.plot(t,X)
plt.plot(t,force)
plt.grid(True)
plt.legend(['Przesuniecie', 'Sila'], loc='lower right')
plt.xlabel ('Czas')
plt.subplot(2,1,2)
plt.plot (abs(Y))
plt.show()
