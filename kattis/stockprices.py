for _ in range(int(input())):
    orders = int(input())
    ask = bid = stock = '-'
    total_ask, total_bid = {}, {}
    for order in range(orders):
        offer = input().split()
        offer_price = int(offer[-1])
        if offer[0] == 'sell':
            total_ask[offer_price] = total_ask.get(offer_price, 0) + int(offer[1])
            if ask == '-' or offer_price < ask:
                ask = offer_price
        else:
            total_bid[offer_price] = total_bid.get(offer_price, 0) + int(offer[1])
            if bid == '-' or offer_price > bid:
                bid = offer_price
        
        if bid != '-' and ask != '-':
            while bid >= ask:
                stock = ask
                purchase = min(total_ask[ask], total_bid[bid])
                total_ask[ask] -= purchase
                if total_ask[ask] == 0:
                    del total_ask[ask]
                    ask = min(total_ask.keys(), default='-')
                total_bid[bid] -= purchase
                if total_bid[bid] == 0:
                    del total_bid[bid]
                    bid = max(total_bid.keys(), default='-')
                if ask == '-' or bid == '-':
                    break
        
        print(ask, bid, stock)