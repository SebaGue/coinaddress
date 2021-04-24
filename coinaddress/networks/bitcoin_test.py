from .base import BaseNetwork
from .registry import registry


@registry.register('bitcoin_test', 'BTCTEST')
class BitcoinTestnet(BaseNetwork):
    """ add bitcoin test """
    pubkey_address_prefix = 0x6F
