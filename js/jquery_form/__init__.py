import fanstatic
from js.jquery import jquery

library = fanstatic.Library('jquery_form', 'resources')

jquery_form = fanstatic.Resource(
    library,
    'jquery.form.js',
    minified='jquery.form.min.js',
    depends=[jquery]
)
