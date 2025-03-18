
{
    'name' : 'Reclutamiento Portal Web Extension',
    'version' : '1.0',
    
    'summary' : 'Reclutamiento Portal Web Extension',
    'description': """
    """,
    'author' : 'Jose Marty.',
    'website' : 'www.martydev.com',
    'depends' : [
        'base',
        'hr_recruitment',
        'website_hr_recruitment'
    ],
    'support': 'jose.m.marty@gmail.com',
    'data' : [
        'views/hr_applicant.xml',
        'pages/website_apply.xml',
        'data/config_data.xml',
    ],
    'installable' : True,
    'application' : True,
}

