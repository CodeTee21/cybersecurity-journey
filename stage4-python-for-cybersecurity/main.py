import socket
import subprocess

history = []


def lookup_domains():
    while True:
        domain = input("Enter domain (or done to stop): ")
        domain = domain.strip().lower()

        if domain == "done":
            break

        try:
            ip = socket.gethostbyname(domain)

        except socket.gaierror:
            print("\nCould not find the IP address.\n")
            continue

        history.append({
            "domain": domain,
            "ip": ip
        })


def show_history():
    subprocess.run(["clear"])

    print("\n=== Investigation History ===\n")

    for record in history:
        print("Domain:", record["domain"])
        print("IP Address:", record["ip"])
        print()


lookup_domains()
show_history()
