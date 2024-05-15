`timescale 1ns / 1ps

module testbench;
    reg a, b, bin;
    wire difference, bout;

    // Инстанциирование вашего модуля full_subtractor
    full_subtractor uut (
        .a(a), 
        .b(b), 
        .bin(bin), 
        .difference(difference), 
        .bout(bout)
    );

    initial begin
        // Инициализация входных сигналов
        a = 0; b = 0; bin = 0;
        #10; // Ждать 10 наносекунд
        
        // Перебор всех возможных комбинаций входов
        {a, b, bin} = 3'b000; #10;
        {a, b, bin} = 3'b001; #10;
        {a, b, bin} = 3'b010; #10;
        {a, b, bin} = 3'b011; #10;
        {a, b, bin} = 3'b100; #10;
        {a, b, bin} = 3'b101; #10;
        {a, b, bin} = 3'b110; #10;
        {a, b, bin} = 3'b111; #10;

        // Завершение симуляции
        $finish;
    end

    initial begin
        $monitor("Time = %d, a = %b, b = %b, bin = %b, difference = %b, bout = %b", $time, a, b, bin, difference, bout);
    end
endmodule
