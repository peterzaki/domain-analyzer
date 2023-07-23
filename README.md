# 👋 Welcome to Domain Analyzer Tool

Domain-Analyzer tool is powerful utility designed to provide comprehensive insights into a list of domain names and extract potential suspicious ones that may be used for evasive activities, such as newly created domains, DGA domains, and fast-flux domains.

It is particularly useful for security professionals, researchers, and system administrators who want to analyze multiple domain names swiftly and efficiently.

The tool aims to save time and effort, and assists in the detection of potential suspicious domains and extract key information from each domain, enabling analysts to make informed decisions and identify potential threats.

****
## Key features of the Domain Analyzer tool:

1. **Detection of Newly Created Domains:** The tool can identify domains that are newly registered or recently created. This capability is crucial for identifying potential malicious or fraudulent activities, as attackers often use newly registered domains for evasive purposes.

2. **Detection of Potential DGA Domains:** The tool can identify domains potentially generated by Domain Generation Algorithms (DGAs). DGAs are commonly used in malware and botnet communication to avoid detection and enhance resilience.

3. **Detection of Potential Fast-Flux Domain:** The tool can identify potential fast-flux domains, a technique used by cyber-criminals to hide the actual location of malicious servers by rapidly changing the associated IP addresses.

5. **Customizable Analysis Parameters:** Users can customize the analysis parameters, such as the threshold for considering a domain as suspicious based on its age, the number of associated IP addresses, or TTL (Time-to-Live).

6. **Multi-Threading Support:** The tool utilizes multi-threading to process multiple domains simultaneously, significantly reducing the analysis time for a large list of domains.

7. **Output to Excel:** The results of the analysis are saved in an well formatted Excel spreadsheet, which provides a clear and organized view of the domain data. The tool generates different sheets according to various types of detections.

8. **User-Friendly Command-Line Interface:** The tool features a user-friendly command-line interface, allowing users to provide input file paths, set analysis parameters, and easily interpret the results.

****
## Installation:

1. **Prerequisites:**
   * Python: Ensure that you have Python3 installed on your system. The Domain Analyzer tool is compatible with Python 3.10

2. **Download the Domain Analyzer Tool:**
   * Download the Domain Analyzer tool package from the source or repository where it is available. You can use git clone to download the repository or download the zip file from the source.

3. **Navigate to the Tool Directory:**
   * Open your terminal or command prompt and navigate to the directory where you have downloaded the Domain Analyzer tool.
  
4. **Install Required Dependencies:**
   * The Domain Analyzer tool may have some external dependencies. You can find the required dependencies in the requirements.txt file. Install them using the following command:
     > **`pip3 install -r requirements.txt`**

5. **Verify the Installation:**
   * To verify that the Domain Analyzer tool is correctly installed, run a test command, for example:
     > **`python3 domain_analyzer.py -h`**

6. **Start Using the Tool:**
   * Now, you are ready to use the Domain Analyzer tool. To analyze a list of domains, create a text file containing one domain per line.
   * Run the tool with appropriate options to analyze the domains in the input file. For example:
     > **`python3 domain_analyzer.py /path/to/input_file.txt -d 30 -p 10 -t 1000`**
   * Replace `"/path/to/input_file.txt"` with the actual path to your input file and adjust the analysis parameters `(-d/--days, -p/--ips, and -t/--ttl)` as needed.

**That's it! You have successfully installed the Domain Analyzer tool and can now use it to analyze domains and detect potential threats. 💪**


