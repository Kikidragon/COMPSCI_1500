import random

class GVCoin:
    def __init__(self, seed):
        random.seed(seed)
        self.is_heads = True
        self.heads = 0
        self.flips = 0

    def flip(self):
        self.is_heads = random.randint(0, 1)
        self.flips += 1
        if self.is_heads == 1:
            self.heads += 1
        return self.is_heads

    def get_is_heads(self):
        return self.is_heads

    def to_string(self):
        str = 'Flips', self.flips,'Heads:',self.heads,'isHeads',self.is_heads
        return str

    def num_flips(self):
        return self.flips

    def num_heads(self):
        return self.heads

    def num_tails(self):
        return self.flips - self.heads

    def set_to_heads(self, h):
        self.is_heads = h

def count_heads(gv_coin, goal):
    heads = 0
    count = 0
    while heads < goal:
        x = gv_coin.flip()
        count += 1
        if x == 1:
            heads += 1
        else:
            continue
    return count

if __name__ == "__main__":
    gv_coin = GVCoin(15)
    num_heads = 20
    num_flips = count_heads(gv_coin, num_heads)
    print('Total number of flips for 20 heads:', num_flips);

    num_heads = 100
    num_flips = count_heads(gv_coin, num_heads)
    print('Total number of flips for 100 heads:', num_flips);

