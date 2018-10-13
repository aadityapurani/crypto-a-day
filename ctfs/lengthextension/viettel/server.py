import time
import string
import random
from hashlib import sha256
from urlparse import parse_qsl

# Run with socat
 
money = random.randint(1000000, 5000000)
signkey = ''.join([random.choice(string.letters+string.digits) for _ in xrange(random.randint(8,32))])
items = [
    ('Samsung Galaxy S9', 19990000),
    ('Oppo F5', 5990000),
    ('iPhone X', 27790000),
    ('Vivo Y55s', 3990000),
    ('Itel A32F', 1350000),
    ('FLAG', 999999999)
]
 
def view_list():
    for i, item in enumerate(items):
        print "%d - %s: %d VND" % (i, item[0], item[1])
 
def order():
    try:
        n = int(raw_input('Item ID: '))
    except:
        print 'Invalid ID!'
        return
    if n < 0 or n >= len(items):
        print 'Invalid ID!'
        return
    payment = 'product=%s&price=%d&timestamp=%d' % (items[n][0], items[n][1], time.time()*1000000)
    sign = sha256(signkey+payment).hexdigest()
    payment += '&sign=%s' % sign
    print 'Your order:\n%s\n' % payment
 
def pay():
    global money
    print 'Your order: '
    payment = raw_input().strip()
    sp = payment.rfind('&sign=')
    if sp == -1:
        print 'Invalid Order!'
        return
    sign = payment[sp+6:]
    payment = payment[:sp]
    signchk = sha256(signkey+payment).hexdigest()
    if signchk != sign:
        print 'Invalid Order!'
        return
 
    for k,v in parse_qsl(payment):
        if k == 'product':
            product = v
        elif k == 'price':
            try:
                price = int(v)
            except:
                print 'Invalid Order!'
                return
 
    if money < price:
        print 'Sorry, you don\'t have enough money'
        return
 
    money -= price
    print 'Your current money: $%d' % money
    print 'You have bought %s' % product
    if product == 'FLAG':
        print 'Good job! Here is your flag: %s' % open('flag').read().strip()
 
def main():
    print 'Viettel Store'
    print 'You were walking on the street. Suddenly, you found a wallet and there are %d VND inside. You decided to go to Viettel Store to buy a new phone' % money
    while True:
        print 'Your wallet: %d VND' % money
        print '1. Phone list'
        print '2. Order'
        print '3. Pay'
        print '4. Exit'
        try:
            inp = int(raw_input())
            print 'Your option: ', inp
            if inp == 1:
                view_list()
            elif inp == 2:
                order()
            elif inp == 3:
                pay()
            elif inp == 4:
                break
        except:
            break
 
if __name__ == '__main__':
    main()
