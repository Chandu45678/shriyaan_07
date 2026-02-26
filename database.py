import chromadb

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./db")  # Stores data locally
collection = chroma_client.get_or_create_collection(name="research_papers")

# Function to add research papers
def add_paper(paper_id, title, content):
    collection.add(
        ids=[paper_id],
        documents=[content],
        metadatas=[{"title": title}]
    )

# Add a research paper
add_paper("paper1", "AI in Healthcare", """
    Artificial Intelligence (AI) is revolutionizing healthcare by improving diagnostics, treatment, and administrative processes. 
    However, challenges like data privacy and bias must be addressed for widespread adoption.
""")

print("✅ Research paper added to ChromaDB!")
///////////////////////////////////////////////////////////////////////////////
Manual Firewall Configuration (Inbound Rule): 
This part explains how to manually block a specific IP using the Windows Firewall GUI. 
Steps: 
1. Open Windows Defender Firewall with Advanced Security. 
2. Click on Inbound Rules. 
3. Click New Rule,on the right panel. 
4. Select Custom and click Next. 
5. Choose All Programs → Click Next. 
6. Protocol and Ports: Keep default → Click Next. 
7. Scope: 
o Under Remote IP address, select These IP addresses. 
o Click Add and enter the IP you want to block (example: 1.2.3.4). 
o Click OK → Next. 
8. Action: Select Block the connection → Next. 
9. Profile: Select Domain, Private, Public → Next. 
10. Name the rule (example: Manual_Block_IP) → Finish. 
This rule will now block all incoming traffic from that specific IP. 
Automated Firewall Configuration (Using Python Script): 
Instead of blocking one IP, the script downloads a list of malicious IPs and blocks all of them 
automatically.

Program: (File name: firewall.py) 
import requests, csv, subprocess 
# source: Abuse CH 
response = requests.get( 
"https://feodotracker.abuse.ch/downloads/ipblocklist.csv" 
).text 
rule = 'netsh advfirewall firewall delete rule name="BadIP"' 
subprocess.run(["PowerShell", "-Command", rule]) 
mycsv = csv.reader( 
f
ilter(lambda x: not x.startswith("#"), response.splitlines()) 
) 
for row in mycsv: 
ip = row[1] 
if ip != "dst_ip": 
print("Added Rule to block:", ip) 
rule = "netsh advfirewall firewall add rule name='BadIP' Dir=Out Action=Block RemoteIP=" + ip 
subprocess.run(["PowerShell", "-Command", rule]) 


Execution Steps: 
1. Open Command Prompt and select Run as Administrator. 
(Firewall rules require admin rights.) 
2. Navigate to the folder where firewall.py is saved. 
Example: cd C:\Users\YourName\Desktop 
3. Make sure Python is installed: python --version 
4. install required library (if not already installed):-  python -m pip install requests 
5. Execute the program: python firewall.py 
6. Output will appear in Command Prompt like: 
Added Rule to block: 45.9.148.221 
Added Rule to block: 103.17.48.5 
For every IP, you will see: 
o “Added Rule to block: <IP>” 
o PowerShell/Command Prompt will also show OK message for successful rule 
creation. 
7. Cross-verify the rules: 
o Open Windows Defender Firewall with Advanced Security 
o Go to Outbound Rules 
o Search for rule name: BadIP 
o You will see many blocked IP addresses listed






xss vulnerabilities
    open docjker desktop ,terminal
docker run --rm -it -p 80:80 vulnerables/web-dvwa
http://localhost in bowser
login with creddentials createdatabse
    
//reflected xss
<script>alert('XSS')</script>
//stored xss
name : Hacked
<script>alert('Stored XSS')</script>
//dom xss in url and dedfault english

http://localhost/vulnerabilities/xss_d/?default=<script>alert('DOM XSS')</script>



//stored xss for document.cookie
<script>alert(document.cookie)</script>
Sign Guestbook
ouput:
PHPSESSID=xxxxx; security=low

//network traffic analysis
Open Terminal in Kali Linux. 
 
Step 3:  
Start a local HTTP server on port 8080 using : 
python3 -m http.server 8080 
 
 
Step 4: In another new terminal start packet capture: 
sudo tcpdump -i any -w capture.pcap port 8080 
 
 
Step 5: Open Firefox in kali Linux and go to: 
http://localhost:8080 
Refresh the page to generate traffic. 
Step 6: 
Go back to tcpdump terminal. 
Stop packet capturing by using Ctrl + C. 
It will stop and show how many packets were captured 
The packets are saved as capture.pcap. 
Step 7: 
• Click the Kali Linux dragon icon (top left). 
•  Type: File Manager and open it. 
•  Your Home folder will open. 
• You will see the file: capture.pcap. 
Step 8:- 
• Since Wireshark is pre-installed in Kali, just double-click capture.pcap. 
• The file will open directly in Wireshark for analysis. 
Step 9:-  
Filter Login Packets 
In Wireshark filter bar, type: http.request.method == "POST" /// here post doesnt work if not test get method GET
Press Enter. 
Now only important packets will show. 
Step 10:- 
Click on any one of the packet and the following data is displayed. 
Browser details such as OS, browser version, language, and visited URLs are visible.If a form is 
submitted, username and password can be seen in plain text.This proves HTTP is insecure. 


