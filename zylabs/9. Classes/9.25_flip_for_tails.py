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


def flip_for_tails(gv_coin, goal):
    tails = 0
    count = 0
    while tails < goal:
        x = gv_coin.flip()
        count += 1
        if x != 1:
            tails += 1
        else:
            continue
    return count


if __name__ == "__main__":
    gv_coin = GVCoin(15)
    num_tails = 100
    total = flip_for_tails(gv_coin, num_tails)
    print('Total number of flips for 100 tails:', total);

