import React, { useEffect } from 'react';
import { Container, Row, Col } from 'react-bootstrap'
import { GiDwarfFace, GiGoblinHead } from "react-icons/gi";

import { Outlet, Link } from "react-router-dom";

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return <Container className="AppWrapper">
    <Row>
      <Col xs={2}><GiDwarfFace className='AppIcon'/> vs <GiGoblinHead className='AppIcon'/></Col>
      <Col xs={6}>
        <Link to="/">home</Link>·
        {/* <Link to="/lore">lore</Link>· */}
        {/* <Link to="/leaderboard">leaderboard</Link>· */}
        {/* <Link to="/wallet">wallet</Link>· */}
        {/* <Link to="/about">about</Link> */}
      </Col>
      {/* <ConnectButton></ConnectButton> */}
      <Col xs={4}>Opensea·Twitter·Etherscan</Col>
    </Row>
    <Row>
      <Outlet />
    </Row>
    <Row>
      <Col>Footer</Col>
    </Row>
  </Container>
}

export default App;
