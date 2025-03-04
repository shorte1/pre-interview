import subprocess
import os
import csv
import timeit

exe_path = r'C:\Users\short\Downloads\School\CSCI\SMT Solver\pre-interview\cvc5-Win64-x86_64-static\bin'
directory = r'C:\Users\short\Downloads\School\CSCI\SMT Solver\pre-interview\queries'

with open('results.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)                                         # Create csv file
    csvwriter.writerow(['QueryName', 'Result', 'ElapsedTime'])              # Append header
    for file in os.listdir(directory):          
        startTime = timeit.default_timer()                                  # Take start time
        result = subprocess.run([exe_path + '\\' + 'cvc5.exe', directory + '\\' + file, '--tlimit=60000'], capture_output=True, text=True)
                                                                            # Run cvc5.exe on file with 60 second timer
        endTime = timeit.default_timer()                                    # Take end time
        elapsedTime = (endTime - startTime) * 1000                          # Calculate elasped time and convert to milliseconds
        if result.stdout != '':                                             # Check if there is a result 
            csvwriter.writerow([file, result.stdout, elapsedTime + ' ms'])  # Append to result file
        else:                                                               # If it timed out
            csvwriter.writerow([file, 'Timeout', elapsedTime + ' ms'])
        print(file + ' processed')                                          # Keep track of progress
        
