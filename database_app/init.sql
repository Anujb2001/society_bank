CREATE DATABASE IF NOT EXISTS transactions_db;
USE transactions_db;

CREATE TABLE IF NOT EXISTS MasterMemberTransaction (
    tran_id VARCHAR(10) PRIMARY KEY,
    tran_date DATETIME(6),
    tran_sr_id VARCHAR(10),
    vchr_type VARCHAR(2),
    mbr_id VARCHAR(10),
    remark VARCHAR(50),
    acc_id VARCHAR(10),
    dr_amt DOUBLE,
    cr_amt DOUBLE,
    vchr_id VARCHAR(10),
    tran_type VARCHAR(2),
    canceled TINYINT(1),
    line_no INT,
    line_printed TINYINT(1),
    balance DOUBLE,
    reference_id VARCHAR(10),
    reference_date DATETIME(6)
);

CREATE TABLE IF NOT EXISTS DetailMemberTransaction (
    tran_id VARCHAR(10) PRIMARY KEY,
    tran_date DATETIME(6),
    vchr_id VARCHAR(10),
    mbr_id VARCHAR(10),
    total_amt DOUBLE,
    vnm_type VARCHAR(5),
    bank_code VARCHAR(50),
    clq_date DATETIME(6),
    chq_no VARCHAR(20),
    remark_cd VARCHAR(5),
    canceled TINYINT(1),
    email_id VARCHAR(50),
    reason VARCHAR(50),
    partular VARCHAR(50),
    created_on DATETIME(6),
    created_by VARCHAR(40),
    modified_by VARCHAR(40),
    modified_on DATETIME(6),
    printed TINYINT(1),
    chq_bounce TINYINT(1),
    rcvry_case_no VARCHAR(30),
    reference_id VARCHAR(10),
    reference_date DATETIME(6),
    bnk_acount_id VARCHAR(10),
    chq_deposited TINYINT(1),
    clq_post_date DATETIME(6),
    utr_no VARCHAR(20)
);
