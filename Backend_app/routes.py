from flask import Blueprint, request, jsonify
from models import db, MasterMemberTransaction, DetailMemberTransaction

api_blueprint = Blueprint('api', __name__)

# API to insert record into Master Member Transaction
@api_blueprint.route('/add_master_transaction', methods=['POST'])
def add_master_transaction():
    try:
        data = request.get_json()
        new_transaction = MasterMemberTransaction(
            tran_id=data['tran_id'],
            tran_date=data['tran_date'],
            tran_sr_id=data.get('tran_sr_id'),
            vchr_type=data.get('vchr_type'),
            mbr_id=data.get('mbr_id'),
            remark=data.get('remark'),
            acc_id=data.get('acc_id'),
            dr_amt=data.get('dr_amt'),
            cr_amt=data.get('cr_amt'),
            vchr_id=data.get('vchr_id'),
            tran_type=data.get('tran_type'),
            canceled=data.get('canceled'),
            line_no=data.get('line_no'),
            line_printed=data.get('line_printed'),
            balance=data.get('balance'),
            reference_id=data.get('reference_id'),
            reference_date=data.get('reference_date')
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Master transaction added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to insert record into Detail Member Transaction
@api_blueprint.route('/add_detail_transaction', methods=['POST'])
def add_detail_transaction():
    try:
        data = request.get_json()
        new_transaction = DetailMemberTransaction(
            tran_id=data['tran_id'],
            tran_date=data['tran_date'],
            vchr_id=data.get('vchr_id'),
            mbr_id=data.get('mbr_id'),
            total_amt=data.get('total_amt'),
            vnm_type=data.get('vnm_type'),
            bank_code=data.get('bank_code'),
            clq_date=data.get('clq_date'),
            chq_no=data.get('chq_no'),
            remark_cd=data.get('remark_cd'),
            canceled=data.get('canceled'),
            email_id=data.get('email_id'),
            reason=data.get('reason'),
            partular=data.get('partular'),
            created_on=data.get('created_on'),
            created_by=data.get('created_by'),
            modified_by=data.get('modified_by'),
            modified_on=data.get('modified_on'),
            printed=data.get('printed'),
            chq_bounce=data.get('chq_bounce'),
            rcvry_case_no=data.get('rcvry_case_no'),
            reference_id=data.get('reference_id'),
            reference_date=data.get('reference_date'),
            bnk_acount_id=data.get('bnk_acount_id'),
            chq_deposited=data.get('chq_deposited'),
            clq_post_date=data.get('clq_post_date'),
            utr_no=data.get('utr_no')
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Detail transaction added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
