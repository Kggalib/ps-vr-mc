import json

with open("builds.json") as f:
    builds = json.load(f)

stable = [b for b in builds if b.get("channel", "") == "STABLE"]
if not stable:
    stable = builds

url = stable[-1]["downloads"]["server:default"]["url"]

with open("dl_url.txt", "w") as f:
    f.write(url)

print("URL:", url)
