# =======================================================
# File: test_http_async.py
# Created by: CD
# Date: 2025-09-26
# =======================================================

import unittest
import asyncio
from aioresponses import aioresponses
from data.manager.http_client_imp import HttpClientImp
from domain.model.api_response import ApiResponse

class TestHttpClientImp(unittest.TestCase):

    def setUp(self):
        self.url = "https://some_fake_url.com"
        # Initialize the client
        self.client = HttpClientImp(timeout=1, maxRetry=3)

    def test_get_success(self):
        expected_body = "Hello World"

        async def run_test():
            with aioresponses() as mocked:
                mocked.get(self.url, status=200, body=expected_body)
                response = await self.client.get(self.url)
                self.assertIsInstance(response, ApiResponse)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.body, expected_body)
        
        asyncio.run(run_test())

    def test_get_retry_success(self):
        expected_body = "Hello After Retry"

        async def run_test():
            with aioresponses() as mocked:
                # First fail, second succeeds
                mocked.get(self.url, exception=Exception("Fail"))
                mocked.get(self.url, status=200, body=expected_body)

                response = await self.client.get(self.url)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.body, expected_body)

        asyncio.run(run_test())

    def test_get_permanent_failure(self):
        client = HttpClientImp(timeout=1, maxRetry=2)

        async def run_test():
            with aioresponses() as mocked:
                mocked.get(self.url, exception=Exception("Fail"))
                mocked.get(self.url, exception=Exception("Fail"))

                response = await client.get(self.url)
                self.assertEqual(response.status_code, -1)
                self.assertIn("Failed with max retry", response.body)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()