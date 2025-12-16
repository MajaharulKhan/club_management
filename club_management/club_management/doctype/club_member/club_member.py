# Copyright (c) 2025, majaharul and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ClubMember(Document):
	def on_update(self):
		if self.user and self.create_user_permission:
			from frappe.permissions import add_user_permission
			add_user_permission(self.doctype, self.name,  self.user, is_default=1)
