pragma circom 2.0.0;

template AtLeastOneZero(n) {
    signal input x[n];
    signal output isZero;

    component notZero[n];
    signal tmp[n];
    signal allNonZero;

    // Instantiate notZero components and connect inputs
    for (var i = 0; i < n; i++) {
        notZero[i] = IsEqual();
        notZero[i].in[0] <== x[i];
        notZero[i].in[1] <== 0;

        // Accumulate product in tmp array
        if (i == 0) {
            tmp[i] <== notZero[i].out;
        } else {
            tmp[i] <== tmp[i-1] * notZero[i].out;
        }
    }

    // Final product in allNonZero
    allNonZero <== tmp[n-1];

    isZero <== 1 - allNonZero;
}

// IsEqual template checks if two inputs are equal using arithmetic
template IsEqual() {
    signal input in[2];
    signal output out;

    // out is 1 if in[0] is equal to in[1], otherwise 0
    out <== 1 - (in[0] - in[1]) * (in[0] - in[1]);
}

component main = AtLeastOneZero(5); // Replace 5 with the desired of inputs


