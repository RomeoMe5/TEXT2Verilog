`timescale 1ns / 1ps

module mux4to1_lut_tb;

  reg [3:0] d;
  reg [1:0] sel;
  wire out;

  // Инстанцирование модуля mux4to1_lut
  mux4to1_lut uut (
    .d(d),
    .sel(sel),
    .out(out)
  );

  initial begin
    // Инициализация входных данных
    d = 4'b1010; // Примерный вектор данных
    sel = 2'b00; // Начальное значение селектора
    #10; // Ждем 10 ns

    sel = 2'b01; #10;
    sel = 2'b10; #10;
    sel = 2'b11; #10;

    // Завершаем симуляцию
    $finish;
  end

  // Отслеживание изменений значений
  initial begin
    $monitor("Time=%t, d=%b, sel=%b, out=%b", $time, d, sel, out);
  end

endmodule
