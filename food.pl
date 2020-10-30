food(X) :- hot(X).
food(X) :- thai(X),beauty(X).  %AND
food(X) :- eng(X);have_cheese(X).   %OR
bad_taste(X) :- sweet(X).
bad_taste(X) :- lao(X).

thai(padthai).
thai(tom_yam_kung).
thai(kuai_tiew).
thai(pad_kra_pao).
thai(kao_pad).
thai(kai_palo).
thai(kai_tom).
%------------------------------------------------
eng(hamberger).
eng(spaghetti).
%have_cheese(kaitom).

beauty(kai_palo).
lao(somtum).
lao(prala).
sweet(padthai).
sweet(kao_pad).
hot(tom_yam_kung).
hot(kuai_tiew).
hot(pad_kra_pao).