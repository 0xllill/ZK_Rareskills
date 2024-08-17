pragma circom 2.0.0;

template AtLeastOneBinary(n) {
    signal input x[n];
    signal output result;

    // Constrain inputs to be binary
    signal binary[n];
    for (var i = 0; i < n; i++) {
        binary[i] <== x[i] * (1 - x[i]);
    }

    // Calculate the product of (1 - x[i])
    signal product[n+1];
    product[0] <== 1;
    for (var i = 0; i < n; i++) {
        product[i+1] <== product[i] * (1 - x[i]);
    }

    // The result is 1 minus the final product
    result <== 1 - product[n];

    // Constrain all binary checks to be 0
    signal sum_binary[n+1];
    sum_binary[0] <== 0;
    for (var i = 0; i < n; i++) {
        sum_binary[i+1] <== sum_binary[i] + binary[i];
    }
    sum_binary[n] === 0;
}

component main = AtLeastOneBinary(5);