# -*- coding: utf-8 -*-
##############################################################################
#
#    Purchase Suggest Min Qty on Product module for Odoo
#    Copyright (C) 2015 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields
import openerp.addons.decimal_precision as dp


class ProductProduct(models.Model):
    _inherit = 'product.product'

    min_qty = fields.Float(
        string=u'Minimum Quantity', track_visibility='onchange',
        digits=dp.get_precision('Product Unit of Measure'),
        company_dependent=True,
        help="If the forecast quantity is lower than the value of this field, "
        "Odoo will suggest to re-order this product. This field is in the "
        "unit of measure of the product.")
