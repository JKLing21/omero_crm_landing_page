
[![Actions Status](https://github.com/vernonlim/omero-crm-landing-page/workflows/OMERO/badge.svg)](https://github.com/vernonlim/omero-crm-landing-page/actions)


OMERO.omero-crm-landing-page
==================================

A landing page for CRM's dataset.

Installation
============

This section assumes that an OMERO.web is already installed. See [OMERO.web installation instructions]<https://github.com/ome/omero-web/blob/master/README.rst> for more details.

Installing from Pypi
--------------------

Install the app using [pip](<https://pip.pypa.io/en/stable/>) .

Ensure that you are running ``pip`` from the Python environment
where ``omero-web`` is installed. Depending on your install, you may need to
call ``pip`` with, for example: ``/path/to_web_venv/venv/bin/pip install ...``

::

    $ pip install -U omero-crm-landing-page


Development mode
----------------

Install `omero-crm-landing-page` in development mode as follows:

    # within your python venv:
    $ cd omero-crm-landing-page
    $ pip install -e .

After installation either from [Pypi](https://pypi.org/) or in development mode, you need to configure the application.
To add the application to the `omero.web.apps` settings, run the following command:

Note the usage of single quotes around double quotes:

    $ omero config append omero.web.apps '"omero-crm-landing-page"'

Optionally, add a link "Landing Page" at the top of the webclient to
open the index page of this app:

    $ omero config append omero.web.ui.top_links '["Landing Page", "omero-crm-landing-page_index", {"title": "Open Landing Page in new tab", "target": "_blank"}]'


Now restart your `omero-web` server and go to
<http://localhost:4080/omero-crm-landing-page/> in your browser.


Further Info
============

1. This app was derived from [cookiecutter-omero-webapp](https://github.com/ome/cookiecutter-omero-webapp).
2. For further info on deployment, see [Deployment](https://docs.openmicroscopy.org/latest/omero/developers/Web/Deployment.html)


License
=======

This project, similar to many Open Microscopy Environment (OME) projects, is
licensed under the terms of the AGPL v3.


Copyright
=========

2024 vernonlim

