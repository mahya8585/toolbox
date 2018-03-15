from azure.storage.blob import BlockBlobService


"""
blobコンテナの作成
"""

# TODO 事前にstorageアカウントを作成してください
account_name = 'YOUR ACCOUNT NAME'
account_key = 'YOUR ACCOUNT KEY'

block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)

block_blob_service.create_container('input')
block_blob_service.create_container('output')
