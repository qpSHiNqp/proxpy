"""
  Copyright notice
  ================

  Copyright (C) 2015
      Shintaro Tanaka     <qpshinqp@mist-t.co.jp>

  This program is free software: you can redistribute it and/or modify it under
  the terms of the GNU General Public License as published by the Free Software
  Foundation, either version 3 of the License, or (at your option) any later
  version.

  This program is distributed in the hope that it will be useful, but WITHOUT ANY
  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
  A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along with
  this program. If not, see <http://www.gnu.org/licenses/>.

  ================

  Functional description
  ================

  tunnel.py
      created at Feb 4th, 2015 by S. Tanaka

  This Utility class handles SSL tunneling on CONNECT method.
  It simply relays raw (encrypted) payloads from one socket to another.


"""

import select

class TunnelUtil():
    @staticmethod
    def wait_read(socks):
        global proxystate

        r, _, x = select.select(socks, [], socks)
        if len(x) > 0:
            proxystate.log.debug("socket exception occurred")
        if r[0] == socks[0]:
            return socks[0], socks[1]
        else:
            return socks[1], socks[0]

    @staticmethod
    def bridge_forever(sock1, sock2):
        bufsize = 4
        while True:
            src, dst = TunnelUtil.wait_read([sock1, sock2])
            msg = src.recv(bufsize)
            if len(msg) == 0:
                src.close()
                dst.close()
                return
            else:
                dst.send(msg)

