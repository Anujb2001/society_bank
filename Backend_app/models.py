from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table 1 Model: Master Member Transaction
class MasterMemberTransaction(db.Model):
    __tablename__ = 'master_member_transaction'

    tran_id = db.Column(db.String(10), primary_key=True)
    tran_date = db.Column(db.DateTime, nullable=False)
    tran_sr_id = db.Column(db.String(10))
    vchr_type = db.Column(db.String(2))
    mbr_id = db.Column(db.String(10))
    remark = db.Column(db.String(50))
    acc_id = db.Column(db.String(10))
    dr_amt = db.Column(db.Float)
    cr_amt = db.Column(db.Float)
    vchr_id = db.Column(db.String(10))
    tran_type = db.Column(db.String(2))
    canceled = db.Column(db.Boolean)
    line_no = db.Column(db.Integer)
    line_printed = db.Column(db.Boolean)
    balance = db.Column(db.Float)
    reference_id = db.Column(db.String(10))
    reference_date = db.Column(db.DateTime)

# Table 2 Model: Detail Member Transaction
class DetailMemberTransaction(db.Model):
    __tablename__ = 'detail_member_transaction'

    tran_id = db.Column(db.String(10), primary_key=True)
    tran_date = db.Column(db.DateTime, nullable=False)
    vchr_id = db.Column(db.String(10))
    mbr_id = db.Column(db.String(10))
    total_amt = db.Column(db.Float)
    vnm_type = db.Column(db.String(5))
    bank_code = db.Column(db.String(50))
    clq_date = db.Column(db.DateTime)
    chq_no = db.Column(db.String(20))
    remark_cd = db.Column(db.String(5))
    canceled = db.Column(db.Boolean)
    email_id = db.Column(db.String(50))
    reason = db.Column(db.String(50))
    partular = db.Column(db.String(50))
    created_on = db.Column(db.DateTime)
    created_by = db.Column(db.String(40))
    modified_by = db.Column(db.String(40))
    modified_on = db.Column(db.DateTime)
    printed = db.Column(db.Boolean)
    chq_bounce = db.Column(db.Boolean)
    rcvry_case_no = db.Column(db.String(30))
    reference_id = db.Column(db.String(10))
    reference_date = db.Column(db.DateTime)
    bnk_acount_id = db.Column(db.String(10))
    chq_deposited = db.Column(db.Boolean)
    clq_post_date = db.Column(db.DateTime)
    utr_no = db.Column(db.String(20))
