# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from random import randint
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare


class MachineAccess(models.Model):
    _name = 'machine.access'
    _description = 'Machine access'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Reference',required=False)
    machine_label = fields.Char(string='Label',required=True)
    machine_type = fields.Many2one('machine.access.type',string="Type",required=True)
    ip_address = fields.Char(string='IP Address',required=True)
    domain_name = fields.Char(string='Domain name')
    cpu_info = fields.Char(string='CPU')
    mem_info = fields.Char(string='Memory')
    disk_info = fields.Char(string='Disk')
    os_info = fields.Char(string='OS')
    access_tags = fields.Many2many('machine.access.tag',relation='machine_access_tags_rel',string='Tags')
    service_ids = fields.One2many('machine.access.service','machine_access_id',string='Services')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code(self._name)
        return super(MachineAccess, self).create(vals)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Machine access name must be unique!"),
        ('machine_label_uniq', 'unique (machine_label)', "Label must be unique!")
    ]

class MachineAccessType(models.Model):
    _name = 'machine.access.type'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')


class MachineAccessService(models.Model):
    _name = 'machine.access.service'



    machine_access_id = fields.Many2one('machine.access',ondelete='cascade',required=True)
    service_type = fields.Many2one('machine.access.service.type',string='Service type')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    port = fields.Char(string='Port')
    note = fields.Html(string='Note/Useful data')


class MachineAccessTag(models.Model):
    _name = "machine.access.tag"
    _description = "Tags"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color', default=_get_default_color)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag already exists!"),
    ]



