# Data Engineering Project - Group 25
Apache Spark serves as a unifying engine for large-scale data analysis across multiple workloads. This technique simplifies data science and engineering by solving several problems with a single processing engine and general-purpose languages.
To begin, the Spark cluster was set up with a single master node and one worker node as per the instructions. The VMs were medium-sized and large-sized and ran Ubuntu 22.04 - 2024.01.15. Scalability experiments were performed by increasing and decreasing the number of worker node cores to compare execution times.
After setting up HDFS locally, we used the Hadoop command-line interface (HDFS CLI) to upload the dataset files in CSV format. Spark then accessed the data directly for processing and analysis.

Data Processing & Analysis
<img width="657" alt="Screenshot 2025-03-21 at 8 52 02 PM" src="https://github.com/user-attachments/assets/371d846d-6a7f-48df-893f-a0e8de68c0c5" />

Weak Scaling
![output2](https://github.com/user-attachments/assets/a30abd9f-737b-4928-8d48-79aba44e1102)

Strong Scaling
![output](https://github.com/user-attachments/assets/f492082c-c309-4b09-b2f3-3e414d860ec3)

Predicting Missing Years
<img width="348" alt="Screenshot 2025-03-21 at 8 53 58 PM" src="https://github.com/user-attachments/assets/87e2368c-be43-4dd1-aa20-ec06673a7c6e" />

