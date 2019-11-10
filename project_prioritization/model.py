# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
class ProjectTask(models.Model):
	_inherit = 'project.task'
	_order = 'computed_priority desc, sequence, date_start, name, id'
	@api.multi
	@api.depends('ease', 'value', 'urgency')
	def _get_priority(self):
		for rec in self:
			rec.computed_priority = rec.ease * rec.value + rec.urgency
	ease = fields.Selection(string="Ease", default=0, selection=[(0, 'Low'), (1, 'Medium'), (2, 'High'), (3, 'Very High')])
	value = fields.Selection(string="Value", default=0, selection=[(0, 'Low'), (1, 'Medium'), (2, 'High'), (3, 'Very High')])
	urgency = fields.Selection(string="Urgency", default=0, selection=[(0, 'Low'), (1, 'Medium'), (2, 'High'), (3, 'Very High')])
	computed_priority = fields.Float(string="Computed Priority", compute="_get_priority", store=True)