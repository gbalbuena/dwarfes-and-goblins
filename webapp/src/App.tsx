import React, { useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useMoralis } from "react-moralis";
import { Avatar, ConnectButton } from 'web3uikit';
import { Container, Row, Col } from 'react-bootstrap'

function App() {
  return <Container className="AppWrapper">
    <Row>
      <Col><Avatar avatarBackground="#ff0000" fontSize={25} isRounded size={80} text="DG" theme="letters" />
      </Col>
      <Col xs={6}></Col>
      <Col><ConnectButton></ConnectButton></Col>
    </Row>
    <Row>
      <Col><h1>Hello world!</h1></Col>
    </Row>
  </Container>
}

export default App;
