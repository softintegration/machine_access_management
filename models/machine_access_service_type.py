# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare


class MachineAccessServiceType(models.Model):
    _name = 'machine.access.service.type'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')

    


