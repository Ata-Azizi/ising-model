# 1D Ising Model — Monte Carlo Simulation

Numerical simulation of the one-dimensional ferromagnetic Ising model using the **Metropolis Monte Carlo algorithm**, implemented in Python.

This project investigates the evolution of spin configurations, mean energy, and statistical uncertainty at finite temperature.

## 1. Theoretical Background

The one-dimensional Ising model describes a chain of interacting spins, where each spin can take one of two values:

$$
s_i \in \{-1,+1\}.
$$

The Hamiltonian is

$$
H=-J\sum_{i=1}^{N}s_i s_{i+1},
$$

where:

- \(J>0\) is the ferromagnetic coupling constant.
- \(N\) is the number of spins.
- \(s_i\) represents the spin at lattice site \(i\).

Periodic boundary conditions are imposed:

$$
s_{N+1}=s_1.
$$

The simulations use \(J=1\) and \(k_B=1\).

## 2. Metropolis Monte Carlo Algorithm

The Metropolis algorithm generates spin configurations according to their Boltzmann statistical weights.

For each Monte Carlo step:

1. Select a random spin.
2. Propose flipping the selected spin.
3. Calculate the energy difference:

   $$
   \Delta E=E_{\mathrm{trial}}-E_{\mathrm{current}}.
   $$

4. Accept the proposed configuration with probability

   $$
   P_{\mathrm{accept}}=\min\left(1,e^{-\Delta E/(k_BT)}\right).
   $$

5. If the move is rejected, retain the previous configuration.

This procedure generates a Markov chain that can sample the canonical equilibrium distribution after equilibration.

## 3. Implementations

### Mean Energy Evolution

**Notebook:** [Ising_Model_Mean_Energy.ipynb](Ising_Model_Mean_Energy.ipynb)

Simulates multiple independent Markov chains and calculates the mean energy as a function of Monte Carlo steps.

Features:

- One-dimensional spin chain with periodic boundary conditions
- Single-spin Metropolis updates
- Multiple independent simulation runs
- Ensemble-averaged energy
- Monte Carlo standard-error estimates
- Visualization of energy evolution and statistical uncertainty

### Spin Configuration Heatmap

**Notebook:** [Ising_Model_Heatmap.ipynb](Ising_Model_Heatmap.ipynb)

Visualizes the evolution of spin configurations during Metropolis sampling.

Features:

- Single-spin-flip Monte Carlo dynamics
- Visualization of spin orientations
- Periodic boundary conditions
- Heatmap of spin configurations over Monte Carlo steps

## 4. Requirements

- Python 3
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 5. Installation and Usage

Clone the repository:

```bash
git clone https://github.com/Ata-Azizi/ising-model.git
cd ising-model
```

Install the required packages:

```bash
python -m pip install numpy matplotlib seaborn jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```

Open either notebook and run the cells.

Alternatively, open the repository directly in VS Code and select a Python kernel.

## 6. Relevance to Quantum Computing

The Ising model is an important framework in quantum optimization and quantum simulation.

Classical Ising Hamiltonians can be mapped to diagonal qubit Hamiltonians by replacing spin variables with Pauli-Z operators:

$$
H_C=-\sum_{\langle i,j\rangle}J_{ij}Z_iZ_j-\sum_i h_i Z_i.
$$

Such Hamiltonians appear in quantum optimization methods including the Quantum Approximate Optimization Algorithm (QAOA).

**This repository implements classical Metropolis Monte Carlo simulations, not QAOA or quantum-circuit simulations.**

## Author

**Ata Azizi Seraji**

MSc Theoretical Physics — University of Göttingen, Germany

[GitHub Profile](https://github.com/Ata-Azizi)
