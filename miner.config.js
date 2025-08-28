module.exports = {
  apps: [
    {
      name: "miner1",
      interpreter: "python3",
      script: "./neurons/miner.py",
      args: "--netuid 50 --logging.debug --logging.trace --wallet.name miner --wallet.hotkey miner_1 --axon.port 8091 --blacklist.force_validator_permit true --blacklist.validator_min_stake 1",
      env: {
        PYTHONPATH: ".",
      },
    },
    {
      name: "miner2",
      interpreter: "python3",
      script: "./neurons/miner.py",
      args: "--netuid 50 --logging.debug --logging.trace --wallet.name miner --wallet.hotkey miner_2 --axon.port 8092 --blacklist.force_validator_permit true --blacklist.validator_min_stake 1",
      env: {
        PYTHONPATH: ".",
      },
    },
    {
      name: "miner3",
      interpreter: "python3",
      script: "./neurons/miner.py",
      args: "--netuid 50 --logging.debug --logging.trace --wallet.name miner --wallet.hotkey miner_3 --axon.port 8093 --blacklist.force_validator_permit true --blacklist.validator_min_stake 1",
      env: {
        PYTHONPATH: ".",
      },
    },
    {
      name: "miner4",
      interpreter: "python3",
      script: "./neurons/miner.py",
      args: "--netuid 50 --logging.debug --logging.trace --wallet.name miner --wallet.hotkey miner_4 --axon.port 8093 --blacklist.force_validator_permit true --blacklist.validator_min_stake 1",
      env: {
        PYTHONPATH: ".",
      },
    },    
  ],
};
