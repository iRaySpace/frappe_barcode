# -*- coding: utf-8 -*-
# Copyright (c) 2018, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import barcode
from barcode.writer import ImageWriter


class BarcodeLabel(Document):
    def generate_barcode(self):
        """Generate barcode label based from the barcode field"""
        if self.flags.in_insert:
            label = barcode.codex.Code39(self.barcode, ImageWriter(), add_checksum=False)

            path = frappe.get_site_path('public', 'files', self.barcode)

            label.save(path)

            file_name = '{0}.png'.format(self.barcode)

            file = frappe.get_doc({
                'doctype': 'File',
                'file_name': file_name,
                'folder': 'Home/Attachments',
                'attached_to_name': self.barcode,
                'attached_to_doctype': 'Barcode Label',
                'file_url': '/files/{0}'.format(file_name),
                'is_private': 0
            })

            file.insert()

            self.image = '/files/{0}'.format(file_name)

    def before_save(self):
        """Setup the document"""
        self.generate_barcode()
