Link : https://www.hackerrank.com/challenges/text-wrap/problem
  
import textwrap

def wrap(string, max_width):
    
    lst = []
    while len(string) > max_width:
        lst.append(string[0:max_width])
        string = string[max_width:]
    #append the remain string which its length is less than max_width
    len(string) >0 and lst.append(string)
    return '\n'.join(lst)

if __name__ == '__main__':
