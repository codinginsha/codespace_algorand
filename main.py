from algokit_utils.beta.algorand_client import(
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams,
)


#client to connect to locanet
algorand=AlgorandClient.default_local_net()

#import dispenser for kmd
dispenser=algorand.account.dispenser()
print("Dispenser ADDRESS:",dispenser.address)

creator = algorand.account.random()
print("Creator ADDRESS:",creator.address)
print(algorand.account.get_information(creator.address))


#Fund creator acc
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        reciver=creator.address,
        amount=10_000_000 #10 algos 
    )

   
)

print(algorand.account.get_information(creator.address))


sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=100,
        asset_name="Edu4Teen",
        unit_name="E4T",
    )
)

asset_id=sent_txn["conformation"]["asset-index"]
print("ASSET ID",asset_id)

reciver_acct=algorand.account.random(
    algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        reciver=reciver_acct.address,
        amount=10_000_000 #10 algos 
    )

   
)
)


#group trans
group_txn=algorand.new_group()

group.txn.add_asset_opt_in(
    AssetOptInParams(
        sender=reciver_acct.address,
        asset_id=asset_id
    )
)

group_txn.add_payment(
    PayParams(
        sender=reciver_acct.address,
        reciver=creator.address,
        amount=1_000_000
    )
)
group_txn.add_asset_transfer(
   AssetTransferParams(
        sender=creator.address,
        reciver=reciver_acct.address
        asset_id=asset_id,
        amount=10
    )
)

group_txn.execute()

print("Reciver Account Balance", algorand.account.get_asset_information)