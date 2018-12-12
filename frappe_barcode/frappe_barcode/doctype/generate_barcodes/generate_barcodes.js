// Copyright (c) 2018, Bai Web and Mobile Lab and contributors
// For license information, please see license.txt

frappe.ui.form.on('Generate Barcodes', {
	refresh: function(frm) {
		frm.page.clear_primary_action();
		frm.trigger('set_primary');
	},
	set_primary: function(frm) {
		frm.page.set_primary_action('Generate', function() {
			frappe.call({
				method: 'frappe_barcode.frappe_barcode.doctype.generate_barcodes.generate_barcodes.generate',
				freeze: true,
				freeze_message: 'Generating Barcodes',
				args: {
					series: frm.doc.series,
					number: frm.doc.number
				},
				callback: function(data) {
					frm.set_value('series', '');
					frm.set_value('number', '');
				}
			})
		});
	}
});
