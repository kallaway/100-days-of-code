def solution(arr):
  maximum = 0
  
  for elem in arr:
    if elem > maximum:
      maximum = elem

  return maximum