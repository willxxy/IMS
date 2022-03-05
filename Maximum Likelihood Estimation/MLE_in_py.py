import numpy as np
import math



x = np.array([[1, 2, 3, 4, 5]])

n = np.shape(x)[1]

print("The sample data: \n", x)
print("The number of data present in x is: ", n)

mu = np.array([[1, 2, 3, 2, 3]])
sigma = np.array([[1, 2, 2, 3, 3]])


print("\nThe mean is: ", mu)
print("The standard deviation is: ", sigma)


print("Mu Sigma logL")
for i in range(5):
    logL = -np.sum(np.square(x - mu[0, i])/(2 * np.square(sigma[0, i]))) - (0.5*n*np.log10(2*math.pi)) - n*np.log10(sigma[0,i])
    print(mu[0,i], sigma[0,i], np.round(logL, 3))
                                                
