# Copyright (c) 2025, majaharul and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import today
from frappe.website.website_generator import WebsiteGenerator

no_cache=True


class ClubEvent(WebsiteGenerator):
	def get_context(self, context):
		context.parents = [{"name": "events", "title": _("All Evetns"),"route": "/events"}]



def get_list_context(context):
	context.parents = [{"name": "events", "title": _("All Evetns"),"route": "/events"}]
	context.title = _("Events")
	context.checkdate = today()
