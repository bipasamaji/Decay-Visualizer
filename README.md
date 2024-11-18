**Decay Visualizer**
--------------------

A Python-based interactive graphical simulation of radioactive decay, showcasing real-time nuclear disintegration probabilities. This project uses libraries like `Pygame`, `Matplotlib`, `NumPy`, and `Pillow` to create an educational and visual learning tool.

**🛠 Features**
---------------

- **Simulate Radioactive Decay**: Visualize the decay of Carbon-14 atoms into Nitrogen-14.
- **Real-Time Graphics**: Watch atoms decay with interactive graphics powered by Pygame.
- **Graph Plotting**: Display concentration of undecayed atoms over time using Matplotlib.
- **Educational Insight**: Learn about decay constants, half-life, and stochastic behavior in nuclear physics.

**🖥 Installation**
-------------------

**Prerequisites**
Before running the project, ensure you have:
- Python 3.x installed.
- The following Python libraries:
  - `Pygame`
  - `Matplotlib`
  - `NumPy`
  - `Pillow`

**Steps to Install**
--------------------

1. **Clone the Repository**:
   
   git clone https://github.com/your-username/decay-visualizer.git
   cd decay-visualizer

2. **Install Dependencies**:

  pip install -r requirements.txt

3. **Prepare Assets**:
   
  assets/
  ├── c14.png    # Image of Carbon-14
  ├── n14.png    # Image of Nitrogen-14
  ├── e0.png     # Image of beta particle

**🚀 How to Run**
------------------

1. **Run the main program**:

  python main.py
  Enter the initial number of atoms when prompted:

  Enter initial number of atoms: 100
  
2. **Watch the simulation**:
   
  Carbon-14 atoms will decay into Nitrogen-14 over time.
  Decay events are visually represented in the simulation window.
  Exit the simulation to see the final plot of Concentration vs Time.
  
**📂 Project Structure**
-------------------------

main.py: Main script that handles the simulation and graphical interface.
atoms.py: Contains the Carbon and betaParticle classes for modeling decay dynamics and graphical behavior.
assets/: Folder containing visual assets (c14.png, n14.png, e0.png).

**📊 Dependencies**
--------------------

This project relies on the following Python libraries:

Pygame - For creating the graphical simulation and handling interactivity.
Matplotlib - For plotting the concentration of undecayed atoms vs time.
NumPy - For handling numerical computations.
Pillow - For processing and displaying image assets.

**🌟 Features in Action**
--------------------------

1. **Graphical Simulation**:
   
  Carbon-14 atoms are randomly placed on the screen.
  Atoms decay based on stochastic probabilities governed by the decay constant.

2. **Beta Particle Emission**:
   
  Decayed Carbon-14 atoms emit beta particles that move across the screen.

3. **Concentration Tracking**:
   
  Tracks the count of undecayed Carbon-14 atoms at every time step.
  Generates a plot of atom concentration versus time.

**🎯 Future Improvements**
---------------------------

Add support for additional isotopes and decay chains.
Enable custom half-life configurations for better experimentation.
Improve visualization of beta particle emission dynamics.

**🤝 Contributing**
--------------------

Contributions are welcome!
Feel free to fork this repository, submit a pull request, or raise issues for improvements.
