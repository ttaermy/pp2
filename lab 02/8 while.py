#simple loop
i = 1
while i < 6:
  print(i)
  i += 1

#break -- stop even if "while" is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue -- to stop on this one and continue with the next one
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else -- once the condition is wrong
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")