import random

def generate_ip():
    ip = "192.168.1."
    ip += str(random.randint(1, 255))
    return ip

def check_firewall_rules(firewall_rules, ip):
    if ip in firewall_rules:
        return True
    return False

def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.16": "block",
        "192.168.1.20": "block",
        "192.168.1.35": "block",
        "192.168.1.129": "block",
        "192.168.1.200": "block",
    }
    
    traffic_nums = int(input("Enter number of traffic to check: "))
    for _ in range(traffic_nums):
        ip = generate_ip()
        if check_firewall_rules(firewall_rules, ip):
            print(f"IP: {ip} is blocked")
        else:
            print(f"IP: {ip} is allowed")
    
if __name__ == '__main__':
    main()