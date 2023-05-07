import argparse
from ipwhois import IPWhois

def main():
    parser = argparse.ArgumentParser(description='IP information lookup')
    parser.add_argument('ip', metavar='ip_address', type=str, help='IP address to lookup')
    parser.add_argument('--asn', action='store_true', help='Display ASN information')
    parser.add_argument('--nets', action='store_true', help='Display network information')
    parser.add_argument('--raw', action='store_true', help='Display raw WHOIS data')
    args = parser.parse_args()

    ip_address = args.ip

    ipwhois_obj = IPWhois(ip_address)

    print(f"Querying information for {ip_address}...")
    results = ipwhois_obj.lookup_rdap()

    if args.asn:
        asn_info = results.get('asn', {})
        print(f"ASN information:")
        print(f"ASN: {asn_info.get('asn', '')}")
        print(f"Country: {asn_info.get('country', '')}")
        print(f"Organization: {asn_info.get('holder', '')}")
    if args.nets:
        nets_info = results.get('network', {})
        print(f"Network information:")
        print(f"CIDR: {nets_info.get('cidr', '')}")
        print(f"Name: {nets_info.get('name', '')}")
        print(f"Country: {nets_info.get('country', '')}")
        print(f"Organization: {nets_info.get('handle', '')}")
    if args.raw:
        raw_info = results.get('raw', '')
        print(f"Raw WHOIS data:")
        print(raw_info)

def get_ip_address():
    ip_address = input("Enter the IP address to lookup: ")
    return ip_address
#more function
if __name__ == '__main__':
    main()
