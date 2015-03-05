from openerp.osv import fields, osv

class custom_items(osv.osv):
    
  _inherit = "product.product"

  _columns = {
    'item_specification': fields.char('Specifications / Size', size=500),
    'item_group':fields.many2one("x.itemgroup", 'Group'),
    'item_subgroup': fields.many2one("x.itemsubgroup", 'Sub Group'),
    'remark1':fields.many2one("x.remark1", 'Remark1'),
    'remark2': fields.many2one("x.remark2", 'Remark2'),
  }

  _defaults ={
    'item_specification': ''
  }

def location_name_search(self, cr, user, name='', args=None, operator='ilike',
                         context=None, limit=100):
    if not args:
        args = []

    ids = []
    if len(name) == 2:
        ids = self.search(cr, user, [('code', 'ilike', name)] + args,
                          limit=limit, context=context)

    search_domain = [('name', operator, name)]
    if ids: search_domain.append(('id', 'not in', ids))
    ids.extend(self.search(cr, user, search_domain + args,
                           limit=limit, context=context))

    locations = self.name_get(cr, user, ids, context)
    return sorted(locations, key=lambda (id, name): ids.index(id))

class Remark1(osv.osv):
    _name = 'x.remark1'
    _description = 'Remark1'
    _columns = {
        'name': fields.char('Remark1', size=64,
            help='The full name of the item group.', translate=True),
        'code': fields.char('Remark Code', size=8,
            help='Remark Code code.\n'),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !')
    ]

    _order='name'

    name_search = location_name_search
    def create(self, cursor, user, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Remark1, self).create(cursor, user, vals,
                context=context)

    def write(self, cursor, user, ids, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Remark1, self).write(cursor, user, ids, vals,
                context=context)

class Remark2(osv.osv):
    _name = 'x.remark2'
    _description = 'Remark2'
    _columns = {
        'name': fields.char('Remark2', size=64,
            help='The full name of the item group.', translate=True),
        'code': fields.char('Remark Code', size=8,
            help='Remark Code code.\n'),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !')
    ]

    _order='name'

    name_search = location_name_search
    def create(self, cursor, user, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Remark2, self).create(cursor, user, vals,
                context=context)

    def write(self, cursor, user, ids, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Remark2, self).write(cursor, user, ids, vals,
                context=context)

class Itemgroup(osv.osv):
    _name = 'x.itemgroup'
    _description = 'Item Group'
    _columns = {
        'name': fields.char('Group', size=64,
            help='The full name of the item group.', translate=True),
        'code': fields.char('Item Group Code', size=8,
            help='Item group code.\n'),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !')
    ]

    _order='name'

    name_search = location_name_search
    def create(self, cursor, user, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Itemgroup, self).create(cursor, user, vals,
                context=context)

    def write(self, cursor, user, ids, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Itemgroup, self).write(cursor, user, ids, vals,
                context=context)
    
class Itemsubgroup(osv.osv):
    _name = 'x.itemsubgroup'
    _description = 'Item Sub Group'
    _columns = {
        'name': fields.char('Sub Group', size=64,
            help='The full name of the item sub group.', translate=True),
        'code': fields.char('Item sub Group Code', size=8,
            help='Item sub group code.\n'),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !')
    ]

    _order='name'

    name_search = location_name_search
    def create(self, cursor, user, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Itemsubgroup, self).create(cursor, user, vals,
                context=context)

    def write(self, cursor, user, ids, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Itemsubgroup, self).write(cursor, user, ids, vals,
                context=context)


custom_items()