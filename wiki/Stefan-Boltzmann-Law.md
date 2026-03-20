# Stefan-Boltzmann Law

## Definition

The **Stefan-Boltzmann law** states that the total power radiated by a blackbody is proportional to the fourth power of its temperature:

$$L = \sigma A T^4$$

where:
- $L$ = luminosity (power radiated, in watts)
- $\sigma = \frac{\pi^2 k_B^4}{60 \hbar^3 c^2} = 5.670374419 \times 10^{-8}$ W m⁻² K⁻⁴ (Stefan-Boltzmann constant)
- $A$ = surface area (m²)
- $T$ = temperature (K)

The law applies to **ideal blackbodies** — objects that absorb all incident radiation and emit thermally according to Planck's law.

## Historical Development

### Stefan's Empirical Discovery (1879)

Josef Stefan observed experimentally that the total radiated power scales as $T^4$. He measured thermal emission from heated platinum wires and found:

$$L \propto T^4$$

This was purely empirical — no theoretical justification.

### Boltzmann's Thermodynamic Derivation (1884)

Ludwig Boltzmann derived the $T^4$ law using **thermodynamics** and Maxwell's electromagnetic theory:

1. Consider radiation in a cavity at temperature $T$
2. Radiation pressure: $P = u/3$ (where $u$ = energy density)
3. From thermodynamics: $P = T \frac{\partial S}{\partial V}$ (pressure-entropy relation)
4. Energy density $u \propto T^4$ emerges from solving these equations
5. Luminosity $L = \sigma T^4$ follows from integrating over all frequencies

Boltzmann's derivation predated Planck's quantum theory by 15 years.

### Planck's Quantum Derivation (1900)

Max Planck derived the **spectral radiance** (energy per frequency per area):

$$B(\nu, T) = \frac{2h\nu^3}{c^2} \frac{1}{e^{h\nu / k_B T} - 1}$$

Integrating over all frequencies:

$$L = A \int_0^\infty B(\nu, T) \, d\nu = A \sigma T^4$$

where $\sigma = \frac{2\pi^5 k_B^4}{15 h^3 c^2}$ (using $h = 2\pi\hbar$, this gives the value above).

**This was the birth of quantum mechanics** — Planck introduced energy quantization ($E = h\nu$) to derive the correct blackbody spectrum.

## Connection to Black Hole Radiation

### Black Holes as Blackbodies

Stephen Hawking (1974) showed that black holes emit **thermal radiation** with a blackbody spectrum at temperature:

$$T_H = \frac{\hbar c^3}{8\pi G M k_B}$$

Applying the Stefan-Boltzmann law:

$$L = \sigma A T_H^4$$

where $A = 4\pi r_s^2 = 16\pi G^2 M^2 / c^4$ is the horizon area.

### Hawking Luminosity Formula

Substituting $T_H$ and $A$:

$$L = \sigma \cdot 16\pi \frac{G^2 M^2}{c^4} \cdot \left( \frac{\hbar c^3}{8\pi G M k_B} \right)^4$$

Simplify:

$$L = \sigma \cdot 16\pi \frac{G^2 M^2}{c^4} \cdot \frac{\hbar^4 c^{12}}{(8\pi)^4 G^4 M^4 k_B^4}$$

$$L = \sigma \cdot \frac{16\pi \hbar^4 c^{12}}{(8\pi)^4 G^2 M^2 k_B^4 c^4} = \sigma \cdot \frac{16\pi \hbar^4 c^8}{4096 \pi^4 G^2 M^2 k_B^4}$$

$$L = \frac{\sigma \hbar^4 c^8}{256 \pi^3 G^2 M^2 k_B^4}$$

Substitute $\sigma = \pi^2 k_B^4 / (60 \hbar^3 c^2)$:

$$L = \frac{\pi^2 k_B^4}{60 \hbar^3 c^2} \cdot \frac{\hbar^4 c^8}{256 \pi^3 G^2 M^2 k_B^4} = \frac{\hbar c^6}{60 \times 256 \pi G^2 M^2}$$

$$L = \frac{\hbar c^6}{15360 \pi G^2 M^2}$$

This is the **Hawking luminosity** — matches the detailed quantum field theory calculation.

### Key Scaling: $L \propto 1/M^2$

**Smaller black holes radiate more power**:
- 10× less massive → 100× more luminous
- Approach Planck mass → luminosity approaches Planck power

This is opposite to normal stars (more massive → more luminous).

## Numerical Examples

### 1. The Sun (Comparison)

- Surface temperature: $T_\odot = 5778$ K
- Radius: $R_\odot = 6.96 \times 10^8$ m
- Surface area: $A = 4\pi R_\odot^2 = 6.09 \times 10^{18}$ m²

Luminosity:

$$L_\odot = \sigma A T^4 = 5.67 \times 10^{-8} \times 6.09 \times 10^{18} \times (5778)^4$$

$$L_\odot \approx 3.83 \times 10^{26} \text{ W}$$

This matches the observed solar luminosity — Stefan-Boltzmann law works for stars.

### 2. Solar-Mass Black Hole

- Mass: $M = 1.989 \times 10^{30}$ kg
- Hawking temperature: $T_H = \frac{\hbar c^3}{8\pi G M k_B} = 6.17 \times 10^{-8}$ K
- Horizon area: $A = 16\pi G^2 M^2 / c^4 = 1.097 \times 10^{14}$ m²

Luminosity:

$$L = \sigma A T_H^4 = 5.67 \times 10^{-8} \times 1.097 \times 10^{14} \times (6.17 \times 10^{-8})^4$$

$$L \approx 9 \times 10^{-29} \text{ W}$$

**Comparison**: $L / L_\odot \approx 2 \times 10^{-55}$ — the black hole radiates $10^{55}$ times less than the Sun.

**Equivalent**: One infrared photon ($\sim 1$ eV $\sim 10^{-19}$ J) per $\sim 10^{10}$ seconds $\sim 300$ years.

### 3. Planck-Mass Black Hole

- Mass: $M_p = 2.176 \times 10^{-8}$ kg
- Hawking temperature: $T_H = \frac{\hbar c^3}{8\pi G M_p k_B} \approx 1.42 \times 10^{32}$ K
- Horizon area: $A = 16\pi (l_p)^2 = 8.26 \times 10^{-69}$ m²

Luminosity:

$$L = \sigma A T_H^4 \approx 5.67 \times 10^{-8} \times 8.26 \times 10^{-69} \times (1.42 \times 10^{32})^4$$

$$L \approx 3.6 \times 10^{52} \text{ W}$$

**Planck power**: $P_p = c^5 / G = 3.628 \times 10^{52}$ W

**Black hole emits at Planck power** — radiates all its mass-energy in $\sim$ one Planck time.

### 4. Mountain-Sized Black Hole

- Mass: $M = 10^{12}$ kg
- Hawking temperature: $T_H \approx 1.2 \times 10^{14}$ K
- Luminosity: $L \approx 3.6 \times 10^{11}$ W

**Equivalent**: 360 MW — comparable to a nuclear power plant.

**Evaporation time**: $\sim 2.6$ billion years (comparable to Earth's age).

## Greybody Factors

The Stefan-Boltzmann law assumes a **perfect blackbody** (emits/absorbs all radiation). Real objects have **emissivity** $\epsilon \leq 1$:

$$L = \epsilon \sigma A T^4$$

For black holes, the horizon is not a perfect blackbody — some radiation reflects off the curved spacetime before escaping. The **greybody factor** $\Gamma(\omega)$ accounts for this:

$$L = \int_0^\infty \Gamma(\omega) B(\omega, T_H) A \, d\omega$$

where $B(\omega, T_H)$ is the Planck spectrum.

For Schwarzschild black holes, $\Gamma(\omega) \approx 1$ at high frequencies (geometric optics limit), but $< 1$ at low frequencies (wavelength $\sim r_s$).

**Net effect**: Hawking luminosity is reduced by a factor $\sim 1$ to $10$ depending on particle species. The formula $L = \hbar c^6 / (15360 \pi G^2 M^2)$ includes averaged greybody factors.

## Derivation of Stefan-Boltzmann Constant

From Planck's law:

$$B(\nu, T) = \frac{2h\nu^3}{c^2} \frac{1}{e^{h\nu / k_B T} - 1}$$

Total energy flux (integrate over frequency and solid angle):

$$L / A = \int_0^\infty \pi B(\nu, T) \, d\nu$$

Change variables: $x = h\nu / (k_B T)$, $d\nu = (k_B T / h) dx$:

$$L / A = \pi \frac{2h}{c^2} \int_0^\infty \left( \frac{k_B T}{h} x \right)^3 \frac{1}{e^x - 1} \frac{k_B T}{h} \, dx$$

$$L / A = \frac{2\pi k_B^4 T^4}{h^3 c^2} \int_0^\infty \frac{x^3}{e^x - 1} \, dx$$

The integral:

$$\int_0^\infty \frac{x^3}{e^x - 1} \, dx = \frac{\pi^4}{15}$$

Therefore:

$$L / A = \frac{2\pi k_B^4 T^4}{h^3 c^2} \cdot \frac{\pi^4}{15} = \frac{2\pi^5 k_B^4 T^4}{15 h^3 c^2}$$

Using $h = 2\pi \hbar$:

$$L / A = \frac{2\pi^5 k_B^4 T^4}{15 (2\pi\hbar)^3 c^2} = \frac{2\pi^5 k_B^4 T^4}{15 \cdot 8\pi^3 \hbar^3 c^2} = \frac{\pi^2 k_B^4 T^4}{60 \hbar^3 c^2}$$

$$\sigma = \frac{\pi^2 k_B^4}{60 \hbar^3 c^2}$$

Numerically:

$$\sigma = \frac{(3.14159)^2 \times (1.381 \times 10^{-23})^4}{60 \times (1.055 \times 10^{-34})^3 \times (3 \times 10^8)^2} = 5.67 \times 10^{-8} \text{ W m}^{-2} \text{ K}^{-4}$$

## Connection to BlackOops

### 1. Evaporation Rate from Stefan-Boltzmann

In the encoder model, Hawking radiation is the release of encoder bits. The Stefan-Boltzmann law sets the **luminosity** (energy release rate):

$$L = \frac{dE}{dt} = c^2 \frac{dM}{dt}$$

From Stefan-Boltzmann:

$$\frac{dM}{dt} = -\frac{L}{c^2} = -\frac{\hbar c^4}{15360 \pi G^2 M^2}$$

Integrating:

$$\int_{M_0}^{0} M^2 \, dM = -\frac{\hbar c^4}{15360 \pi G^2} \int_0^{t_{evap}} dt$$

$$\frac{M_0^3}{3} = \frac{\hbar c^4}{15360 \pi G^2} t_{evap}$$

$$t_{evap} = \frac{5120 \pi G^2 M_0^3}{\hbar c^4}$$

This is Hawking's evaporation formula, derived from Stefan-Boltzmann + thermodynamics.

### 2. Bit Release Rate

Each bit corresponds to energy $\sim k_B T_H$ (thermal energy per degree of freedom). Bits released per second:

$$\frac{dN}{dt} \sim \frac{L}{k_B T_H}$$

Substituting:

$$\frac{dN}{dt} \sim \frac{\hbar c^6}{15360 \pi G^2 M^2 k_B T_H} = \frac{\hbar c^6}{15360 \pi G^2 M^2 k_B} \cdot \frac{8\pi G M k_B}{\hbar c^3}$$

$$\frac{dN}{dt} \sim \frac{8\pi c^3}{15360 \pi G M} = \frac{c^3}{1920 G M}$$

Total bits: $N = A / (4 l_p^2 \ln 2) \sim (GM/c^2)^2 / l_p^2$

Time to release all bits:

$$t \sim \frac{N}{dN/dt} \sim \frac{(GM/c^2)^2 / l_p^2}{c^3 / (GM)} \sim \frac{G^3 M^3}{c^7 l_p^2}$$

This scales as $M^3$, matching Hawking's formula.

### 3. Temperature and Encoder Bit Spacing

The Hawking temperature sets the **energy scale** for encoder bits. A bit flip releases energy $\sim k_B T_H$:

$$E_{bit} = k_B T_H = \frac{\hbar c^3}{8\pi G M}$$

For solar-mass black hole:

$$E_{bit} = \frac{1.055 \times 10^{-34} \times (3 \times 10^8)^3}{8\pi \times 6.67 \times 10^{-11} \times 1.989 \times 10^{30}} \approx 8.5 \times 10^{-31} \text{ J}$$

**Equivalent**: $5.3 \times 10^{-12}$ eV (far infrared photon, wavelength $\sim 47$ km).

The encoder's "energy resolution" is $\sim k_B T_H$ — releasing one bit changes the black hole's energy by this amount.

### 4. Planck-Mass Saturation

At Planck mass, $T_H \sim T_p$ (Planck temperature):

$$L \sim \sigma \times 16\pi l_p^2 \times T_p^4 \sim P_p$$

The black hole radiates at **Planck power** — maximum possible luminosity in quantum gravity. This is the "1-bit encoder self-destruct" regime.

## See Also

- [[Hawking Radiation]]
- [[Bekenstein-Hawking Entropy]]
- [[Planck Units]]
- [[Blackbody Radiation]]
- [[Thermodynamic Laws]]

## References

1. Stefan, J. (1879). "Über die Beziehung zwischen der Wärmestrahlung und der Temperatur". *Sitzungsberichte der Kaiserlichen Akademie der Wissenschaften Wien*, 79, 391–428.
2. Boltzmann, L. (1884). "Ableitung des Stefan'schen Gesetzes, betreffend die Abhängigkeit der Wärmestrahlung von der Temperatur". *Annalen der Physik*, 258(6), 291–294.
3. Planck, M. (1901). "Über das Gesetz der Energieverteilung im Normalspektrum". *Annalen der Physik*, 309(3), 553–563.
4. Hawking, S. W. (1975). "Particle Creation by Black Holes". *Communications in Mathematical Physics*, 43(3), 199–220.
