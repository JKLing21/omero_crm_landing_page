#!/usr/bin/env python
#
# Copyright (c) 2024 vernonlim.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.templatetags import static

from omeroweb.webclient.decorators import login_required

@login_required()
def index(request, conn=None, **kwargs):
    """
    Svelte App Home Page
    """
    # We need to serve the create-react-app build.
    # Load the template html and replace OMEROWEB_INDEX
    template = loader.get_template('index.html')
    html = template.render({}, request)

    # update links to static files
    static_dir = static.static('/')
    html = html.replace('href="/static/', 'href="%s' % static_dir)
    html = html.replace('src="/static/', 'src="%s' % static_dir)
    return HttpResponse(html)
