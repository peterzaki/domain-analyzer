# 👋 Welcome to Domain Analyzer Tool

Domain-Analyzer tool is powerful utility designed to provide comprehensive insights into a list of domain names and extract potential suspicious ones that may be used for evasive activities, such as newly created domains, DGA domains, and fast-flux domains.

It is particularly useful for security professionals, researchers, and system administrators who want to analyze multiple domain names swiftly and efficiently.

The tool aims to save time and effort, and assists in the detection of potential suspicious domains and extract key information from each domain, enabling analysts to make informed decisions and identify potential threats.

****
## Key features:

1. **Detection of Newly Created Domains:** The tool can identify domains that are newly registered or recently created. This capability is crucial for identifying potential malicious or fraudulent activities, as attackers often use newly registered domains for evasive purposes.

2. **Detection of Potential DGA Domains:** The tool can identify domains potentially generated by Domain Generation Algorithms (DGAs). DGAs are commonly used in malware and botnet communication to avoid detection and enhance resilience.

3. **Detection of Potential Fast-Flux Domain:** The tool can identify potential fast-flux domains, a technique used by cyber-criminals to hide the actual location of malicious servers by rapidly changing the associated IP addresses.

5. **Customizable Analysis Parameters:** Users can customize the analysis parameters, such as the threshold for considering a domain as suspicious based on its age, the number of associated IP addresses, or TTL (Time-to-Live).

6. **Multi-Threading Support:** The tool utilizes multi-threading to process multiple domains simultaneously, which significantly reduces the analysis time, especially when dealing with a large list of domains. This efficiency is achieved by leveraging the available CPU cores to execute domain analysis tasks concurrently. The more cores there are, the faster the analysis can be completed for larger domain lists.

7. **Output to Excel:** The results of the analysis are saved in an well formatted Excel spreadsheet, which provides a clear and organized view of the domain data. The tool generates different sheets according to various types of detections.

8. **User-Friendly Command-Line Interface:** The tool features a user-friendly command-line interface, allowing users to provide input file paths, set analysis parameters, and easily interpret the results.

****
## Usage:

1. **Input File:** Prepare a text file containing a list of domain names, with each domain listed on a separate line. This file will serve as the input for the Domain Analyzer Tool.

2. **Run the Tool:** Launch the Domain Analyzer Tool from the command line.

3. **Load Input File:** Provide the path to the text file containing the list of domain names as an input parameter to the tool using (`-i/--input`). The tool will read and process the domains from this file. For example:
     > **`python3 domain_analyzer.py -i domain_list.txt`**

5. **Domain Analysis and Output Results:** The Domain Analyzer Tool will start analyzing each domain from the input file and generate an output Excel file (`DA-Results_YYYY-MM-DD_HH-MM.xlsx`) presenting the results with the following sheets:
   * **"`Newly Created`" sheet:** contains detcted newly created domain names. By default, Domain-Analyzer Tool checks for domains that are newly created within the last 30 days.
     * Customize Domain Age (Optional): You can customize the number of days to consider a domain as newly created by using the (`-d/--days`) option followed by the desired number of days. For example, to check for domains created within the last 15 days, use:
       > **`python3 domain_analyzer.py -i domain_list.txt -d 15`**
   * **"`Potential DGA`" sheet:** contains domain names that are detcted with high propability as DGA domains.
   * **"`Potential Fast-Flux`" sheet:** contains domain names detcted with many assigned IP addresses (A records) and low TTL (Time to Live). By default, Domain-Analyzer Tool checks for domains with 10 or more assigned IP addresses and TTL value of 1000 seconds or less.
     * Customize Fast-Flux Detection (Optional): You can adjust the threshold of number of assigned IP addresses and the TTL using the (`-p/--ips`) and (`-t/--ttl`) options. For example, to check for domains with 20 or more assigned IP addresses and TTL value of 300 seconds or less, use:
       > **`python3 domain_analyzer.py -i domain_list.txt -p 20 -t 300`**
   * **"`Overview`" sheet:** contains full analysis for all the domain names. Additionally, Domain-Analyzer Tool may assign a suspicion level (`e.g., Low, Medium, High, Very High`) to each domain based on the combination of detected characteristics.
   * **"`Invalid`" sheet:** contains invalid inputs values (non-domains).

6. **Actionable Insights:** Use the insights provided by the tool to make informed decisions regarding the domains. Domains with high suspicion levels may require further investigation or precautionary measures.

7. **Repeat and Update:** Periodically use the Domain Analyzer Tool to reanalyze domain lists, especially when dealing with very large and dynamic datasets. Regularly updating the tool and its data sources will ensure the most accurate and up-to-date results.

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
   * Replace "`/path/to/input_file.txt`" with the actual path to your input file and adjust the analysis parameters (`-d/--days, -p/--ips, and -t/--ttl`) as needed.

**That's it! You have successfully installed the Domain Analyzer tool and can now use it to analyze domains and detect potential threats. 💪**


