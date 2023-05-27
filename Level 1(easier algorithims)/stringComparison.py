def solution(text,ending):
  return True if text[len(text)-len(ending):len(text)] == ending else False


print(solution("hey","y"))