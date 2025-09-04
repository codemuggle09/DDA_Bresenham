import matplotlib.pyplot as plt

# Define cube vertices
cube = [
    [-1, -1, -1], [1, -1, -1],
    [1,  1, -1], [-1, 1, -1],
    [-1, -1,  1], [1, -1,  1],
    [1,  1,  1], [-1, 1,  1]
]

# Define cube edges (pairs of vertices)
edges = [(0,1),(1,2),(2,3),(3,0),
         (4,5),(5,6),(6,7),(7,4),
         (0,4),(1,5),(2,6),(3,7)]

# -------- Projection functions --------
def orthographic_projection(point):
    x, y, z = point
    return (x, y)   # simply drop z

def perspective_projection(point, d=3):
    x, y, z = point
    return (x*d/(z+d+1e-5), y*d/(z+d+1e-5))  # avoid divide by zero

# -------- Plotting function --------
def plot_projection(projection_func, ax, title):
    proj_points = [projection_func(p) for p in cube]
    
    # Draw cube edges
    for e in edges:
        x_vals = [proj_points[e[0]][0], proj_points[e[1]][0]]
        y_vals = [proj_points[e[0]][1], proj_points[e[1]][1]]
        ax.plot(x_vals, y_vals, "bo-")  # blue lines with circle nodes
    
    ax.set_title(title)
    ax.set_aspect("equal")
    ax.grid(True)

# -------- Main visualization --------
fig, axs = plt.subplots(1, 2, figsize=(10,5))

plot_projection(orthographic_projection, axs[0], "Orthographic Projection")
plot_projection(perspective_projection, axs[1], "Perspective Projection")

plt.show()
