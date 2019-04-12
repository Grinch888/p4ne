import requests, json, pprint
from flask import Flask, jsonify, render_template


def gettoken():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    r = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    token = r.json()['response']['serviceTicket']
    return token


def topology(token):
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json"}
    header['X-Auth-Token'] = token
    r = requests.get(url, headers=header, verify=False)
    return r

def device(token):
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/network-device"
    header = {"content-type": "application/json"}
    header['X-Auth-Token'] = token
    r = requests.get(url, headers=header, verify=False)
    return r

def hosts(token):
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/host"
    header = {"content-type": "application/json"}
    header['X-Auth-Token'] = token
    r = requests.get(url, headers=header, verify=False)
    return r


"""
token = gettoken()
r = topology(token)
topo = r.json()['response']
r = device(token)
hostslist = r.json()['response']
r = device(token)
dev = r.json()['response']
"""






app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("topology.html")


@app.route('/api/topology')
def topology():
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json"}
    header['X-Auth-Token'] = gettoken()
    r = requests.get(url, headers=header, verify=False)
    topo = r.json()['response']

    return jsonify(topo)

if __name__ == '__main__':
    app.run(debug=True)