import numpy as np
import matplotlib.pyplot as plt
import K_nearest

x_train = np.asarray([(5,1),(2,3),(4,6),(9,8),(8,1),(7,2),(0,5)])
y_train = np.asarray([0,0,1,0,1,1,1])
x_test = np.asarray([(1,2)])
knn = K_nearest.KNN(2)
knn.fit(x_train,y_train)
fg,ax = plt.subplots()
y_test = np.asarray(knn.predict(x_test))
plt.scatter(x_train[:,0],x_train[:,1],c=y_train)
plt.scatter(x_test[:,0],x_test[:,1],c=y_test ,marker = "^")
plt.show()
print(y_test)




