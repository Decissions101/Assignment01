import numpy as np


def generate_annulus_4d(
    n_samples=1500, inner_radius=0.7, outer_radius=1.0, noise=0.02, seed=42
):
    np.random.seed(seed)

    theta = np.random.uniform(0, 2 * np.pi, n_samples)
    r = np.random.uniform(inner_radius, outer_radius, n_samples)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    z = np.random.normal(0, noise, n_samples)
    data_3d = np.column_stack([x, y, z])

    transform_matrix = np.array(
        [[0.5, 0.5, 0.5], [0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, -0.5, 0.5]]
    ) * np.sqrt(2)  # Scale to preserve distances
    data_4d = data_3d @ transform_matrix.T

    return data_4d, r
