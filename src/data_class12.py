from helpers import p, lst, olist, formula, diagram, sticky, mnemonic, section, chapter, derivation, solved, mistake, tip, pyq

CLASS_LABEL = "Class XII"
CLASS_TITLE = "Class XII Physics — CHSE Odisha (+2 2nd Year)"
CLASS_INTRO = ("Electricity, magnetism, optics and modern physics — the year that explains phones, "
               "power grids, glasses, X-rays and nuclear reactors, all with the same handful of laws. "
               "Every chapter has derivations, solved numericals and an Exam Corner to push you past 90%.")

UNITS = []

def add_unit(roman, name, chapters):
    UNITS.append({"roman": roman, "name": name, "chapters": chapters})

# ----------------------------------------------------------------------
add_unit("I", "Electrostatics", [
chapter("ch01", 1, "Electric Charges and Fields",
  "Two kinds of charge, one law, and an invisible field connecting every one of them.",
  ["Coulomb's law", "electric field", "Gauss's law"],
  sections=[
    section("Charge & Coulomb's Law", [
      p("Charge is <b>conserved</b> (total charge of an isolated system never changes) and <b>quantised</b> "
        "(always an integer multiple of e = 1.6×10⁻¹⁹ C). Like charges repel, unlike charges attract."),
      formula("Coulomb's law", ["F = k q1q2 / r²  ,  k = 1/(4πε0) ≈ 9 × 10⁹ N m² C⁻²"]),
      p("For multiple charges, the net force on any charge is the <b>vector sum</b> of forces due to each other "
        "charge individually — the superposition principle."),
      solved(
        "Two point charges +2μC and +3μC are placed 30 cm apart. Find the force between them.",
        [
          "F = kq1q2/r² = 9×10⁹ × 2×10⁻⁶ × 3×10⁻⁶ / (0.3)²",
          "= 9×10⁹ × 6×10⁻¹² / 0.09 = 54×10⁻³/0.09",
        ],
        "F = 0.6 N (repulsive)",
      ),
      mistake("Forgetting to convert μC to C, or cm to m, before substituting into Coulomb's law is the single most common numerical error in this chapter."),
    ]),
    section("Electric Field & Dipoles", [
      diagram("pointChargeField", "Electric field lines radiate outward from a positive point charge.", 420, 260),
      formula("Electric field", ["E = F/q = kQ/r²  (due to a point charge)"]),
      diagram("dipoleField", "An electric dipole: field lines run from the +ve to the −ve charge.", 460, 220),
      derivation("Electric field on the equatorial line of a dipole", "A dipole of charges +q and −q separated by 2a; point P on the perpendicular bisector at distance r from the centre.",
        [
          "Field due to +q and −q at P have equal magnitude kq/(r²+a²) each, directed along the lines joining charge to P.",
          "Components perpendicular to the dipole axis cancel by symmetry; components along the axis (anti-parallel to p) add.",
          "Each component along axis = [kq/(r²+a²)] × [a/√(r²+a²)]; total E = 2kqa/(r²+a²)^(3/2) = kp/(r²+a²)^(3/2)",
          "For r ≫ a: E ≈ kp/r³ (opposite direction to dipole moment p)",
        ],
        "Eequatorial = kp/(r²+a²)^(3/2) ≈ kp/r³ for r ≫ a"),
      formula("Electric dipole", [
        "Dipole moment: p = q × 2a  (from −q to +q)",
        "Axial field: Eaxial = 2kpr/(r²−a²)² ≈ 2kp/r³",
        "Torque in uniform field: τ = p × E",
      ]),
    ]),
    section("Electric Flux & Gauss's Law", [
      diagram("gaussSurface", "A Gaussian surface enclosing a charge — flux through it depends only on the enclosed charge.", 460, 260),
      formula("Gauss's law", ["Φ = ∮E·dA = qenclosed / ε0"]),
      derivation("Electric field due to an infinite line charge (using Gauss's law)", "A uniformly charged infinite line with linear charge density λ; choose a cylindrical Gaussian surface of radius r and length L, coaxial with the line.",
        [
          "By symmetry, E is radial and has the same magnitude at every point on the curved surface.",
          "Flux through flat circular ends = 0 (E is parallel to these surfaces); flux through curved surface = E × 2πrL",
          "By Gauss's law: E × 2πrL = λL/ε0",
        ],
        "E = λ/(2πε0r)"),
      p("Gauss's law makes it easy to find E for highly symmetric charge distributions — infinite line charge, "
        "infinite sheet, and uniformly charged spherical shell — without doing messy integrals directly."),
      sticky("Handy results", "Infinite line charge: E = λ/2πε0r &middot; Infinite sheet: E = σ/2ε0 &middot; "
             "Charged spherical shell (outside): E = kQ/r² (behaves like a point charge!)", "blue"),
    ]),
  ],
  recap=[
    "Charge is conserved and quantised (q = ne).",
    "Coulomb's law: F = kq1q2/r²; superposition gives net force from multiple charges.",
    "Electric field E = F/q; dipole moment p = q(2a); torque τ = p×E.",
    "Gauss's law: Φ = qenc/ε0 — powerful for symmetric charge distributions.",
  ],
  exam_corner=[
    pyq(1, "What is the SI unit of electric dipole moment?"),
    pyq(1, "State Gauss's law in electrostatics."),
    pyq(2, "Two charges of +4μC and −4μC are 20 cm apart. Find the electric field at the midpoint between them."),
    pyq(2, "Write the expression for torque on an electric dipole placed in a uniform electric field, defining all terms."),
    pyq(3, "Derive the expression for electric field due to an infinite plane sheet of charge using Gauss's law."),
    pyq(5, "State Gauss's law and derive the expression for the electric field due to an infinitely long straight uniformly charged wire at a point at perpendicular distance r from it."),
  ]),

chapter("ch02", 2, "Electrostatic Potential and Capacitance",
  "Energy per unit charge — and the clever devices built to store it.",
  ["electric potential", "capacitors", "dielectrics"],
  sections=[
    section("Electric Potential", [
      p("<b>Electric potential (V)</b> at a point = work done per unit charge in bringing a small test charge from "
        "infinity to that point, without acceleration."),
      formula("Potential", ["V = kQ/r  (point charge)", "Potential energy of two charges: U = kq1q2/r"]),
      p("<b>Equipotential surfaces</b> are surfaces where potential is the same everywhere — no work is done moving "
        "a charge along one, and field lines are always perpendicular to them."),
      solved(
        "Find the potential at a point 20 cm from a point charge of 5μC.",
        ["V = kQ/r = 9×10⁹ × 5×10⁻⁶ / 0.2"],
        "V = 2.25×10⁵ V",
      ),
    ]),
    section("Capacitors & Capacitance", [
      diagram("parallelPlateCapacitor", "A parallel plate capacitor stores equal and opposite charge on its two plates.", 460, 220),
      derivation("Capacitance of a parallel plate capacitor", "Two parallel plates of area A separated by distance d in vacuum, with charge ±Q.",
        [
          "Electric field between the plates (from Gauss's law for a conductor's surface): E = σ/ε0 = Q/(Aε0)",
          "Potential difference V = E × d = Qd/(Aε0)",
          "Capacitance C = Q/V = Q / [Qd/(Aε0)]",
        ],
        "C = ε0A/d"),
      formula("Capacitance", [
        "C = Q/V",
        "Parallel plate capacitor: C = ε0A/d  (vacuum), C = Kε0A/d  (with dielectric of constant K)",
        "Energy stored: U = ½CV² = ½QV = Q²/2C",
      ]),
      solved(
        "A parallel plate capacitor has plate area 0.02 m² and separation 1 mm. Find its capacitance and the energy stored when charged to 200 V. (ε0 = 8.85×10⁻¹² F/m)",
        [
          "C = ε0A/d = 8.85×10⁻¹² × 0.02/0.001 = 1.77×10⁻¹⁰ F",
          "U = ½CV² = ½ × 1.77×10⁻¹⁰ × (200)² = ½ × 1.77×10⁻¹⁰ × 40000",
        ],
        "C ≈ 177 pF, U ≈ 3.54×10⁻⁶ J",
      ),
    ]),
    section("Combinations of Capacitors", [
      formula("Series & parallel combination", [
        "Series: 1/Ceq = 1/C1 + 1/C2 + …   (charge same on each, voltage adds)",
        "Parallel: Ceq = C1 + C2 + …   (voltage same on each, charge adds)",
      ]),
      mnemonic("Capacitors in series behave like resistors in parallel (and vice-versa) — the formulas literally "
               "swap roles!"),
      tip("When a question gives 'n identical capacitors of capacitance C', memorise: series → Ceq = C/n; parallel → Ceq = nC. This shortcut saves crucial time."),
    ]),
  ],
  recap=[
    "Potential V = work/charge; equipotential surfaces ⊥ field lines, no work done moving along them.",
    "C = Q/V; parallel plate capacitor C = Kε0A/d.",
    "Energy stored in a capacitor: U = ½CV².",
    "Series capacitors: 1/Ceq adds; Parallel capacitors: Ceq adds directly.",
  ],
  exam_corner=[
    pyq(1, "Define electric potential at a point."),
    pyq(1, "What happens to the capacitance of a parallel plate capacitor if a dielectric slab is inserted between the plates?"),
    pyq(2, "Three capacitors of 2μF, 3μF, 6μF are connected in series. Find the equivalent capacitance."),
    pyq(2, "Why do equipotential surfaces never intersect each other?"),
    pyq(3, "Derive the expression for capacitance of a parallel plate capacitor with vacuum between the plates."),
    pyq(5, "Derive the expression for energy stored in a charged capacitor. Two capacitors 4μF and 6μF are connected in parallel across a 10V battery — find total charge and total energy stored."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("II", "Current Electricity", [
chapter("ch03", 3, "Current Electricity",
  "Ohm's law, resistors, and the two rules that solve any circuit ever drawn.",
  ["Ohm's law", "resistivity", "Kirchhoff's rules", "Wheatstone bridge"],
  sections=[
    section("Current, Drift Velocity & Ohm's Law", [
      p("Electric current is the rate of flow of charge: <b>I = q/t</b>. Inside a conductor, free electrons don't "
        "travel in straight lines at high speed — they drift slowly (drift velocity vd) superimposed on their random "
        "thermal motion, under the push of an electric field."),
      diagram("simpleCircuit", "A simple circuit: a cell drives current I through a resistor R.", 440, 220),
      derivation("Relation between current and drift velocity", "Consider a conductor of length L, area A, with n free electrons per unit volume, each moving with drift velocity vd.",
        [
          "In time t, each electron moves a distance vdt, so all electrons within a volume A×(vdt) cross a given cross-section.",
          "Number of electrons crossing = n × A × vd × t",
          "Total charge crossing q = n A vd t e, so current I = q/t = nAvde",
        ],
        "I = nAvde"),
      formula("Ohm's law & resistivity", [
        "V = IR  (Ohm's law, for ohmic conductors)",
        "R = ρL/A   (ρ = resistivity, a material property)",
        "I = neAvd   (n = free electron density)",
      ]),
      solved(
        "A wire of resistivity 1.7×10⁻⁸ Ωm, length 2 m and area 1 mm² carries a current of 2 A from a 0.068 V source. Verify Ohm's law by finding R two ways.",
        [
          "From geometry: R = ρL/A = 1.7×10⁻⁸ × 2 / 1×10⁻⁶ = 0.034 Ω",
          "From Ohm's law: R = V/I = 0.068/2 = 0.034 Ω — both match!",
        ],
        "R = 0.034 Ω",
      ),
      p("Resistance generally <b>increases with temperature</b> for metals (more collisions), but decreases for "
        "semiconductors (more charge carriers get freed as temperature rises)."),
    ]),
    section("Cells, EMF & Internal Resistance", [
      formula("Cell equations", ["EMF ε = V + Ir  (r = internal resistance)", "Terminal voltage: V = ε − Ir"]),
      lst([
        "Cells in <b>series</b>: EMFs add, useful for higher voltage.",
        "Cells in <b>parallel</b>: useful for higher current, EMF stays same as one cell (if identical cells).",
      ]),
      solved(
        "A cell of EMF 2V and internal resistance 0.5Ω is connected to an external resistance of 4.5Ω. Find the current and terminal voltage.",
        [
          "I = ε/(R+r) = 2/(4.5+0.5) = 2/5 = 0.4 A",
          "V = ε − Ir = 2 − 0.4×0.5 = 2 − 0.2 = 1.8 V",
        ],
        "I = 0.4 A, V = 1.8 V",
      ),
    ]),
    section("Kirchhoff's Rules & Wheatstone Bridge", [
      formula("Kirchhoff's rules", [
        "Junction rule (charge conservation): ΣIin = ΣIout at any junction",
        "Loop rule (energy conservation): ΣV = 0 around any closed loop",
      ]),
      p("The <b>Wheatstone bridge</b> is a clever four-resistor circuit used to measure an unknown resistance precisely "
        "— when the bridge is 'balanced' (no current through the galvanometer), P/Q = R/S."),
      mistake("In Kirchhoff's loop rule, sign convention errors (treating a voltage rise as a drop or vice versa while tracing the loop) is the top reason for wrong answers — always fix a direction and stick to it."),
    ]),
  ],
  recap=[
    "I = q/t; V = IR for ohmic conductors; R = ρL/A.",
    "Drift velocity is the slow, net electron motion caused by the applied field.",
    "EMF = V + Ir; terminal voltage drops as current drawn increases.",
    "Kirchhoff's junction rule (charge conservation) + loop rule (energy conservation) solve any circuit.",
  ],
  exam_corner=[
    pyq(1, "Define drift velocity of electrons."),
    pyq(1, "State Kirchhoff's junction rule."),
    pyq(2, "Derive the relation I = neAvd between current and drift velocity."),
    pyq(2, "A cell of EMF 1.5V and internal resistance 1Ω is short-circuited. Find the current drawn."),
    pyq(3, "State Kirchhoff's rules and explain the principle of a balanced Wheatstone bridge."),
    pyq(5, "Derive the relation between electric current and drift velocity of electrons in a conductor. In a Wheatstone bridge P=10Ω, Q=20Ω, R=15Ω, find S for the bridge to be balanced."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("III", "Magnetic Effects of Current and Magnetism", [
chapter("ch04", 4, "Moving Charges and Magnetism",
  "Electric current isn't just about voltage — it also makes its own magnetic field.",
  ["Biot-Savart law", "Ampere's law", "force on charges", "galvanometer"],
  sections=[
    section("Biot–Savart Law & Ampere's Law", [
      diagram("wireFieldLines", "Magnetic field forms concentric circles around a current-carrying straight wire.", 440, 260),
      formula("Field due to currents", [
        "Biot–Savart law: dB = (μ0/4π) · I dl × r̂ / r²",
        "Field at centre of circular loop: B = μ0I / 2R",
        "Long straight wire: B = μ0I / 2πr",
        "Ideal solenoid (inside): B = μ0nI  (n = turns per unit length)",
      ]),
      derivation("Magnetic field at the centre of a current-carrying circular loop", "A circular loop of radius R carrying current I; using the Biot-Savart law for each element dl.",
        [
          "By Biot-Savart law, field due to element dl at the centre: dB = (μ0/4π)(I dl sin90°)/R² (since dl ⊥ r̂ for every element at the centre)",
          "All dB contributions point in the same direction (along the axis) by symmetry, so they add directly.",
          "B = ∮dB = (μ0I/4πR²) ∮dl = (μ0I/4πR²)(2πR)",
        ],
        "B = μ0I/2R"),
      solved(
        "Find the magnetic field at the centre of a circular coil of radius 10 cm carrying 5 A current. (μ0 = 4π×10⁻⁷ T·m/A)",
        ["B = μ0I/2R = (4π×10⁻⁷ × 5)/(2×0.1)"],
        "B ≈ 3.14×10⁻⁵ T",
      ),
    ]),
    section("Force on Moving Charges & Current-Carrying Conductors", [
      formula("Magnetic forces", [
        "Force on a moving charge: F = qv × B  (magnitude qvB sinθ)",
        "Force on current-carrying wire: F = IL × B",
        "Force between two parallel wires: F/L = μ0I1I2 / 2πd",
      ]),
      p("This last formula literally <b>defines the ampere</b> — the SI base unit of current!"),
      solved(
        "A straight wire of length 0.5 m carrying 4 A current is placed perpendicular to a magnetic field of 0.2 T. Find the force on it.",
        ["F = BIL sinθ, θ=90° → F = 0.2 × 4 × 0.5"],
        "F = 0.4 N",
      ),
    ]),
    section("Current Loop & Moving-Coil Galvanometer", [
      diagram("currentLoopTorque", "A current loop in a magnetic field experiences a torque — the working principle of a galvanometer/motor.", 440, 220),
      formula("Current loop as a magnetic dipole", ["Magnetic moment: m = IA", "Torque: τ = m × B"]),
      p("A <b>moving coil galvanometer</b> uses exactly this torque to deflect a coil (and pointer) proportional to "
        "current. Adding a small shunt resistance converts it to an <b>ammeter</b>; adding a large resistance in "
        "series converts it to a <b>voltmeter</b>."),
      mistake("A galvanometer is converted to an ammeter using a LOW shunt resistance in PARALLEL, and to a voltmeter using a HIGH resistance in SERIES — students frequently mix these up."),
    ]),
  ],
  recap=[
    "Biot–Savart law gives dB due to a current element; use it (or Ampere's law) to find B for wires, loops, solenoids.",
    "Force on moving charge: F = qv×B; force on wire: F = IL×B.",
    "Parallel currents in the same direction attract; opposite directions repel.",
    "Galvanometer + small shunt = ammeter; galvanometer + large series resistance = voltmeter.",
  ],
  exam_corner=[
    pyq(1, "Write the SI unit of magnetic field (magnetic flux density)."),
    pyq(1, "How is a galvanometer converted into an ammeter?"),
    pyq(2, "State the Biot-Savart law and write its mathematical expression."),
    pyq(2, "Two parallel wires carrying current in the same direction — do they attract or repel? Why?"),
    pyq(3, "Derive the expression for magnetic field at the centre of a current-carrying circular coil."),
    pyq(5, "State and derive the expression for the force between two long parallel current-carrying conductors, and use it to define the ampere. Two parallel wires 1 m apart carry 5A and 8A in the same direction — find the force per unit length between them."),
  ]),

chapter("ch05", 5, "Magnetism and Matter",
  "Every magnet is secretly just current loops, arranged neatly.",
  ["bar magnet", "magnetic dipole", "dia/para/ferro-magnetism"],
  sections=[
    section("Bar Magnet as an Equivalent Solenoid", [
      diagram("solenoidField", "A bar magnet behaves like a solenoid — field lines emerge from N, curve around, and enter S.", 460, 200),
      p("A bar magnet's field pattern outside closely matches that of a finite solenoid carrying current — this "
        "connects 'ordinary' magnets to the same physics as current loops."),
      formula("Magnetic dipole (bar magnet)", ["Magnetic dipole moment: m = qm × 2l", "Torque in uniform field: τ = m × B"]),
      solved(
        "A bar magnet of dipole moment 2 A·m² is placed in a uniform field of 0.5 T at 30° to the field. Find the torque on it.",
        ["τ = mB sinθ = 2 × 0.5 × sin30° = 1 × 0.5"],
        "τ = 0.5 N·m",
      ),
    ]),
    section("Classifying Magnetic Materials", [
      lst([
        "<b>Diamagnetic:</b> weakly repelled by a magnetic field; no permanent dipole moment (e.g. bismuth, copper).",
        "<b>Paramagnetic:</b> weakly attracted; have permanent atomic dipoles that partially align with the field "
        "(e.g. aluminium, sodium).",
        "<b>Ferromagnetic:</b> strongly attracted; dipoles align in large domains, retaining magnetisation even after "
        "the field is removed (e.g. iron, cobalt, nickel).",
      ]),
      sticky("Effect of temperature", "Above a critical temperature (Curie temperature), ferromagnetic materials lose "
             "their strong magnetism and start behaving like paramagnetic materials — thermal agitation disrupts the "
             "aligned domains.", "pink"),
    ]),
  ],
  recap=[
    "A bar magnet's external field pattern resembles a finite current-carrying solenoid.",
    "Magnetic dipole moment m = qm(2l); torque τ = m×B.",
    "Diamagnetic: weakly repelled. Paramagnetic: weakly attracted. Ferromagnetic: strongly attracted, retains magnetism.",
    "Above the Curie temperature, ferromagnets become paramagnetic.",
  ],
  exam_corner=[
    pyq(1, "Define Curie temperature."),
    pyq(1, "Give one example each of a diamagnetic and a ferromagnetic material."),
    pyq(2, "Distinguish between paramagnetic and ferromagnetic materials."),
    pyq(2, "A bar magnet of moment 5 A·m² is held perpendicular to a field of 0.3 T. Find the torque acting on it."),
    pyq(3, "Compare the magnetic field pattern of a bar magnet with that of a solenoid."),
    pyq(5, "Explain diamagnetism, paramagnetism and ferromagnetism with reference to atomic dipole alignment, and describe the effect of temperature on each."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("IV", "Electromagnetic Induction and Alternating Currents", [
chapter("ch06", 6, "Electromagnetic Induction",
  "Move a magnet near a wire and — with no battery at all — current appears.",
  ["Faraday's law", "Lenz's law", "self & mutual induction"],
  sections=[
    section("Faraday's Laws & Lenz's Law", [
      diagram("emiMagnetCoil", "Moving a magnet near a coil changes flux through it, inducing an EMF and current.", 440, 220),
      formula("Faraday's law of EM induction", ["ε = −dΦ/dt   (Φ = magnetic flux = B·A cosθ)"]),
      p("The <b>negative sign (Lenz's law)</b> says the induced current always opposes the very change that produced "
        "it — this is really just conservation of energy in disguise: you must do work to push the magnet in "
        "precisely because the induced current fights back."),
      derivation("Motional EMF", "A rod of length l moves with velocity v perpendicular to a uniform magnetic field B, sliding on rails.",
        [
          "Free electrons in the rod experience a magnetic force F = e(v×B), pushing them to one end.",
          "This charge separation creates an electric field inside the rod; equilibrium is reached when electric force balances magnetic force: eE = evB → E = vB",
          "EMF = E × l (potential difference across the rod)",
        ],
        "ε = Bvl"),
      solved(
        "A rod of length 0.5 m moves at 4 m/s perpendicular to a magnetic field of 0.2 T. Find the induced EMF.",
        ["ε = Bvl = 0.2 × 4 × 0.5"],
        "ε = 0.4 V",
      ),
    ]),
    section("Self and Mutual Induction", [
      lst([
        "<b>Self-inductance (L):</b> a coil induces an EMF in <i>itself</i> when its own current changes — opposes any "
        "sudden change in current (like electrical inertia).",
        "<b>Mutual inductance (M):</b> a changing current in one coil induces EMF in a <i>nearby</i> coil — the basic "
        "principle behind transformers.",
      ]),
      formula("Induced EMF from inductance", ["ε = −L(dI/dt)  (self)", "ε2 = −M(dI1/dt)  (mutual)"]),
      mistake("Lenz's law direction questions are commonly answered backward under pressure — always re-derive the direction using 'induced current opposes the change in flux', don't just guess."),
    ]),
  ],
  recap=[
    "Faraday's law: induced EMF = −rate of change of magnetic flux.",
    "Lenz's law: induced current opposes the change producing it (energy conservation).",
    "Self-inductance opposes change in its own current; mutual inductance links two coils.",
  ],
  exam_corner=[
    pyq(1, "State Lenz's law."),
    pyq(1, "Define coefficient of self-inductance and give its SI unit."),
    pyq(2, "State Faraday's laws of electromagnetic induction."),
    pyq(2, "A coil of 100 turns has a flux of 0.02 Wb linked through it, which drops to zero in 0.1 s. Find the induced EMF."),
    pyq(3, "Derive the expression for motional EMF induced in a conducting rod moving through a magnetic field."),
    pyq(5, "State and explain Faraday's law and Lenz's law of electromagnetic induction with an appropriate diagram, and show how Lenz's law follows from the principle of conservation of energy."),
  ]),

chapter("ch07", 7, "Alternating Current",
  "Current that keeps changing its mind about direction, 50 times a second in India.",
  ["AC circuits", "LCR circuit", "resonance", "transformer"],
  sections=[
    section("AC Basics & rms Values", [
      diagram("acWaveform", "Voltage and current in an AC circuit can be out of phase depending on the circuit elements.", 460, 220),
      formula("AC fundamentals", [
        "v(t) = v0 sinωt , i(t) = i0 sin(ωt − φ)",
        "rms value: vrms = v0/√2  (what your multimeter reads!)",
      ]),
      solved(
        "The peak voltage of the AC mains in India is about 311 V. Find its rms value.",
        ["vrms = v0/√2 = 311/1.414"],
        "vrms ≈ 220 V",
      ),
    ]),
    section("Reactance, Impedance & Series LCR Resonance", [
      derivation("Impedance of a series LCR circuit", "A resistor R, inductor L and capacitor C in series, carrying current i(t) = i0 sinωt.",
        [
          "Voltage across R is in phase with current: VR = i0R",
          "Voltage across L leads current by 90°: VL = i0XL (XL = ωL); voltage across C lags current by 90°: VC = i0XC (XC = 1/ωC)",
          "Using a phasor diagram, VL and VC are opposite (180° apart), so net reactive voltage = i0(XL − XC)",
          "Resultant voltage (phasor sum of VR and net reactive voltage): V0 = i0√(R² + (XL−XC)²)",
        ],
        "Z = V0/i0 = √(R² + (XL − XC)²)"),
      formula("Reactance & impedance in a series LCR circuit", [
        "Inductive reactance: XL = ωL",
        "Capacitive reactance: XC = 1/ωC",
        "Impedance: Z = √(R² + (XL − XC)²)",
        "Resonance (Z minimum, current maximum) at: ω0 = 1/√(LC)",
      ]),
      formula("Power in AC circuits", ["Average power: P = vrms irms cosφ   (cosφ = power factor)"]),
      solved(
        "A series LCR circuit has R=30Ω, XL=50Ω, XC=10Ω. Find the impedance and the phase angle.",
        [
          "Z = √(R² + (XL−XC)²) = √(30² + 40²) = √(900+1600) = √2500",
          "tanφ = (XL−XC)/R = 40/30 = 1.33",
        ],
        "Z = 50 Ω, φ ≈ 53° (voltage leads current, since XL > XC)",
      ),
      sticky("Wattless current", "In a purely inductive or purely capacitive AC circuit, average power consumed is "
             "zero even though current flows — this is called 'wattless current' (cosφ = 0, since φ = 90°).", "yellow"),
    ]),
    section("AC Generator & Transformer", [
      diagram("transformerCore", "A transformer changes AC voltage using two coils linked by a common iron core.", 460, 200),
      p("An <b>AC generator</b> converts mechanical energy to electrical energy using EM induction — a coil rotates "
        "in a magnetic field, and flux through it changes sinusoidally, inducing a sinusoidal EMF."),
      formula("Ideal transformer relation", ["Vs/Vp = Ns/Np = Ip/Is"]),
      solved(
        "A step-down transformer converts 220V to 11V. If the primary coil has 2000 turns, find the number of secondary turns.",
        ["Ns/Np = Vs/Vp → Ns = Np × Vs/Vp = 2000 × 11/220"],
        "Ns = 100 turns",
      ),
    ]),
  ],
  recap=[
    "rms value = peak/√2; this is what AC meters actually display.",
    "Series LCR: Z = √(R²+(XL−XC)²); resonance at ω0 = 1/√(LC), where Z is minimum.",
    "Average AC power = vrmsirmscosφ; wattless current occurs when φ = 90°.",
    "Transformer: Vs/Vp = Ns/Np — steps voltage up or down using mutual induction.",
  ],
  exam_corner=[
    pyq(1, "What is the value of power factor in a pure inductor circuit?"),
    pyq(1, "Write the relation between rms value and peak value of AC."),
    pyq(2, "Define resonant frequency of a series LCR circuit and write its formula."),
    pyq(2, "A transformer has 500 turns in primary and 100 turns in secondary. If primary voltage is 220V, find the secondary voltage."),
    pyq(3, "Derive the expression for impedance of a series LCR circuit using a phasor diagram."),
    pyq(5, "Explain resonance in a series LCR circuit and derive the resonant frequency. A series LCR circuit has L=0.5H, C=8μF, R=10Ω — find the resonant frequency and the impedance at resonance."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("V", "Electromagnetic Waves", [
chapter("ch08", 8, "Electromagnetic Waves",
  "Light, radio, X-rays and gamma rays — all one family, just different wavelengths.",
  ["displacement current", "EM wave properties", "EM spectrum"],
  sections=[
    section("Displacement Current & the Need for it", [
      p("Maxwell noticed Ampere's law alone gave inconsistent results for circuits with a capacitor (current seems to "
        "'break' between the plates). He fixed this by proposing a <b>displacement current</b> — arising from a "
        "changing electric field — which exists even where no charge physically flows."),
      formula("Displacement current", ["Id = ε0 (dΦE/dt)"]),
    ]),
    section("Properties of Electromagnetic Waves", [
      lst([
        "EM waves are produced by <b>accelerating charges</b> and consist of oscillating electric and magnetic fields.",
        "They are <b>transverse</b>: E, B and the direction of propagation are mutually perpendicular.",
        "They require <b>no medium</b> — can travel through vacuum, unlike sound.",
        "All EM waves travel at speed <b>c</b> in vacuum, regardless of wavelength.",
      ]),
    ]),
    section("The Electromagnetic Spectrum", [
      diagram("emSpectrumBar", "The EM spectrum, arranged by increasing frequency (decreasing wavelength).", 500, 160),
      formula("Speed of EM waves", ["c = 1/√(μ0ε0) ≈ 3 × 10⁸ m/s = f λ"]),
      solved(
        "Find the frequency of an EM wave of wavelength 600 nm (visible light).",
        ["f = c/λ = 3×10⁸ / 600×10⁻⁹"],
        "f = 5×10¹⁴ Hz",
      ),
      sticky("Quick uses", "Radio: broadcasting &middot; Microwave: radar, cooking &middot; IR: remote controls, thermal "
             "imaging &middot; Visible: seeing! &middot; UV: sterilisation &middot; X-ray: medical imaging &middot; "
             "Gamma: cancer treatment, nuclear studies", "blue"),
    ]),
  ],
  recap=[
    "Displacement current (ε0 dΦE/dt) completes Ampere's law where conduction current is absent.",
    "EM waves: transverse, self-sustaining oscillations of E and B, need no medium.",
    "All EM waves travel at c in vacuum; they differ only in frequency/wavelength.",
    "EM spectrum order (low→high frequency): radio, micro, IR, visible, UV, X-ray, gamma.",
  ],
  exam_corner=[
    pyq(1, "Why did Maxwell introduce the concept of displacement current?"),
    pyq(1, "Arrange radio waves, X-rays and visible light in order of increasing frequency."),
    pyq(2, "State any two properties of electromagnetic waves."),
    pyq(2, "Name the part of the EM spectrum used in (a) treating cancer (b) remote controls."),
    pyq(3, "Explain the concept of displacement current and its role in Ampere's law."),
    pyq(5, "Describe the electromagnetic spectrum, listing the different regions in order with one use of each, and explain why electromagnetic waves are called transverse waves."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("VI", "Optics", [
chapter("ch09", 9, "Ray Optics and Optical Instruments",
  "Light drawn as straight-line rays — enough to design every lens and mirror ever made.",
  ["reflection & refraction", "lenses & mirrors", "optical instruments"],
  sections=[
    section("Reflection, Refraction & Total Internal Reflection", [
      formula("Mirror & refraction formulas", [
        "Mirror formula: 1/v + 1/u = 1/f",
        "Snell's law: n1 sinθ1 = n2 sinθ2",
      ]),
      diagram("totalInternalReflection", "Beyond the critical angle, light reflects entirely back into the denser medium.", 460, 220),
      p("<b>Total internal reflection</b> happens when light travels from a denser to a rarer medium at an angle "
        "greater than the <b>critical angle</b> — the basis of optical fibres carrying data as light pulses."),
      solved(
        "The critical angle for a glass-air interface is 42°. Find the refractive index of glass.",
        ["sinθc = 1/n → n = 1/sin42° = 1/0.669"],
        "n ≈ 1.49",
      ),
    ]),
    section("Lenses", [
      diagram("convexLensRay", "A convex lens converges parallel rays to a focus, forming a real, inverted image here.", 460, 240),
      derivation("Mirror formula (concave mirror, real image)", "An object is placed beyond the centre of curvature of a concave mirror of focal length f; using similar triangles from the ray diagram.",
        [
          "From similar triangles (object/image height vs. their distances from the pole): comparing triangles formed by the incident ray through the centre of curvature and the mirror,",
          "Using sign convention and simplifying the geometric relation between object distance u, image distance v and focal length f",
        ],
        "1/v + 1/u = 1/f"),
      formula("Lens formulas", [
        "Thin lens formula: 1/v − 1/u = 1/f",
        "Lens maker's formula: 1/f = (n−1)(1/R1 − 1/R2)",
        "Power of a lens: P = 1/f (f in metres, P in dioptre)",
        "Combination of thin lenses in contact: 1/F = 1/f1 + 1/f2 + …",
      ]),
      solved(
        "An object is placed 30 cm in front of a convex lens of focal length 10 cm. Find the image distance and magnification.",
        [
          "1/v − 1/u = 1/f → 1/v = 1/f + 1/u = 1/10 + 1/(−30) [taking u = −30 cm by sign convention]",
          "1/v = 3/30 − 1/30 = 2/30 → v = 15 cm",
          "Magnification m = v/u = 15/(−30) = −0.5",
        ],
        "v = 15 cm (real image), m = −0.5 (inverted, diminished)",
      ),
      mistake("Sign convention errors (not treating distances against incident light as negative) are the #1 cause of wrong numerical answers in ray optics — always draw the ray diagram first."),
    ]),
    section("Optical Instruments", [
      diagram("concaveMirrorRay", "A concave mirror also converges rays — used in telescopes and torches.", 460, 220),
      p("<b>Microscopes</b> use two converging lenses to magnify nearby small objects. <b>Astronomical telescopes</b> "
        "use an objective (large aperture, collects light from far away) and an eyepiece to magnify distant objects — "
        "reflecting telescopes use a concave mirror instead of an objective lens, avoiding chromatic aberration."),
      formula("Magnifying power of astronomical telescope (normal adjustment)", ["M = fo/fe  (fo, fe = focal lengths of objective, eyepiece)"]),
    ]),
  ],
  recap=[
    "Mirror formula 1/v+1/u=1/f; Snell's law n1sinθ1 = n2sinθ2.",
    "TIR happens beyond the critical angle, going denser→rarer — basis of optical fibres.",
    "Lens maker's formula gives f from the lens's curvature and refractive index; P = 1/f.",
    "Telescopes/microscopes combine objective + eyepiece lenses (or mirrors) for magnification.",
  ],
  exam_corner=[
    pyq(1, "Define critical angle."),
    pyq(1, "What is the SI unit of power of a lens?"),
    pyq(2, "State the conditions for total internal reflection to occur."),
    pyq(2, "A convex lens has focal length 20 cm. Find its power."),
    pyq(3, "Derive the lens maker's formula for a thin convex lens (statement of formula with explanation of terms is sufficient if full derivation not asked)."),
    pyq(5, "Derive the mirror formula 1/v+1/u=1/f for a concave mirror forming a real image, using a ray diagram. An object 5 cm tall is placed 20 cm from a concave mirror of focal length 15 cm — find the image position, size and nature."),
  ]),

chapter("ch10", 10, "Wave Optics",
  "Light as a wave — the only way to explain interference and diffraction patterns.",
  ["Huygens' principle", "interference", "diffraction"],
  sections=[
    section("Huygens' Principle", [
      p("Every point on a wavefront acts as a source of new secondary wavelets; the new wavefront is the surface "
        "tangent to all these wavelets. Huygens' construction can be used to derive the laws of reflection and "
        "refraction geometrically."),
    ]),
    section("Young's Double Slit Experiment", [
      diagram("youngDoubleSlit", "Two coherent slits produce overlapping waves that create alternating bright and dark fringes.", 480, 240),
      derivation("Fringe width in Young's double slit experiment", "Two coherent slits S1, S2 separated by distance d, screen at distance D, point P on screen at distance y from centre.",
        [
          "Path difference at P: Δ = S2P − S1P ≈ yd/D (for D ≫ d, using small angle approximation)",
          "Bright fringe (constructive interference) when Δ = nλ → yn = nλD/d",
          "Fringe width β = separation between consecutive bright (or dark) fringes = y(n+1) − yn",
        ],
        "β = λD/d"),
      formula("Interference fringe width", ["β = λD / d   (D = slit-to-screen distance, d = slit separation)"]),
      solved(
        "In a YDSE, slits are 0.5 mm apart and the screen is 1.5 m away. If the fringe width is 1.5 mm, find the wavelength of light used.",
        ["β = λD/d → λ = βd/D = 1.5×10⁻³ × 0.5×10⁻³ / 1.5"],
        "λ = 5×10⁻⁷ m = 500 nm",
      ),
      p("Bright fringes need <b>coherent sources</b> (constant phase difference) — this is why the two slits are lit "
        "by the same single source, not two independent bulbs."),
    ]),
    section("Diffraction", [
      p("<b>Diffraction</b> is the bending of waves around obstacles/slits, most noticeable when the slit width is "
        "comparable to the wavelength. A single slit produces a wide, bright central maximum flanked by much "
        "fainter, narrower secondary maxima — quite different from the evenly-spaced fringes of double-slit "
        "interference."),
    ]),
  ],
  recap=[
    "Huygens' principle: every wavefront point spawns secondary wavelets; envelope = new wavefront.",
    "YDSE fringe width β = λD/d; needs coherent sources for a stable pattern.",
    "Diffraction = bending of waves at obstacles/slits; single-slit central maximum is wide and bright.",
  ],
  exam_corner=[
    pyq(1, "State Huygens' principle."),
    pyq(1, "What are coherent sources of light?"),
    pyq(2, "Write the expression for fringe width in Young's double slit experiment and define all terms."),
    pyq(2, "How does the fringe width change if the distance between the slits is doubled?"),
    pyq(3, "Derive the expression for fringe width in Young's double slit experiment."),
    pyq(5, "Describe Young's double slit experiment with a labelled diagram and derive the expression for fringe width. In a YDSE, d=1mm, D=1m, λ=600nm — find the fringe width and the position of the 3rd bright fringe."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("VII", "Dual Nature of Radiation and Matter", [
chapter("ch11", 11, "Dual Nature of Radiation and Matter",
  "Light behaves like a wave AND a particle — and so, weirdly, does every electron.",
  ["photoelectric effect", "de Broglie waves"],
  sections=[
    section("Photoelectric Effect", [
      diagram("photoelectricEffect", "Light striking a metal surface can eject electrons instantly — the photoelectric effect.", 460, 240),
      p("Hertz and Lenard observed that light shining on a metal surface can eject electrons — but only if the "
        "light's <b>frequency</b> is above a minimum threshold, no matter how intense a lower-frequency light is. "
        "This stumped classical wave theory completely."),
      formula("Einstein's photoelectric equation", ["hν = φ0 + KEmax", "KEmax = hν − hν0   (ν0 = threshold frequency)"]),
      solved(
        "The work function of a metal is 2.0 eV. Find the maximum kinetic energy of photoelectrons ejected by light of frequency 7.5×10¹⁴ Hz. (h = 6.63×10⁻³⁴ Js, 1eV = 1.6×10⁻¹⁹J)",
        [
          "hν = 6.63×10⁻³⁴ × 7.5×10¹⁴ = 4.97×10⁻¹⁹ J = 3.11 eV",
          "KEmax = hν − φ0 = 3.11 − 2.0",
        ],
        "KEmax ≈ 1.11 eV",
      ),
      sticky("Why this needed 'particle' light", "Classical (wave) theory predicted intensity, not frequency, should "
             "control ejection — the opposite of what was observed. Einstein's photon (particle) picture, "
             "E = hν per photon, explained it perfectly and won him the Nobel Prize.", "pink"),
    ]),
    section("Matter Waves — de Broglie Hypothesis", [
      p("If light (a wave) can behave like particles (photons), de Broglie proposed the reverse: every moving "
        "particle should have an associated <b>wave nature</b> too."),
      formula("de Broglie wavelength", ["λ = h/p = h/mv"]),
      solved(
        "Find the de Broglie wavelength of an electron moving at 10⁶ m/s. (mass of electron = 9.1×10⁻³¹ kg, h=6.63×10⁻³⁴ Js)",
        ["λ = h/mv = 6.63×10⁻³⁴/(9.1×10⁻³¹ × 10⁶)"],
        "λ ≈ 7.28×10⁻¹⁰ m",
      ),
      mnemonic("The de Broglie wavelength of everyday objects (a cricket ball, a car) is absurdly tiny — that's why "
               "we never notice their 'wave' side. It only matters for very light, fast particles like electrons."),
    ]),
  ],
  recap=[
    "Photoelectric effect needs frequency above threshold ν0; intensity only affects the number of electrons, not their max KE.",
    "Einstein: hν = φ0 + KEmax — explains photoelectric effect via photons.",
    "de Broglie: every particle has wavelength λ = h/mv — matter has a wave nature too.",
  ],
  exam_corner=[
    pyq(1, "Define work function of a metal."),
    pyq(1, "Write the formula for de Broglie wavelength."),
    pyq(2, "State Einstein's photoelectric equation and explain each term."),
    pyq(2, "Why does the photoelectric effect support the particle nature of light?"),
    pyq(3, "Explain the effect of increasing (a) intensity (b) frequency of incident light on photoelectric emission."),
    pyq(5, "State Einstein's photoelectric equation and explain how it accounts for the threshold frequency and the linear relationship between stopping potential and frequency. Light of frequency 8×10¹⁴ Hz falls on a metal with threshold frequency 5×10¹⁴ Hz — find the maximum kinetic energy and stopping potential of photoelectrons."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("VIII", "Atoms and Nuclei", [
chapter("ch12", 12, "Atoms",
  "From a solid pudding of charge to a tiny nucleus with electrons orbiting like planets.",
  ["Rutherford's model", "Bohr's model", "hydrogen spectrum"],
  sections=[
    section("Rutherford's Alpha-Scattering Experiment", [
      p("Firing alpha particles at thin gold foil, Rutherford found most passed straight through, but a few "
        "bounced back sharply — proving atoms are mostly <b>empty space</b> with a tiny, dense, positively charged "
        "<b>nucleus</b> at the centre, around which electrons revolve."),
    ]),
    section("Bohr's Model of the Hydrogen Atom", [
      diagram("bohrModel", "Bohr's model: electrons occupy only certain fixed, quantised circular orbits.", 460, 260),
      derivation("Radius and energy of the nth Bohr orbit", "An electron of charge −e revolves around a nucleus of charge +e in a circular orbit of radius rn, with quantised angular momentum.",
        [
          "Coulomb force provides centripetal force: ke²/rn² = mv²/rn",
          "Bohr's quantisation condition: mvrn = nh/2π → v = nh/2πmrn",
          "Substituting v into the force equation and solving for rn: rn = n²h²ε0/(πme²) = n² × 0.529 Å",
          "Total energy En = KE + PE = ½mv² − ke²/rn; substituting rn gives En = −13.6/n² eV",
        ],
        "rn = n² × 0.529 Å,  En = −13.6/n² eV"),
      formula("Bohr's postulates & key results", [
        "Angular momentum is quantised: mvr = nh/2π",
        "Radius of nth orbit: rn = n² × 0.529 Å  (for hydrogen)",
        "Energy of nth orbit: En = −13.6/n² eV",
      ]),
      solved(
        "Find the energy of an electron in the 2nd Bohr orbit of hydrogen, and the energy released when it jumps to the 1st orbit.",
        [
          "E2 = −13.6/2² = −3.4 eV",
          "E1 = −13.6/1² = −13.6 eV",
          "Energy released = E2 − E1 = −3.4 − (−13.6)",
        ],
        "Energy released = 10.2 eV (emitted as a photon)",
      ),
      p("Electrons jumping between these fixed orbits absorb or emit photons of specific energies — explaining "
        "the sharp, discrete <b>hydrogen line spectrum</b> instead of a continuous glow."),
    ]),
  ],
  recap=[
    "Rutherford: atom = tiny dense positive nucleus + mostly empty space + orbiting electrons.",
    "Bohr: angular momentum quantised (mvr = nh/2π); En = −13.6/n² eV for hydrogen.",
    "Electron transitions between fixed orbits → discrete emission/absorption lines.",
  ],
  exam_corner=[
    pyq(1, "What is the energy of a hydrogen atom in its ground state?"),
    pyq(1, "State one limitation of Rutherford's model of the atom."),
    pyq(2, "State Bohr's postulates of the atomic model (any two)."),
    pyq(2, "Find the radius of the 2nd Bohr orbit of hydrogen."),
    pyq(3, "Describe Rutherford's alpha-particle scattering experiment and its observations."),
    pyq(5, "Derive the expression for the radius and energy of the nth Bohr orbit of a hydrogen atom. Find the wavelength of radiation emitted when an electron in hydrogen jumps from n=3 to n=2 (Rydberg constant R=1.097×10⁷ m⁻¹)."),
  ]),

chapter("ch13", 13, "Nuclei",
  "Split it or fuse it — either way, a tiny bit of mass turns into a huge amount of energy.",
  ["nuclear composition", "mass defect", "fission & fusion"],
  sections=[
    section("Nuclear Composition & Size", [
      p("A nucleus contains <b>protons and neutrons (nucleons)</b>, held together at extremely short range by the "
        "<b>strong nuclear force</b> — strong enough to overcome the electrostatic repulsion between protons packed "
        "so closely together."),
      formula("Nuclear size", ["R = R0 A^(1/3)  ,  R0 ≈ 1.2 fm"]),
      solved(
        "Find the radius of a nucleus with mass number 64. (R0 = 1.2 fm)",
        ["R = R0 A^(1/3) = 1.2 × 64^(1/3) = 1.2 × 4"],
        "R = 4.8 fm",
      ),
    ]),
    section("Mass Defect & Binding Energy", [
      diagram("bindingEnergyCurve", "Binding energy per nucleon peaks around iron (A ≈ 56) — the most stable nuclei.", 480, 220),
      formula("Mass-energy relation", ["E = mc²", "Mass defect: Δm = (Zmp + Nmn) − Mnucleus", "Binding energy: BE = Δm c²"]),
      solved(
        "Find the binding energy of a helium nucleus (mass defect Δm = 0.0304 u). (1u = 931 MeV/c²)",
        ["BE = Δm × 931 MeV = 0.0304 × 931"],
        "BE ≈ 28.3 MeV",
      ),
      p("The <b>binding energy per nucleon</b> curve explains both fission and fusion: nuclei can release energy by "
        "moving <i>toward</i> the peak (around iron) — heavy nuclei splitting (fission) or light nuclei combining "
        "(fusion) both increase average binding energy per nucleon."),
    ]),
    section("Nuclear Fission & Fusion", [
      diagram("nuclearFission", "A neutron striking a heavy nucleus like U-235 splits it, releasing more neutrons and energy.", 460, 220),
      lst([
        "<b>Nuclear fission:</b> a heavy nucleus (e.g. U-235) splits into lighter nuclei after absorbing a neutron, "
        "releasing huge energy plus more neutrons — enabling a chain reaction (used in nuclear reactors, atom bombs).",
        "<b>Nuclear fusion:</b> light nuclei (e.g. hydrogen isotopes) combine into a heavier nucleus at extremely "
        "high temperature/pressure, releasing even more energy per unit mass — the process powering the Sun.",
      ]),
      tip("For 'explain fission vs fusion' questions, always mention the binding-energy-per-nucleon curve as the underlying reason energy is released — this single diagram/explanation answers most conceptual questions in this chapter."),
    ]),
  ],
  recap=[
    "Nucleus = protons + neutrons, held by the strong nuclear force; R = R0A^(1/3).",
    "Mass defect Δm converts to binding energy via E = mc².",
    "Binding energy per nucleon peaks near iron — driving both fission (heavy→lighter) and fusion (light→heavier).",
    "Fission powers nuclear reactors; fusion powers the Sun.",
  ],
  exam_corner=[
    pyq(1, "Define mass defect of a nucleus."),
    pyq(1, "What is the approximate value of R0 in the nuclear size formula?"),
    pyq(2, "Distinguish between nuclear fission and nuclear fusion."),
    pyq(2, "Find the mass defect of a nucleus with binding energy 92 MeV. (1u = 931 MeV)"),
    pyq(3, "Explain, with reference to the binding energy per nucleon curve, why energy is released in both nuclear fission and fusion."),
    pyq(5, "Define binding energy and mass defect. Sketch and explain the binding energy per nucleon vs mass number curve, and use it to explain why heavy nuclei undergo fission while light nuclei undergo fusion."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("IX", "Electronic Devices", [
chapter("ch14", 14, "Semiconductor Electronics: Materials, Devices and Simple Circuits",
  "Silicon that's neither a good conductor nor a good insulator — and that's exactly what makes it useful.",
  ["energy bands", "p-n junction", "diode as rectifier"],
  sections=[
    section("Energy Bands in Solids", [
      diagram("semiconductorBands", "Conductors, semiconductors and insulators differ mainly in the size of their energy gap.", 480, 160),
      lst([
        "<b>Conductors:</b> conduction and valence bands overlap — electrons move freely.",
        "<b>Insulators:</b> a huge energy gap separates the bands — electrons can't jump across.",
        "<b>Semiconductors:</b> a small energy gap — some electrons cross it at room temperature, more do as "
        "temperature rises (unlike metals!).",
      ]),
    ]),
    section("Intrinsic & Extrinsic Semiconductors", [
      p("A <b>pure (intrinsic)</b> semiconductor like silicon has few free charge carriers. <b>Doping</b> it with "
        "impurities creates <b>extrinsic</b> semiconductors: <b>p-type</b> (trivalent dopant, creates 'holes' — "
        "majority carriers) and <b>n-type</b> (pentavalent dopant, creates extra free electrons — majority carriers)."),
      mistake("In p-type semiconductors, majority carriers are HOLES (not electrons) — a frequent mix-up when writing conduction-mechanism answers."),
    ]),
    section("p-n Junction & Diode as a Rectifier", [
      diagram("pnJunction", "At a p-n junction, a depletion region forms where mobile charge carriers have diffused away.", 460, 220),
      p("Joining p-type and n-type semiconductors forms a <b>p-n junction diode</b>. In <b>forward bias</b> "
        "(p to +ve, n to −ve), current flows easily; in <b>reverse bias</b>, only a tiny leakage current flows — "
        "this one-way behaviour makes a diode ideal as a <b>rectifier</b>, converting AC to DC."),
      sticky("Half-wave vs full-wave", "A single diode gives half-wave rectification (blocks one half of the AC cycle); "
             "four diodes in a bridge arrangement give full-wave rectification (uses both halves) — smoother DC "
             "output.", "yellow"),
    ]),
  ],
  recap=[
    "Conductors: bands overlap. Insulators: huge gap. Semiconductors: small gap, conductivity rises with temperature.",
    "Doping creates p-type (holes, majority carriers) or n-type (electrons, majority carriers) semiconductors.",
    "p-n junction diode conducts easily in forward bias, barely in reverse bias.",
    "Diodes rectify AC to DC — single diode: half-wave; four-diode bridge: full-wave.",
  ],
  exam_corner=[
    pyq(1, "What are majority charge carriers in an n-type semiconductor?"),
    pyq(1, "Define depletion region in a p-n junction diode."),
    pyq(2, "Distinguish between intrinsic and extrinsic semiconductors."),
    pyq(2, "Draw the circuit symbol of a p-n junction diode and label the p and n regions."),
    pyq(3, "Explain the forward and reverse bias characteristics of a p-n junction diode."),
    pyq(5, "Explain the working of a p-n junction diode as a full-wave rectifier with a labelled circuit diagram and input-output waveforms."),
  ]),
])

CHAPTERS_FLAT = [ch for unit in UNITS for ch in unit["chapters"]]
