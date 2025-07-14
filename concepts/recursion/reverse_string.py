import sys

def reverse_string(s):
  if len(s) == 0:
    return ''
  return s[-1] + reverse_string(s[0:-1])

if __name__ == '__main__':
  s = sys.argv[1]
  print(f"{s}, {reverse_string(s)}")

