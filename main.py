from circuit_solver import CircuitSolver

circuitSolver = CircuitSolver.compileCircuitFromFile('circuit.crc')
circuitSolver.solve()
circuitSolver.showCircuit()