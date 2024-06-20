// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

pragma abicoder v2;

import "forge-std/Test.sol";
import {Verifier,Pairing} from "../src/verifier.sol";
import "lib/forge-std/src/StdInvariant.sol";

contract VerifierTest is Test {
    Verifier public verif;

    function setUp() public {
        verif = new Verifier();
    }

    function testPairing() public view returns (bool) {
        Pairing.G1Point memory G1 = Pairing.G1Point({X: 1, Y: 2});
        Pairing.G2Point memory G2 = Pairing.G2Point({
            X: [10857046999023057135944570762232829481370756359578518086990519993285655852781, 11559732032986387107991004021392285783925812861821192530917403151452391805634],
            Y: [8495653923123431417604973247489272438418190587263600148770280649306958101930, 4082367875863433681332203403145435568316851327593401208105741076214120093531]
        });

        return Pairing.pairing(
            G1,
            G2,
            G1,
            G2,
            G1,
            G2,
            G1,
            G2
        );
    }

    function testScalarMulG2() public view returns (bool success) {
        Pairing.G2Point memory G2 = Pairing.G2Point({
            X: [10857046999023057135944570762232829481370756359578518086990519993285655852781, 11559732032986387107991004021392285783925812861821192530917403151452391805634],
            Y: [8495653923123431417604973247489272438418190587263600148770280649306958101930, 4082367875863433681332203403145435568316851327593401208105741076214120093531]
        });

        Pairing.G2Point memory G2Bis = Pairing.scalar_mul2(G2,uint256(8));
        return true;

    }

}
