import json
from pprint import pprint



# List to hold elements of the clean nodeJS api json
ext_list = []


# For the assert part of the api
# This is where the methods rely in the json given by the website
# Open a json file as read and load contents into json_data
json_path = "assert.json"
with open(json_path,"r") as json_file:
    assert_data = json.load(json_file)
    json_file.close()

for v in assert_data["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    # Create a list each element of which is a dict to use for writing into
    # my own json file
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})


# For buffer
json_path = "buffer.json"
with open(json_path,"r") as json_file:
    buffer_data = json.load(json_file)
    json_file.close()

for v in buffer_data["modules"][0]["classes"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    # Create a list each element of which is a dict to use for writing into
    # my own json file
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

# child_process
json_path = "child_process.json"
with open(json_path,"r") as json_file:
    child_process_data = json.load(json_file)
    json_file.close()
for v in child_process_data["modules"][0]["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in child_process_data["modules"][0]["modules"][1]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

# cluster
json_path = "cluster.json"
with open(json_path,"r") as json_file:
    cluster_data = json.load(json_file)
    json_file.close()
for v in cluster_data["modules"][0]["classes"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in cluster_data["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

# console
json_path = "console.json"
with open(json_path,"r") as json_file:
    console_data = json.load(json_file)
    json_file.close()
for v in console_data["modules"][0]["classes"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#crypto
json_path = "crypto.json"
with open(json_path,"r") as json_file:
    crypto_data = json.load(json_file)
    json_file.close()

for v in crypto_data["modules"][0]["modules"][1]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in crypto_data["modules"][0]["classes"]:
    for vv in v["methods"]:
        raw_text = vv["textRaw"]
        params = [p["name"] for p in vv["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#dgram UDP
json_path = "dgram.json"
with open(json_path,"r") as json_file:
    dgram_data = json.load(json_file)
    json_file.close()

for v in dgram_data["modules"][0]["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in dgram_data["modules"][0]["classes"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#dns
json_path = "dns.json"
with open(json_path,"r") as json_file:
    dns_data = json.load(json_file)
    json_file.close()

for v in dns_data["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

# os
json_path = "os.json"
with open(json_path,"r") as json_file:
    os_data = json.load(json_file)
    json_file.close()

for v in os_data["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#path
json_path = "path.json"
with open(json_path,"r") as json_file:
    path_data = json.load(json_file)
    json_file.close()

for v in path_data["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#querystring
json_path = "querystring.json"
with open(json_path,"r") as json_file:
    query_data = json.load(json_file)
    json_file.close()

for v in query_data["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#events
json_path = "events.json"
with open(json_path,"r") as json_file:
    events_data = json.load(json_file)
    json_file.close()

for v in events_data["modules"][0]["classes"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in events_data["modules"][0]["classes"][0]["events"]:
    raw_text = v["textRaw"]
    params = v["params"]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#filesystem
json_path = "fs.json"
with open(json_path,"r") as json_file:
    fs_data = json.load(json_file)
    json_file.close()

for v in fs_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in fs_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#http
json_path = "http.json"
with open(json_path,"r") as json_file:
    http_data = json.load(json_file)
    json_file.close()

for v in http_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in http_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#https
json_path = "https.json"
with open(json_path,"r") as json_file:
    https_data = json.load(json_file)
    json_file.close()

for v in https_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in https_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#net
json_path = "net.json"
with open(json_path,"r") as json_file:
    net_data = json.load(json_file)
    json_file.close()

for v in net_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in net_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#readline
json_path = "readline.json"
with open(json_path,"r") as json_file:
    readline_data = json.load(json_file)
    json_file.close()

for v in readline_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in readline_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#repl
json_path = "repl.json"
with open(json_path,"r") as json_file:
    repl_data = json.load(json_file)
    json_file.close()

for v in repl_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in repl_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#string decoder
json_path = "string_decoder.json"
with open(json_path,"r") as json_file:
    stringdec_data = json.load(json_file)
    json_file.close()
for v in stringdec_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#tls
json_path = "tls.json"
with open(json_path,"r") as json_file:
    tls_data = json.load(json_file)
    json_file.close()

for v in tls_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in tls_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#tty
json_path = "tty.json"
with open(json_path,"r") as json_file:
    tty_data = json.load(json_file)
    json_file.close()

for v in tty_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in tty_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#vm
json_path = "vm.json"
with open(json_path,"r") as json_file:
    vm_data = json.load(json_file)
    json_file.close()

for v in vm_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in vm_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#zlib
json_path = "zlib.json"
with open(json_path,"r") as json_file:
    zlib_data = json.load(json_file)
    json_file.close()

for v in zlib_data["modules"][0]["methods"]:
        raw_text = v["textRaw"]
        params = [p["name"] for p in v["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in zlib_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
                raw_text = mth["textRaw"]
                params = [p["name"] for p in mth["signatures"][0]["params"]]
                ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#globals
json_path = "globals.json"
with open(json_path,"r") as json_file:
    globals_data = json.load(json_file)
    json_file.close()

for v in globals_data["globals"]:
    raw_text = v["textRaw"]
    params = []
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#process
json_path = "process.json"
with open(json_path,"r") as json_file:
    process_data = json.load(json_file)
    json_file.close()

for v in process_data["globals"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#stream
json_path = "stream.json"
with open(json_path,"r") as json_file:
    stream_data = json.load(json_file)
    json_file.close()

for v in stream_data["modules"][0]["miscs"]:
    for ms in v["miscs"]:
        if "classes" in ms:
            for cl in ms["classes"]:
                if "methods" in cl:
                    for mth in cl["methods"]:
                        raw_text = mth["textRaw"]
                        params = [p["name"] for p in mth["signatures"][0]["params"]]
                        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#timers
json_path = "timers.json"
with open(json_path,"r") as json_file:
    timers_data = json.load(json_file)
    json_file.close()

for v in timers_data["modules"][0]["modules"]:
    for md in v["methods"]:
        raw_text = md["textRaw"]
        params = [p["name"] for p in md["signatures"][0]["params"]]
        ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in timers_data["modules"][0]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
            raw_text = mth["textRaw"]
            params = [p["name"] for p in mth["signatures"][0]["params"]]
            ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})

#url
json_path = "url.json"
with open(json_path,"r") as json_file:
    url_data = json.load(json_file)
    json_file.close()

for v in url_data["modules"][0]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in url_data["modules"][0]["modules"][2]["methods"]:
    raw_text = v["textRaw"]
    params = [p["name"] for p in v["signatures"][0]["params"]]
    ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})
for v in url_data["modules"][0]["modules"][2]["classes"]:
    if "methods" in v:
        for mth in v["methods"]:
            raw_text = mth["textRaw"]
            params = [p["name"] for p in mth["signatures"][0]["params"]]
            ext_list.append({"textRaw": raw_text, "params": params, "cl": -1})














# Write to my json file. This will hold a much cleaner version of the nodeJS api
with open('data.json', 'w') as f:
     json.dump(ext_list, f, indent=4, sort_keys=True)
