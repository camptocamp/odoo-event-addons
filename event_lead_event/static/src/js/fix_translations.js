odoo.define('event_lead_event.fix_translations', function (require) {
    'use strict';

    var core = require('web.core');
    var session = require('web.session');

    session.session_bind(session.origin).then(function () {
        // Manually add 'website_sign' to module list and load the
        // translations.
        session.module_list.push('event_lead_event');
        session.load_translations();
    });
});
