module full_subtractor (input a, input b, input bin, output difference, output bout); 
assign difference = a ^ b ^ bin; 
assign bout = (!a & b) | (!a & bin) | (b & bin); 
endmodule