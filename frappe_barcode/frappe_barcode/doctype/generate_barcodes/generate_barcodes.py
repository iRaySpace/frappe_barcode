# -*- coding: utf-8 -*-
# Copyright (c) 2018, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class GenerateBarcodes(Document):
	pass


@frappe.whitelist()
def generate(series, number):
	number = int(number)

	for i in range(number):
		barcode = frappe.get_doc({
			'doctype': 'Barcode Label',
			'barcode': make_autoname(series, 'Barcode Label')
		})
		barcode.save()

	return {'success': True}