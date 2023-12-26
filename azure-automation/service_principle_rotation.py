from .cli_helper import az_cli
import os
from datetime import datetime
import time

class SPRotation(object):
    @staticmethod
    def _authorize():
        try:
            client_id = os.environ['ARM_CLIENT_ID']
            client_secret = os.environ['ARM_CLIENT_SECRET']
            tenant_id = os.environ['ARM_TENANT_ID']
            subscription_id = os.environ['ARM_SUBSCRIPTION_ID']
            exit_code, output, error = az_cli(f"login --service-principal -u {client_id} -p {client_secret} --tenant {tenant_id}") 
            exit_code, output, error = az_cli(f"account set -s {subscription_id}") 
            if exit_code != 0:
                raise
            else:
                return True
        except Exception as e:
            print(e)
    def check_sp_status(self, sp):
        auth = SPRotation._authorize()
        print("auth", auth)
        flag = False
        output = az_cli(f"ad sp list --display-name {sp}")
        print(output)
        time.sleep(10)
        client_id = output[0]['appId']

        out = az_cli(f"ad sp credential list --id {client_id}")
        expdate = out[0]['endDate']
        expdate = datetime.fromisoformat(expdate)
        now = datetime.now()
        if expdate.date() < now.date():
            flag = True
        if flag:
            self.renew_sp(client_id)
    
    def renew_sp(self, clientid):
        out = az_cli(f"ad app credential reset --id {clientid}")
        client_secret =  out['passowrd']
        print("new client secret", client_secret)
        return client_secret