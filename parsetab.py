
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDleftORrightNOTleftLESSGREATHERLESSEQGREATHEREQEQUALITYDIFERENTleftPLUSMINUSleftTIMESDIVleftPOTrightUMINUSAND BOOL CHAR DECIMAL DIFERENT DIV ELSE EQUAL EQUALITY FALSE FLOAT GREATHER GREATHEREQ ID IF INT LBRACE LESS LESSEQ LOWERCASE LPAR MINUS NOT NUMBER OR PARSE PLUS POT PRINT PRINTLN RBRACE RPAR SEMICOL STR STRING TIMES TRUE TYPEOF UPPERCASE WHILEinit : instruccionesinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion  : print\n                    | println\n                    | definicion\n                    | asignacion\n                    | while\n                    | if\n                    | if_elseprint : PRINT LPAR exp_logica RPARprintln : PRINTLN LPAR exp_logica RPARdefinicion : IDasignacion : ID EQUAL exp_logicawhile : WHILE LPAR exp_logica RPAR LBRACE instrucciones RBRACEif : IF LPAR exp_logica RPAR LBRACE instrucciones RBRACEif_else : IF LPAR exp_logica RPAR LBRACE instrucciones RBRACE ELSE LBRACE instrucciones RBRACEexp_logica    : exp_logica AND exp_logica\n                    | exp_logica OR exp_logicaexp_logica : NOT exp_logicaexp_logica : exp_relacionalexp_relacional   : exp_relacional LESS exp_relacional\n                        | exp_relacional LESSEQ exp_relacional\n                        | exp_relacional GREATHER exp_relacional\n                        | exp_relacional GREATHEREQ exp_relacional\n                        | exp_relacional EQUALITY exp_relacional\n                        | exp_relacional DIFERENT exp_relacionalexp_relacional : exp_aritmeticaexp_aritmetica   : exp_aritmetica PLUS exp_aritmetica\n                        | exp_aritmetica MINUS exp_aritmetica\n                        | exp_aritmetica TIMES exp_aritmetica\n                        | exp_aritmetica DIV exp_aritmetica\n                        | exp_aritmetica POT exp_aritmeticaexp_aritmetica : MINUS exp_aritmetica %prec UMINUSexp_aritmetica : LPAR exp_logica RPARexp_aritmetica  : NUMBERexp_aritmetica : DECIMALexp_aritmetica : CHARexp_aritmetica : STRINGexp_aritmetica : TRUEexp_aritmetica : FALSEexp_aritmetica : ID'
    
_lr_action_items = {'PRINT':([0,2,3,4,5,6,7,8,9,10,13,16,25,26,28,29,30,31,32,33,34,36,40,43,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,],[11,11,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-21,-28,-36,-37,-38,-39,-40,-41,-42,-14,-11,-20,-34,-12,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,11,11,11,11,-15,-16,11,11,-17,]),'PRINTLN':([0,2,3,4,5,6,7,8,9,10,13,16,25,26,28,29,30,31,32,33,34,36,40,43,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-21,-28,-36,-37,-38,-39,-40,-41,-42,-14,-11,-20,-34,-12,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,12,12,12,12,-15,-16,12,12,-17,]),'ID':([0,2,3,4,5,6,7,8,9,10,13,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,34,34,34,34,34,34,34,-21,-28,34,-36,-37,-38,-39,-40,-41,-42,-14,-11,34,34,-20,34,34,34,34,34,34,34,34,34,34,34,-34,-12,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,13,13,13,13,-15,-16,13,13,-17,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,13,16,25,26,28,29,30,31,32,33,34,36,40,43,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-21,-28,-36,-37,-38,-39,-40,-41,-42,-14,-11,-20,-34,-12,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,14,14,14,14,-15,-16,14,14,-17,]),'IF':([0,2,3,4,5,6,7,8,9,10,13,16,25,26,28,29,30,31,32,33,34,36,40,43,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-21,-28,-36,-37,-38,-39,-40,-41,-42,-14,-11,-20,-34,-12,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,15,15,15,15,-15,-16,15,15,-17,]),'$end':([1,2,3,4,5,6,7,8,9,10,13,16,25,26,28,29,30,31,32,33,34,36,40,43,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,77,78,82,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-21,-28,-36,-37,-38,-39,-40,-41,-42,-14,-11,-20,-34,-12,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,-15,-16,-17,]),'RBRACE':([3,4,5,6,7,8,9,10,13,16,25,26,28,29,30,31,32,33,34,36,40,43,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,78,81,82,],[-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-21,-28,-36,-37,-38,-39,-40,-41,-42,-14,-11,-20,-34,-12,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,77,78,-15,-16,82,-17,]),'LPAR':([11,12,14,15,17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[17,18,20,21,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'EQUAL':([13,],[19,]),'NOT':([17,18,19,20,21,22,24,41,42,],[24,24,24,24,24,24,24,24,24,]),'MINUS':([17,18,19,20,21,22,24,26,27,28,29,30,31,32,33,34,41,42,44,45,46,47,48,49,50,51,52,53,54,55,59,68,69,70,71,72,],[27,27,27,27,27,27,27,51,27,-36,-37,-38,-39,-40,-41,-42,27,27,27,27,27,27,27,27,27,27,27,27,27,-34,-35,-29,-30,-31,-32,-33,]),'NUMBER':([17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'DECIMAL':([17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'CHAR':([17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'STRING':([17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'TRUE':([17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'FALSE':([17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'RPAR':([23,25,26,28,29,30,31,32,33,34,35,37,38,39,43,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[40,-21,-28,-36,-37,-38,-39,-40,-41,-42,56,57,58,59,-20,-34,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'AND':([23,25,26,28,29,30,31,32,33,34,35,36,37,38,39,43,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[41,-21,-28,-36,-37,-38,-39,-40,-41,-42,41,41,41,41,41,-20,-34,-35,-18,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'OR':([23,25,26,28,29,30,31,32,33,34,35,36,37,38,39,43,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[42,-21,-28,-36,-37,-38,-39,-40,-41,-42,42,42,42,42,42,-20,-34,-35,42,-19,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'LESS':([25,26,28,29,30,31,32,33,34,55,59,62,63,64,65,66,67,68,69,70,71,72,],[44,-28,-36,-37,-38,-39,-40,-41,-42,-34,-35,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'LESSEQ':([25,26,28,29,30,31,32,33,34,55,59,62,63,64,65,66,67,68,69,70,71,72,],[45,-28,-36,-37,-38,-39,-40,-41,-42,-34,-35,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'GREATHER':([25,26,28,29,30,31,32,33,34,55,59,62,63,64,65,66,67,68,69,70,71,72,],[46,-28,-36,-37,-38,-39,-40,-41,-42,-34,-35,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'GREATHEREQ':([25,26,28,29,30,31,32,33,34,55,59,62,63,64,65,66,67,68,69,70,71,72,],[47,-28,-36,-37,-38,-39,-40,-41,-42,-34,-35,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'EQUALITY':([25,26,28,29,30,31,32,33,34,55,59,62,63,64,65,66,67,68,69,70,71,72,],[48,-28,-36,-37,-38,-39,-40,-41,-42,-34,-35,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'DIFERENT':([25,26,28,29,30,31,32,33,34,55,59,62,63,64,65,66,67,68,69,70,71,72,],[49,-28,-36,-37,-38,-39,-40,-41,-42,-34,-35,-22,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,]),'PLUS':([26,28,29,30,31,32,33,34,55,59,68,69,70,71,72,],[50,-36,-37,-38,-39,-40,-41,-42,-34,-35,-29,-30,-31,-32,-33,]),'TIMES':([26,28,29,30,31,32,33,34,55,59,68,69,70,71,72,],[52,-36,-37,-38,-39,-40,-41,-42,-34,-35,52,52,-31,-32,-33,]),'DIV':([26,28,29,30,31,32,33,34,55,59,68,69,70,71,72,],[53,-36,-37,-38,-39,-40,-41,-42,-34,-35,53,53,-31,-32,-33,]),'POT':([26,28,29,30,31,32,33,34,55,59,68,69,70,71,72,],[54,-36,-37,-38,-39,-40,-41,-42,-34,-35,54,54,54,54,-33,]),'LBRACE':([57,58,79,],[73,74,80,]),'ELSE':([78,],[79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,73,74,80,],[2,75,76,81,]),'instruccion':([0,2,73,74,75,76,80,81,],[3,16,3,3,16,16,3,16,]),'print':([0,2,73,74,75,76,80,81,],[4,4,4,4,4,4,4,4,]),'println':([0,2,73,74,75,76,80,81,],[5,5,5,5,5,5,5,5,]),'definicion':([0,2,73,74,75,76,80,81,],[6,6,6,6,6,6,6,6,]),'asignacion':([0,2,73,74,75,76,80,81,],[7,7,7,7,7,7,7,7,]),'while':([0,2,73,74,75,76,80,81,],[8,8,8,8,8,8,8,8,]),'if':([0,2,73,74,75,76,80,81,],[9,9,9,9,9,9,9,9,]),'if_else':([0,2,73,74,75,76,80,81,],[10,10,10,10,10,10,10,10,]),'exp_logica':([17,18,19,20,21,22,24,41,42,],[23,35,36,37,38,39,43,60,61,]),'exp_relacional':([17,18,19,20,21,22,24,41,42,44,45,46,47,48,49,],[25,25,25,25,25,25,25,25,25,62,63,64,65,66,67,]),'exp_aritmetica':([17,18,19,20,21,22,24,27,41,42,44,45,46,47,48,49,50,51,52,53,54,],[26,26,26,26,26,26,26,55,26,26,26,26,26,26,26,26,68,69,70,71,72,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',137),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',141),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','gramatica.py',146),
  ('instruccion -> print','instruccion',1,'p_instruccion','gramatica.py',150),
  ('instruccion -> println','instruccion',1,'p_instruccion','gramatica.py',151),
  ('instruccion -> definicion','instruccion',1,'p_instruccion','gramatica.py',152),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','gramatica.py',153),
  ('instruccion -> while','instruccion',1,'p_instruccion','gramatica.py',154),
  ('instruccion -> if','instruccion',1,'p_instruccion','gramatica.py',155),
  ('instruccion -> if_else','instruccion',1,'p_instruccion','gramatica.py',156),
  ('print -> PRINT LPAR exp_logica RPAR','print',4,'p_print','gramatica.py',160),
  ('println -> PRINTLN LPAR exp_logica RPAR','println',4,'p_println','gramatica.py',164),
  ('definicion -> ID','definicion',1,'p_definicion','gramatica.py',168),
  ('asignacion -> ID EQUAL exp_logica','asignacion',3,'p_asignacion','gramatica.py',172),
  ('while -> WHILE LPAR exp_logica RPAR LBRACE instrucciones RBRACE','while',7,'p_while','gramatica.py',176),
  ('if -> IF LPAR exp_logica RPAR LBRACE instrucciones RBRACE','if',7,'p_if','gramatica.py',180),
  ('if_else -> IF LPAR exp_logica RPAR LBRACE instrucciones RBRACE ELSE LBRACE instrucciones RBRACE','if_else',11,'p_if_else','gramatica.py',184),
  ('exp_logica -> exp_logica AND exp_logica','exp_logica',3,'p_logica_binaria','gramatica.py',188),
  ('exp_logica -> exp_logica OR exp_logica','exp_logica',3,'p_logica_binaria','gramatica.py',189),
  ('exp_logica -> NOT exp_logica','exp_logica',2,'p_logica_not','gramatica.py',194),
  ('exp_logica -> exp_relacional','exp_logica',1,'p_logica_to_relacional','gramatica.py',198),
  ('exp_relacional -> exp_relacional LESS exp_relacional','exp_relacional',3,'p_relacional_binaria','gramatica.py',202),
  ('exp_relacional -> exp_relacional LESSEQ exp_relacional','exp_relacional',3,'p_relacional_binaria','gramatica.py',203),
  ('exp_relacional -> exp_relacional GREATHER exp_relacional','exp_relacional',3,'p_relacional_binaria','gramatica.py',204),
  ('exp_relacional -> exp_relacional GREATHEREQ exp_relacional','exp_relacional',3,'p_relacional_binaria','gramatica.py',205),
  ('exp_relacional -> exp_relacional EQUALITY exp_relacional','exp_relacional',3,'p_relacional_binaria','gramatica.py',206),
  ('exp_relacional -> exp_relacional DIFERENT exp_relacional','exp_relacional',3,'p_relacional_binaria','gramatica.py',207),
  ('exp_relacional -> exp_aritmetica','exp_relacional',1,'p_relacinal_to_aritmetica','gramatica.py',216),
  ('exp_aritmetica -> exp_aritmetica PLUS exp_aritmetica','exp_aritmetica',3,'p_aritmetica_binaria','gramatica.py',220),
  ('exp_aritmetica -> exp_aritmetica MINUS exp_aritmetica','exp_aritmetica',3,'p_aritmetica_binaria','gramatica.py',221),
  ('exp_aritmetica -> exp_aritmetica TIMES exp_aritmetica','exp_aritmetica',3,'p_aritmetica_binaria','gramatica.py',222),
  ('exp_aritmetica -> exp_aritmetica DIV exp_aritmetica','exp_aritmetica',3,'p_aritmetica_binaria','gramatica.py',223),
  ('exp_aritmetica -> exp_aritmetica POT exp_aritmetica','exp_aritmetica',3,'p_aritmetica_binaria','gramatica.py',224),
  ('exp_aritmetica -> MINUS exp_aritmetica','exp_aritmetica',2,'p_aritmetica_negativo','gramatica.py',232),
  ('exp_aritmetica -> LPAR exp_logica RPAR','exp_aritmetica',3,'p_aritmetica_agrupacion','gramatica.py',236),
  ('exp_aritmetica -> NUMBER','exp_aritmetica',1,'p_aritmetica_basico_num','gramatica.py',240),
  ('exp_aritmetica -> DECIMAL','exp_aritmetica',1,'p_aritmetica_basico_dec','gramatica.py',244),
  ('exp_aritmetica -> CHAR','exp_aritmetica',1,'p_aritmetica_basico_char','gramatica.py',248),
  ('exp_aritmetica -> STRING','exp_aritmetica',1,'p_aritmetica_basico_str','gramatica.py',252),
  ('exp_aritmetica -> TRUE','exp_aritmetica',1,'p_aritmetica_basico_true','gramatica.py',256),
  ('exp_aritmetica -> FALSE','exp_aritmetica',1,'p_aritmetica_basico_false','gramatica.py',260),
  ('exp_aritmetica -> ID','exp_aritmetica',1,'p_aritmetica_basico_id','gramatica.py',264),
]
