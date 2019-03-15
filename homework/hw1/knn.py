def read_dataset():
    f = open("breast-cancer-wisconsin.data", "r")
    cnt = 0
    data = dict()

    for d in f:
        # print("No." + str(cnt) + ": " + d)
        dd = d[:len(d)-1].split(",", 11)
        # data[str(dd[0])] = (dd[1], dd[2], dd[3], dd[4], dd[5], dd[6], dd[7], dd[8], dd[9])
        data[cnt] = (dd[1], dd[2], dd[3], dd[4], dd[5], dd[6], dd[7], dd[8], dd[9], dd[10])
        

        #print data for test 
        # print(data[cnt], end='')
        # print(" Status: ", end='')
        # if label[cnt] == True:
        #     print("Benign")
        # else:
        #     print("Malignant")
        cnt += 1

    f.close()

    return data

def train_test_split(data):
    import random
    train_data = dict()
    train_label = dict()
    test_data = dict()
    test_label = dict()

    # print(data[0])
    random.shuffle(data)
    # print(data[0])

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

if __name__ == '__main__':
    dataset = read_dataset()
    train_data, train_label, test_data, test_label = train_test_split(dataset)
    print(euclidean_distance(train_data[0], test_data[0]))
    # print(train_data[0])
    # print(len(train_data[0]))