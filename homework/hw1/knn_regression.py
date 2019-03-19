
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
 
 
n_dots = 40
X = 5 * np.random.rand(n_dots, 1)
y = np.cos(X).ravel()
print(X)
#add noise
y += 0.1 * np.random.rand(n_dots) - 0.1
 
#KNN Regression
k = 5
knn = KNeighborsRegressor(k)
knn.fit(X,y)
prec = knn.score(X, y)  #计算拟合曲线针对训练样本的拟合准确性
print(prec)
 
#generate enough predict data
T = np.linspace(0, 5, 500)[:, np.newaxis]
y_pred = knn.predict(T)
 
#draw regress curve
plt.figure(figsize=(16, 10), dpi = 81)
plt.scatter(X, y, c='g', label='data', s=100) #训练样本
plt.scatter(T, y_pred, c='k', label='prediction', lw=2) #拟合曲线
plt.axis('tight')
plt.title('KNN regression (k =%i)'%k)
#plt.title()
plt.show()
#print(X)
#print(y)
 
plt.show()


# def read_dataset():
#     f = open("machine.data", "r")
#     cnt = 0
#     data = dict()

#     for d in f:
#         #因為dataset有問號的資訊，無法被判斷數值，所以此資料跳過
#         if d.find('?') == -1:
#             dd = d[:len(d)-1].split(",", 10)
#             data[cnt] = (dd[2], dd[3], dd[4], dd[5], dd[6], dd[7], dd[8], dd[9])
#             cnt += 1
        
#     f.close()

#     return data

# if __name__ == '__main__':
#     dataset = read_dataset()
#     print(dataset)
#     accu_array = []
#     accuracy = []

