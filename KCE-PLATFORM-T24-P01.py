def calc(expr):
  tokens = expr.split()
  allowed_ops = ["+", "-", "*", "/"]
  i = 0
  while i < len(tokens):
    t = tokens[i]
    if t not in allowed_ops:
        try:
          float(t)
        except Exception as e:
          return 'Input Mismatch'
    else:
        if t not in allowed_ops:
            return 'Input Mismatch'
    i = i+1
  is_float = False
  i = 0
  while i < len(tokens):
    if "." in tokens[i] or tokens[i]=="/":
        is_float = True
        break
    i = i+1
  i = 0
  while i < len(tokens):
    if tokens[i]=="*"  or tokens[i]=="/":
        a = float(tokens[i-1])
        b = float(tokens[i+1])
        if tokens[i]=="*":
            result = a*b
        else:
            if b==0:
                return 'Error: divide by zero'
            result = a/b
        tokens[i-1] = str(result)
        tokens[i:i+2] = []
        i = i-1
    else:
        i = i+1
  result = float(tokens[0])
  i = 1
  while i < len(tokens)-1:
    op = tokens[i]
    value = float(tokens[i+1])
    if op=="+":
        result = result+value
    elif op=="-":
        result = result-value
    i = i+2
  if is_float:
      return result
  else:
      if int(result)==result:
          return int(result)
      return result
print(calc("2 + 3"))
print(calc("2 + 3 * 4"))
print(calc("10 / 2 - 3"))
print(calc("2 + abc"))