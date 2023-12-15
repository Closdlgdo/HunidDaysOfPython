import scapy.all as scapy


def scan(ip):
    # Create an ARP request packet
    arp_request = scapy.ARP(pdst=ip)

    # Create an Ethernet frame to send the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = broadcast / arp_request

    # Send the packet and receive the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # List to store the results
    clients_list = []

    # Process the response
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


def print_result(results_list):
    print("IP Address\t\tMAC Address")
    print("----------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


if __name__ == "__main__":
    target_ip = input("Enter the target IP or IP range (e.g., 192.168.1.1/24): ")
    scan_result = scan(target_ip)
    print_result(scan_result)
