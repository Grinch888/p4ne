from flask import Flask, jsonify
import ipaddress, re
import re
import glob
import pprint

def Classifier(configs):

    hosts = {}

    for f in configs:
        host = ''
        ip = []
        with open(f) as file:

            for s in file:

                if re.match("^(hostname)", s):
                    s = s.replace("hostname ", "")
                    host = s.rstrip()

                elif re.match("^( ip address) ([0-9]{1,3}\.?){4} ([0-9]{1,3}\.?){4}$", s):
                    s = s.replace("ip address ", "")
                    t = re.split(" ", s)
                    ip.append(t[1])

                hosts[host] = ip
    return hosts

h = Classifier(glob.glob("/Users/grinch/Seafile/p4ne_training/config_files/*.txt"))

print(h)


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    s = """
        /configs -  список хостов 
        /configs/hostname - IP адреса хоста hostname
    """
    return s

@app.route('/configs')
def page1():
    list = h.keys()
    return str(list)

@app.route('/configs/<hostname>'):
def hosts_ip(hostname):
    for h in



if __name__ == '__main__':
    app.run(debug=True)

