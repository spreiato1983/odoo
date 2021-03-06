# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv
from openerp.tools.translate import _

class res_partner(osv.osv):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_columns = {
	   'x_preciocostousd' : fields.boolean('x_preciocostousd'),
	   'x_fechanacimiento' : fields.date('x_fechanacimiento'),
	}

res_partner()