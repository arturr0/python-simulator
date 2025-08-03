# Vibrational System Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.20+-orange)
![SciPy](https://img.shields.io/badge/SciPy-1.7+-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-green)

A Python simulation of a damped harmonic oscillator with forced vibration analysis using FFT.

## Table of Contents
- [Description](#description)
- [Mathematical Model](#mathematical-model)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Parameters](#parameters)
- [Output](#output)
- [Customization](#customization)
- [Theory](#theory)
- [License](#license)

## Description

This program simulates the behavior of a damped harmonic oscillator under forced vibration, then analyzes the displacement using Fast Fourier Transform (FFT). The simulation includes:

- Time-domain analysis of displacement and force
- Frequency-domain analysis via FFT
- Visualization of both time and frequency responses

## Mathematical Model

The system is modeled using the second-order differential equation:
mẍ + cẋ + kx = F₀cos(ωt)

text

Converted to state-space representation:
Aẋ + Bx = F

text
where:
- `A = [[m, 0], [0, 1]]`
- `B = [[c, k], [-1, 0]]`
- `F = [F₀cos(ωt), 0]`

## Dependencies

- Python 3.x
- NumPy (>=1.20)
- SciPy (>=1.7)
- Matplotlib (>=3.4)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vibration-simulation.git
cd vibration-simulation
```
Install required packages:

```bash
pip install numpy scipy matplotlib
```

## Usage
Run the simulation:

```bash
python vibration_simulation.py
```

## Parameters

| Parameter  | Description                  | Default Value |
|------------|------------------------------|----------------|
| `m`        | Mass (kg)                    | 2.0            |
| `k`        | Spring constant (N/m)        | 2.0            |
| `c`        | Damping coefficient (Ns/m)   | 0.2            |
| `omega`    | Forcing frequency (rad/s)    | 1.0            |
| `F0`       | Force amplitude (N)          | 1.0            |
| `delta_t`  | Time step (s)                | 0.001          |
| `time`     | Simulation duration (s)      | 100            |

## Output

The program generates two plots:

Time Domain:

- Displacement (x) vs. Time
- Force (F) vs. Time

Frequency Domain:

- FFT magnitude of the displacement
- Shows dominant frequency components

## Customization

To modify the simulation:

Change system parameters at the top of the script:

```python
m = 2.0  # Mass
k = 2.0  # Spring constant
c = 0.2  # Damping
```

Adjust forcing function:

```python
if t <= 15:  # Force duration
    F[0] = F0 * np.cos(omega*t)
else:
    F[0] = 0.0  # Force removal
```

Change simulation duration and time step:

```python
delta_t = 0.001  # Time step
time = np.arange(0.0, 100.0, delta_t)  # Simulation time
```

## Theory

### Numerical Integration

The state-space equations are solved using forward Euler integration:

```python
x = x + delta_t * inv(A).dot(F - B.dot(x))
```

### Fast Fourier Transform

The displacement data is analyzed using SciPy's FFT:

```python
Y = fft(X)
```

## License

Free for academic, personal, and research use.
