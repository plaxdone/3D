import matplotlib.pyplot as plt
from skimage import data
camera = data.camera()
print('dtype:', camera.dtype)
print('shape:', camera.shape)

corte = 100
for x in range(len(camera)):
    for y in range(len(camera[x])):
        valor = camera[x][y]

        if valor <= corte:
            valor = 0
        else:
            valor = 255

        camera[x][y] = valor
print(camera)

plt.figure(figsize=(4, 4))
plt.imshow(camera, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.tight_layout()
plt.show()