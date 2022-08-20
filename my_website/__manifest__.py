{
    'name': "welcome",
    'summary': """
    Appscomp hr module customization
    """,
    'description': """
    Appscomp hr module customization
    """,
    'author': "Eddie Brown",
    'website': "http://www.appscomp.com",
    'category': 'HR',
    'version': '15',
    'depends': ['website'],
    'data': [
        'data/menu.xml',
        'view/template.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'my_website/static/src/js/employee_info.js', ]
    },
    'demo': [],
}
