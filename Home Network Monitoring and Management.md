



Flashcard 72
Front: Explain the role of SSL Certificates in securing web traffic.

Back: SSL Certificates authenticate the identity of a website and enable encrypted connections between the server and clients. They ensure that data transmitted over HTTPS is secure from interception and tampering, protecting sensitive information like login credentials and personal data.




Flashcard 73
Front: What is Network Segmentation and why is it important for security?

Back: Network Segmentation divides a network into smaller, isolated segments or subnets. It enhances security by limiting access to sensitive areas, containing potential breaches, reducing the attack surface, and improving traffic management and performance within each segment.




Flashcard 74
Front: Define Load Balancer and its function in a network.

Back: A Load Balancer is a device or software that distributes incoming network traffic across multiple servers or resources. Its primary function is to ensure no single server is overwhelmed, enhance performance, provide redundancy, and improve the availability of applications and services.




Flashcard 75
Front: What is SSL Termination and how does it benefit server performance?

Back: SSL Termination is the process of decrypting SSL/TLS encrypted traffic at the edge of a network, typically at a reverse proxy or load balancer, before forwarding the unencrypted traffic to backend servers. It benefits server performance by offloading the computationally intensive decryption task, allowing backend servers to handle application logic more efficiently.




Flashcard 76
Front: What is Docker Swarm and how does it manage containerized applications?

Back: Docker Swarm is Docker’s native clustering and orchestration tool that manages a group of Docker engines (nodes) as a single virtual system. It automates the deployment, scaling, and management of containerized applications, ensuring high availability and efficient resource utilization across the cluster.




Flashcard 77
Front: Explain the purpose of Load Balancing in containerized environments.

Back: In containerized environments, Load Balancing distributes network traffic across multiple containers running the same service. This ensures efficient utilization of resources, improves application performance, enhances scalability, and provides redundancy to handle failures or increased load without disrupting service availability.




Flashcard 78




Flashcard 79
Front: Define Microservices Architecture and its advantages over monolithic architecture.

Back: Microservices Architecture structures an application as a collection of small, independent services that communicate over APIs. Advantages include:

Scalability: Services can be scaled independently.
Flexibility: Different technologies can be used for different services.
Resilience: Failure in one service doesn't impact others.
Ease of Deployment: Smaller codebases are easier to manage and deploy.



Flashcard 80
Front: What is High Availability (HA) and how is it achieved in network systems?

Back: High Availability refers to the ability of a system to remain operational and accessible with minimal downtime, even in the event of failures. It is achieved through redundancy (multiple instances of critical components), failover mechanisms, load balancing, and robust monitoring to quickly detect and respond to issues.

12. Security Enhancements



Flashcard 81
Front: What is Two-Factor Authentication (2FA) and why is it important?

Back: Two-Factor Authentication (2FA) is a security mechanism that requires users to provide two different forms of identification before accessing an account or system. It enhances security by adding an additional layer of protection beyond just a password, making unauthorized access more difficult.




Flashcard 82
Front: Describe Firewall Rules and their significance in network security.

Back: Firewall Rules are predefined criteria that determine how incoming and outgoing network traffic is handled. They specify which types of traffic are allowed or blocked based on factors like IP addresses, ports, and protocols. Firewall rules are crucial for protecting the network from unauthorized access, cyberattacks, and malicious activities.




Flashcard 83
Front: What is Intrusion Detection System (IDS) and how does it differ from Intrusion Prevention System (IPS)?

Back:

IDS: Monitors network traffic for suspicious activities and alerts administrators upon detection. It does not take action to block the threat.
IPS: Not only detects suspicious activities but also takes proactive measures to block or mitigate threats in real-time.



Flashcard 84
Front: Explain the concept of Least Privilege in network security.

Back: The Principle of Least Privilege dictates that users and systems should have the minimum level of access—or permissions—necessary to perform their functions. This reduces the risk of accidental or malicious misuse of privileges, limiting potential damage from security breaches or insider threats.




Flashcard 85

13. Practical Tools and Commands



Flashcard 86




Flashcard 87




Flashcard 88




Flashcard 89
Front: How do you check the status of a Docker container named pihole?

Back:

bash
Copy code
docker ps -a | grep pihole



Flashcard 90




Flashcard 91
Front: How do you start all services defined in a docker-compose.yml file?

Back:

bash
Copy code
docker-compose up -d



Flashcard 92
Front: What command is used to generate a new SSH key pair?

Back:

bash
Copy code
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"



Flashcard 93
Front: How can you view the current DNS settings on a Linux system?

Back:

bash
Copy code
cat /etc/resolv.conf



Flashcard 94
Front: What is the command to restart the Pi-hole service?

Back:

bash
Copy code
pihole restartdns



Flashcard 95
Front: How do you access the Pi-hole Admin Dashboard from a web browser?

Back: Open a web browser and navigate to http://<Pi-hole_IP_address>/admin. Replace <Pi-hole_IP_address> with the actual IP address of your Pi-hole server.




Flashcard 96
Front: What is the command to list all active Docker containers?

Back:

bash
Copy code
docker ps



Flashcard 97
Front: How do you stop a Docker container named grafana?

Back:

bash
Copy code
docker stop grafana



Flashcard 98
Front: What command is used to view the logs of a Docker container named prometheus?

Back:

bash
Copy code
docker logs prometheus



Flashcard 99
Front: How can you create a new user on a Linux system?

Back:

bash
Copy code
sudo adduser <username>
Replace <username> with the desired username.




Flashcard 100
Front: What is the command to update Docker Compose to the latest version?

Back:

bash
Copy code
sudo pip3 install --upgrade docker-compose
