# python3
import sys

def preFixFunction(p):
    n = len(p)
    s = [-1]*n
    s[0] = 0
    border = 0
    
    for i in range(1, n):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s
    
def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    # Implement this function yourself
    string = pattern + '$' + text
    s = preFixFunction(string)
    n = len(string)
    p = len(pattern)
    
    #print(s)
    for i in range(len(pattern)+1, n):
        if s[i] == p:
            result.append(i - 2*p)
            
    return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

