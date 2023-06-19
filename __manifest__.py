
# -*- coding: utf-8 -*-
{
    'name': 'Asignación de Material',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Módulo para el control del material y epis de los trabajadores',
    'description': """
        Módulo para el control del material y epis de los trabajadores.
    """,
    'author': 'Raul Ramirez',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'data/secuencia.xml',
        'views/view_asignacion.xml',
        'report/report_asignacion_material.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
