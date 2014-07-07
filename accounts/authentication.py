import requests
import sys
from accounts.models import ListUser

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        #send the assertion to Mozilla's verifer service/
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('sending to Mozilla', data, file=sys.stderr)
        resp = requests.post('http://verifier.login.per')
        print('got', resp.content, file=sys.stderr)

        #Did the verifier respond?
        if resp.ok:
            #Parse the response
            verification_data = resp.json()

            #Check if the assertion was valid
            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.object.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)