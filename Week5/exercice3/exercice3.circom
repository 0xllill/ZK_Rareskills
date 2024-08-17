pragma circom 2.0.0;

template BipartiteGraph2Coloring(n) {
    signal input adj[n][n]; // Adjacency matrix of the graph
    signal input color[n]; // Color array for each node (0 or 1)
    signal output valid; // Output that checks if the coloring is valid

    // Ensure colors are binary (0 or 1)
    signal colorBinary[n];
    for (var i = 0; i < n; i++) {
        colorBinary[i] <== color[i] * (1 - color[i]);
    }

    // Check adjacent nodes have different colors
    signal colorDiff[n][n];
    signal validEdge[n][n];
    signal edgeCheck[n][n];
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < i; j++) { // Only check lower triangle to avoid duplicate checks
            colorDiff[i][j] <== color[i] - color[j];
            validEdge[i][j] <== adj[i][j] * colorDiff[i][j];
            edgeCheck[i][j] <== validEdge[i][j] * validEdge[i][j];
        }
    }

    // Calculate the total number of checks
    var totalChecks = n + (n * (n-1) / 2);

    // Aggregate all checks
    signal validChecks[totalChecks + 1];
    validChecks[0] <== 1;

    var idx = 1;
    for (var i = 0; i < n; i++) {
        // Add color binary check
        validChecks[idx] <== validChecks[idx-1] * (1 - colorBinary[i]);
        idx++;

        // Add edge checks
        for (var j = 0; j < i; j++) {
            validChecks[idx] <== validChecks[idx-1] * (edgeCheck[i][j] + 1 - adj[i][j]);
            idx++;
        }
    }

    valid <== validChecks[totalChecks];
}

component main = BipartiteGraph2Coloring(4); // Example with 4 nodes