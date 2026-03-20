"""
GRAY CODE UNIVERSE — Physical Constants & Encoder Model Foundations
===================================================================
Framework mapping rotary encoder / Gray code information theory
onto black hole thermodynamics and quantum gravity.

Core hypothesis: The universe encodes state transitions such that
only one bit flips between adjacent states (Gray code constraint).
The Planck scale defines the encoder's angular resolution.

Author: Loputo & Claude (Anthropic)
License: MIT — share freely, break things, report back
"""

import numpy as np
from dataclasses import dataclass

# =============================================================================
# FUNDAMENTAL CONSTANTS (SI units)
# =============================================================================
G = 6.67430e-11       # Gravitational constant [m³ kg⁻¹ s⁻²]
c = 2.99792458e8      # Speed of light [m/s]
hbar = 1.054571817e-34 # Reduced Planck constant [J·s]
k_B = 1.380649e-23    # Boltzmann constant [J/K]
pi = np.pi

# =============================================================================
# PLANCK UNITS — The encoder's fundamental resolution
# =============================================================================
l_p = np.sqrt(hbar * G / c**3)          # Planck length  ~ 1.616e-35 m
t_p = np.sqrt(hbar * G / c**5)          # Planck time    ~ 5.391e-44 s
m_p = np.sqrt(hbar * c / G)             # Planck mass    ~ 2.176e-8 kg
E_p = np.sqrt(hbar * c**5 / G)          # Planck energy  ~ 1.956e9 J
T_p = np.sqrt(hbar * c**5 / (G * k_B**2))  # Planck temp ~ 1.417e32 K
A_p = l_p**2                            # Planck area    ~ 2.612e-70 m²

# Solar mass for reference black holes
M_sun = 1.989e30  # kg

# =============================================================================
# ENCODER MODEL — Mapping physics to rotary encoder concepts
# =============================================================================

@dataclass
class EncoderState:
    """Represents a black hole as a Gray code rotary encoder."""
    mass_kg: float
    label: str = ""

    @property
    def schwarzschild_radius(self) -> float:
        """Encoder physical radius [m]."""
        return 2 * G * self.mass_kg / c**2

    @property
    def horizon_area(self) -> float:
        """Total encoder surface area [m²]."""
        r_s = self.schwarzschild_radius
        return 4 * pi * r_s**2

    @property
    def n_bits(self) -> float:
        """Number of encoder positions (Bekenstein-Hawking entropy in bits).
        S = A / (4 * l_p²) in natural units; S/ln(2) for bits."""
        return self.horizon_area / (4 * A_p * np.log(2))

    @property
    def n_nats(self) -> float:
        """Bekenstein-Hawking entropy in nats (natural units)."""
        return self.horizon_area / (4 * A_p)

    @property
    def angular_resolution_sr(self) -> float:
        """Angular resolution per bit [steradians].
        Total solid angle (4π) divided by number of bits."""
        return 4 * pi / self.n_bits

    @property
    def hawking_temperature(self) -> float:
        """Hawking temperature [K]."""
        return hbar * c**3 / (8 * pi * G * self.mass_kg * k_B)

    @property
    def hawking_luminosity(self) -> float:
        """Hawking radiation power [W] (Stefan-Boltzmann on horizon).
        L = σ * A * T⁴ where σ = π²k_B⁴/(60ℏ³c²)."""
        sigma = pi**2 * k_B**4 / (60 * hbar**3 * c**2)
        T = self.hawking_temperature
        A = self.horizon_area
        return sigma * A * T**4

    @property
    def evaporation_time(self) -> float:
        """Total Hawking evaporation time [s].
        t_evap = 5120 * π * G² * M³ / (ℏ * c⁴)."""
        M = self.mass_kg
        return 5120 * pi * G**2 * M**3 / (hbar * c**4)

    @property
    def bits_per_planck_time(self) -> float:
        """Rate at which encoder releases bits (Hawking luminosity / E_p * t_p).
        This is the key observable: how many encoder positions unwind per tick."""
        # Energy per bit ~ k_B * T_H (thermal bit)
        E_per_bit = k_B * self.hawking_temperature
        if E_per_bit == 0:
            return 0
        return self.hawking_luminosity / E_per_bit * t_p

    @property
    def alignment_probability(self) -> float:
        """Probability of infalling info aligning with the recursive loop
        per Planck time. P ~ 1/N."""
        N = self.n_bits
        if N == 0:
            return 0
        return 1.0 / N

    @property
    def gray_code_traversal_depth(self) -> float:
        """Number of Gray code flips needed to traverse all N positions.
        In standard reflected Gray code, a full cycle takes 2^n steps
        for n-bit code. But N positions ~ 2^n means log2(N) bits,
        so full traversal ~ N steps (each position visited once)."""
        return self.n_bits  # One flip per position in Gray code cycle

    def summary(self) -> str:
        """Human-readable summary."""
        lines = [
            f"{'='*60}",
            f"ENCODER STATE: {self.label or 'unnamed'}",
            f"{'='*60}",
            f"  Mass:                  {self.mass_kg:.3e} kg ({self.mass_kg/M_sun:.2e} M☉)",
            f"  Schwarzschild radius:  {self.schwarzschild_radius:.3e} m",
            f"  Horizon area:          {self.horizon_area:.3e} m²",
            f"  Encoder bits (N):      {self.n_bits:.3e}",
            f"  Angular res/bit:       {self.angular_resolution_sr:.3e} sr",
            f"  Hawking temperature:   {self.hawking_temperature:.3e} K",
            f"  Hawking luminosity:    {self.hawking_luminosity:.3e} W",
            f"  Evaporation time:      {self.evaporation_time:.3e} s ({self.evaporation_time/(3.154e7):.3e} yr)",
            f"  Bits/Planck time:      {self.bits_per_planck_time:.3e}",
            f"  Alignment prob/tick:   {self.alignment_probability:.3e}",
            f"{'='*60}",
        ]
        return "\n".join(lines)


# =============================================================================
# PRESET ENCODERS
# =============================================================================

def solar_mass_bh():
    return EncoderState(M_sun, "Solar Mass Black Hole")

def planck_mass_bh():
    return EncoderState(m_p, "Planck Mass (1-bit sweet spot)")

def sgr_a_star():
    return EncoderState(4.0e6 * M_sun, "Sgr A* (Milky Way center)")

def m87_star():
    return EncoderState(6.5e9 * M_sun, "M87* (first imaged BH)")

def primordial_bh(mass_kg=1e12):
    return EncoderState(mass_kg, f"Primordial BH ({mass_kg:.0e} kg)")

def custom_bh(mass_kg, label="Custom"):
    return EncoderState(mass_kg, label)
