import os
from azure.keyvault.secrets import SecretClient
from azure.identity import EnvironmentCredential
from azure.core.exceptions import HttpResponseError

class KeyVaultClient:
    def __init__(self):
        keyvault_name = os.environ["KEY_VAULT_NAME"]
        credential = EnvironmentCredential()
        self.client = SecretClient(
            vault_url=f"https://{keyvault_name}.vault.azure.net",
            credential=credential)

    def get_secret(self, secret_name: str) -> str:
        try:
            return self.client.get_secret(secret_name).value
        except HttpResponseError as e:
            print(f"Error occured getting secret: {e.message}")
