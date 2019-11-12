def solution(arr):
  mx = arr[0]

  for i in arr:
    mx = max(i, mx)

  return mx