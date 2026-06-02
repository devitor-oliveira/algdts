
def freqmap(s: str) -> dict:
  hash = {}
  for ch in s:
    if ch in hash:
      hash[ch] += 1
    else:
      hash[ch] = 1
  return hash


print(freqmap("AABBCCAA"))