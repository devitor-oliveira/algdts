#problema: Verificar o maior substring ou subarray que não tenha mais que dois valores repetidos

def slidwin(s: str) -> int:
  l: int = 0
  r: int = 0 
  _max = 1 # verificar se um item atingiu o tamanho máximo
  counter = {} # Hashmap | ddicionário
  counter[s[0]] = 1 # Registra o primeiro item com 1 contagem

  # Loop de expansão da substring para a direita (-1 para que a contagem não ultrapasse o tamanho da string original)
  while r < len(s) -1:
    r += 1  # Avança a seleção
    if counter.get(s[r]):  # pyright: ignore[reportUnknownMemberType] # verifica se o item existe no Hashmap
      counter[s[r]] += 1 #incrementa a contagem do item atual
    else: # Se não existe, inciializa no hashmap
      counter[s[r]] = 1
    while counter[s[r]] == 3: # Verifica se o ultimo item atingiu o limite
      counter[s[l]] -= 1 # Retira o item do range
      l+=1  # Avança o inicio da substring
    _max = max(_max, r-l+1)  # Calcula o máximo que pode haver. O máximo entre o _max atual e o tamanho da substring.

  return _max


print(slidwin("bcbbbcba"))