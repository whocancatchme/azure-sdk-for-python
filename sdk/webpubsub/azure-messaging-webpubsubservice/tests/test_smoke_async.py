# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
from testcase import WebpubsubPowerShellPreparer
from testcase_async import WebpubsubTestAsync


class WebpubsubSmokeTestAsync(WebpubsubTestAsync):

    @WebpubsubPowerShellPreparer()
    async def test_webpubsub_send_to_all(self, webpubsub_endpoint):
        client = self.create_client(endpoint=webpubsub_endpoint)
        await client.send_to_all('Hub', {'hello': 'test_webpubsub_send_to_all'})

    @WebpubsubPowerShellPreparer()
    async def test_webpubsub_send_to_all_apim_proxy(self, webpubsub_endpoint, webpubsub_reverse_proxy_endpoint=None):
        client = self.create_client(endpoint=webpubsub_endpoint, reverse_proxy_endpoint=webpubsub_reverse_proxy_endpoint)
        await client.send_to_all('Hub', {'hello': 'test_webpubsub_send_to_all_apim_proxy'})

    @WebpubsubPowerShellPreparer()
    async def test_get_client_access_token(self, webpubsub_endpoint):
        client = self.create_client(endpoint=webpubsub_endpoint)
        access_token = await client.get_client_access_token(hub='hub')
        assert len(access_token) == 3
        assert access_token['baseUrl'][:3] == "wss"
        assert access_token['token']
        assert access_token['url'][:3] == "wss"
