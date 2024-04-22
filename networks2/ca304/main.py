from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return{"Home": {"project": "IP Address Calculator"}}

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

class ipa(BaseModel):
    ipa: str

@app.get("/ipcalc")
async def ipcalc(info: ipa):

    dict = {}

    split_ip = int(info.ipa.split(".")[0])

    a = class_info["a"]
    b = class_info["b"]
    c = class_info["c"]

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

    else:
        dict["CLASS"] = "D / E"
        dict["FIRST ADDRESSES, LAST ADDRESSES"] = "224.0.0.0 / 240.0.0.0, 239.255.255.255 / 255.255.255.255"

    return dict
