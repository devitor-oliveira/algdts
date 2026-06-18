def binary_search(nums: list[int], n: int): # type: ignore
  low = 0
  high = len(nums)
  steps = 0
  while low < high:
    steps+=1
    mid = int((low+high)/2)

    if nums[mid] == n:
      print("Encontrado: ", nums[mid])
      print("Steps: ", steps)
      print("mid: ", nums[mid])
      print("low: ", nums[low])
      print("high: ", nums[high -1])
      return mid
    elif nums[mid] < n:
      print("mid: ", nums[mid])
      print("low: ", nums[low])
      print("high: ", nums[high -1])
      low = mid + 1
    else:
      print("mid: ", nums[mid])
      print("low: ", low)
      print("high: ", high)
      high = mid 
    
  return -1

a = [1, 2, 3 , 4, 5 , 78]

binary_search(a, 5);
