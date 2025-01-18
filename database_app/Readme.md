# Database App

This directory contains the setup for the MySQL database used in the Society Bank Project.

## Features
- Initializes the MySQL database with the required tables:
  - `MasterMemberTransaction`
  - `DetailMemberTransaction`

## Prerequisites
- Docker and Docker Compose

## Setup

### 1. Build and Run Docker Containers
Use Docker Compose to set up the MySQL database:
```bash
docker-compose up --build
```

### 2. Access the Database
The MySQL database will be available at `localhost:3306` with the following credentials:
- Username: `root`
- Password: `root`
- Database: `transactions_db`

## Project Structure
```
├── Dockerfile           # Dockerfile for MySQL
├── init.sql             # SQL script to initialize the database
```

## Database Schema

### MasterMemberTransaction
- `tran_id`: VARCHAR(10) PRIMARY KEY
- `tran_date`: DATETIME(6)
- `tran_sr_id`: VARCHAR(10)
- `vchr_type`: VARCHAR(2)
- `mbr_id`: VARCHAR(10)
- `remark`: VARCHAR(50)
- `acc_id`: VARCHAR(10)
- `dr_amt`: DOUBLE
- `cr_amt`: DOUBLE
- `vchr_id`: VARCHAR(10)
- `tran_type`: VARCHAR(2)
- `canceled`: TINYINT(1)
- `line_no`: INT
- `line_printed`: TINYINT(1)
- `balance`: DOUBLE
- `reference_id`: VARCHAR(10)
- `reference_date`: DATETIME(6)

### DetailMemberTransaction
- `tran_id`: VARCHAR(10) PRIMARY KEY
- `tran_date`: DATETIME(6)
- `vchr_id`: VARCHAR(10)
- `mbr_id`: VARCHAR(10)
- `total_amt`: DOUBLE
- `vnm_type`: VARCHAR(5)
- `bank_code`: VARCHAR(50)
- `clq_date`: DATETIME(6)
- `chq_no`: VARCHAR(20)
- `remark_cd`: VARCHAR(5)
- `canceled`: TINYINT(1)
- `email_id`: VARCHAR(50)
- `reason`: VARCHAR(50)
- `partular`: VARCHAR(50)
- `created_on`: DATETIME(6)
- `created_by`: VARCHAR(40)
- `modified_by`: VARCHAR(40)
- `modified_on`: DATETIME(6)
- `printed`: TINYINT(1)
- `chq_bounce`: TINYINT(1)
- `rcvry_case_no`: VARCHAR(30)
- `reference_id`: VARCHAR(10)
- `reference_date`: DATETIME(6)
- `bnk_acount_id`: VARCHAR(10)
- `chq_deposited`: TINYINT(1)
- `clq_post_date`: DATETIME(6)
- `utr_no`: VARCHAR(20)

## License
This project is licensed under the MIT License.