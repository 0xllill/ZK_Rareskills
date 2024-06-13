// SPDX-License-Identifier: MIT
pragma solidity 0.8.25;

contract Problem2 {
    struct ECPoint {
        uint256 x;
        uint256 y;
    }

    function matmul (
            uint256[] calldata matrix,
            uint256 n, // n x n for the matrix
            ECPoint[] calldata s, // n elements
            uint256[] calldata o // n elements
    ) public returns (bool verified) {
        
        // Elliptic curve parameters for BN128
        uint256 curve_order = 21888242871839275222246405745257275088548364400416034343698204186575808495617;

        // got generator point from py_ecc.bn128 as well
        uint256 gx = 1;
        uint256 gy = 2;

        // revert if dimensions don't make sense or the matrices are empty
        require(matrix.length == n * n, "Matrix dimensions do not match n x n");
        require(s.length == n, "Vector s dimensions do not match n");
        require(o.length == n, "Vector o dimensions do not match n");

        // return true if Ms == o elementwise. You need to do n equality checks. If you're lazy, you can hardcode n to 3, but it is suggested that you do this with a for loop 
        // Compute Ms = o element-wise
        
        for (uint256 i = 0; i < n; i++) {
            
            // Initialize sum to zero (point at infinity)
            uint256 sumX = 0;
            uint256 sumY = 0;
            bool first = true;

            for (uint256 j = 0; j < n; j++) {
                uint256 m_ij = matrix[i * n + j];

                // Multiply m_ij by s[j] using elliptic curve multiplication
                (uint256 tmpX, uint256 tmpY) = ecMul(m_ij, s[j].x, s[j].y);

                // Add the result to the sum
                if (first) {
                    sumX = tmpX;
                    sumY = tmpY;
                    first = false;
                } else {
                    (sumX, sumY) = ecAdd(sumX, sumY, tmpX, tmpY);
                }
            }

            // Multiply o[i] by the generator point G
            (uint256 oGx, uint256 oGy) = ecMul(o[i], gx, gy);

            // Check if the computed sum matches o[i] * G
            if (sumX != oGx || sumY != oGy) {
                return false;
            }
        }

        return true;

    }

    // Elliptic curve multiplication
    function ecMul(uint256 scalar, uint256 x, uint256 y) internal view returns (uint256, uint256) {
        (bool success, bytes memory result) = address(7).staticcall(abi.encode(x, y, scalar));
        require(success, "Elliptic curve multiplication failed");
        return abi.decode(result, (uint256, uint256));
    }

    // Elliptic curve addition
    function ecAdd(uint256 x1, uint256 y1, uint256 x2, uint256 y2) internal view returns (uint256, uint256) {
        (bool success, bytes memory result) = address(6).staticcall(abi.encode(x1, y1, x2, y2));
        require(success, "Elliptic curve addition failed");
        return abi.decode(result, (uint256, uint256));
    }
    

}