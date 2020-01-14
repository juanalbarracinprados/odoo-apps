# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
class ProjectTask(models.Model):
	_inherit = 'project.task'
	_order = 'computed_priority desc, sequence, date_start, name, id'
	@api.multi
	@api.depends('effort', 'value', 'urgency')
	def _get_priority(self):
		for rec in self:
			rec.computed_priority = rec.value + rec.urgency + 4 - rec.effort
	effort = fields.Selection(string="Effort", help="Amount of effort required to complete the task.", default=1, selection=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High')])
	value = fields.Selection(string="Value", help="Amount of value that this task produces on the client.", default=1, selection=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High')])
	urgency = fields.Selection(string="Urgency", help="Level of urgency for this task.", default=1, selection=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High')])
	computed_priority = fields.Float(string="Computed Priority", compute="_get_priority", store=True)