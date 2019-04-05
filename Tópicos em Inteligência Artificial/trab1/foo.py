import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def load_data(x_file, y_file):
  with open(x_file) as file:
    lines = file.readlines()
    X = np.asarray(lines, dtype=np.float32)
    file.close()

  with open(y_file) as file:
    lines = file.readlines()
    Y = np.asarray(lines, dtype=np.float32)
    file.close()

  X = np.expand_dims(X, 1)
  Y = np.expand_dims(Y, 1)

  return X, Y


def calculate_h_theta(X, thetas, m):
  # Inserir código do cálculo do h_theta

  h_theta = np.zeros((m,1))
  
  return h_theta
  
def calculate_J(X, Y, thetas):
  # Inserir o código do cálculo de J(theta_0, theta_1)
  J = 0
  
  return J

def do_train(X, Y, thetas, alpha, iterations):
  J = np.zeros(iterations)
  m, _ = np.shape(X)
  for i in range(iterations):
    J[i] = calculate_J(X, Y, thetas)
    h_theta = calculate_h_theta(X, thetas, m)
    # Inserir código para atualização dos valores de theta_0 e theta_1


  return J


if __name__ == "__main__":
  X, Y = load_data('entradas_x.txt', 'saidas_y.txt')

  thetas = np.zeros((2,1))
  alpha = 0

  J = do_train(X, Y, thetas, alpha=alpha, iterations=500)

  # Graphs to improve data visualization
  
  # J curve
  plt.figure(1)
  plt.subplot(121)
  plt.plot(J)
  plt.ylabel(r"$J(\theta)$", rotation=0)
  plt.xlabel("iteração")

  m, _ = np.shape(X)
  h_thetas = calculate_h_theta(X, thetas, m)

  # Dots and predicted line
  plt.subplot(122)
  plt.plot([X[0], X[-1]], [h_thetas[0], h_thetas[-1]])
  plt.plot(X, Y,'or')
  plt.xlabel('Idade')
  plt.ylabel('Altura')
  plt.axis([0.9*np.min(X), 1.1*np.max(X), 0.9*np.min(Y), 1.1*np.max(Y)])

  # Surface
  fig = plt.figure(2)
  ax = fig.gca(projection='3d')

  theta0_vals = np.arange(-3.0, 3.0, 0.06)
  theta1_vals = np.arange(-1.0, 1.0, 0.06)

  theta0_vals_, theta1_vals_ = np.meshgrid(theta0_vals, theta1_vals)
  J_surf = np.zeros((np.size(theta1_vals),np.size(theta0_vals)))

  for i in range(len(theta0_vals)):
      for j in range(len(theta1_vals)):
          thetas[0] = theta0_vals_[j,i]
          thetas[1] = theta1_vals_[j,i]
          J_surf[j,i] = calculate_J(X, Y, thetas)

  # Plot the surface.
  surf = ax.plot_surface(theta0_vals_, theta1_vals_, J_surf, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

  ax.set_xlabel(r'$\theta_0$')
  ax.set_ylabel(r'$\theta_1$')
  ax.set_zlabel(r'$J(\theta)$')
  plt.show()
