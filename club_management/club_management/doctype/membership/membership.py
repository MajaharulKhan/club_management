# Copyright (c) 2025, majaharul and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import nowdate
from frappe.model.document import Document


class Membership(Document):
    def before_submit(self):
        active_membership_exists = frappe.db.exists(
            "Membership",
            {
                "club_member": self.club_member,
                "docstatus": 1, 
                "end_date": (">=", nowdate()), 

                
            }
        )

        if active_membership_exists:
            frappe.throw("There is an active membership for this member. ")
            


def expire_membership():
	today = nowdate()
	frappe.db.sql(
		"""
		UPDATE `tabMembership`
		SET status = 'Expired'
		WHERE 
			end_date < %s 
			AND docstatus = 1
			AND status != 'Expired'
		""", 
		(today,), # %s এর মান হিসাবে আজকের তারিখ (today) পাস করা হলো
	)
	frappe.db.commit()
