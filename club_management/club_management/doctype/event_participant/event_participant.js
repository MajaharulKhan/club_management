// Copyright (c) 2025, majaharul and contributors
// For license information, please see license.txt

frappe.ui.form.on("Event Participant", {
	refresh(frm) {
        if (frm.doc.status!=="Paid") {
            frm.add_custom_button(__("Paid"), ()=>{
                frm.call("mark_as_paid")
            })
        }
	},
});
