import pandas as pd
import os
import random


# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)


# Sample larger dataset with more job titles and skills
data = [
    {"job_title": "Data Scientist", "skills": "Python;Machine Learning;Pandas;Numpy;TensorFlow;Keras;Data Visualization;SQL"},
    {"job_title": "Web Developer", "skills": "HTML;CSS;JavaScript;React;Node.js;Express;MongoDB;REST APIs"},
    {"job_title": "AI Engineer", "skills": "Python;TensorFlow;Keras;Deep Learning;Computer Vision;Natural Language Processing;PyTorch"},
    {"job_title": "Backend Developer", "skills": "Python;Django;REST;PostgreSQL;GraphQL;Redis;AWS;Docker"},
    {"job_title": "Frontend Developer", "skills": "HTML;CSS;JavaScript;Vue.js;React;Bootstrap;SASS;AJAX"},
    {"job_title": "Mobile App Developer", "skills": "Kotlin;Java;Android;Firebase;Swift;iOS;React Native;Xcode"},
    {"job_title": "DevOps Engineer", "skills": "AWS;Docker;Kubernetes;CI/CD;Terraform;Jenkins;Linux;Monitoring"},
    {"job_title": "Cybersecurity Analyst", "skills": "Networking;Security;Firewalls;Encryption;Penetration Testing;Risk Management;Ethical Hacking"},
    {"job_title": "Business Analyst", "skills": "Excel;SQL;Tableau;Power BI;Data Analysis;Requirement Gathering;Communication"},
    {"job_title": "Cloud Architect", "skills": "AWS;Azure;Cloud;DevOps;Kubernetes;Microservices;Docker;Terraform"},
    {"job_title": "Full Stack Developer", "skills": "JavaScript;Node.js;React;MongoDB;Express;HTML;CSS;Git;Docker"},
    {"job_title": "Software Engineer", "skills": "Java;C++;Python;Data Structures;Algorithms;Object-Oriented Programming;Git;Linux"},
    {"job_title": "Data Analyst", "skills": "Excel;SQL;Tableau;Power BI;Data Cleaning;Statistical Analysis;Python;R"},
    {"job_title": "Cloud Engineer", "skills": "AWS;Azure;Google Cloud;Terraform;Kubernetes;Docker;Linux;Automation"},
    {"job_title": "Product Manager", "skills": "Agile;Scrum;JIRA;Project Management;Roadmap Planning;Stakeholder Communication"},
    {"job_title": "Quality Assurance Engineer", "skills": "Manual Testing;Automation Testing;Selenium;Jenkins;JUnit;TestNG;Agile;Bug Tracking"},
    {"job_title": "Systems Administrator", "skills": "Linux;Windows Server;Networking;Active Directory;AWS;Virtualization;PowerShell"},
    {"job_title": "Network Engineer", "skills": "Networking;TCP/IP;Cisco;Firewalls;Routing;Switching;VPN;Security"},
    {"job_title": "Game Developer", "skills": "C++;Unity;Unreal Engine;Game Design;3D Modeling;Python;Game Theory"},
    {"job_title": "Blockchain Developer", "skills": "Blockchain;Solidity;Ethereum;Smart Contracts;Cryptocurrency;DApps;Node.js"},
    {"job_title": "Machine Learning Engineer", "skills": "Python;TensorFlow;Keras;PyTorch;Scikit-learn;Data Engineering;Model Deployment"},
    {"job_title": "Database Administrator", "skills": "SQL;Oracle;MySQL;PostgreSQL;Database Optimization;Backup and Recovery;Data Security"},
    {"job_title": "IT Support Specialist", "skills": "Networking;Windows;Linux;Troubleshooting;Technical Support;Hardware;Software"},
    {"job_title": "Technical Writer", "skills": "Documentation;Technical Writing;API Documentation;Markdown;Javadoc;HTML"},
    {"job_title": "Network Security Engineer", "skills": "Networking;Firewalls;IDS/IPS;VPN;Encryption;Security Protocols;Ethical Hacking"},
    {"job_title": "Embedded Systems Engineer", "skills": "C;C++;Embedded Systems;RTOS;Microcontrollers;IoT;Circuit Design"},
    {"job_title": "Robotics Engineer", "skills": "Python;C++;Robotics;ROS;Automation;Machine Learning;AI;CAD"},
    {"job_title": "AI Researcher", "skills": "Python;TensorFlow;Keras;Machine Learning;Deep Learning;Research;Data Science"},
    {"job_title": "Scrum Master", "skills": "Agile;Scrum;JIRA;Kanban;Project Management;Stakeholder Communication;Team Leadership"},
    {"job_title": "IT Project Manager", "skills": "Project Management;Agile;Scrum;JIRA;Risk Management;Leadership;Stakeholder Engagement"},
    {"job_title": "Data Engineer", "skills": "Python;SQL;ETL;Data Warehousing;Spark;Hadoop;Kafka;Data Pipeline"},
    {"job_title": "UX/UI Designer", "skills": "UX Design;UI Design;Figma;Sketch;Wireframing;Prototyping;User Research;HTML"},
    {"job_title": "Salesforce Developer", "skills": "Salesforce;Apex;Visualforce;Lightning;SOQL;JavaScript;Cloud Computing"},
    {"job_title": "Artificial Intelligence Specialist", "skills": "Machine Learning;Deep Learning;AI;Neural Networks;TensorFlow;NLP;Python;Data Science"},
]


# Sample job descriptions and salary ranges
descriptions = [
    "Remote position with flexible hours.",
    "Onsite role at company HQ with full-time benefits.",
    "Hybrid role requiring 2 days in office per week.",
    "Startup environment with equity options and fast growth.",
    "Corporate setting with structured training and mentorship.",
]


salaries = [
    "$50,000 - $70,000",
    "$70,000 - $100,000",
    "$100,000 - $150,000",
    "$150,000 - $200,000",
    "$200,000+",
]


# Add to each entry
for job in data:
    job['description'] = random.choice(descriptions)
    job['salary'] = random.choice(salaries)


# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv('data/job_dataset.csv', index=False)


print("✅ job_dataset.csv created with job descriptions and salaries.")