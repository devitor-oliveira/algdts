# Eleemntos duplicados - Hashmap/Array

from typing import List


array = [1, 1, 2, 3]

def contains_duplicate(nums: List[int]) -> bool:
  hash = {}
  # hash[nums[0]] = 1
  for n in nums:
    # if n in hash:
      # hash[nums[n]] += 1
    if hash.get(n):
      return True
    hash[n] = 1
  return False


print("Contém duplicata: ", contains_duplicate(array))
