
import argparse
from ipwhois import IPWhois

def main():
    parser = argparse.ArgumentParser(description='ASN information lookup')
    parser.add_argument('ip', metavar='ip_address', type=str, help='IP address to lookup')
    args = parser.parse_args()

    ip_address = args.ip

    ipwhois_obj = IPWhois(ip_address)

    print(f"Querying information for {ip_address}...")
    results = ipwhois_obj.lookup_rdap()

    asn_info = results.get('asn', {})
    print(f"ASN information:")
    print(f"ASN: {asn_info.get('asn', '')}")
    print(f"Country: {asn_info.get('country', '')}")
    print(f"Organization: {asn_info.get('holder', '')}")
# more function
if __name__ == '__main__':
    main()
