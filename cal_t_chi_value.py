# -*- coding: utf-8 -*-
import sys
import json
import scipy.stats


def read_data(file_path):
    with open(file_path) as json_file:
        raw_data = json.load(json_file)
    times = []
    for i in raw_data:
        times.append(i['execTime'])
    return times


# 计算均值
def cal_mean(data):
    return sum(data) / len(data)


# 计算方差
def cal_variance(data):
    n = len(data)
    m = cal_mean(data)
    r = 0.0
    for v in data:
        r += ((v - m) ** 2) / n
    return r


# 计算样本方差
def cal_sample_variance(data):
    n = len(data)
    return cal_variance(data) * n / (n - 1)


# 计算t值
def cal_t_value(e, m, s, n):
    t = (e - m) / ((s / n) ** (1/2))

    return t


# 计算chi-square值
def cal_chi_square_value(s, r, n):
    chi = (n - 1) * s / r

    return chi


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 3:
        print('用法：check_gpu_time <第一组GPU时间数据文件> <第二组GPU时间数据文件>')
    data1 = read_data(sys.argv[1])
    print(data1)
    data2 = read_data(sys.argv[2])
    print(data2)
    e1 = cal_mean(data1)
    r1 = cal_variance(data1)
    print(f'样本1均值为：{e1}、标准差为：{r1 ** 0.5}')
    e2 = cal_mean(data2)
    r2 = cal_sample_variance(data2)
    print(f'样本2均值为：{e2}、标准差为：{r2 ** 0.5}、样本方差为：{r2}')
    t = cal_t_value(e2, e1, r2, len(data2))
    p = scipy.stats.t.sf(abs(t), df=len(data2) - 1)
    print(f't value = {t}, p value = {p}')
    chi = cal_chi_square_value(r2, r1, len(data2))
    p = scipy.stats.chi2.sf(chi, df=len(data2) - 1)
    print(f'chi value = {chi}, p value = {p}')

