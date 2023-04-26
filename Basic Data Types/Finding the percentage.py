Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for key,values in student_marks.items():
        if query_name == key:
            val = values
 
    summ = 0
    for i in val:
        summ+=i
        
    x = summ/len(values)
    print(format(x,'.2f'))
