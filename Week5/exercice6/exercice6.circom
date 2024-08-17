pragma circom 2.0.0;

template IsPowerOfTwo(n) {
    signal input v;
    signal output isPowerOfTwo;

    // Signals to store the binary representation of v
    signal binary[n];

    // Constraint to ensure v is positive
    v * (v - 1) === 0;

    // Encode v in binary
    var acc = 0;
    for (var i = 0; i < n; i++) {
        binary[i] <-- (v \ (2**i)) % 2;  // Integer division and modulo
        binary[i] * (binary[i] - 1) === 0;  // Constrain binary[i] to be 0 or 1
        acc += binary[i] * (2**i);
    }
    v === acc;  // Ensure the binary representation matches v

    // Count the number of 1s in the binary representation
    signal oneCount[n+1];
    oneCount[0] <== 0;
    for (var i = 0; i < n; i++) {
        oneCount[i+1] <== oneCount[i] + binary[i];
    }

    // v is a power of two if and only if there's exactly one 1 in its binary representation
    // and v is not zero
    signal isOne;
    signal isNotZero;
    isOne <== 1 - (oneCount[n] - 1) * (oneCount[n] - 1);
    isNotZero <== 1 - (v - 1) * (v - 1);
    isPowerOfTwo <== isOne * isNotZero;
}

component main = IsPowerOfTwo(32);  // Adjust 32 based on the maximum expected value of v