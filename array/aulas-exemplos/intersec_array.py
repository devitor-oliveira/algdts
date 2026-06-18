# Problema intersecção dos arrays

# Solução desenvolvida a pedido do Augusto na aula: Percorrer os dois arrays uma vez, fazendo dedup com hashmap. 
# Após, comparar os arrays e identificar a intersecção entre eles (Números que estão em ambos arrays)
# Possivelmente pode ser resolvido com SET também já que é uma lista de valores únicos

from typing import List

nums2 = [1, 2, 2, 1, 3]
nums1 = [2, 2, 3]

def intersec(nums1: List[int], nums2: List[int]) -> List[int]:
  seen1 = {}
  seen2 = {}
  result = []

  for n in nums1:
    if n not in seen1:
      seen1[n] = 1
    
  for n2 in nums2:
    if n2 not in seen2:
      seen2[n2] = 1
    
  for num in seen1: # type: ignore
    if num in seen2: # type: ignore
      result.append(num) # type: ignore
    
  return result # type: ignore
  
  
print("result: ", intersec(nums1, nums2))

# Solução da Aula: Como comentado acima, ele utiliza o SET
# Transformar as listas em Sets e retornar a intersecção entre os dois SETs (Operador &)

def intersec_set(nums1: List[int], nums2: List[int]) -> List[int]:
  setNums1 = set(nums1)
  setNums2 = set(nums2)

  return list(setNums1&setNums2)

print("Intersecção de SETs: ", intersec_set(nums1, nums2))


