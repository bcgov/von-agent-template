# Running on Sovrin

To start OrgBook connecting to the Sovrin Staging Network (SSN) you just need to run the following command:

```
GENESIS_URL=https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_sandbox_genesis ./manage start seed=<seed1>
```

For the issuing agent, set the following parameters in config/settings.yml (and then just run "./manage build" and then "./manage start"):

```
WALLET_SEED_VONX: <seed2>
INDY_GENESIS_URL: https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_sandbox_genesis
LEDGER_PROTOCOL_VERSION: "1.6"
AUTO_REGISTER_DID: false
```

Note that seed1 and seed2 need to be pre-registered on the SSN.

Also note that once your issuer registers their schema(s) and credential definition(s) on the SSN, then if you reset your local environment (i.e. delete the issuer wallet) you will need to "bump" your schema version number(s).


