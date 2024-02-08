import numpy as np
from sklearn.manifold import LocallyLinearEmbedding, SpectralEmbedding
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set seed for reproducibility
np.random.seed(1)

# Generate Swissroll dataset
Nall = 8000
N = 6000
a = ((7/2*np.pi-np.pi/2)*(np.random.rand(Nall, 1)**0.65) + np.pi/2)
tall = 100*np.random.rand(Nall, 1)
Yall = np.column_stack([a*np.cos(a), tall, a*np.sin(a)])
Y = Yall[:N, :]
t = tall[:N, 0]
Yt = Yall[N:, :]
tt = tall[N:, 0]

# Plot the Swissroll dataset
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
ax1.scatter(Y[:, 0], Y[:, 1], Y[:, 2], s=3, c=t)
ax1.set_box_aspect([1, 1, 1])
ax1.view_init(-10, 2)
plt.show()

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection='3d')
ax2.scatter(Yt[:, 0], Yt[:, 1], Yt[:, 2], s=3, c=tt)
ax2.set_box_aspect([1, 1, 1])
ax2.view_init(-10, 2)
plt.show()

# Compute Gaussian affinities with bandwidth s and kW neighbors
print('Computing Gaussian affinities...')
s = 1.5
kW = 400
distances = np.sum((Y[:, None, :] - Y[None, :, :]) ** 2, axis=-1)
W = np.exp(-distances / (2 * s**2))
W_knn = np.zeros_like(W)
indices = np.argsort(distances, axis=-1)[:, :kW]
for i in range(N):
    W_knn[i, indices[i]] = W[i, indices[i]]
W = (W_knn + W_knn.T) / 2  # Make it symmetric

# Type of Laplacian and dimension of latent space
nl = 0
d = 2

# The usual Laplacian Eigenmaps on the entire dataset
print('Computing Laplacian Eigenmaps...')
embedding_le = SpectralEmbedding(n_components=d, affinity='precomputed')
XLE = embedding_le.fit_transform(W)

# Total number of landmarks and number of landmarks for each point, for LLL
L = 500
kZ = 3

# LLL
print('Computing LLL...')
embedding_lll = LocallyLinearEmbedding(n_components=d, n_neighbors=kZ, method='standard')
X = embedding_lll.fit_transform(Y)

# Project test points (in Yt) using LLL out-of-sample mapping
print('Computing LLL out-of-sample mapping...')
Xt = embedding_lll.transform(Yt)

# Plot results
fig3 = plt.figure(3)
plt.scatter(XLE[:, 0], XLE[:, 1], s=20, c=t)
plt.title(f'Laplacian Eigenmaps, runtime: {t1:.2f} s')
plt.show()

fig4 = plt.figure(4)
plt.scatter(X[:, 0], X[:, 1], s=20, c=t)
plt.title(f'LLL, runtime: {t2:.2f} s')
plt.show()

fig5 = plt.figure(5)
plt.scatter(Xt[:, 0], Xt[:, 1], s=20, c=tt)
plt.title(f'LLL (out-of-sample), runtime: {t3:.2f} s')
plt.show()
