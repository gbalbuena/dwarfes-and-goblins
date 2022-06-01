# dwarfes-and-goblins

## Introduction

On a remote metaverse, DWARFS mine $GOLD in a abandoned mines while GOBLINS are looking for opportunities to steal their precious rewards.
Once a player depleted all resources from a mine they can used them to recruit more creatures (Dwarfs/Goblins) to strengthening there fraction.

Our Game is risk protocol for NFTs using pseudo randomness to steal or mine `$GOLD` resources.
Those are then used re-enforce due recruitment of creatures and finally set the battle to the last standing (END OF GAME).

Each group can attack one another once a creature has no more HP I'll DIE in a final Battle where a last standing creature will live to be the last to tell the story.

Victors history will be written and recorded as on-chain record. For everyone to see the and observe and review the battle.

GOBLINS are good to steal but not so good for war, in the other side DWARFS are war machines but while mining they have the limitations of their weight and slow speed so It's a disadvantage agains greedy GOBLINS

Last standing characters will be reward: Stay tuned

## Game Design Whitepaper

-   [Whitepaper](./docs/whitepaper-v1.md)

## Game Design Concepts

Our game asset will be generative in nature using low
level on-chain encoding of pixel art.
We have developed a few concepts of the Dwarf and Goblin
rase

### Dwarfs

 ![Dwarfs pixel concept](/assets/dwarfs.png)

### Goblins

 ![Dwarfs pixel concept](/assets/goblins.png)

## Prerequisites

Please install or have installed the following:

-   [nodejs and npm](https://nodejs.org/en/download/)
-   [python](https://www.python.org/downloads/)

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```

Or, if that doesn't work, via pip

```bash
pip install eth-brownie
```

2. Install Dependencies

```bash
brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0
brownie pm install smartcontractkit/chainlink@1.4.1
```

## Run Tests

```bash
make t
```

## Contributors

* bushwalker.eth
* anotherme.eth
* bleaknight