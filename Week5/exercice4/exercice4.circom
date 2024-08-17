pragma circom 2.0.0;

include "../node_modules/circomlib/circuits/comparators.circom";

template Max3(n) {
    signal input x;
    signal input y;
    signal input z;
    signal output k;

    signal xy;
    signal yz;
    signal xz;

    component lt_xy = LessThan(n);
    lt_xy.in[0] <== x;
    lt_xy.in[1] <== y;
    xy <== lt_xy.out;

    component lt_yz = LessThan(n);
    lt_yz.in[0] <== y;
    lt_yz.in[1] <== z;
    yz <== lt_yz.out;

    component lt_xz = LessThan(n);
    lt_xz.in[0] <== x;
    lt_xz.in[1] <== z;
    xz <== lt_xz.out;

    // Determine if y is greater than or equal to x and z
    signal y_ge_x_and_z;
    y_ge_x_and_z <== (1 - xy) * yz;

    // Determine if z is greater than or equal to x and y
    signal z_ge_x_and_y;
    z_ge_x_and_y <== xz * (1 - yz);

    // Determine if x is the greatest
    signal x_is_greatest;
    x_is_greatest <== (1 - xy) * (1 - xz);

    // Final output k
    signal k_is_y;
    signal k_is_z;
    signal k_is_x;

    k_is_y <== y_ge_x_and_z * y;
    k_is_z <== z_ge_x_and_y * z;
    k_is_x <== x_is_greatest * x;

    k <== k_is_y + k_is_z + k_is_x;
}

component main = Max3(252);