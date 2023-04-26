Link : https://www.hackerrank.com/challenges/find-a-string/problem
  
def count_substring(string, sub_string):
    index = [i for i in range(len(string)) if string.startswith(sub_string, i)]
    i = len(index)
    return i

if __name__ == '__main__':
