

{
    'name': 'Project - Agil',
    'category': "Project",
    'summary': 'chiffer votre projet .',
    'website': 'https://www.agilorg.com/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
        
        """,
    'author': 'imane',
    'depends': ['project'],
    'depends': ['account'],
    'data': [
        'views/project_view.xml',
        'views/unite_view.xml',
        'views/lots_view.xml',
        'views/menu.xml',
	    'views/exemple_report.xml',
        'views/estimation_view.xml',
        'views/parametres_projet_view.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'images': [
        'static/description/logo.png',
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
