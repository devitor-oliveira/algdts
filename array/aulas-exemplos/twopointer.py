def twop( s: str):
  res = ''
  l, r = 0, 0
  # enquanto r for menor que a palavra
  while r < len(s):
    # se ponteiro right for diferente de um espaço em branco (Está dentro da palavra) andar pra direita
    if s[r] != " ":
      r += 1
      # se não, concatenar a primeira palavra na resposta e pular pra próxima palavra
    else:
      # Selecionar de ponteiro Left (inicio) até ponteiro right (Espaço em branco) e inverter
      res += s[l:r + 1][::-1]
      r += 1 # ponteiro right pula para a primeira letra da próxima palavra
      l = r # ponteiro left acompanha
  res += " " # adiciona espaço em branco
  res += s[l:r + 2][::-1] # Seleciona as palavras e inverte o restante
  return res[1:] # Retorna sem o espaço em branco adicionado
  
string = "Mr Ding"
print(twop(string));
