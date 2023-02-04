from circuit_solver import CircuitSolver

circuitSolver = CircuitSolver.compileCircuitFromFile('circuit.crc')
circuitSolver.setRoundingPlace(5)
circuitSolver.solve()
circuitSolver.showStepByStepReasoning(showVoltageSteps=False, showCurrentSteps=False, showResistanceSteps=True)
print('\n\n')
circuitSolver.showCircuit(showVoltage=False, showCurrent=False, showResistance=True, showLegs=True, showResistors=False)