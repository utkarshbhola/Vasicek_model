import numpy as np
import matplotlib.pyplot as plt

# Parameters for the Vasicek model
theta = 0.1   # Speed of reversion
mu = 0.05     # Long-term mean
sigma = 0.02  # Volatility
r0 = 0.03     # Initial interest rate
T = 1.0       # Time period (1 year)
N = 1000      # Number of time steps
M = 1000      # Number of Monte Carlo simulations
dt = T / N    # Time step size

# Initialize the array to store the simulated paths
interest_rate_paths = np.zeros((M, N))
interest_rate_paths[:, 0] = r0  # All paths start at the initial rate

# Generate the Monte Carlo simulations
for t in range(1, N):
    Z = np.random.normal(0, 1, M)  # Random normal variable for each path
    interest_rate_paths[:, t] = (interest_rate_paths[:, t-1] + 
                                 theta * (mu - interest_rate_paths[:, t-1]) * dt +
                                 sigma * np.sqrt(dt) * Z)

# Plot a few of the simulated paths
plt.plot(np.linspace(0, T, N), interest_rate_paths[:10].T)
plt.title('Monte Carlo Simulation of Interest Rate Paths (Vasicek Model)')
plt.xlabel('Time')
plt.ylabel('Interest Rate')
plt.show()