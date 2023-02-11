from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
PRIVATE_KEY = "<your-private-key-here>"
from thirdweb.types.nft import NFTMetadataInput

# Set the network you want to operate on, or add your own RPC URL here
NETWORK = "mumbai"

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK(NETWORK)

contract = sdk.get_nft_collection("0xA550040e9b90d8D5afec67b86e44f50356F6FCe6")



# Note that you can customize this metadata however you like
metadata = NFTMetadataInput.from_json({
    "name": "Cool NFT",
    "description": "This is a cool NFT",
    "image": open("path/to/file.jpg", "rb"),
})
