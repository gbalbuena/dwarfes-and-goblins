## Setup pyenv

[Setup Pyenv](https://github.com/pyenv/pyenv)
[Setup Direnv](https://direnv.net/)


### Python Setup

```bash
pip install -r requirements.txt
```


### Brownie

```bash
brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0 
```

```bash
brownie test
```

### ganache
requires 7.0.4+

```bash
yarn global remove ganache-cli ganache-core
yarn global add ganache@7.0.4
```


### VScode Settings

```js
{
    "solidity.defaultCompiler": "remote",
    "solidity.compileUsingRemoteVersion": "v0.8.9+commit.e5eed63a",
    "solidity.remappingsUnix": [
        "@openzeppelin/=/home/gwi/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.5.0/"
    ],
    "python.analysis.extraPaths": [
        "contracts/.direnv/python-3.8.12/lib/python3.8/site-packages",
    ],
}
```



