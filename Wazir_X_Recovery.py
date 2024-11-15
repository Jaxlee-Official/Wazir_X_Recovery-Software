import os
from mnemonic import Mnemonic
from web3 import Web3
from eth_account import Account
import requests
import json
import time
import ctypes

# Enable Mnemonic features of Account
Account.enable_unaudited_hdwallet_features()

art = r"""
__      __               .__         ____  ___    __________                                              
/  \    /  \_____  _______|__|______  \   \/  /    \______   \ ____   ____  _______  __ ___________ ___.__.
\   \/\/   /\__  \ \___   /  \_  __ \  \     /      |       _// __ \_/ ___\/  _ \  \/ // __ \_  __ <   |  |
 \        /  / __ \_/    /|  ||  | \/  /     \      |    |   \  ___/\  \__(  <_> )   /\  ___/|  | \/\___  |
  \__/\  /  (____  /_____ \__||__|____/___/\  \_____|____|_  /\___  >\___  >____/ \_/  \___  >__|   / ____|
       \/        \/      \/     /_____/     \_/_____/      \/     \/     \/                \/       \/      /
"""

print(art)
print("Made By :- @seedbrutoforceofficial | @nova_algo")

#connect to web3 and infura
api = "https://mainnet.infura.io/v3/{YOURINFURAPIHERE}"
web3 = Web3(Web3.HTTPProvider(api))
if web3.is_connected():
    print("Starting Search...")
else:
    print("Failed to connect to Servers | please contact the owner")

mnemo = Mnemonic("english")

def earned(wallet_gen):
    with open("found_it.txt", "a") as file:
        file.write(wallet_gen + "\n")
    print("Wallet with balance saved to fount_it.txt")

    
def generation():
 checked_count = 0
 address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
 while True:
  mnemonic_phrase = mnemo.generate(strength=128)
  acct = Account.from_mnemonic(mnemonic_phrase)
  eth_address = acct.address
  wallet_gen = f"{address} - Targeted Address| {eth_address} Generated Address | mnemonic: {mnemonic_phrase}"
  print(wallet_gen)
  checked_count += 1
  title = f"Lucas Software | Wazir X Recovery | Checked:{checked_count} | @seedbrutoforceofficial & @nova_algo"
  ctypes.windll.kernel32.SetConsoleTitleW(title)
  if eth_address == address:
     earned(wallet_gen)

  #time.sleep(0)

generation()

#Made By :- @seedbrutoforceofficial | @nova_algo
#Made By :- @seedbrutoforceofficial | @nova_algo
#Made By :- @seedbrutoforceofficial | @nova_algo
