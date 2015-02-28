from osv import osv, fields

class res_partner_add_text_field(osv.osv):
    # This OpenERP object inherits from res.partner 
    # to add a new textual field
    _inherit = 'res.partner'

    _columns = {
	'place': fields.many2one("x.place", 'Place'),
	'vendor_office_contact_name' : fields.char('Contact Name', size=128),
        'vendor_site_contact_name' : fields.char('Contact Name', size=128),
        'district': fields.many2one("x.district", 'Destrict'),
	'office_place': fields.many2one("x.place", 'Place'),
	'site_place': fields.many2one("x.place", 'Place'),
	'site_district': fields.many2one("x.district", 'Destrict'),
	'site_zip' : fields.char('Pin Code', size=128),
	'site_state_id': fields.many2one("res.country.state", 'State'),
	'site_country_id': fields.many2one('res.country', 'Country'),
	'site_phone' : fields.char('Phone No.', size=128),
	'site_fax' : fields.char('Fax No.', size=128),
	'site_mobile' : fields.char('Contact Number', size=128),
	'site_email' : fields.char('Email', size=128),
	'Vendor_registration_number': fields.binary('File',help="Select a file here"),
	'ecc' : fields.char('ECC', size=128),
	'vendor_pan_no':fields.char('PAN', size=128),
	'vendor_cst_tin':fields.char('CST TIN', size=128),
	'vendor_vat_tin':fields.char('VAT TIN', size=128),
	'vendor_st_no':fields.char('Service Tax No.', size=128),
	'vendor_tan':fields.char('TAN', size=128),
	'vendor_bank_detail': fields.binary('File',help="Select a file here"),
	'vendor_account_number' : fields.char('Account Number', size=128),
	'vendor_bank_name':fields.many2one("x.vendorbank", 'Bank Name'),
	'vendor_account_type':fields.many2one("x.vendoracctype", 'Account Type'),
	'vendor_bank_address':fields.char('Branch Address', size=255),
	'vendor_bank_phone':fields.char('Branch Phone Number', size=128),
	'vendor_bank_email':fields.char('Branch Email', size=128),
	'vendor_bank_fsc':fields.char('FSC Code', size=128),
    'vendor_tc_price_basis':fields.char('Prise Basis', size=255),
    'vendor_tc_delivery_schedule':fields.char('Delivery Schedule', size=128),
    'vendor_tc_excise_duty':fields.char('Excise Duty', size=128),
    'vendor_tc_sales_test':fields.char('Sales Tax', size=128),
    'vendor_tc_packing_charges':fields.char('Packing Charges', size=255),
    'vendor_tc_to_and_fro':fields.char('To & Fro', size=128),
    'vendor_tc_payment_term':fields.char('Payment Term', size=128),
    'vendor_tc_mode_of_dispatch':fields.char('Mode of Dispatch', size=128),
    'vendor_tc_guarantee':fields.char('Guarantee', size=128),
    'vendor_tc_special_term':fields.char('Special Terms', size=128)
	
    }
    
    _defaults = {
       
    }
    
    def import_file(self, cr, uid, ids, context=None):
    	fileobj = TemporaryFile('w+')
    	fileobj.write(base64.decodestring(data)) 
    	# your treatment
    	return

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

class Vendorbank(osv.osv):
    _name = 'x.vendorbank'
    _description = 'Vendor Bank Name'
    _columns = {
        'name': fields.char('Bank Name', size=64,
            help='The full name of the Bank.', translate=True),
        'code': fields.char('Bank Code', size=8,
            help='The Bank code in .\n'
            'You can use this field for quick search.'),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !'),
        ('code_uniq', 'unique (code)',
            'The code of the banks must be unique !')
    ]

    _order='name'

    name_search = location_name_search

    def create(self, cursor, user, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Vendorbank, self).create(cursor, user, vals,
                context=context)

    def write(self, cursor, user, ids, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Vendorbank, self).write(cursor, user, ids, vals,
                context=context)

class Vendoraccounttype(osv.osv):
    _name = 'x.vendoracctype'
    _description = 'Vendor Bank Name'
    _columns = {
        'name': fields.char('Bank Name', size=64,
            help='The full name of the Bank.', translate=True),
        'code': fields.char('Bank Account type Code', size=8,
            help='The Bank type Code in .\n'
            'You can use this field for quick search.'),
        
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the bank must be unique !'),
    ]

    _order='name'

    name_search = location_name_search

    def create(self, cursor, user, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Vendoraccounttype, self).create(cursor, user, vals,
                context=context)

    def write(self, cursor, user, ids, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(Vendoraccounttype, self).write(cursor, user, ids, vals,
                context=context)


class District(osv.osv):
    _name = 'x.district'
    _description = 'District'
    _columns = {
        'name': fields.char('District Name', size=64,
            help='The full name of the District.', required=True, translate=True),
        'code': fields.char('District Code', size=2,
            help='The District code in two chars.\n'
            'You can use this field for quick search.'),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the country must be unique !'),
        ('code_uniq', 'unique (code)',
            'The code of the country must be unique !')
    ]

    _order='name'

    name_search = location_name_search

    def create(self, cursor, user, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(District, self).create(cursor, user, vals,
                context=context)

    def write(self, cursor, user, ids, vals, context=None):
        if vals.get('code'):
            vals['code'] = vals['code'].upper()
        return super(District, self).write(cursor, user, ids, vals,
                context=context)


class Place(osv.osv):
    _name = 'x.place'
    _description = 'Place'
    _columns = {
        'name': fields.char('Place', size=64,
            help='The full name of the District.', required=True, translate=True),
    }
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
            'The name of the country must be unique !')
    ]

    _order='name'

    name_search = location_name_search
