
class _Position:
    def __init__(self, shares, share_price):
        if share_price <= 0:
            raise ValueError("Please enter a positive number for share_price")
        self.shares = shares
        self.position_size = float(shares * share_price)

    def buy(self, shares, share_price):
        self.current_price = share_price
        if shares < 0 or share_price <= 0:
            raise ValueError(" Please enter positive numbers for shares and share_price", shares, share_price)
        if self.shares >= 0:
            self.shares += shares
            self.position_size += shares * share_price
            return float('NaN')
        else:  # covering short position
            if abs(self.shares) >= shares:
                profit = (self.position_size / self.shares) * shares - share_price * shares
                self.position_size += share_price * shares + profit
                self.shares += shares
                return profit
            else:
                profit = self.position_size - share_price * self.shares
                self.shares += shares
                self.position_size += shares * share_price + profit
                return profit
    def sell(self, shares, share_price):
        self.current_price = share_price
        if shares < 0 or share_price <= 0:
            raise ValueError(" Please enter positive numbers for shares and share_price")
        if self.shares <= 0:
            self.shares -= shares
            self.position_size -= shares * share_price
            return float('NaN')
        else:  # covering long position
            if self.shares >= shares:
                profit = share_price * shares - (self.position_size / self.shares) * shares
                self.shares -= shares
                self.position_size -= shares * share_price - profit
                return profit
            else:
                profit = share_price * self.shares - self.position_size
                self.shares -= shares
                self.position_size -= shares * share_price - profit
                return profit
    def setcp(self,current_price):
        self.current_price = current_price

    def get_position_value(self):
        self.position_value = (self.shares*self.current_price)-self.position_size
        return self.position_value

    def get_shares(self):
        return self.shares

    def to_tuple(self):
        self.get_position_value()
        return self.shares, self.current_price , self.position_size, self.position_value

    def to_dict(self):
        self.get_position_value()
        return {'shares': self.shares,'current_price':self.current_price, 'position_size': self.position_size, 'position_value':self.position_value}