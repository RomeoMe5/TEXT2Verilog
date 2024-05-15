`timescale 1ns / 1ps

module moore_fsm_101_tb;

    reg clk, reset, in;
    wire out;

    // Инстанцирование moore_fsm_101
    moore_fsm_101 uut (
        .clk(clk),
        .reset(reset),
        .in(in),
        .out(out)
    );

    // Генерация тактового сигнала
    initial begin
        clk = 0;
        forever #10 clk = ~clk;
    end

    // Тестовый сценарий
    initial begin
        reset = 1; in = 0; #20;
        reset = 0; in = 1; #20; // Переход к S1
        in = 0; #20; // Переход к S2, должен активировать выход
        in = 1; #20; // Возвращение к S1
        in = 0; #20; // Переход к S2, снова активируется выход
        reset = 1; #20; // Сброс и возвращение к начальному состоянию
        $finish;
    end

    // Отслеживание сигналов
    initial begin
        $monitor("Время=%t, Сброс=%b, Вход=%b, Состояние=%b, Выход=%b", $time, reset, in, uut.state, out);
    end

endmodule
