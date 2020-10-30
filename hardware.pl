hardware(X) :- process(X).
hardware(X) :- input(X).
hardware(X) :- output(X).

process(case).
process(power_supply).
process(main_board).
process(cpu).
%------------------------------------------------
input(display_card).
input(mouse).
input(keyboard).
input(monitor).
%------------------------------------------------
output(kai_palo).
output(somtum).
output(prala).
output(padthai).
output(kao_pad).