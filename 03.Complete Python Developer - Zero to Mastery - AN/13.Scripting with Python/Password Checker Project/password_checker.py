import requests
import hashlib
import sys

base_url = 'https://api.pwnedpasswords.com/range/'

#request to API
def request_api_data(query_char):
    response = requests.get(base_url + query_char)
    if response.status_code != 200:
        raise RuntimeError(f'Error in fetching: {response.status_code}, pls check API and try again.')
    else:
        return response


#read response
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,c in hashes:
        if h == hash_to_check:
            return c
    return 0


#main function
def pwned_api_check(password):
    #check password if it exists in API response
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_chars,tail = sha1_password[:5],sha1_password[5:]

    #call API
    resp = request_api_data(first_five_chars)
    return get_password_leaks_count(resp, tail)
    

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} has been leaked {count} times. You should probably changed your password.')
        else:
            print(f'{password} was not found. Carry on.')
    print('Program Completed!')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

#how to run
#python password_checker.py password123 abc123