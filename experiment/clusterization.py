# скрипт для кластеризации приходских центров Софийской пошлины до степени,
# при которой каждая группа будет находиться в пределах только одной десятины

import doCluster

levels = 0

def func(group, desyatina):
    if len(set(desyatina)) == 1:
        return
    doCluster(group)
    func(ClusterID, desyatina)

# как передать в doCluster значения слоя постгис?


