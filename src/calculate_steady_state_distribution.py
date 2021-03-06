import numpy as np
import collections

def generate_SSD_with_uniform_distribution(initialProbabilities, transitionMatrix):
    steadyStateProbabilities = np.zeros([len(initialProbabilities),1])
    countIterations = 0
    transitionMatrix = transitionMatrix.T

    while collections.Counter(initialProbabilities.T[0]) != collections.Counter(steadyStateProbabilities.T[0]):
        steadyStateProbabilities = initialProbabilities
        initialProbabilities = transitionMatrix @ initialProbabilities
        countIterations += 1

    print("Steady state vector generated with " + str(countIterations) + " iterations:\n" + str(steadyStateProbabilities))
    return steadyStateProbabilities

def generate_SSD_with_matrix_method(transitionMatrix):
    numberOfStates = len(transitionMatrix)
    
    identityMatrix = np.identity(numberOfStates)
    transitionMatrix = transitionMatrix - identityMatrix
    transitionMatrix = np.vstack((transitionMatrix.T, np.ones([1, numberOfStates])))
    
    results = np.zeros([1, numberOfStates])
    results = np.append(results, 1)

    x,_,_,_ = np.linalg.lstsq(transitionMatrix, results, rcond=None)

    print("Steady state vector generated with the matrix method:\n" + str(x))
    return x

def main():
    v = np.array([[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]]).T
    T = np.loadtxt("resources/transition_matrix.txt", dtype=float)

    # method 1
    ssd1 = generate_SSD_with_uniform_distribution(v, T)

    # method 2
    ssd2 = generate_SSD_with_matrix_method(T)

    # not working
    # if ssd1.all() == ssd2.all():
    #     print("Success!")

if __name__ == "__main__":
    main()