from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

credential = DefaultAzureCredential()

secret_client = SecretClient(vault_url="https://maps-demo.vault.azure.net/", credential=credential)
username = secret_client.get_secret("maps-demo-db-creds-username")
secret = secret_client.get_secret("maps-demo-db-creds")

f = open("/usr/bin/postgrest.conf", "w")
f.write( "db-uri = \"postgres://" + username.value  + ":" + secret.value + "@a935dfca9111.maps-demo.private.postgres.database.azure.com:5432/contacts\"\n")
f.write( "db-schemas   = \"public\"\n")
f.write( "db-anon-role   = \"anon\"\n")
f.write ( "jwt-secret = \"{ \\\"e\\\": \\\"AQAB\\\",  \\\"kty\\\": \\\"RSA\\\",  \\\"n\\\": \\\"spvQcXWqYrMcvcqQmfSMYnbUC8U03YctnXyLIBe148OzhBrgdAOmPfMfJi_tUW8L9svVGpk5qG6dN0n669cRHKqU52GnG0tlyYXmzFC1hzHVgQz9ehve4tlJ7uw936XIUOAOxx3X20zdpx7gm4zHx4j2ZBlXskAj6U3adpHQNuwUE6kmngJWR-deWlEigMpRsvUVQ2O5h0-RSq8Wr_x7ud3K6GTtrzARamz9uk2IXatKYdnj5Jrk2jLY6nWt-GtxlA_l9XwIrOl6Sqa_pOGIpS01JKdxKvpBC9VdS8oXB-7P5qLksmv7tq-SbbiOec0cvU7WP7vURv104V4FiI_qoQ\\\"}\"\n")
f.write ( "jwt-role-claim-key = \".roles[0]\"\n")
f.close
