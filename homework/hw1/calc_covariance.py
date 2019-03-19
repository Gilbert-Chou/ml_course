def read_dataset():
    f = open("breast-cancer-wisconsin.data", "r")
    cnt = 0
    data = []

    for i in range(0, 9):
        data.append([])

    for d in f:
        #因為dataset有問號的資訊，無法被判斷數值，所以此資料跳過
        if d.find('?') == -1:
            dd = d[:len(d)-1].split(",", 11)
            data[0].append(int(dd[1]))
            data[1].append(int(dd[2]))
            data[2].append(int(dd[3]))
            data[3].append(int(dd[4]))
            data[4].append(int(dd[5]))
            data[5].append(int(dd[6]))
            data[6].append(int(dd[7]))
            data[7].append(int(dd[8]))
            data[8].append(int(dd[9]))
            cnt += 1
        
    f.close()

    return data

if __name__ == '__main__':
    dataset = read_dataset()
    # print(dataset)
    import numpy as np
    # print(dataset[1])
    X = np.vstack((dataset[0], dataset[1], dataset[2], dataset[3], dataset[4], dataset[5], dataset[6], dataset[7], dataset[8]))
    res = np.cov(X)
    coef = np.corrcoef(res)

    # for i in res:
    #     for j in i:
    #         print(str(np.round(j, 3)) + "  ", end='')
    #     print()
    # print(np.round(res, 3))
    print(np.round(coef, 3))
    # print(np.cov(dataset[0], dataset[1])#, dataset[2], dataset[3], dataset[4], dataset[5], dataset[6], dataset[7], dataset[8]))