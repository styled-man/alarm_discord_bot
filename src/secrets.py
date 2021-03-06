#!/usr/bin/env python3
import boto3


def get_secret(code_secret):
    secret_name = "Alarm_Discord_Bot"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager',
                            region_name=region_name)

    response = str(client.get_secret_value(SecretId=secret_name))
    response = response[response.find('SecretString'):response.find('}') + 1]

    secret_value = [i for i in range(len(response)) if response.startswith('"', i)]
    x, y = 0, 1
    for secrets in range(int(len(secret_value) / 2)):
        if response[secret_value[x] + 1:secret_value[y]] == code_secret:
            return response[secret_value[x + 2] + 1:secret_value[y + 2]]
        x += 4; y += 4
