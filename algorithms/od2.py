"""
某系统中有众多服务，每个服务用字符串(只包含字母和数字，长度<=10)唯一标识，服务间可能有依赖关系，如A
依赖B，则当B故障时导致A也故障。依赖具有传递性，如A依赖B，B依赖C，当C故障时导致B故障，也导致A故障。给
出所有依赖关系，以及当前已知故障服务，要求输出所有正常服务。

依赖关系:服务1-服务2表示“服务1”依赖“服务2”

不必考虑输入异常，用例保证:依赖关系列表、故障列表非空，且依赖关系数，故障服务数都不会超过3000服务标
识格式正常

输入描述

半角逗号分隔的依赖关系列表(换行)

半角逗号分隔的故障服务列表

输出描述

依赖关系列表中提及的所有服务中可以正常工作的服务列表，用半角逗号分隔，按依赖

关系列表中出现的次序排序。

特别的，没有正常节点输出单独一个半角逗号.

"""


def server_available(dependencies: list, faultServers: list):
    depMap = {}
    servers = set()
    for d in dependencies:
        servers.add(d[0])
        servers.add(d[1])
        if depMap.get(d[1]) is not None:
            depMap[d[1]].append(d[0])
        else:
            depMap[d[1]] = [d[0]]

    def deleteBrokenServers(s: str):
        servers.remove(s)
        if depMap.get(s) is not None:
            for fs in depMap.get(s):
                deleteBrokenServers(fs)

    for s in faultServers:
        deleteBrokenServers(s)

    return list(servers)


assert server_available([["a1", "a2"], ["a5", "a6"], ["a2", "a3"]], ["a5", "a2"]) == [
    "a6",
    "a3",
]

assert server_available([["a1", "a2"]], ["a2"]) == []
