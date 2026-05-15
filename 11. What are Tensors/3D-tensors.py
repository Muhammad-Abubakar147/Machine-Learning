import numpy as np
# Height = 2
# Width = 2
# Channels = 3 (RGB)
image = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
])
print(image)
print("Shape:", image.shape)