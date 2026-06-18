def binary_search(nums: list[int], n: int, low=0, high=None): # type: ignore
  if high is None:
    high = len(nums) -1
  while low < high:
    mid = int((low+high)/2)

    if nums[mid] == n:
      return mid
    elif nums[mid] < n:
      low = mid + 1
    else:
      high = mid 
  return -1

a = [1, 2, 3 , 4, 5 , 78]

def exposearch(arr, target): # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
  if arr[0] == target:
    return 0
  n = len(arr) # pyright: ignore[reportUnknownArgumentType]
  i = 1 #right pointer

  while i < n and arr[i] < target: # Se o ponteiro right for menor que o tamanho do array e menor que o target dobrar a área de busca
    i*=2
  if arr[i] == target: # se a posição do right pointer for igual ao target, a busca é concluida
    return i
  
  # executa a binary search passando o left e o right pointers do subarray que foi encontrado
  return binary_search(arr, target, i//2, min(i, n-1) ) # pyright: ignore[reportUnknownArgumentType, reportUnknownVariableType, reportCallIssue]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

target = 20
res = exposearch(numeros, target)

print("Found at: ", res)
