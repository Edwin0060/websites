
{
    'name': 'Res Branch',
    'version': '15.0.1.0.0',
    'author': 'Appscomp',
    'website': 'http://www.appcom.com',
    'category': 'Generic Module',
    'complexity': 'easy',
    'Summary': 'Res Branch',
    'images': ['static/description/EMS.jpg'],
    'depends': [
        'mail','base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_branch_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
