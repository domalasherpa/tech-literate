
fn = "hello"
sn = "world"
fs = "{0} {1}".format(fn, sn)  #using the format method

print(fs)
print("{1} {0}". format(fn, sn))

ss = f"{fn} {sn}"   #using the f-string method/ direct method

print(ss)