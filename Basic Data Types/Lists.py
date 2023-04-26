Link : https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
  
if __name__ == '__main__':
    N = int(input())
    
commands = []
list_ = []

for i in range(0, N):
    command = input()
    commands.append(command)
    
for command in commands:
    if command.split()[0] == "insert":
        list_.insert(int(command.split()[1]),int(command.split()[2]))
    elif command.split()[0] == "print":
        print(list_)
    elif command.split()[0] == "remove":
        list_.remove(int(command.split()[1]))
    elif command.split()[0] == "append":
        list_.append(int(command.split()[1]))
    elif command.split()[0] == "sort":
        list_.sort()
    elif command.split()[0] == "pop":
        list_.pop()
    elif command.split()[0] == "reverse":
        list_.reverse()
