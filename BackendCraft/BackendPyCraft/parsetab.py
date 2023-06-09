
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANY BOOLEAN BREAK CADENA COLON COMA CONCAT CONSOLE CONTINUE DECIMAL DISTINTO_QUE DIVIDE ELSE ENTERO FOR FUNCTION IF IGUAL INTERFACE LET LITERAL LOG L_CORCHETE L_LLAVE L_PAREN MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MOD NOT NULL NUMBER OF OR POTENCIA PUNTO RETURN R_CORCHETE R_LLAVE R_PAREN SEMI_COLON SPLIT STRING TIMES TOEXPONENTIAL TOFIXED TOLOWERCASE TOSTRING TOUPPERCASE TRIPLE_IGUAL WHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : console_pro sc\n                        | declaration_instruction sc\n                        | assig_pro sc\n                        | if_pro sc\n                        | while_pro sc\n                        | for_pro sc\n                        | for_each_pro sc\n                        | sumadores scsc   : SEMI_COLON\n            |declaration_instruction      : LET declaracion_listdeclaracion_list      : declaracion_list COMA assignacion_instructiondeclaracion_list      : assignacion_instructionassignacion_instruction      : LITERAL COLON type IGUAL aassignacion_instruction      : LITERAL COLON typeassignacion_instruction      : LITERAL IGUAL atype      : NUMBER\n                 | STRING\n                 | BOOLEAN\n                 | ANY assig_pro      : LITERAL IGUAL aif_pro      : IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_proelse_pro      : ELSE IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_proelse_pro      : ELSE L_LLAVE instrucciones R_LLAVEelse_pro      : while_pro      : WHILE L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVEfor_pro      : FOR L_PAREN declaration_instruction SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE\n                    | FOR L_PAREN assig_pro SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVEfor_each_pro : FOR L_PAREN for_each_dec R_PAREN L_LLAVE instrucciones R_LLAVEfor_each_dec : LET LITERAL OF afor_each_dec : LET LITERAL COLON type OF aconsole_pro      : CONSOLE PUNTO LOG L_PAREN expresion R_PARENexpresion      : expresion COMA aexpresion      : aa      : a OR ba      : b b      : b AND c b      : c c      : NOT d c      : d  d     : d DISTINTO_QUE e\n                | d MENOR_QUE e\n                | d MENOR_IGUAL_QUE e\n                | d MAYOR_QUE e\n                | d MAYOR_IGUAL_QUE e\n                | d TRIPLE_IGUAL e  d     : e  e     : e MAS f\n                | e MENOS f  e     : f  f     : f TIMES g\n                | f DIVIDE g\n                | f MOD g\n                | f POTENCIA g f     : g f    : g PUNTO nativeFun L_PAREN expresion R_PAREN g     : ENTERO\n              | DECIMAL\n              | CADENA\n              | LITERAL g     : L_PAREN a R_PAREN sumadores     : LITERAL MAS MAS\n                          | LITERAL MENOS MENOS nativeFun    : TOSTRING\n                    | TOFIXED\n                    | TOEXPONENTIAL\n                    | TOLOWERCASE\n                    | TOUPPERCASE\n                    | SPLIT\n                    | CONCAT'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,29,30,42,43,44,45,47,48,49,50,52,53,54,55,56,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,121,122,125,128,130,132,133,136,141,142,145,147,148,154,155,156,158,159,160,162,163,164,166,167,168,169,],[12,12,-3,-13,-13,-13,-13,-13,-13,-13,-13,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,12,12,12,-35,-17,12,12,12,-28,-29,-32,-59,-25,12,12,12,12,12,12,-27,-30,-31,12,12,-28,-26,]),'LET':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,29,30,37,42,43,44,45,47,48,49,50,52,53,54,55,56,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,121,122,125,128,130,132,133,136,141,142,145,147,148,154,155,156,158,159,160,162,163,164,166,167,168,169,],[13,13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,62,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,13,13,13,-35,-17,13,13,13,-28,-29,-32,-59,-25,13,13,13,13,13,13,-27,-30,-31,13,13,-28,-26,]),'LITERAL':([0,2,3,4,5,6,7,8,9,10,11,13,18,19,20,21,22,23,24,25,26,27,29,30,32,35,36,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,91,92,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,121,122,125,126,128,129,130,131,132,133,134,135,136,141,142,145,146,147,148,154,155,156,157,158,159,160,162,163,164,166,167,168,169,],[14,14,-3,-13,-13,-13,-13,-13,-13,-13,-13,31,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,42,42,42,63,31,42,-63,-24,-39,-41,42,-43,-50,-53,-58,42,-60,-61,-62,-65,-66,94,42,-15,-18,-20,-21,-22,-23,-19,42,42,-42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,14,14,14,42,-35,42,-17,42,14,14,63,63,14,-28,-29,-32,42,-59,-25,14,14,14,42,14,14,14,-27,-30,-31,14,14,-28,-26,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,29,30,42,43,44,45,47,48,49,50,52,53,54,55,56,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,121,122,125,128,130,132,133,136,141,142,145,147,148,149,154,155,156,158,159,160,162,163,164,166,167,168,169,],[15,15,-3,-13,-13,-13,-13,-13,-13,-13,-13,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,15,15,15,-35,-17,15,15,15,-28,-29,-32,-59,-25,153,15,15,15,15,15,15,-27,-30,-31,15,15,-28,-26,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,29,30,42,43,44,45,47,48,49,50,52,53,54,55,56,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,121,122,125,128,130,132,133,136,141,142,145,147,148,154,155,156,158,159,160,162,163,164,166,167,168,169,],[16,16,-3,-13,-13,-13,-13,-13,-13,-13,-13,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,16,16,16,-35,-17,16,16,16,-28,-29,-32,-59,-25,16,16,16,16,16,16,-27,-30,-31,16,16,-28,-26,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,29,30,42,43,44,45,47,48,49,50,52,53,54,55,56,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,121,122,125,128,130,132,133,136,141,142,145,147,148,154,155,156,158,159,160,162,163,164,166,167,168,169,],[17,17,-3,-13,-13,-13,-13,-13,-13,-13,-13,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,17,17,17,-35,-17,17,17,17,-28,-29,-32,-59,-25,17,17,17,17,17,17,-27,-30,-31,17,17,-28,-26,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,29,30,42,43,44,45,47,48,49,50,52,53,54,55,56,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,128,130,141,142,145,147,148,162,163,164,168,169,],[0,-1,-3,-13,-13,-13,-13,-13,-13,-13,-13,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-35,-17,-28,-29,-32,-59,-25,-27,-30,-31,-28,-26,]),'R_LLAVE':([3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,29,30,42,43,44,45,47,48,49,50,52,53,54,55,56,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,128,130,132,133,136,141,142,145,147,148,158,159,160,162,163,164,167,168,169,],[-3,-13,-13,-13,-13,-13,-13,-13,-13,-2,-4,-12,-5,-6,-7,-8,-9,-10,-11,-14,-16,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-35,-17,141,142,145,-28,-29,-32,-59,-25,162,163,164,-27,-30,-31,168,-28,-26,]),'SEMI_COLON':([4,5,6,7,8,9,10,11,29,30,42,43,44,45,47,48,49,50,52,53,54,55,56,59,60,65,66,67,68,69,70,71,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,123,124,128,130,138,141,142,145,147,148,162,163,164,168,169,],[20,20,20,20,20,20,20,20,-14,-16,-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,-65,-66,91,92,-15,-18,-20,-21,-22,-23,-19,-42,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,134,135,-35,-17,-18,-28,-29,-32,-59,-25,-27,-30,-31,-28,-26,]),'PUNTO':([12,42,50,52,53,54,120,],[28,-63,87,-60,-61,-62,-64,]),'IGUAL':([14,31,63,66,67,68,69,70,94,138,],[32,41,32,97,-20,-21,-22,-23,41,97,]),'MAS':([14,33,42,48,49,50,52,53,54,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[33,55,-63,81,-53,-58,-60,-61,-62,81,81,81,81,81,81,-51,-52,-54,-55,-56,-57,-64,-59,]),'MENOS':([14,34,42,48,49,50,52,53,54,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[34,56,-63,82,-53,-58,-60,-61,-62,82,82,82,82,82,82,-51,-52,-54,-55,-56,-57,-64,-59,]),'L_PAREN':([15,16,17,32,35,36,38,41,46,51,64,72,73,75,76,77,78,79,80,81,82,83,84,85,86,91,92,97,112,113,114,115,116,117,118,119,126,129,131,146,153,157,],[35,36,37,51,51,51,64,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,131,-67,-68,-69,-70,-71,-72,-73,51,51,51,51,157,51,]),'LOG':([28,],[38,]),'COMA':([29,30,42,44,45,47,48,49,50,52,53,54,65,66,67,68,69,70,71,74,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,130,138,139,140,147,],[39,-16,-63,-39,-41,-43,-50,-53,-58,-60,-61,-62,-15,-18,-20,-21,-22,-23,-19,-42,129,-37,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-17,-18,-36,129,-59,]),'COLON':([31,94,],[40,127,]),'NOT':([32,35,36,41,51,64,72,73,91,92,97,126,129,131,146,157,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'ENTERO':([32,35,36,41,46,51,64,72,73,75,76,77,78,79,80,81,82,83,84,85,86,91,92,97,126,129,131,146,157,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'DECIMAL':([32,35,36,41,46,51,64,72,73,75,76,77,78,79,80,81,82,83,84,85,86,91,92,97,126,129,131,146,157,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'CADENA':([32,35,36,41,46,51,64,72,73,75,76,77,78,79,80,81,82,83,84,85,86,91,92,97,126,129,131,146,157,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'NUMBER':([40,127,],[67,67,]),'STRING':([40,127,],[68,68,]),'BOOLEAN':([40,127,],[69,69,]),'ANY':([40,127,],[70,70,]),'TIMES':([42,49,50,52,53,54,106,107,108,109,110,111,120,147,],[-63,83,-58,-60,-61,-62,83,83,-54,-55,-56,-57,-64,-59,]),'DIVIDE':([42,49,50,52,53,54,106,107,108,109,110,111,120,147,],[-63,84,-58,-60,-61,-62,84,84,-54,-55,-56,-57,-64,-59,]),'MOD':([42,49,50,52,53,54,106,107,108,109,110,111,120,147,],[-63,85,-58,-60,-61,-62,85,85,-54,-55,-56,-57,-64,-59,]),'POTENCIA':([42,49,50,52,53,54,106,107,108,109,110,111,120,147,],[-63,86,-58,-60,-61,-62,86,86,-54,-55,-56,-57,-64,-59,]),'DISTINTO_QUE':([42,47,48,49,50,52,53,54,74,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[-63,75,-50,-53,-58,-60,-61,-62,75,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-59,]),'MENOR_QUE':([42,47,48,49,50,52,53,54,74,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[-63,76,-50,-53,-58,-60,-61,-62,76,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-59,]),'MENOR_IGUAL_QUE':([42,47,48,49,50,52,53,54,74,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[-63,77,-50,-53,-58,-60,-61,-62,77,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-59,]),'MAYOR_QUE':([42,47,48,49,50,52,53,54,74,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[-63,78,-50,-53,-58,-60,-61,-62,78,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-59,]),'MAYOR_IGUAL_QUE':([42,47,48,49,50,52,53,54,74,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[-63,79,-50,-53,-58,-60,-61,-62,79,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-59,]),'TRIPLE_IGUAL':([42,47,48,49,50,52,53,54,74,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[-63,80,-50,-53,-58,-60,-61,-62,80,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-59,]),'AND':([42,44,45,47,48,49,50,52,53,54,74,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,147,],[-63,73,-41,-43,-50,-53,-58,-60,-61,-62,-42,73,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-59,]),'OR':([42,43,44,45,47,48,49,50,52,53,54,57,58,71,74,88,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,123,124,130,137,139,147,152,161,],[-63,72,-39,-41,-43,-50,-53,-58,-60,-61,-62,72,72,72,-42,72,72,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,72,72,72,72,72,-59,72,72,]),'R_PAREN':([42,43,44,45,47,48,49,50,52,53,54,57,58,61,74,88,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,120,137,139,140,143,144,147,152,161,],[-63,-24,-39,-41,-43,-50,-53,-58,-60,-61,-62,89,90,93,-42,120,128,-37,-38,-40,-44,-45,-46,-47,-48,-49,-51,-52,-54,-55,-56,-57,-64,-33,-36,147,150,151,-59,-34,165,]),'OF':([67,68,69,70,94,138,],[-20,-21,-22,-23,126,146,]),'TOSTRING':([87,],[113,]),'TOFIXED':([87,],[114,]),'TOEXPONENTIAL':([87,],[115,]),'TOLOWERCASE':([87,],[116,]),'TOUPPERCASE':([87,],[117,]),'SPLIT':([87,],[118,]),'CONCAT':([87,],[119,]),'L_LLAVE':([89,90,93,149,150,151,165,],[121,122,125,154,155,156,166,]),'ELSE':([141,168,],[149,149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,121,122,125,154,155,156,166,],[2,132,133,136,158,159,160,167,]),'instruccion':([0,2,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[3,18,3,3,3,18,18,18,3,3,3,18,18,18,3,18,]),'console_pro':([0,2,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaration_instruction':([0,2,37,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[5,5,59,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'assig_pro':([0,2,37,121,122,125,132,133,134,135,136,154,155,156,158,159,160,166,167,],[6,6,60,6,6,6,6,6,143,144,6,6,6,6,6,6,6,6,6,]),'if_pro':([0,2,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'while_pro':([0,2,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'for_pro':([0,2,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'for_each_pro':([0,2,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'sumadores':([0,2,121,122,125,132,133,136,154,155,156,158,159,160,166,167,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'sc':([4,5,6,7,8,9,10,11,],[19,21,22,23,24,25,26,27,]),'declaracion_list':([13,62,],[29,29,]),'assignacion_instruction':([13,39,62,],[30,65,30,]),'a':([32,35,36,41,51,64,91,92,97,126,129,131,146,157,],[43,57,58,71,88,96,123,124,130,137,139,96,152,161,]),'b':([32,35,36,41,51,64,72,91,92,97,126,129,131,146,157,],[44,44,44,44,44,44,98,44,44,44,44,44,44,44,44,]),'c':([32,35,36,41,51,64,72,73,91,92,97,126,129,131,146,157,],[45,45,45,45,45,45,45,99,45,45,45,45,45,45,45,45,]),'d':([32,35,36,41,46,51,64,72,73,91,92,97,126,129,131,146,157,],[47,47,47,47,74,47,47,47,47,47,47,47,47,47,47,47,47,]),'e':([32,35,36,41,46,51,64,72,73,75,76,77,78,79,80,91,92,97,126,129,131,146,157,],[48,48,48,48,48,48,48,48,48,100,101,102,103,104,105,48,48,48,48,48,48,48,48,]),'f':([32,35,36,41,46,51,64,72,73,75,76,77,78,79,80,81,82,91,92,97,126,129,131,146,157,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,106,107,49,49,49,49,49,49,49,49,]),'g':([32,35,36,41,46,51,64,72,73,75,76,77,78,79,80,81,82,83,84,85,86,91,92,97,126,129,131,146,157,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,108,109,110,111,50,50,50,50,50,50,50,50,]),'for_each_dec':([37,],[61,]),'type':([40,127,],[66,138,]),'expresion':([64,131,],[95,140,]),'nativeFun':([87,],[112,]),'else_pro':([141,168,],[148,169,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',279),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','grammar.py',283),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',290),
  ('instruccion -> console_pro sc','instruccion',2,'p_instruccion','grammar.py',297),
  ('instruccion -> declaration_instruction sc','instruccion',2,'p_instruccion','grammar.py',298),
  ('instruccion -> assig_pro sc','instruccion',2,'p_instruccion','grammar.py',299),
  ('instruccion -> if_pro sc','instruccion',2,'p_instruccion','grammar.py',300),
  ('instruccion -> while_pro sc','instruccion',2,'p_instruccion','grammar.py',301),
  ('instruccion -> for_pro sc','instruccion',2,'p_instruccion','grammar.py',302),
  ('instruccion -> for_each_pro sc','instruccion',2,'p_instruccion','grammar.py',303),
  ('instruccion -> sumadores sc','instruccion',2,'p_instruccion','grammar.py',304),
  ('sc -> SEMI_COLON','sc',1,'p_semi_colon','grammar.py',308),
  ('sc -> <empty>','sc',0,'p_semi_colon','grammar.py',309),
  ('declaration_instruction -> LET declaracion_list','declaration_instruction',2,'p_instruccion_declarationInstruction','grammar.py',314),
  ('declaracion_list -> declaracion_list COMA assignacion_instruction','declaracion_list',3,'p_instruccion_declaracion_list','grammar.py',318),
  ('declaracion_list -> assignacion_instruction','declaracion_list',1,'p_instruccion_declaracion_list2','grammar.py',322),
  ('assignacion_instruction -> LITERAL COLON type IGUAL a','assignacion_instruction',5,'p_instruccion_assignacion_instruction','grammar.py',327),
  ('assignacion_instruction -> LITERAL COLON type','assignacion_instruction',3,'p_instruccion_assingnacion_instruction2','grammar.py',331),
  ('assignacion_instruction -> LITERAL IGUAL a','assignacion_instruction',3,'p_instruccion_assignacion_instruction3','grammar.py',335),
  ('type -> NUMBER','type',1,'p_instruccion_type','grammar.py',338),
  ('type -> STRING','type',1,'p_instruccion_type','grammar.py',339),
  ('type -> BOOLEAN','type',1,'p_instruccion_type','grammar.py',340),
  ('type -> ANY','type',1,'p_instruccion_type','grammar.py',341),
  ('assig_pro -> LITERAL IGUAL a','assig_pro',3,'p_instruccion_assig_pro','grammar.py',345),
  ('if_pro -> IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro','if_pro',8,'p_instruccion_if_pro','grammar.py',349),
  ('else_pro -> ELSE IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro','else_pro',9,'p_instruccion_else_pro','grammar.py',355),
  ('else_pro -> ELSE L_LLAVE instrucciones R_LLAVE','else_pro',4,'p_instruccion_else_pro2','grammar.py',359),
  ('else_pro -> <empty>','else_pro',0,'p_instruccion_else_pro3','grammar.py',363),
  ('while_pro -> WHILE L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE','while_pro',7,'p_instruccion_while_pro','grammar.py',368),
  ('for_pro -> FOR L_PAREN declaration_instruction SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE','for_pro',11,'p_instruccion_for_pro','grammar.py',373),
  ('for_pro -> FOR L_PAREN assig_pro SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE','for_pro',11,'p_instruccion_for_pro','grammar.py',374),
  ('for_each_pro -> FOR L_PAREN for_each_dec R_PAREN L_LLAVE instrucciones R_LLAVE','for_each_pro',7,'p_instruccion_for_each_pro','grammar.py',381),
  ('for_each_dec -> LET LITERAL OF a','for_each_dec',4,'p_instruccion_fore_dec','grammar.py',384),
  ('for_each_dec -> LET LITERAL COLON type OF a','for_each_dec',6,'p_instruccion_fore_dec_type','grammar.py',387),
  ('console_pro -> CONSOLE PUNTO LOG L_PAREN expresion R_PAREN','console_pro',6,'p_instruccion_console','grammar.py',392),
  ('expresion -> expresion COMA a','expresion',3,'p_instruccion_expresion','grammar.py',397),
  ('expresion -> a','expresion',1,'p_instruccion_expresion2','grammar.py',400),
  ('a -> a OR b','a',3,'p_instruccion_expresion3','grammar.py',405),
  ('a -> b','a',1,'p_instruccion_expresion4','grammar.py',408),
  ('b -> b AND c','b',3,'p_instruccion_expresion5','grammar.py',412),
  ('b -> c','b',1,'p_instruccion_expresion6','grammar.py',416),
  ('c -> NOT d','c',2,'p_instruccion_expresion7','grammar.py',420),
  ('c -> d','c',1,'p_instruccion_expresion8','grammar.py',424),
  ('d -> d DISTINTO_QUE e','d',3,'p_instruccion_expresion9','grammar.py',428),
  ('d -> d MENOR_QUE e','d',3,'p_instruccion_expresion9','grammar.py',429),
  ('d -> d MENOR_IGUAL_QUE e','d',3,'p_instruccion_expresion9','grammar.py',430),
  ('d -> d MAYOR_QUE e','d',3,'p_instruccion_expresion9','grammar.py',431),
  ('d -> d MAYOR_IGUAL_QUE e','d',3,'p_instruccion_expresion9','grammar.py',432),
  ('d -> d TRIPLE_IGUAL e','d',3,'p_instruccion_expresion9','grammar.py',433),
  ('d -> e','d',1,'p_instruccion_expresion10','grammar.py',437),
  ('e -> e MAS f','e',3,'p_instruccion_expresion11','grammar.py',441),
  ('e -> e MENOS f','e',3,'p_instruccion_expresion11','grammar.py',442),
  ('e -> f','e',1,'p_instruccion_expresion12','grammar.py',446),
  ('f -> f TIMES g','f',3,'p_instruccion_expresion13','grammar.py',450),
  ('f -> f DIVIDE g','f',3,'p_instruccion_expresion13','grammar.py',451),
  ('f -> f MOD g','f',3,'p_instruccion_expresion13','grammar.py',452),
  ('f -> f POTENCIA g','f',3,'p_instruccion_expresion13','grammar.py',453),
  ('f -> g','f',1,'p_instruccion_expresion14','grammar.py',457),
  ('f -> g PUNTO nativeFun L_PAREN expresion R_PAREN','f',6,'p_instruccion_expresion15','grammar.py',461),
  ('g -> ENTERO','g',1,'p_instruccion_expresion16','grammar.py',464),
  ('g -> DECIMAL','g',1,'p_instruccion_expresion16','grammar.py',465),
  ('g -> CADENA','g',1,'p_instruccion_expresion16','grammar.py',466),
  ('g -> LITERAL','g',1,'p_instruccion_expresion16','grammar.py',467),
  ('g -> L_PAREN a R_PAREN','g',3,'p_instruccion_expresion17','grammar.py',471),
  ('sumadores -> LITERAL MAS MAS','sumadores',3,'p_instruccion_sumadores','grammar.py',476),
  ('sumadores -> LITERAL MENOS MENOS','sumadores',3,'p_instruccion_sumadores','grammar.py',477),
  ('nativeFun -> TOSTRING','nativeFun',1,'p_instruccion_nativas','grammar.py',486),
  ('nativeFun -> TOFIXED','nativeFun',1,'p_instruccion_nativas','grammar.py',487),
  ('nativeFun -> TOEXPONENTIAL','nativeFun',1,'p_instruccion_nativas','grammar.py',488),
  ('nativeFun -> TOLOWERCASE','nativeFun',1,'p_instruccion_nativas','grammar.py',489),
  ('nativeFun -> TOUPPERCASE','nativeFun',1,'p_instruccion_nativas','grammar.py',490),
  ('nativeFun -> SPLIT','nativeFun',1,'p_instruccion_nativas','grammar.py',491),
  ('nativeFun -> CONCAT','nativeFun',1,'p_instruccion_nativas','grammar.py',492),
]
