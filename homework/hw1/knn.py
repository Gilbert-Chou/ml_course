def read_dataset():
    f = open("breast-cancer-wisconsin.data", "r")
    cnt = 0

    for d in f:
        print("No." + str(cnt) + ": " + d)
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

def train_test_split():
    import random
    print(data[0])
    random.shuffle(data)
    print(data[0])

    train_cnt = 0
    test_cnt = 0

    for train_cnt in range(0, len(data)):
        if train_cnt < (len(data) * 0.7):
            train_data[train_cnt] = (data[train_cnt][0], data[train_cnt][1], data[train_cnt][2], data[train_cnt][3], data[train_cnt][4], data[train_cnt][5], data[train_cnt][6], data[train_cnt][7], data[train_cnt][8])
        else:
            test_data[test_cnt] = (data[train_cnt][0], data[train_cnt][1], data[train_cnt][2], data[train_cnt][3], data[train_cnt][4], data[train_cnt][5], data[train_cnt][6], data[train_cnt][7], data[train_cnt][8])
            test_cnt += 1

        # 2 for benign(良性) is labeled as True, 4 for malignant(惡性) is labeled as False
        if data[train_cnt][9]=='2':
            label[train_cnt] = True
        else:
            label[train_cnt] = False


if __name__ == '__main__':
    data = dict()
    label = dict()
    train_data = dict()
    test_data = dict()

    read_dataset()
    train_test_split()