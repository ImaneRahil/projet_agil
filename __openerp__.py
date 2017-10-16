{
    'name': 'MSA',
    'category': "Project",
    'summary': 'MSA_PROJECT .',
    'website': 'https://www.agilorg.com/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
        
        """,
    'author': 'AgilOrg',
    'depends': ['project'],
    'depends': ['account'],
    'depends': ['hr_timesheet', 'hr'],

    
    
    
    'data': [
        'views/taches_msa_view.xml',

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
