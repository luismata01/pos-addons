# -*- coding: utf-8 -*-
{
    'name': "Extencion Terminal Punto de Venta JS",

    'summary': """Añade mejoras al Punto de Venta""",

    'description': """
       Añade mejoras al Punto de Venta, tales como la inclusión en el recibo del nombre del cliente, Telf. y Dirección.

    """,
    'version': '1.2',
    'author': 'TeletrabajoVE',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
            'views/pos_config.xml'
        ],

    'assets': {
        'point_of_sale.assets': [
            '/ext_tpdv/static/src/css/style.css',
            '/ext_tpdv/static/src/js/OrderlineCustomerNoteButtonNew.js',
            '/ext_tpdv/static/src/js/note_receipt.js',
            '/ext_tpdv/static/src/js/PaymentScreen.js'
        ],
        'web.assets_qweb': [
            'ext_tpdv/static/src/xml/**/*',
        ],
    },

    'application': True,
}
