from azure.storage.blob import BlockBlobService


# blob setting
account_name = 'YOUR ACCOUNT NAME'
account_key = 'YOUR ACCOUNT KEY'
container_name = 'output'

# コンテナ丸ごと取得
print('blob download')
block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
blobs = block_blob_service.list_blobs(container_name)

# テキストファイルだけダウンロードする
for blob in blobs:
    print("Blob name: " + blob.name)
    block_blob_service.get_blob_to_path(container_name, blob.name, blob.name)
