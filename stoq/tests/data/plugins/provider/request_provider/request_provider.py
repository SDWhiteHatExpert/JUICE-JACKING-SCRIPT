#!/usr/bin/env python3

#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from asyncio import Queue

from stoq import Payload, Request, RequestMeta
from stoq.plugins import ProviderPlugin


class RequestProvider(ProviderPlugin):
    SPECIFY_REQUEST_META = True
    async def ingest(self, queue: Queue) -> None:
        request_meta = None
        if self.SPECIFY_REQUEST_META:
            request_meta = RequestMeta(extra_data={'dummy': '1'})
        await queue.put(Request([Payload(b'Dummy payload')], request_meta))