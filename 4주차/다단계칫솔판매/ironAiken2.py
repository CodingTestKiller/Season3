import sys
sys.setrecursionlimit(10**6)

def make_tree(enroll, referral, tree, earn):
    for name, refer in zip(enroll, referral):
        tree[name] = refer
        earn[name] = 0
    

def cal_money(tree, earn, seller, amount):
    thief = int(amount*0.1)
    amount -= thief
    earn[seller] += amount
    
    if tree[seller] == '-':
        return
    
    if thief < 1:
        return
    cal_money(tree, earn, tree[seller], thief)
    
def solution(enroll, referral, seller, amount):
    tree = {}
    earn = {}
    make_tree(enroll, referral, tree, earn)
    for name, money in zip(seller, amount):
        cal_money(tree, earn, name, money*100)
        
    ans = []
    for name in earn:
        ans.append(earn[name])
        
    return ans
    
    