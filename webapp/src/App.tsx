import React, { useEffect } from 'react';
import { Container, Row, Col } from 'react-bootstrap'
import { GiDwarfFace, GiGoblinHead } from "react-icons/gi";

import { Outlet, Link } from "react-router-dom";

// import '@rainbow-me/rainbowkit/styles.css';

import {
  getDefaultWallets,
  RainbowKitProvider,
} from '@rainbow-me/rainbowkit';
import {
  chain,
  configureChains,
  createClient,
  WagmiConfig,
} from 'wagmi';
import { alchemyProvider } from 'wagmi/providers/alchemy';
import { publicProvider } from 'wagmi/providers/public';
import { ConnectButton } from '@rainbow-me/rainbowkit';

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum],
  [
    alchemyProvider({ alchemyId: process.env.ALCHEMY_ID }),
    publicProvider()
  ]
);

const { connectors } = getDefaultWallets({
  appName: 'My RainbowKit App',
  chains
});

const wagmiClient = createClient({
  autoConnect: true,
  connectors,
  provider
})

function App() {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Container className="AppWrapper">
          <Row>
            <Col xs={2}><GiDwarfFace className='AppIcon' /> vs <GiGoblinHead className='AppIcon' /></Col>
            <Col xs={6}>
              <Link to="/">home</Link>·
              <Link to="/lore">lore</Link>
              ·<Link to="/leaderboard">leaderboard</Link>
              ·<Link to="/wallet">wallet</Link>
              ·<Link to="/about">about</Link>
            </Col>
            <ConnectButton></ConnectButton>
          </Row>

          <Row>
            <Outlet />
          </Row>
          <Row>
            <Col xs={4}>Opensea·Twitter·Etherscan</Col>
          </Row>

        </Container>
      </RainbowKitProvider>
    </WagmiConfig>
  )
}

export default App;
