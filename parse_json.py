import json

# Load the JSON data from the file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 6)

# Iterate through the interfaces and print the required information
for interface in data['imdata']:
    attributes = interface['l1PhysIf']['attributes']
    dn = attributes['dn']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print("{:<50} {:<20} {:<8} {:<8}".format(dn, "", speed, mtu))