with open("guineec.broken", "r") as f, open("guineec_new.broken", "w+") as of:
  for line in f:
    if len(line) == 23:
      of.write(line[:-2] + "\n")
    else:
      of.write(line)