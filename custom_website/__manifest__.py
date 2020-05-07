{
    'name': 'Snippets Product',
    'category': '',
    'author': 'Trung',
    'sequence': 100,
    'summary': 'test snippets',
    'website': '',
    'version': '1.0',
    'description': "",
    'depends': ['base','website', 'website_sale', 'website_payment', 'website_mail', 'website_form', 'website_rating', 'digest'],
    'data': [
        'views/snippets_product.xml',
        'views/assets.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
