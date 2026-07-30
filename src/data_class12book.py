from helpers import p, lst, olist, formula, diagram, sticky, mnemonic, section, chapter, derivation, solved, mistake, tip, pyq

BOOK_TITLE = "Class XII Physics — Bureau's Higher Secondary Physics (Textbook Edition)"
BOOK_INTRO = ("Notes built directly from your prescribed textbook — Bureau's Higher Secondary Physics, "
              "Class XII, published by the Odisha State Bureau of Textbook Preparation and Production. "
              "Chapter numbering, section order and worked examples follow the book itself, redrawn in "
              "handwritten-notes style with derivations, diagrams and an Exam Corner. Chapters are added "
              "one at a time — Chapter 1 is ready; the rest follow as they're prepared.")

SYLLABUS_META = "As printed in the textbook: Syllabus [2016-2017], Council of Higher Secondary Education, Odisha — Physics Theory, Class XII. Full Marks: 70 (160 Periods)."

SYLLABUS_UNITS = [
  {"roman": "I", "name": "Electrostatics", "periods": 22, "topics": [
    "Electric charges and fields: Electric charge and its quantization, conservation of charge, Coulomb's law, force between two point charges, force between multiple charges, superposition principle, continuous charge distribution. <i>(Ch. 1)</i>",
    "Electric field due to a point charge, electric field lines, electric field due to a dipole at any point, torque on a dipole in uniform electric field. Electric flux, Gauss's theorem (statement only) and its applications to find field due to uniformly charged infinite plane sheet, infinitely long straight wire, and uniformly charged thin spherical shell (inside &amp; outside). <i>(Ch. 2)</i>",
    "Electrostatic potential and capacitance: Electric potential, potential difference, potential due to a point charge, potential due to a dipole, potential due to a system of charges. Equipotential surfaces, electrical PE of a system of two point charges and of an electric dipole in a field. <i>(Ch. 2 &amp; 3)</i>",
    "Conductors, insulators, free and bound charges inside a conductor, dielectrics and electric polarisation. <i>(Ch. 2)</i>",
    "Capacitors and capacitance, parallel plate capacitor with/without dielectric medium, combinations of capacitors in series and parallel, energy stored in a capacitor. <i>(Ch. 3)</i>",
  ]},
  {"roman": "II", "name": "Current Electricity", "periods": 20, "topics": [
    "Electric current, drift velocity, mobility and their relation with electric current, Ohm's law, resistance, conductance, resistivity, conductivity, effect of temperature on resistance, V-I characteristics, electrical energy and power, carbon resistors and colour code, combinations of resistors in series/parallel. <i>(Ch. 5)</i>",
    "EMF and potential difference, internal resistance of a cell, combination of cells in series and parallel, Kirchhoff's laws and applications: Wheatstone bridge and metre bridge. Potentiometer — principle and applications to measure potential difference, compare EMFs, and measure internal resistance. <i>(Ch. 6)</i>",
  ]},
  {"roman": "III", "name": "Magnetic Effect of Current and Magnetism", "periods": 23, "topics": [
    "Moving charges and magnetism: concept of magnetic field, Oersted's experiment, Biot-Savart law and its application to find B on the axis and at the centre of a current-carrying circular loop, Ampere's law and its application to an infinitely long straight wire, straight and toroidal solenoid (qualitative), force on a moving charge in uniform magnetic and electric fields. <i>(Ch. 8)</i> Cyclotron. <i>(Ch. 17)</i>",
    "Force on a current-carrying conductor in a uniform magnetic field, force between two parallel current-carrying conductors — definition of ampere, torque on a current loop in a uniform magnetic field, moving coil galvanometer — current sensitivity and conversion to ammeter/voltmeter. <i>(Ch. 8)</i>",
    "Magnetism and matter: current loop as a magnetic dipole and its magnetic moment, magnetic moment of a revolving electron, magnetic field intensity due to a bar magnet along its axis and perpendicular to it, torque on a bar magnet in a uniform field, bar magnet as an equivalent solenoid, magnetic field lines, Earth's magnetic field and elements. <i>(Ch. 8)</i>",
    "Para-, dia- and ferro-magnetic substances with examples, electromagnets and factors affecting their strength, permanent magnets. <i>(Ch. 4)</i>",
  ]},
  {"roman": "IV", "name": "Electromagnetic Induction and Alternating Current", "periods": 20, "topics": [
    "Electromagnetic induction: Faraday's laws, induced EMF and current, Lenz's law, eddy currents, self and mutual induction. <i>(Ch. 9)</i>",
    "Alternating current: peak and RMS values, reactance and impedance, LC oscillations (qualitative), LCR series circuit, resonance, power in AC circuits, wattless current, AC generator and transformer. <i>(Ch. 10)</i>",
  ]},
  {"roman": "V", "name": "Electromagnetic Waves", "periods": 4, "topics": [
    "Basic idea of displacement current, qualitative idea about characteristics of electromagnetic waves and their transverse nature. Electromagnetic spectrum (radio waves, microwaves, infrared, visible, X-ray and gamma rays), including elementary ideas about their uses. <i>(Ch. 14)</i>",
  ]},
  {"roman": "VI", "name": "Optics", "periods": 25, "topics": [
    "Ray optics and optical instruments: reflection of light, spherical mirrors, mirror formula, lateral &amp; longitudinal magnification. <i>(Ch. 11)</i> Refraction of light, refractive index, its relation with velocity of light, total internal reflection and applications, optical fibre, refraction at spherical surfaces, thin lens formula, lens maker's formula, magnification, power of lenses, combination of thin lenses in contact, combination of a lens and mirror, refraction and dispersion through a prism, scattering of light. <i>(Ch. 12)</i>",
    "Optical instruments: microscopes and telescopes (reflecting and refracting) and their magnifying powers. <i>(Ch. 13)</i>",
    "Wave optics: wavefront, Huygen's principle, reflection and refraction of a plane wave using wavefronts, proof of laws of reflection and refraction using Huygen's principle. Interference, Young's double slit experiment and fringe width, coherent sources, sustained interference, diffraction due to a single slit, width of central maximum, resolving power of microscope and astronomical telescope (qualitative), polarisation, plane polarised light, Brewster's law, uses of polaroids. <i>(Ch. 14)</i>",
  ]},
  {"roman": "VII", "name": "Dual Nature of Radiation and Matter", "periods": 8, "topics": [
    "Dual nature of radiation, photoelectric effect, Hertz and Lenard's observations, Einstein's photoelectric equation, particle nature of light. Matter waves — wave nature of particles, de-Broglie relation, Davisson-Germer experiment (conclusions only). <i>(Ch. 16)</i>",
  ]},
  {"roman": "VIII", "name": "Atoms and Nuclei", "periods": 14, "topics": [
    "Atoms: alpha-particle scattering experiment, Rutherford's model of the atom and its limitations, Bohr model, energy levels, hydrogen spectrum. <i>(Ch. 16)</i>",
    "Nuclei: atomic nucleus — composition, size, nuclear mass, nature of nuclear force, mass defect, binding energy per nucleon and its variation with mass number, nuclear fission, fusion, radioactivity — alpha, beta, gamma rays and their properties, radioactive decay law, half life and decay constant. <i>(Ch. 17)</i>",
  ]},
  {"roman": "IX", "name": "Semiconductor Electronics", "periods": 10, "topics": [
    "Energy bands in conductors, semiconductors and insulators (qualitative), p-type and n-type semiconductors, semiconductor diode, V-I characteristics in forward/reverse bias, diode as half and full wave rectifier (centre tap), efficiency (no derivation). <i>(Ch. 19)</i>",
    "Special purpose p-n junction diodes: LED, photodiode, solar cell, Zener diode and its characteristics, Zener diode as a voltage regulator. <i>(Ch. 19)</i>",
    "Junction transistor, transistor action, characteristics of a transistor, transistor as an amplifier (CE configuration). <i>(Ch. 20)</i> Basic idea of analog and digital signals, logic gates (OR, AND, NOT, NAND, NOR). <i>(Ch. 22)</i>",
  ]},
  {"roman": "X", "name": "Communication System", "periods": 10, "topics": [
    "Elements of a communication system (block diagram only), bandwidth of signals (speech, TV, digital data), bandwidth of transmission medium, propagation of EM waves in the atmosphere, sky and space wave propagation, satellite communication, need for modulation, qualitative idea of amplitude and frequency modulation, advantages of FM over AM, basic idea about internet, mobile telephony and GPS. <i>(Ch. 21)</i>",
  ]},
]

# Full textbook table of contents (22 chapters). Only chapters with `ready=True` are clickable;
# others render as "coming soon" placeholders until prepared in a future pass.
TOC = [
  {"number": 1, "title": "Electrostatics", "id": "ch01", "ready": True,
   "tagline": "Charge, Coulomb's law, superposition, continuous charge distribution."},
  {"number": 2, "title": "Electric Field and Potential", "id": "ch02", "ready": False},
  {"number": 3, "title": "Capacitance", "id": "ch03", "ready": False},
  {"number": 4, "title": "Magnetism", "id": "ch04", "ready": False},
  {"number": 5, "title": "Electric Current", "id": "ch05", "ready": False},
  {"number": 6, "title": "Direct Current Circuits", "id": "ch06", "ready": False},
  {"number": 7, "title": "Thermal and Chemical Effects of Electric Current", "id": "ch07", "ready": False},
  {"number": 8, "title": "Magnetic Effect of Electric Current", "id": "ch08", "ready": False},
  {"number": 9, "title": "Electromagnetic Induction", "id": "ch09", "ready": False},
  {"number": 10, "title": "Alternating Currents", "id": "ch10", "ready": False},
  {"number": 11, "title": "Reflection and Spherical Mirror", "id": "ch11", "ready": False},
  {"number": 12, "title": "Refraction, Dispersion and Lens", "id": "ch12", "ready": False},
  {"number": 13, "title": "Eye and Optical Instruments", "id": "ch13", "ready": False},
  {"number": 14, "title": "Wave Optics and Interference", "id": "ch14", "ready": False},
  {"number": 15, "title": "Relativity", "id": "ch15", "ready": False},
  {"number": 16, "title": "Atomic Physics", "id": "ch16", "ready": False},
  {"number": 17, "title": "Nuclear Physics", "id": "ch17", "ready": False},
  {"number": 18, "title": "Electron Emission", "id": "ch18", "ready": False},
  {"number": 19, "title": "Solids", "id": "ch19", "ready": False},
  {"number": 20, "title": "Transistors", "id": "ch20", "ready": False},
  {"number": 21, "title": "Space Communication", "id": "ch21", "ready": False},
  {"number": 22, "title": "Digital Electronics", "id": "ch22", "ready": False},
]

_note = ("These questions are adapted directly from the Model Questions at the end of this chapter in "
         "Bureau's Higher Secondary Physics — several are themselves drawn from past CHSE/CBSE papers, "
         "as cited in the textbook.")

CHAPTERS = [
chapter("ch01", 1, "Electrostatics",
  "Two kinds of charge, one law of force, and every trick for adding them up.",
  ["electric charge", "Coulomb's law", "superposition", "charge density"],
  sections=[
    section("What Is Electrostatics?", [
      p("<b>Electrostatics</b> is the branch of physics dealing with the properties of electricity at rest — "
        "i.e. stationary (static) charge. Stationary charge is produced on insulating substances like amber, "
        "ebonite, or glass by rubbing them with fur or silk. The key properties studied under electrostatics are "
        "electric charge, electric field, electric potential, dielectric polarisation, and capacitance."),
      p("Electric charge is a fundamental property of matter, carried by particles like electrons and protons, "
        "alongside their mass. A body can gain or lose electrons — a body with an excess of electrons or a "
        "deficit compared to its neutral state is called a <b>charged body</b>. Charge is best understood not by "
        "what it <i>is</i>, but by what it <i>does</i> — it produces forces on other charges."),
    ]),
    section("Characteristics of Electric Charge", [
      olist([
        "<b>Two kinds of charge:</b> the electric force between two electrons at a distance apart is repulsive, "
        "same as between two protons. But between a proton and an electron at the same separation, the force is "
        "attractive. Hence there must be two distinct kinds of charge — called <b>positive</b> and <b>negative</b>.",
        "<b>Charge is quantised:</b> the smallest unit of charge (the basic/elementary charge) equals the "
        "magnitude of charge on an electron, e = 1.60218 × 10⁻¹⁹ C. Any physically existing charge Q is an "
        "integral multiple of e: Q = ne, where n is a positive or negative integer. Fractional basic charge does "
        "not exist in nature.",
        "<b>Charge is conserved:</b> the algebraic sum of electric charges in any closed system remains constant "
        "— no exceptions have ever been discovered. (E.g. when a neutron decays into a proton, an electron and "
        "an antineutrino, the net charge before and after is still zero.)",
        "<b>Charge is a scalar</b> and hence charges obey ordinary scalar addition (with sign).",
        "<b>Charge is relativistically invariant</b> — its value doesn't change with relative motion of the "
        "observer.",
      ]),
      solved(
        "In Millikan's oil drop experiment, the charges on four different drops were found to be "
        "1 × 1.6×10⁻¹⁹ C, 4 × 1.6×10⁻¹⁹ C, 5 × 1.6×10⁻¹⁹ C, and 7 × 1.6×10⁻¹⁹ C. What do you infer from these results?",
        [
          "Each measured charge is a whole-number multiple of 1.6×10⁻¹⁹ C.",
          "This is exactly the elementary charge e — the charge on a single electron/proton.",
        ],
        "Charge is quantised: every observed charge is an integral multiple (n = 1, 4, 5, 7) of the elementary charge e.",
      ),
    ]),
    section("Electrification — How Bodies Get Charged", [
      p("<b>Electrification</b> is the process of charging an uncharged body. In their normal state, bodies are "
        "electrically neutral (equal numbers of protons and electrons). Rubbing transfers electrons from one "
        "body to the other."),
      diagram("chargingByInduction", "Bringing a charged rod near a neutral conductor redistributes its charge — induced charges appear at each end.", 480, 260),
      olist([
        "<b>Electrification by friction:</b> rubbing a glass rod with silk transfers electrons from the glass to "
        "the silk — the glass becomes positively charged (deficit of electrons), the silk negatively charged "
        "(excess of electrons). Substances can be ranked in a series (Table 1.1 in the text) — whichever occurs "
        "earlier becomes positive when rubbed against one occurring later.",
        "<b>Electrification by induction:</b> bringing a charged rod near (without touching) an uncharged "
        "conductor causes electrons to redistribute — the near end gets an induced charge opposite to the rod's, "
        "the far end gets a charge of the same sign as the rod. This is <i>temporary</i>: removing the rod lets "
        "the charges redistribute and disappear. A conductor <i>can</i> be permanently charged by induction using "
        "two touching spheres, separating them while the charged rod is still nearby.",
        "<b>Electrification by conduction:</b> touching a charged conductor to an uncharged one transfers some "
        "charge of the <i>same sign</i> to the second conductor — the amount depends on the size/shape of each.",
      ]),
      mistake("Charging by induction never transfers charge of the same sign as the inducing rod to the near "
              "side — the near end always gets the <i>opposite</i> sign. Mixing this up is a very common error."),
    ]),
    section("Point Charge & Coulomb's Law", [
      p("A <b>point charge</b> is any charged body whose dimensions are negligible compared to its distance from "
        "the point where its effect is being studied — even a charged body as large as the Earth can be treated "
        "as a point charge if we're only interested in its effect as far away as the Sun."),
      diagram("coulombsLawForce", "Coulomb's law: like charges repel with equal and opposite forces along the line joining them.", 480, 220),
      p("<b>Coulomb's law</b> states that the force of attraction or repulsion between two point charges at rest "
        "is directly proportional to the product of the charges and inversely proportional to the square of the "
        "distance between them."),
      formula("Coulomb's law", [
        "F = K0 · Q1Q2 / r²   (K0 = constant of proportionality, depends on system of units and medium)",
        "In free space (SI): F = (1/4πε0) · Q1Q2 / r²",
      ]),
    ]),
    section("Coulomb's Law and Units of Charge", [
      lst([
        "<b>CGS-esu system:</b> K0 is set equal to unity, defining the <b>statcoulomb</b> — the charge which, "
        "placed 1 cm from an identical charge in vacuum, repels it with a force of 1 dyne.",
        "<b>SI system:</b> the measured value of K0 is 8.98755 × 10⁹ N m² C⁻² (≈ 9 × 10⁹ N m² C⁻²). One "
        "<b>coulomb</b> is defined as the charge which, placed 1 m from an identical charge in vacuum, repels it "
        "with a force of 9 × 10⁹ N.",
      ]),
      formula("Permittivity of free space", ["K0 = 1/(4πε0)", "ε0 = 8.854 × 10⁻¹² C² N⁻¹ m⁻² (permittivity of free space)"]),
      solved(
        "Find the relation between coulomb and statcoulomb.",
        [
          "Consider two point charges of q coulomb each, r metres apart, in free space.",
          "SI Coulomb force: F = 9×10⁹ q²/r² Newton",
          "Same setup in c.g.s-esu (converting q coulomb to x·q statcoulomb, r metres to 100r cm): F = (xq)²/(100r)² dyne = 10⁻⁵ N",
          "Equating the two expressions for F and solving gives x² = 9×10¹⁸, so x = 3×10⁹",
        ],
        "1 coulomb = 3 × 10⁹ statcoulomb",
      ),
    ]),
    section("Effect of Medium — Permittivity & Dielectric Constant", [
      p("Coulomb's law as written above (F = Q1Q2/4πε0r²) holds for charges in <b>vacuum</b>. If a material medium "
        "fills the space between the charges, the force is <i>reduced</i>. This is accounted for by replacing ε0 "
        "with ε, the <b>permittivity of the medium</b>."),
      formula("Force in a medium", [
        "F = Q1Q2 / (4πε r²)   where ε = ε0 · εr  (εr = relative permittivity = dielectric constant K)",
        "F(medium) = F(vacuum) / K",
      ]),
      p("<b>Dielectric constant (K)</b> is dimensionless, with the same value in cgs and SI systems. Its minimum "
        "value is 1 (vacuum/air) and its maximum is infinite (for good conductors)."),
      sticky("Typical dielectric constants", "Air ≈ 1.0006 &middot; Water 80–83 &middot; Mica 5.6–6.6 &middot; Glass 6–10 &middot; Oil 2–2.2", "blue"),
    ]),
    section("Principle of Superposition & Force Due to Multiple Charges", [
      p("Coulomb's law by itself only tells us the force between <i>two</i> point charges. The <b>principle of "
        "superposition</b> extends this: the force between any two charges in a group is independent of the "
        "presence of all other charges — the net force on any one charge is simply the vector sum of the "
        "individual Coulomb forces due to every other charge."),
      diagram("chargeSuperposition", "The resultant force on a charge is the vector sum of the individual Coulomb forces from every other charge.", 460, 260),
      derivation("Net force on a charge due to n other charges", "Charges Q1, Q2, ... Qn at position vectors r1, r2, ... rn from a charge Q at the origin.",
        [
          "Force on Q due to Q1 alone: F1 = (1/4πε0)(QQ1/r1²) r̂1, and similarly for F2, F3, ... Fn.",
          "By the superposition principle, these individual forces add vectorially (they don't interfere with each other).",
        ],
        "F = F1 + F2 + ... + Fn = (Q/4πε0) Σ (Qi/ri²) r̂i"),
      solved(
        "Three identical charges, each of charge q, are placed at the three vertices of an equilateral triangle "
        "of side a. Find the force on any one charge due to the other two.",
        [
          "Force from each neighbouring charge has the same magnitude: F1 = F2 = q²/(4πε0a²).",
          "The angle between F1 and F2 is 60° (from the triangle's geometry), so the resultant bisects this angle.",
          "Resultant magnitude: F = √(F1² + F2² + 2F1F2cos60°) = √3 · q²/(4πε0a²).",
        ],
        "F = √3 q² / (4πε0 a²), directed along the bisector, away from the triangle.",
      ),
      solved(
        "Two identical pith balls, each of mass 19.6×10⁻⁵ kg, are suspended from the same point by two silk "
        "threads each 1.0 m long. They carry identical charge and repel each other so the threads make an angle "
        "of 90° at the point of suspension. Find the charge on each ball.",
        [
          "By symmetry, each thread makes 45° with the vertical.",
          "For equilibrium: T cosθ = mg and T sinθ = F, so F = mg tanθ = mg (since θ = 45°, tan45° = 1).",
          "F also equals q²/(4πε0r²) where r is the separation between the balls.",
          "Solving q² = 4πε0 r² mg for q (with r worked out from the geometry) gives q ≈ 0.65 μC.",
        ],
        "q ≈ 0.65 μC on each ball",
      ),
    ]),
    section("Salient Features of Coulomb Interaction", [
      lst([
        "Coulomb's law is an <b>experimental law</b> (established by Coulomb using a torsion balance).",
        "It applies to <b>point charges</b>.",
        "The Coulomb force between any two charges is <b>unaffected by other charges</b> nearby.",
        "It is a <b>central force</b> (acts along the line joining the two charges).",
        "It is a <b>conservative force</b> (work done is path-independent).",
        "It is an <b>unsaturated force</b> — a single charge can simultaneously interact with any number of other charges.",
        "It is a <b>long-range force</b>.",
      ]),
      sticky("Coulomb force vs. gravitational force", "Both are central, long-range, conservative forces obeying an "
             "inverse-square law. But Coulomb force can be attractive <i>or</i> repulsive (gravity is only "
             "attractive), depends on the intervening medium (gravity doesn't), and is about 10³⁶ times "
             "<i>stronger</i> than the gravitational force between the same pair of particles.", "blue"),
    ]),
    section("Continuous Charge Distribution", [
      p("Charge is fundamentally discrete (always an integral multiple of e), so strictly speaking a "
        "'continuous' charge distribution isn't microscopically real. But for macroscopic bodies with enormous "
        "numbers of elementary charges, it's extremely useful to treat charge as continuously spread — exactly "
        "like treating a fluid as continuous in hydrodynamics despite it being made of molecules."),
      diagram("chargeDensityTypes", "Three ways to describe continuously distributed charge, depending on the shape of the charged body.", 500, 220),
      formula("Charge density definitions", [
        "Linear charge density: λ = Δq/Δℓ  (charge per unit length; used for wires/rods) — q = ∫λ dℓ",
        "Surface charge density: σ = Δq/ΔS  (charge per unit area; used for charged sheets/plates) — q = ∫σ dS",
        "Volume charge density: ρ = Δq/ΔV  (charge per unit volume; used for charged solids) — q = ∫ρ dV",
      ]),
    ]),
  ],
  recap=[
    "Charge is conserved, quantised (Q = ne), and a scalar that adds algebraically.",
    "Electrification: by friction (permanent transfer), induction (temporary, opposite charge on the near side), or conduction (same-sign charge transferred).",
    "Coulomb's law: F = Q1Q2/(4πε0r²) in vacuum, reduced by a factor K (dielectric constant) in a medium.",
    "Superposition principle: net force on a charge = vector sum of individual Coulomb forces from every other charge.",
    "Coulomb force is central, conservative, unsaturated, long-range, and ~10³⁶ times stronger than gravity between the same particles.",
    "Continuous charge distributions use linear (λ), surface (σ), or volume (ρ) charge density depending on geometry.",
  ],
  exam_corner_note=_note,
  exam_corner=[
    pyq(1, "State Coulomb's law of electric force between two charged bodies. [CHSE 1989]"),
    pyq(1, "What is the value and dimensional formula for ε0?"),
    pyq(1, "Is Coulomb's force between two electrons greater than the gravitational force between them? If so, by what factor?"),
    pyq(2, "What do you understand by the principle of superposition of Coulomb forces?"),
    pyq(2, "Give two points of distinction between electric charge and mass."),
    pyq(2, "Two charges +1μC and +5μC are placed 0.1 cm apart. What is the ratio of the Coulomb force acting on each of the two charges? [CHSE 2002]"),
    pyq(3, "Two point charges 4Q and Q are situated a distance d apart. Find the position of a third charge q so that it is in equilibrium, and discuss whether this equilibrium is stable or unstable."),
    pyq(3, "The distance between the electron and proton in a hydrogen atom is 0.53 Å. Find the electric force of attraction between them."),
    pyq(3, "Three equal charges, each of 1 μC, are placed at the three corners of an equilateral triangle of side 1 m. Find the force experienced by each charge due to the other two."),
    pyq(5, "Discuss the different characteristics of electric charge. What do you mean by conservation of charge?"),
    pyq(5, "What do you mean by electrification? Discuss the various ways of electrifying a body. How can a conductor be charged positively by induction?"),
    pyq(5, "State Coulomb's law in electrostatics and hence define the unit of charge in the e.s.u and SI systems."),
    pyq(5, "State the principle of superposition in electrostatics. Obtain an expression for the force on one charge due to all other charges present in its neighbourhood."),
  ]),
]
