# Copyright (c) 2025, majaharul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventParticipant(Document):
	def before_validate(self):


		if not self.club_member:
			member = frappe.db.get_list('Club Member', pluck='name', page_length=1)
			frappe.msgprint(str(member))
			if member:
				self.club_member = member[0]
		if frappe.db.exists("Event Participant",{"event": self.event, "club_member": self.club_member}):
			frappe.throw("This member is already registered for this event.")
		
			
		
	
	@frappe.whitelist()
	def mark_as_paid(self):
		self.set('status', 'Paid')
		self.save()
