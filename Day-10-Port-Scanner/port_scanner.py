import socket

def scan_single_port(target_ip, port):
    open_ports = 0
    closed_ports = 0

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"

            print(f"[+] Port {port} is OPEN ({service})")
            open_ports += 1
        else:
            print(f"[-] Port {port} is CLOSED")
            closed_ports += 1

        s.close()

    except socket.error:
        print("Connection error.")

    return open_ports, closed_ports


def scan_port_range(target_ip, start_port, end_port):
    open_ports = 0
    closed_ports = 0

    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown Service"

                print(f"[+] Port {port} is OPEN ({service})")
                open_ports += 1
            else:
                print(f"[-] Port {port} is CLOSED")
                closed_ports += 1

            s.close()

        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            break

        except socket.error:
            print("Couldn't connect.")
            break

    return open_ports, closed_ports


def main():
    print("====== PYTHON PORT SCANNER ======")

    target = input("Enter target IP or domain: ")

    try:
        target_ip = socket.gethostbyname(target)
        print(f"Resolved IP Address: {target_ip}")
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return

    print("\n1. Scan Single Port")
    print("2. Scan Port Range")

    choice = input("Choose option (1/2): ")

    if choice == "1":
        port = int(input("Enter port number: "))
        open_count, close_count = scan_single_port(target_ip, port)

    elif choice == "2":
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        open_count, close_count = scan_port_range(target_ip, start_port, end_port)

    else:
        print("Invalid choice.")
        return

    print("\n====== SCAN SUMMARY ======")
    print(f"Total Open Ports   : {open_count}")
    print(f"Total Closed Ports : {close_count}")


if __name__ == "__main__":
    main()