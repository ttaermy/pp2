import json

json_data = '''
{
    "totalCount": "400",
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/33",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        }
        // Add more interface data here if needed
    ]
}
'''

data = json.loads(json_data)

print("Interface Status")
print("=" * 80)
print("DN", "Description".ljust(20), "Speed".ljust(8), "MTU")
print("-" * 80)

for interface in data['imdata']:
    attributes = interface['l1PhysIf']['attributes']
    
    dn = attributes['dn']
    descr = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    
    print(dn.ljust(50), descr.ljust(20), speed.ljust(8), mtu)