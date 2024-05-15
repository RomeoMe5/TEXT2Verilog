`timescale 1ns / 1ps

module ram_16x8_tb;

    reg clk;
    reg [3:0] addr;
    reg [7:0] data_in;
    reg write_en;
    wire [7:0] data_out;

    // Инстанцирование модуля ram_16x8
    ram_16x8 uut (
        .clk(clk),
        .addr(addr),
        .data_in(data_in),
        .write_en(write_en),
        .data_out(data_out)
    );

    // Генерация тактового сигнала
    initial begin
        clk = 0;
        forever #10 clk = ~clk; // Период в 20ns
    end

    // Тестовый сценарий
    initial begin
        write_en = 0; addr = 0; data_in = 0; #5; // Начальная инициализация
        write_en = 1; addr = 4; data_in = 8'hA5; #20; // Запись значения A5 по адресу 4
        write_en = 0; #20; // Отключение записи
        addr = 4; #20; // Чтение из адреса 4
        write_en = 1; addr = 2; data_in = 8'h3C; #20; // Запись значения 3C по адресу 2
        write_en = 0; addr = 2; #20; // Чтение из адреса 2
        $finish;
    end

    // Отслеживание сигналов
    initial begin
        $monitor("Время=%t, Адрес=%h, Входные данные=%h, Разрешение записи=%b, Выходные данные=%h", $time, addr, data_in, write_en, data_out);
    end

endmodule
