Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    

    lis=[]
    for i in arr:
        if i not in lis:
         lis.append(i)
         
    lis =sorted(lis, reverse=True)
    
    
    print(lis[1])
