// SPDX-License-Identifier: MIT
pragma solidity 0.8.25;

contract Problem1 {

    struct ECPoint {
        uint256 x;
        uint256 y;
    }

    function rationalAdd(ECPoint calldata A, ECPoint calldata B, uint256 num, uint256 den) public view returns (bool verified) {

        // return true if the prover knows two numbers that add up to num/den

        // Elliptic curve parameters for BN128
        uint256 curve_order = 21888242871839275222246405745257275088548364400416034343698204186575808495617;

        // got generator point from py_ecc.bn128 as well
        uint256 gx = 1;
        uint256 gy = 2;
    
        // Compute inverse of den using Fermat's Little Theorem
            // pow(a,-1,curve_order) == pow(a,curve_order-2,curve_order)
        uint256 invDen = doModExp(den,curve_order - 2,curve_order);

        // Compute num * invDen (mod curve_order)
        uint256 numDen = mulmod(num, invDen, curve_order);

        // Get num/den * G using elliptic curve multiplication (precompiled contract at address 7)
        (bool success, bytes memory eccNumDen) = address(7).staticcall(abi.encode(gx, gy, numDen));
        require(success, "mul ec failed");
        (uint256 eccNumDenX, uint256 eccNumDenY) = abi.decode(eccNumDen, (uint256, uint256));

        // ---

        // Add points A and B using elliptic curve addition (precompiled contract at address 6)
        (bool ok, bytes memory CResult) = address(6).staticcall(abi.encode(A.x, A.y, B.x, B.y));
        require(ok, "failed ec addition");
        (uint256 abX, uint256 abY) = abi.decode(CResult, (uint256, uint256));

        require(abX < curve_order && abY < curve_order,"abX or abY > curve_order");
        
        // Verify if the sum of points A and B equals the computed point from num/den
        return (abX == eccNumDenX && abY == eccNumDenY);
    }

    // Function to perform modular exponentiation using the precompiled contract at address 0x05
    function doModExp(uint256 _b, uint256 _e, uint256 _m) public returns (uint256 result) {
        assembly {
            // Free memory pointer
            let pointer := mload(0x40)

            // Define length of base, exponent and modulus. 0x20 == 32 bytes
            mstore(pointer, 0x20)
            mstore(add(pointer, 0x20), 0x20)
            mstore(add(pointer, 0x40), 0x20)

            // Define variables base, exponent and modulus
            mstore(add(pointer, 0x60), _b)
            mstore(add(pointer, 0x80), _e)
            mstore(add(pointer, 0xa0), _m)

            // Store the result
            let value := mload(0xc0)

            // Call the precompiled contract 0x05 = bigModExp
            if iszero(call(not(0), 0x05, 0, pointer, 0xc0, value, 0x20)) {
                revert(0, 0)
            }

            result := mload(value)
        }
    }

}