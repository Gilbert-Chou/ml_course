def read_dataset():
    f = open("breast-cancer-wisconsin.data", "r")
    cnt = 0
    data = dict()

    for d in f:
        #因為dataset有問號的資訊，無法被判斷數值，所以此資料跳過
        if d.find('?') == -1:
            dd = d[:len(d)-1].split(",", 11)
            data[cnt] = (dd[1], dd[2], dd[3], dd[4], dd[5], dd[6], dd[7], dd[8], dd[9], dd[10])
            cnt += 1
        
    f.close()

    return data

#分資料集 training set：test set = 7 : 3
def train_test_split(data):
    import random
    train_data = dict()
    train_label = dict()
    test_data = dict()
    test_label = dict()

    random.shuffle(data)

    train_cnt = 0
    test_cnt = 0

    for train_cnt in range(0, len(data)):
        if train_cnt < (len(data) * 0.7):
            train_data[train_cnt] = (data[train_cnt][0], data[train_cnt][1], data[train_cnt][2], data[train_cnt][3], data[train_cnt][4], data[train_cnt][5], data[train_cnt][6], data[train_cnt][7], data[train_cnt][8])
            train_label[train_cnt] = return_label(data[train_cnt][9])
        else:
            test_data[test_cnt] = (data[train_cnt][0], data[train_cnt][1], data[train_cnt][2], data[train_cnt][3], data[train_cnt][4], data[train_cnt][5], data[train_cnt][6], data[train_cnt][7], data[train_cnt][8])
            test_label[test_cnt] = return_label(data[train_cnt][9])
            test_cnt += 1
    
    return train_data, train_label, test_data, test_label

def return_label(index):
    # 2 for benign(良性) is labeled as True, 4 for malignant(惡性) is labeled as False
    if index=='2':
        return True
    else:
        return False

def euclidean_distance(x, y):
    import math
    if len(x) != len(y):
        return 0
    
    sum = 0
    for i in range(0, len(x)):
        sum += math.pow(math.fabs(float(x[i]) - float(y[i])), 2)

    return math.sqrt(sum)

#算所有test data的class
def knn_with_all(res, k = 3):
    predict = dict()

    for i in range(0, len(res)):
        predict[i] = knn(res[i], k)

    return predict

def knn(one_res, k):
    t = 0
    f = 0
    if k > len(one_res):
        return False

    for i in range(1, k):
        if one_res[i].get_label() == True:
            t += 1
        else:
            f += 1
    
    if t >= f:
        return True
    
    return False

def calc_accuracy(expect, actual):
    right = 0
    wrong = 0

    for i in range(0, len(expect)):
        if expect[i] == actual[i]:
            right += 1
        else:
            wrong += 1

    return right/(right + wrong)

class Calc_result:
    def __init__(self, dist, label):
        self.dist = dist
        self.label = label
    
    def get_dist(self):
        return self.dist
    
    def get_label(self):
        return self.label

def sort_cmp(elem):
    return elem.get_dist()

#執行knn演算法
def knn_execute(dataset):
    train_data, train_label, test_data, test_label = train_test_split(dataset)
    res = []

    #計算所有測資的距離
    for i in range(0, len(test_data)):
        tmp = []
        for j in range(len(train_data)):
            dist = euclidean_distance(test_data[i], train_data[j])
            tmp.append(Calc_result(dist, train_label[j]))
        
        res.append(tmp)

    #排序計算後距離
    for i in range(0, len(test_data)):
        res[i].sort(key=sort_cmp)

    accuracy = []
    #計算結果k = 3 ~ 15
    for i in range(3, 16):
        # print("k = " + str(i) + " accuracy is ", end='')
        predict = knn_with_all(res, i)
        accu = calc_accuracy(predict, test_label)
        # print(accu)
        accuracy.append(accu)

    return accuracy

if __name__ == '__main__':
    dataset = read_dataset()
    accu_array = []
    accuracy = []

    for i in range(0, 13):
        accuracy.append(0.0)

    #跑10次取平均
    for i in range(0, 10):
        accu_array.append(knn_execute(dataset))
        for j in range(0, len(accu_array[i])):
            accuracy[j] += accu_array[i][j]
 
    for i in range(3, 16):
        print("k = " + str(i) + " accuracy is ", end='')
        accuracy[i-3] = accuracy[i-3]/10
        print(accuracy[i-3])

     #畫圖
    import numpy as np
    import matplotlib.pyplot as plt

    plt.plot(range(3, 16), accuracy)
    plt.show()

    
