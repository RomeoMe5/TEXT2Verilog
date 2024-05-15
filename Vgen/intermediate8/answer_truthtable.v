// This is a circuit synthesized from a truth table
// The truth table is for a three-input, one-output function. It has 8 rows for each of the 8 possible input combinations, and one output column. 
// There are four inputs combinations where the output is 1, and four where the output is 0.
//    Inputs   |  Outputs
//  x3  x2  x1 |    f 
//  0   0   0  |    1
//  0   0   1  |    1
//  0   1   0  |    0
//  0   1   1  |    1
//  1   0   0  |    0
//  1   0   1  |    0
//  1   1   0  |    1
//  1   1   1  |    0
module truthtable(input x3, input x2, input x1, output f );

assign f = (~x3 && ~x2 && ~x1) || (~x3 && ~x2 && x1) || (~x3 && x2 && x1) || (x3 && x2 && ~x1);

endmodule