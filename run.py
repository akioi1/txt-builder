import photomosaic as pm

image = pm.imread("C:/Users/Administrator/Desktop/txt builder/image/CSPRP++.jpg", as_gray=False)

pool = pm.make_pool("C:/Users/Administrator/Desktop/txt builder/image2/*.jpg")

mosaic = pm.basic_mosaic(image, pool, (325, 991))

pm.imsave("C:/Users/Administrator/Desktop/txt builder/out.jpg", mosaic)