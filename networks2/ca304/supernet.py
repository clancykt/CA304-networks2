# supernet calculator
# supernetting is the procedure of combining networks

# creates a string of binary digits from the IP
def conv_binary(ip):
    spl = ip.split(".")
    return ['{0:08b}'.format(int(n)) for n in spl]

# creates a string of decimal digits seperated by dots
def conv_decimal(ip_ls):
    return ".".join([str(int(n, 2)) for n in ip_ls])

def supernet_dets(class_c_list):
    binary_ls = []
    for netwk in class_c_list:
        bin_ls = conv_binary(netwk)
        bin = "".join(bin_ls)
        binary_ls.append(bin)

supernet_dets(["205.100.0.0"])
