# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os

from devtools_testutils.perfstress_tests import PerfStressTest
from azure.identity import DefaultAzureCredential
from azure.identity.aio import DefaultAzureCredential as AsyncDefaultAzureCredential
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.aio import KeyClient as AsyncKeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm
from azure.keyvault.keys.crypto.aio import CryptographyClient as AsyncCryptographyClient
from azure.mgmt.keyvault.models import KeyPermissions, Permissions


# without keys/get, a CryptographyClient created with a key ID performs all ops remotely
NO_GET = Permissions(keys=[p.value for p in KeyPermissions if p.value != "get"])


class DecryptTest(PerfStressTest):

    def __init__(self, arguments):
        super().__init__(arguments)

        # Auth configuration
        self.credential = DefaultAzureCredential()
        self.async_credential = AsyncDefaultAzureCredential()

        # Create clients
        vault_url = self.get_from_env("AZURE_KEYVAULT_URL")
        self.client = KeyClient(vault_url, self.credential, **self._client_kwargs)
        self.async_client = AsyncKeyClient(vault_url, self.async_credential, **self._client_kwargs)
        self.key_name = "livekvtestdecryptperfkey"

    async def global_setup(self):
        """The global setup is run only once."""
        await super().global_setup()
        rsa_key = await self.async_client.create_rsa_key(self.key_name)
        self.crypto_client = CryptographyClient(rsa_key.id, self.credential, permissions=NO_GET, **self._client_kwargs)
        self.async_crypto_client = AsyncCryptographyClient(
            rsa_key.id, self.async_credential, permissions=NO_GET, **self._client_kwargs
        )

        self.test_algorithm = EncryptionAlgorithm.rsa_oaep_256
        plaintext = os.urandom(32)
        self.ciphertext = self.crypto_client.encrypt(self.test_algorithm, plaintext).ciphertext

    async def global_cleanup(self):
        """The global cleanup is run only once."""
        await self.async_client.delete_key(self.key_name)
        await self.async_client.purge_deleted_key(self.key_name)
        await super().global_cleanup()

    async def close(self):
        """This is run after cleanup."""
        await self.async_client.close()
        await self.async_crypto_client.close()
        await self.async_credential.close()
        await super().close()

    def run_sync(self):
        """The synchronous perf test."""
        self.crypto_client.decrypt(self.test_algorithm, self.ciphertext)

    async def run_async(self):
        """The asynchronous perf test."""
        await self.async_crypto_client.decrypt(self.test_algorithm, self.ciphertext)
