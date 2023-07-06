# TChallenge
GitHub repo of finished assignment and to present the work. To present the written material in a deck

## Architecture

<img width="1041" alt="image" src="https://github.com/pennSword/TChallenge/assets/93257912/3d663e87-d230-40af-b319-3185905ecd8d">


## Design Overview

<img width="375" alt="image" src="https://github.com/pennSword/TChallenge/assets/93257912/ed334a88-dd05-45e3-aa55-9d4b0dd3847b">





## Implementation Details




Google Cloud Set Up for the Technical Challenge

Machine Type / Region / Zone
![image](https://github.com/pennSword/TChallenge/assets/93257912/84b2067f-7b04-4ca4-a072-850f14b38722)


Container
![image](https://github.com/pennSword/TChallenge/assets/93257912/209627a5-ea3c-44d6-bf23-90f9556cbae0)

Virtual Machine
![image](https://github.com/pennSword/TChallenge/assets/93257912/8544e327-c148-4077-ad9c-9b726ce3c523)

SSH into the Virtual Machine
![image](https://github.com/pennSword/TChallenge/assets/93257912/464848a7-07bb-45c6-979d-065822273ea1)


Problem Dataset Uploaded to Google Cloud Platform
![image](https://github.com/pennSword/TChallenge/assets/93257912/fa691fe0-175d-4f2b-8a25-d67f2e3fd4df)

Install Postgresql
sudo apt update
sudo apt -y install postgresql postgresql-client postgresql-contrib
sudo -u postgres psql postgres
\password postgres
CREATE EXTENSION adminpack;

Create Table in Postgresql - Initially no rows
![image](https://github.com/pennSword/TChallenge/assets/93257912/99fb3180-869c-41e2-b4e1-94dd410285c3)


After executing the ETL Pipeline
<img width="892" alt="image" src="https://github.com/pennSword/TChallenge/assets/93257912/9f4e47ee-4cef-467f-aef4-9a2b8b5334a2">


## Testing

Testing performed on negative test data

<img width="709" alt="image" src="https://github.com/pennSword/TChallenge/assets/93257912/cc6f3bdf-968d-4fe0-8077-acced83a6338">


## Demo !
