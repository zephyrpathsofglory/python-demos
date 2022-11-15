import subprocess

r = subprocess.call(["nslookup", "www.baidu.com"])
print("result code: %s" % (r,))

p = subprocess.Popen(
    ["nslookup"], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE
)
output, err = p.communicate(b"set q=mx\nwww.nightruminate.com\nexit\n")
print(output.decode("utf-8"))
print(p.returncode)
