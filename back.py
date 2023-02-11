from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
import os
from dotenv import load_dotenv
import PIL

load_dotenv() 
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

# Set the network you want to operate on, or add your own RPC URL here
NETWORK = "mumbai"

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY,NETWORK)

contract = sdk.get_nft_collection("0xA550040e9b90d8D5afec67b86e44f50356F6FCe6")



# Note that you can customize this metadata however you like
metadata = NFTMetadataInput.from_json({
    "name": "MagicBall",
    "description": "",
    "image": open("gdsc.svg", "rb"),
})

tx = contract.mint_to("0xDA892A53c6d76Fa3394B0Fd9B0203cb645a50464", metadata)



receipt = tx.receipt
token_id = tx.id
print(receipt)
print(token_id)
