`timescale 1ns / 1ps

module encoder4to2_ifelse_tb;

    reg [3:0] in;
    wire [1:0] out;

    // Инстанцирование модуля encoder4to2_ifelse
    encoder4to2_ifelse uut (
        .in(in),
        .out(out)
    );

    initial begin
        // Инициализация входных сигналов
        in = 4'b0000; #20;
        in = 4'b0001; #20;
        in = 4'b0010; #20;
        in = 4'b0100; #20;
        in = 4'b1000; #20;
        in = 4'b0011; #20; // Тест с несколькими активными входами
        in = 4'b0000; #20; // Повторное тестирование без активных входов

        // Завершение симуляции
        $finish;
    end

    initial begin
        $monitor("Время=%t, Входной сигнал=%b, Выход=%b", $time, in, out);
    end

endmodule
