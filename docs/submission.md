## Inspiration

Our inspiration is taken from the D&D domain and text based adventure game for the late 90's.
There is a big community of people who love the lore and the details put into text based games
which rich theory-craft and number mechanics.
We will be leveraging the lore and design craft around stats and attributes and bringing an initially simple game to the blockchain.
Our main challenge is how to use randomness effectively to design the game without making it
predictable. Randomness on blockchains is a complicated subject and we aim to create engaging
and fun concept around known limitation.  

## What it does

Our game is an NFT wich is using staking mechanism and on-chain randomness to implement
described game mechanics.
We have written a [light-paper](https://github.com/gbalbuena/dwarves-and-goblins/blob/main/docs/whitepaper-v1.md) of our game design with some details for the game mechanics. 

### Implemented functionality
- staking NFT's to mine resources
- generate randomness using chainlink VRF2
- creature factory for generating creatures using randomness for the DNA

### Limitations
- on-chain data encoding is not yet implemented (but we have encoder/decoder)
- currently all creatures share the same random seed but this is can be easily extended 
- NFT creature class design is basic
- NFT metadata encoding is not implemented yet

### Lore
On a remote metaverse, DWARFS mine $GOLD in a abandoned mines while GOBLINS are looking for opportunities to steal their precious rewards.
Once a player depleted all resources from a mine they can used them to recruit more creatures (Dwarfs/Goblins) to strengthening there fraction.

Our Game is risk protocol for NFTs using pseudo randomness to steal or mine `$GOLD` resources.
Those are then used re-enforce due recruitment of creatures and finally set the battle to the last standing (END OF GAME).

Each group can attack one another once a creature has no more HP I'll DIE in a final Battle where a last standing creature will live to be the last to tell the story.

Victors history will be written and recorded as on-chain record. For everyone to see the and observe and review the battle.

GOBLINS are good to steal but not so good for war, in the other side DWARFS are war machines but while mining they have the limitations of their weight and slow speed so It's a disadvantage agains greedy GOBLINS

## How we built it

We focused on the aspects of the solution we hadn't done before.
Some team member have experience developing a on-chain NFT [Bitstrays](https://bitstrays.wtf/) using RLE encoded binary data. So we know that we can solve that part later.
[RLE Implementation](https://etherscan.io/address/0x9da7811ef73222393077730e7b4853a01eede1c3#code) 

Our Game currently consists of a couple of contracts.
- NFT Creatures Contract which is used to summon or generate player of the game
- NFT CreatureFactory which is Creatures and uses the random number to create DNA
DNA will be use to derive the properties of the characters.
- Staking contract which is used to issue the resources to the players
Gold Token which is reward for action in the game

We used TDD for our smart contract using brownie for local testing.

More Details in the [light-paper](https://github.com/gbalbuena/dwarfes-and-goblins/blob/main/docs/whitepaper-v1.md)

## Challenges we ran into

- Testing VRF on testnet turned out to be a bit tricky we only managed to get it running locally
- Time constraints to deliver something working given that all team members are full time employed was challenging
- true Randomness on-chain is sparse. Our game would require large quantities of random actions will requires some research details see  [light-paper](https://github.com/gbalbuena/dwarfes-and-goblins/blob/main/docs/whitepaper-v1.md)
- On-chain asset encoding will be challenging in terms of deployment cost some EVM chains

## Accomplishments that we're proud of

We spend a fair amount of time to build a good understanding around the game mechanics
in the process we really started liking the idea.
Which means this project is grown bigger than just the hack event
- onboarding some of the team members to brownie and test driven development
- prototype wich will help to iterated on and further developed in the future
- Test driven development approach
- Game design white paper will help to explain our vison as we grow our community

## What we learned

- Randomness on blockchain is expensive
- VRF Randomness break the synchronous process and requires planning to incentivize user to generate there seeds before minting creatures
- On-chain NFT storage challenges
- concepts of how to make our game flexible potentially extensible in the future  

## What's next for Dwarfs vs Goblins

- Building community
- Implement onchain image encoding using REL and SVG conversion [Bitstrays.wtf Project](https://etherscan.io/address/0x9da7811ef73222393077730e7b4853a01eede1c3#code)
- Improve and grow image asset collection
- Refactor NFTToken and move VRF to factory (better design)
- Adding more sophisticated bit shift capability to maximize randomseed 
- Implement game mechanics around the battle of fractions
- enhance staking concept to incorporate goblin attack and randomness
- Deploy on testnet
