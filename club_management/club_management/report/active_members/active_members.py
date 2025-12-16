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
			"label": _("Full Name"),
			"fieldname": "full_name",
			"fieldtype": "Data",
		},
		{
			"label": _("Phone"),
			"fieldname": "phone",
			"fieldtype": "Phone",
		},
		{
			"label": _("Join Date"),
			"fieldname": "join_date",
			"fieldtype": "Date",
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Select",
		},
	]


def get_data() -> list[list]:
	am= frappe.qb.DocType("Club Member")
	data=(
		frappe.qb.from_(am)
		.select(
			am.full_name,
			am.phone,
			am.join_date,
			am.status,
		)
		.where(
			am.status == "Active"
		)
	)
	query=data.run(as_dict=True)
	return query
