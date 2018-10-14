with open("guineec.broken", "r") as f, open("practical3.pot", "w") as of:
  formatted = ""
  for line in f:
    of.write(line.replace(" ", ":"))
