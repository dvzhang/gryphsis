from itertools import combinations, permutations, product
from collections import defaultdict

def def_value():
    return 0

def create_sybils(ip_pool, wallets):
    """
    Parameters:
    ip_pool - the ip list, which contain 8 ip, will be used. ex:(2, 3, 5, 6, 7, 8, 9, 10)
    wallets - the wallets will be used ex: [1, 2, 3, 4, 5]

    Returns:
        all possible combination between ip_pool & wallets
        
    EX:
        len(create_sybils((2, 3, 5, 6, 7, 8, 9, 10), range(1, 6))) == 390625 == 5^8
    """
    # 递归结束
    if len(ip_pool) == 1:
        return [["{}-{}".format(ip_pool[0], wallet)] for wallet in wallets]
    # 递归，减而治之
    sybils = create_sybils(ip_pool[1:], wallets)
    ans = []
    for sybil in sybils:
        for wallet in wallets:
            ans.append(["{}-{}".format(ip_pool[0], wallet)] + sybil)
    return ans


def canUse(sybil, cooc_dict, walletNum_thres = 4, cooc_thres = 3):
    """
    check if we add this sybil to our code book, will we be detected
    """
    comb = list(combinations(sybil, walletNum_thres))
    for cooc_sybil in comb:
        if cooc_dict[" ".join(cooc_sybil)] == cooc_thres:
            return False
    for cooc_sybil in comb:
        cooc_dict[" ".join(cooc_sybil)] += 1
    return True


def sybil_hunter(sybil_list, ip_num=10, wallet_num=5):
    """
    check whether some addresses are sybil
    """
    ips = range(1, 1+ip_num)
    sybilCom_dict = combinations(ips, 8)
    # co-occurrence counter
    cooc_dict = defaultdict(def_value)
    for sybil in sybil_list:
        if not canUse(sybil, cooc_dict):
            return False
    # for i in cooc_dict:
    #     print("{}\t{}".format(i, cooc_dict[i]))
    return True


def sybilAttact_queue(ip_num=10, wallet_num=5):
    ips = range(1, 1+ip_num)
    wallets = range(1, 1+wallet_num)
    
    sybilCom_dict = combinations(ips, 8)

    # co-occurrence counter
    cooc_dict = defaultdict(def_value)
    ans = []
    
    for i, ip_pool in enumerate(sybilCom_dict):
        for sybil in create_sybils(ip_pool, wallets):
            if canUse(sybil, cooc_dict):
                ans.append(sybil)
                
    print(len(ans))
    print(ans[:20])
    # print(sybil_hunter(ans))


sybilAttact_queue()