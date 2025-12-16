# Copyright (c) 2025, majaharul and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	
	columns = get_columns()
	data = get_data()

	return columns, data


def get_columns() -> list[dict]:
	
	return [
		{
			"label": _("Membership"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Membership"
		},
		{
			"label": _("Membership Plan"),
			"fieldname": "membership_plan",
			"fieldtype": "Link",
			"options": "Membership Plan"
		},
		{
			"label": _("Start Date"),
			"fieldname": "start_date",
			"fieldtype": "Date",
		},
		{
			"label": _("End Date"),
			"fieldname": "end_date",
			"fieldtype": "Date",
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Select",
		},
		{
			"label": _("Amount"),
			"fieldname": "amount",
			"fieldtype": "currency",
		}
	]


def get_data() -> list[list]:
	mp=frappe.qb.DocType("Membership") 
	data=(
		frappe.qb.from_(mp)
		.select(
			mp.name,
			mp.membership_plan,
			mp.start_date,
			mp.end_date,
			mp.status,
			mp.amount
		)
		.where(mp.docstatus == 1 and mp.status == "Expired")
	)
	quary= data.run(as_dict=True)
	return quary
