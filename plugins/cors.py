"""
  Copyright notice
  ================

  Copyright (C) 2015
      Shintaro Tanaka     <qpshinqp@mist-t.co.jp>

  This program is free software: you can redistribute it and/or modify it under
  the terms of the GNU General Public License as published by the Free Software
  Foundation, either version 3 of the License, or (at your option) any later
  version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along with
  this program. If not, see <http://www.gnu.org/licenses/>.

  ================

  Functional description of this plugin
  ================

  This plugin is for the ``modified proxpy <https://github.com/qpSHiNqp/proxpy>''
  based on the original <http://code.google.com/p/proxpy/> revision r29.
  With this plugin, you will be able to load resource from another site
  even if the site doesn't provides an CORS header.

  You may want to run proxpy with the command
      "./proxpy.py -x plugin/cors.py"
  on your local laptop, and config HTTP proxy settings in order to test
  your service which utilizes resource in the site that is no under your control.

"""

def proxy_mangle_request(req):
    req.removeHeader("Origin")
    return req

def proxy_mangle_response(res):
    res.addHeader("Access-Control-Allow-Origin", "*")
    return res
