def read_dataset():
    f = open("breast-cancer-wisconsin.data", "r")
    cnt = 0
    data = dict()

    for d in f:
        dd = d[:len(d)-1].split(",", 11)
        data[cnt] = (dd[1], dd[2], dd[3], dd[4], dd[5], dd[6], dd[7], dd[8], dd[9], dd[10])
        cnt += 1
        
    f.close()

    #處理dataset有問號的資訊
    return missing_data_handler(data)


def missing_data_handler(data):
    import numpy as np
    data_handled = dict()
    data_handled_T = []
    data_handled_F = []
    attribute_T = np.zeros(9)
    attribute_T_cnt = np.zeros(9)
    attribute_F = np.zeros(9)
    attribute_F_cnt = np.zeros(9)

    for d in data:
        if data[d][9] == '2':
            for i in range(0, len(data[d])-1):
                if data[d][i] != '?' :
                    attribute_T[i] += int(data[d][i])
                    attribute_T_cnt[i] += 1
        else:
            for i in range(0, len(data[d])-1):
                if data[d][i] != '?' :
                    attribute_F[i] += int(data[d][i])
                    attribute_F_cnt[i] += 1

    mean_T = attribute_T / attribute_T_cnt
    mean_F = attribute_F / attribute_F_cnt

#All of data
    for d in data:
        if find_missing(data[d]) == -1:
            data_handled[d] = (int(data[d][0]), int(data[d][1]), int(data[d][2]), int(data[d][3]), int(data[d][4]), int(data[d][5]), int(data[d][6]), int(data[d][7]), int(data[d][8]), int(data[d][9]))
        else:
            if data[d] == '2':
                data_handled[d] = (int(data[d][0]), int(data[d][1]), int(data[d][2]), int(data[d][3]), int(data[d][4]), round(mean_T[find_missing(data[d])]), int(data[d][6]), int(data[d][7]), int(data[d][8]), int(data[d][9]))
            else:
                data_handled[d] = (int(data[d][0]), int(data[d][1]), int(data[d][2]), int(data[d][3]), int(data[d][4]), round(mean_F[find_missing(data[d])]), int(data[d][6]), int(data[d][7]), int(data[d][8]), int(data[d][9]))

#Split True and False data  
    for i in range(0, 10):
        data_handled_T.append([])
        data_handled_F.append([])
 
    for d in data:
        if data[d][9] == '2':
            data_handled_T[0].append(int(data[d][0]))
            data_handled_T[1].append(int(data[d][1]))
            data_handled_T[2].append(int(data[d][2]))
            data_handled_T[3].append(int(data[d][3]))
            data_handled_T[4].append(int(data[d][4]))
            data_handled_T[6].append(int(data[d][6]))
            data_handled_T[7].append(int(data[d][7]))
            data_handled_T[8].append(int(data[d][8]))
            data_handled_T[9].append(int(data[d][9]))
            if find_missing(data[d]) == -1:
                data_handled_T[5].append(int(data[d][5]))
            else:
                data_handled_T[5].append(round(mean_T[find_missing(data[d])]))
        else:
            data_handled_F[0].append(int(data[d][0]))
            data_handled_F[1].append(int(data[d][1]))
            data_handled_F[2].append(int(data[d][2]))
            data_handled_F[3].append(int(data[d][3]))
            data_handled_F[4].append(int(data[d][4]))
            data_handled_F[6].append(int(data[d][6]))
            data_handled_F[7].append(int(data[d][7]))
            data_handled_F[8].append(int(data[d][8]))
            data_handled_F[9].append(int(data[d][9]))
            if find_missing(data[d]) == -1:
                data_handled_F[5].append(int(data[d][5]))
            else:
                data_handled_F[5].append(round(mean_F[find_missing(data[d])]))


    return data_handled, data_handled_T, data_handled_F

def find_missing(d):
    for i in range(0, len(d)-1):
        if(d[i] == '?'):
            return i
            
    return -1


def return_label(index):
    # 2 for benign(良性) is labeled as True, 4 for malignant(惡性) is labeled as False
    if index=='2':
        return True
    else:
        return False

def gnb(dataset_T, dataset_F, test):
    import numpy as np
    import math
    attr_mean_T = []
    attr_mean_F = []
    attr_var_T = []
    attr_var_F = []
    probability_T = len(dataset_T)+1 / (len(dataset_T) + len(dataset_F) + 2)
    probability_F = len(dataset_F)+1 / (len(dataset_T) + len(dataset_F) + 2)
    
    #p(attr | true)
    T_of_attr = []
    #p(attr | false)
    F_of_attr = []

    for i in range(0, 9):
        attr_mean_T.append(np.mean(dataset_T[i]))
        attr_mean_F.append(np.mean(dataset_F[i]))
        attr_var_T.append(np.var(dataset_T[i]))
        attr_var_F.append(np.var(dataset_F[i]))
    
    for i in range(0, 9):
        T_of_attr.append( (1 / math.sqrt(2 * math.pi * attr_var_T[i])) * math.exp( (math.pow((test[i] - attr_mean_T[i]), 2) / (-2 * attr_var_T[i]))) )
        F_of_attr.append( (1 / math.sqrt(2 * math.pi * attr_var_F[i])) * math.exp( (math.pow((test[i] - attr_mean_F[i]), 2) / (-2 * attr_var_F[i]))) )

    predict_T = probability_T * T_of_attr[0] * T_of_attr[1] * T_of_attr[2] * T_of_attr[3] * T_of_attr[4] * T_of_attr[5] * T_of_attr[6] * T_of_attr[7] * T_of_attr[8]
    predict_F = probability_F * F_of_attr[0] * F_of_attr[1] * F_of_attr[2] * F_of_attr[3] * F_of_attr[4] * F_of_attr[5] * F_of_attr[6] * F_of_attr[7] * F_of_attr[8]
    result = -1

    if (predict_T / (predict_T + predict_F)) >= predict_F / (predict_T + predict_F):
        result = 2
    else:
        result = 4
    
    if result == test[9]:
        # print("Bingo")
        return True
    else:
        return False


if __name__ == '__main__':
    dataset, dataset_T, dataset_F = read_dataset()

    correct = 0
    incorrect = 0
    import random
    for i in range(0, 300):
        tmp = random.randint(0, 698)
        if gnb(dataset_T, dataset_F, dataset[tmp]):
            correct += 1
        else:
            incorrect += 1

    print("Accuracy is :", correct / 300)

