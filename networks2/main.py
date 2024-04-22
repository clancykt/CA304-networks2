from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return{"Home": {"project": "IP Address Calculator"}}

# using a dictionary to store info about classes
# this will be used to classify each IP address
class_info = {
    "a": {
        "bits_in_host": 24,
        "bits_in_network": 7
    },
    "b": {
        "bits_in_host": 16,
        "bits_in_network": 14
    },
    "c": {
        "bits_in_host": 8,
        "bits_in_network": 21
    },
}
# class D and E not included
# these bits are reserved for multicasting
# multicasting - sending packets to multiple IP addresses

class ipaClass(BaseModel):
    ipa: str

# using 'GET' requests so something is returned in response

@app.get("/ipcalc") # endpoint = /ipcalc
async def ipcalc(info: ipaClass, description="classifies each address by splitting it up & examining first octet"):

    dict = {}

    # split each Ip address into 4 parts 'octets'
    # at the dot
    split_ip = int(info.ipa.split(".")[0])

    a = class_info["a"]
    b = class_info["b"]
    c = class_info["c"]

    # classify by examining first octet
    if split_ip in range (0, 127):
        dict["IP CLASS"] = "a"
        dict["HOSTS"] = 2 ** a["bits_in_host"]
        dict["NETWORKS"] = 2 ** a["bits_in_network"]
        dict["FIRST ADDRESS, LAST ADDRESS"] = "0.0.0.0, 127.255.255.255"

    elif split_ip in range (128, 191):
        dict["IP CLASS"] = "b"
        dict["HOSTS"] = 2 ** b["bits_in_host"]
        dict["NETWORKS"] = 2 ** b["bits_in_network"]
        dict["FIRST ADDRESS, LAST ADDRESS"] = "128.0.0.0, 191.255.255.255"

    elif split_ip in range (192, 223):
        dict["IP CLASS"] = "c"
        dict["HOSTS"] = 2 ** c["bits_in_host"]
        dict["NETWORKS"] = 2 ** c["bits_in_network"]
        dict["FIRST ADDRESS, LAST ADDRESS"] = "192.0.0.0, 223.255.255.255"

    # only info given about class D & E is first & last address
    else:
        dict["CLASS"] = "D / E"
        dict["FIRST ADDRESSES, LAST ADDRESSES"] = "224.0.0.0 / 240.0.0.0, 239.255.255.255 / 255.255.255.255"

    return "IP Calculated: " + dict

# subnetting - procedure to divide the network into sub-networks
# networks address bits increased
class subnetClass(BaseModel):
    ipa: str
    sbmask: str

    # subnet mask helps us understand the difference
    # between the network and host parts of addresses

@app.get("/subnet")
async def subnet(info: subnetClass, description="returns a CIDR representation of the address, gets no. valid hosts / subnet"):

    dict = {}

    # removing the dots from the IP address and mask address
    info = info.ipa
    ipa = info.ipa.split(".")
    submask = info.sbmask.split(".")
    oct = info.ipa.split(".")

    # converting into octets and then to binary format
    bin = ".".join([b(int(n) + 256)[3:] for n in submask])
    bin_ls = [format(int(n), "{0:08b}") for n in submask]

    bin_str = "".join(bin)

    # counter for CIDR will hold
    # num of '1's in te binary string
    CIDR_count = 0

    for x in bin_str:
        if x == "1":
            CIDR_count += 1

    # no. of subnets calculated by converting submask to binary
    # counter for the '1's in the binary list
    subnet_count = 0
    # working with octet at pos 3
    # which is last octet
    for x in bin_ls[3]:
        if x == str(1):
            subnet_count += 1

    sub_num = (2 ** subnet_count)

    # unmasked bits are identified by tracking all instances of '0'
    # the counter is returned to show num of unmasked bits
    unmasked_count = 0

    # calculating the number of addressable hosts
    # per subnet
    # by iterating through binary list
    # and upping counter by one when a zero is found
    for x in bin_ls[3]:
        if x == str(0):
            unmasked_count += 1

    available_hosts = (2 ** unmasked_count - 2)

    subnets_check = []
    # [3] calls for the last octet to be returned
    msk = int(submask[3])

    # getting number of valid subnets
    size = (256 - msk)
    # convert octet to string and add to list if class A
    i = 0
    while i <= msk:
        ipa[3] = str(i)
        subnet_check.append(".".join(ipa))
        i += size

        # broadcast address always found before next subnet
        brdcast = []
        brdcast_size = size - 1

        while brdcast_size <= 255:
            ipa[3] = str[brdcast_size]

    # return values
    dict["address_in_CIDR"] = str(info) + "/" + str(CIDR_count)
    dict["no_of_subnets"] = sub_num
    dict["hosts_/_subnets"] = available_hosts
    dict["valid_subnets"] = subnets_check
    dict["broadcast_addresses"]

    return "IP Calculated: " + dict

# example input: '136.206.18.7'
# example output: (outputted in above format) 'Class B', 'Host 65536', 'Network: 16384',
# 'First & Last Address: '128.0.0.0','191.255.255.255''

# references:
# https://www.youtube.com/watch?v=-ykeT6kk4bk - 'Python FastAPI Tutorial'
# https://www.youtube.com/watch?v=LqTFvASGdtM - 'FastAPI with Python'
# https://www.youtube.com/watch?v=lE7obYznoyk&t=56s - 'what are endpoints'
# https://www.youtube.com/watch?v=LIzTo6e4FgY - 'IP Addresses explained'
# https://www.youtube.com/watch?v=s_Ntt6eTn94&t=57s - 'subnet mask explained'

