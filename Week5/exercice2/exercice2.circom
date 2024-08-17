pragma circom 2.0.0;

template AllOnes(n) {
    signal input x[n];
    signal output isAllOne;

    signal tmp[n];
    signal product;

    // Initialize the first element of tmp to the first input value
    tmp[0] <== x[0];

    // Calculate the product of all inputs iteratively
    for (var i = 1; i < n; i++) {
        tmp[i] <== tmp[i-1] * x[i];
    }

    // The final product is stored in tmp[n-1]
    product <== tmp[n-1];

    // Check if the product is 1
    signal isProductOne;
    isProductOne <== product - 1;
    isAllOne <== 1 - isProductOne * isProductOne;
}


component main = AllOnes(5); // Replace 5 with the desired of inputs


