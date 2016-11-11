from monzo.monzo import Monzo

class API():
    '''
    The main API class to interact with the monzo object.
    '''

    def __init__(self, secret_key=None):
        '''
        This method sets up variables to be used be other methods
        '''
        if secret_key is None:
            with open('/var/monzo/key', 'r') as f:
                secret_key = f.readline()

        client = Monzo(secret_key)
        self.client = client
        self.account_id = client.get_first_account()['id']

    def get_balance_amount(self):
        '''
        This returns the current balance of the account in a nice format.
        '''
        balance_dict = self.client.get_balance(self.account_id)
        return balance_dict['balance']/100

    def get_spend(self):
        '''
        THis treturns the datily sepnd
        '''
        balance_dict = self.client.get_balance(self.account_id)
        return balance_dict['spend_today']/100

if __name__ == '__main__':
    mon = API()
    balance = mon.get_balance_amount()
    spend = mon.get_spend()
    print("GBP {} total\nGBP {} spent today".format(balance, spend))

