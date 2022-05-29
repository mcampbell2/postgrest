from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

credential = DefaultAzureCredential()

secret_client = SecretClient(vault_url="https://maps-demo.vault.azure.net/", credential=credential)
username = secret_client.get_secret("maps-demo-db-creds-username")
secret = secret_client.get_secret("maps-demo-db-creds")

f = open("/usr/bin/postgrest.conf", "w")
f.write( "db-uri = postgres://" + username.value  + ":" + secret.value + "@a935dfca9111.maps-demo.private.postgres.database.azure.com:5432/contacts\n")
f.write( "db-schemas   = \"public\"\n")
f.write( "db-anon-role   = \"anon\"\n")
f.write ( "jwt-secret = \"{  \"e\": \"AQAB\",  \"kty\": \"RSA\",  \"n\": \"spvQcXWqYrMcvcqQmfSMYnbUC8U03YctnXyLIBe148OzhBrgdAOmPfMfJi_tUW8L9svVGpk5qG6dN0n669cRHKqU52Gn>
f.write ( "jwt-role-claim-key = \".roles[0]\"\n")
f.close
