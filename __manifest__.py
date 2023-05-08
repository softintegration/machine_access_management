# -*- coding: utf-8 -*- 
{
 'name': 'Machine access management',
 'author': 'Soft-integration',
 'application': False,
 'installable': True,
 'auto_install': False,
 'qweb': [],
 'description': False,
 'images': [],
 'version': '1.0.1.1',
 'category': 'Technical tools',
 'demo': [],
 'depends': ['mail'],
 'data': ['data/ir_sequence_data.xml',
          'data/machine_access_management_data.xml',
         'security/machine_access_management_security.xml',
         'security/ir.model.access.csv',
         'views/machine_access_views.xml'
          ],
 'license': 'LGPL-3',
 }