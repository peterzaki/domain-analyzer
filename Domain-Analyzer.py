# Domain-Analyzer is a powerful tool designed to analyze domains listed in a text file, one domain per line.
# The tool extracts various characteristics of these domains and outputs the results to an Excel workbook with multiple sheets, as follows:
#
# 1. Calculates the age of each domain in days to identify newly created domains, which are listed in the "Newly Created" sheet.
# 2. Checks if a domain could be a potential DGA or not, and displays the results in the "Potential DGA" sheet.
# 3. Examines the assigned IP addresses and their TTL (Time To Live) to identify and output potential fast-flux domains in the "Potential Fast-Flux" sheet.
# 4. Finally, the "Overview" sheet provides a summary of all the domains along with their respective characteristics.
#    Each domain is assigned a suspicion level (Low, Medium, High, Very High) based on the detected characteristics.
#    For example, if a domain is only detected as "Newly Created," it is assigned a "Low" suspicion level.
#    However, if it is detected as "Newly Created," "Potential DGA," and "Potential Fast-Flux (Many IPs with low TTL)," then it is assigned a "Very High" suspicion level.
#
# For instance, utilize the command below to search for domains that are younger than 30 days, have 10 or more IP addresses, and a TTL of 1000 seconds or less.
# "python3 Domain-Analyzer.py -i /domains.txt -d 30 -p 10 -t 1000"
#
# Check the help options with [-h] option
# Required option is [-i] for input text file
#
# Developed by Peter Zaki @ 2023
# Contact me: linkedin.com/in/peterzaki

def print_domain_analyzer():
    domain_analyzer_art = """

       /$$$$$$$                                    /$$                          
      | $$__  $$                                  |__/                          
      | $$  \ $$  /$$$$$$  /$$PETER/ZAKI  /$$$$$$  /$$ /$$$$$$$                 
      | $$  | $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$| $$__  $$                
      | $$  | $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$  \ $$                
      | $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$| $$  | $$                
      | $$$$$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$  | $$                
      |_______/  \______/ |__/ |__/ |__/ \_______/|__/|__/  |__/                 
                                                                                                                                                         
                                                                                
        /$$$$$$                      /$$                                        
       /$$__  $$                    | $$                                        
      | $$  \ $$ /$$$$$$$   /$$$$$$ | $$ /$$   /$$ /$$$$$$$$  /$$$$$$   /$$$$$$ 
      | $$$$$$$$| $$__  $$ |____  $$| $$| $$  | $$|____ /$$/ /$$__  $$ /$$__  $$
      | $$__  $$| $$  \ $$  /$$$$$$$| $$| $$  | $$   /$$$$/ | $$$$$$$$| $$  \__/
      | $$  | $$| $$  | $$ /$$__  $$| $$| $$  | $$  /$$__/  | $$_____/| $$      
      | $$  | $$| $$  | $$|  $$$$$$$| $$|  $$$$$$$ /$$$PETER|  ZAKI$$$| $$      
      |__/  |__/|__/  |__/ \_______/|__/ \____  $$|________/ \_______/|__/      
                                         /$$  | $$                              
                                        |  $$$$$$/                              
                                         \______/                                
 
    """
    print(domain_analyzer_art)

print_domain_analyzer()

import os, sys
from modules import main as m

if __name__ == "__main__":
    try:
        m.main()
    except:
        sys.exit(0)
