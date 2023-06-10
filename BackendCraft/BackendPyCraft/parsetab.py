
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANY BOOLEAN BREAK CADENA COLON COMA CONCAT CONSOLE CONTINUE DECIMAL DISTINTO_QUE DIVIDE ELSE ENTERO FOR FUNCTION IF IGUAL INTERFACE LET LITERAL LOG L_CORCHETE L_LLAVE L_PAREN MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MOD NOT NULL NUMBER OF OR POTENCIA PUNTO RETURN R_CORCHETE R_LLAVE R_PAREN SEMI_COLON SPLIT STRING TIMES TOEXPONENTIAL TOFIXED TOLOWERCASE TOSTRING TOUPPERCASE TRIPLE_IGUAL WHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : console_pro sc\n                        | declaration_instruction sc\n                        | assig_pro sc\n                        | if_pro sc\n                        | while_pro sc\n                        | for_pro sc\n                        | for_each_pro sc\n                        | interface_pro sc\n                        | continue_pro sc\n                        | break_pro sc\n                        | return_pro sc\n                        | function_pro sc\n                        | call_function_pro sc\n                        | sumadores scsc   : SEMI_COLON\n            |function_pro : FUNCTION LITERAL L_PAREN parameters_pro R_PAREN L_LLAVE instrucciones R_LLAVEfunction_pro : FUNCTION LITERAL L_PAREN R_PAREN L_LLAVE instrucciones R_LLAVEcall_function_pro    : LITERAL L_PAREN values R_PARENcall_function_pro    : LITERAL L_PAREN R_PARENvalues   : values COMA avalues   : aparameters_pro   : parameters_pro COMA parameter_proparameters_pro   : parameter_proparameter_pro    : LITERAL COLON typeparameter_pro    : LITERALcontinue_pro : CONTINUEbreak_pro : BREAKreturn_pro : RETURNreturn_pro : RETURN ainterface_pro    : INTERFACE LITERAL L_LLAVE interface_atributos R_LLAVEinterface_atributos  : interface_atributos interface_atributo scinterface_atributos  : interface_atributo   : LITERAL COLON typeinterface_atributo   : LITERALdeclaration_instruction      : LET declaracion_listdeclaracion_list      : declaracion_list COMA assignacion_instructiondeclaracion_list      : assignacion_instructionassignacion_instruction      : LITERAL COLON type IGUAL aassignacion_instruction      : LITERAL COLON typeassignacion_instruction      : LITERAL IGUAL atype      : NUMBER\n                 | STRING\n                 | BOOLEAN\n                 | ANY\n                 | LITERALassig_pro      : LITERAL IGUAL aif_pro      : IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_proelse_pro      : ELSE IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_proelse_pro      : ELSE L_LLAVE instrucciones R_LLAVEelse_pro      : while_pro      : WHILE L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVEfor_pro      : FOR L_PAREN declaration_instruction SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE\n                    | FOR L_PAREN assig_pro SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVEfor_each_pro : FOR L_PAREN for_each_dec R_PAREN L_LLAVE instrucciones R_LLAVEfor_each_dec : LET LITERAL OF afor_each_dec : LET LITERAL COLON type OF aconsole_pro      : CONSOLE PUNTO LOG L_PAREN expresion R_PARENexpresion      : expresion COMA aexpresion      : aa      : a OR ba      : b b      : b AND c b      : c c      : NOT d c      : d  d     : d DISTINTO_QUE e\n                | d MENOR_QUE e\n                | d MENOR_IGUAL_QUE e\n                | d MAYOR_QUE e\n                | d MAYOR_IGUAL_QUE e\n                | d TRIPLE_IGUAL e  d     : e  e     : e MAS f\n                | e MENOS f  e     : f  f     : f TIMES g\n                | f DIVIDE g\n                | f MOD g\n                | f POTENCIA g f     : g f    : g PUNTO nativeFun L_PAREN expresion R_PAREN\n            | g PUNTO nativeFun L_PAREN R_PAREN g     : ENTERO\n              | DECIMAL\n              | CADENA\n              | LITERAL\n              | call_function_pro\n              | array_pro\n              | interface_assi g     : L_PAREN a R_PAREN sumadores     : LITERAL MAS MAS\n                          | LITERAL MENOS MENOS interface_assi   : L_LLAVE atributos_assi R_LLAVEatributos_assi   : atributos_assi COMA LITERAL COLON aatributos_assi   : LITERAL COLON aarray_pro    : L_CORCHETE values R_CORCHETEnativeFun    : TOSTRING\n                    | TOFIXED\n                    | TOEXPONENTIAL\n                    | TOLOWERCASE\n                    | TOUPPERCASE\n                    | SPLIT\n                    | CONCAT'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[18,18,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,18,18,18,-34,18,-61,-42,18,18,18,-86,18,18,-54,-55,-58,-85,18,-21,-51,-20,18,18,18,18,18,18,-53,-56,-57,18,18,-54,-52,]),'LET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,55,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[19,19,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,91,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,19,19,19,-34,19,-61,-42,19,19,19,-86,19,19,-54,-55,-58,-85,19,-21,-51,-20,19,19,19,19,19,19,-53,-56,-57,19,19,-54,-52,]),'LITERAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,49,50,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,80,82,84,85,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,114,115,116,117,118,119,120,121,122,123,124,125,128,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,158,159,166,168,169,172,173,174,175,176,177,178,181,183,184,185,186,187,188,189,190,191,192,195,196,198,199,201,203,205,206,209,210,211,212,214,215,216,221,223,224,225,226,227,228,229,231,232,233,235,236,237,238,],[20,20,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,48,56,-30,-31,69,75,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,69,69,69,69,92,-33,-65,-67,69,-69,-76,-79,-84,69,-87,-88,-89,-90,-91,-92,-93,69,113,48,117,69,-50,-23,-95,-96,131,-36,69,69,-68,69,69,69,69,69,69,69,69,69,69,69,69,160,69,-40,-49,-43,-45,-46,-47,-48,-44,-22,69,69,69,175,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,179,69,69,20,20,20,69,117,-38,-34,-19,69,117,160,20,-61,69,-42,20,20,92,92,20,117,-35,-86,69,20,20,-54,-55,-58,69,-37,-85,20,-21,-51,-20,20,20,20,69,20,20,20,-53,-56,-57,20,20,-54,-52,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,217,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[21,21,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,21,21,21,-34,21,-61,-42,21,21,21,-86,21,21,-54,-55,-58,-85,21,-21,-51,222,-20,21,21,21,21,21,21,-53,-56,-57,21,21,-54,-52,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[22,22,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,22,22,22,-34,22,-61,-42,22,22,22,-86,22,22,-54,-55,-58,-85,22,-21,-51,-20,22,22,22,22,22,22,-53,-56,-57,22,22,-54,-52,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[23,23,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,23,23,23,-34,23,-61,-42,23,23,23,-86,23,23,-54,-55,-58,-85,23,-21,-51,-20,23,23,23,23,23,23,-53,-56,-57,23,23,-54,-52,]),'INTERFACE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[24,24,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,24,24,24,-34,24,-61,-42,24,24,24,-86,24,24,-54,-55,-58,-85,24,-21,-51,-20,24,24,24,24,24,24,-53,-56,-57,24,24,-54,-52,]),'CONTINUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[25,25,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,25,25,25,-34,25,-61,-42,25,25,25,-86,25,25,-54,-55,-58,-85,25,-21,-51,-20,25,25,25,25,25,25,-53,-56,-57,25,25,-54,-52,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[26,26,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,26,26,26,-34,26,-61,-42,26,26,26,-86,26,26,-54,-55,-58,-85,26,-21,-51,-20,26,26,26,26,26,26,-53,-56,-57,26,26,-54,-52,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[27,27,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,27,27,27,-34,27,-61,-42,27,27,27,-86,27,27,-54,-55,-58,-85,27,-21,-51,-20,27,27,27,27,27,27,-53,-56,-57,27,27,-54,-52,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,168,169,172,176,184,185,187,188,189,192,198,201,203,205,206,209,212,214,215,216,221,223,224,225,227,228,229,231,232,233,235,236,237,238,],[28,28,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,28,28,28,-34,28,-61,-42,28,28,28,-86,28,28,-54,-55,-58,-85,28,-21,-51,-20,28,28,28,28,28,28,-53,-56,-57,28,28,-54,-52,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,176,185,187,198,205,206,209,212,215,216,221,231,232,233,237,238,],[0,-1,-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-34,-61,-42,-86,-54,-55,-58,-85,-21,-51,-20,-53,-56,-57,-54,-52,]),'R_LLAVE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,93,96,112,116,117,118,119,120,121,122,123,124,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,175,176,177,180,185,187,188,189,192,196,198,203,205,206,209,211,212,213,214,215,216,221,227,228,229,231,232,233,236,237,238,],[-3,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-30,-31,-32,-2,-4,-18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,-36,-68,157,-40,-49,-43,-45,-46,-47,-48,-44,-22,176,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-38,-34,-19,-99,-61,-42,205,206,209,-35,-86,215,-54,-55,-58,-37,-85,-98,221,-21,-51,-20,231,232,233,-53,-56,-57,237,-54,-52,]),'SEMI_COLON':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,26,27,46,47,57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,84,85,88,89,96,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,170,171,175,176,177,185,187,194,198,205,206,209,211,212,215,216,221,231,232,233,237,238,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,-30,-31,-32,-39,-41,-33,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,-23,-95,-96,128,129,-68,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,190,191,-38,-34,31,-61,-42,-43,-86,-54,-55,-58,-37,-85,-21,-51,-20,-53,-56,-57,-54,-52,]),'PUNTO':([18,64,66,67,68,69,70,71,72,82,124,155,156,157,],[45,109,-87,-88,-89,-90,-91,-92,-93,-23,-22,-94,-100,-97,]),'IGUAL':([20,48,92,117,118,119,120,121,122,131,194,],[49,79,49,-49,166,-45,-46,-47,-48,79,166,]),'L_PAREN':([20,21,22,23,27,49,50,53,54,60,65,69,73,75,76,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,147,148,149,150,151,152,153,154,159,166,173,178,186,199,210,222,226,],[50,53,54,55,65,65,65,65,65,65,65,50,65,114,115,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,178,-101,-102,-103,-104,-105,-106,-107,65,65,65,65,65,65,65,226,65,]),'MAS':([20,51,62,63,64,66,67,68,69,70,71,72,82,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[51,84,103,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,-22,103,103,103,103,103,103,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'MENOS':([20,52,62,63,64,66,67,68,69,70,71,72,82,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[52,85,104,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,-22,104,104,104,104,104,104,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'NOT':([27,49,50,53,54,65,73,79,94,95,115,125,128,129,159,166,173,178,186,199,210,226,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'ENTERO':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,173,178,186,199,210,226,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'DECIMAL':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,173,178,186,199,210,226,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'CADENA':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,173,178,186,199,210,226,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'L_CORCHETE':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,173,178,186,199,210,226,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'L_LLAVE':([27,49,50,53,54,56,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,126,127,128,129,130,159,162,166,173,178,182,186,199,210,217,218,219,226,234,],[74,74,74,74,74,93,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,168,169,74,74,172,74,184,74,74,74,201,74,74,74,223,224,225,74,235,]),'LOG':([45,],[76,]),'COMA':([46,47,58,59,61,62,63,64,66,67,68,69,70,71,72,81,82,83,96,111,112,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,160,161,163,164,165,167,180,187,194,197,198,200,202,204,212,213,],[77,-41,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,125,-23,-25,-68,125,158,-40,-49,-43,-45,-46,-47,-48,-44,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-29,183,-27,186,-63,-24,-99,-42,-43,186,-86,-28,-26,-62,-85,-98,]),'COLON':([48,113,131,160,175,179,],[78,159,174,181,195,199,]),'R_PAREN':([50,58,59,61,62,63,64,66,67,68,69,70,71,72,80,81,82,83,86,87,90,96,110,114,117,119,120,121,122,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,160,161,163,164,165,167,178,193,197,198,200,202,204,207,208,212,220,230,],[82,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-50,124,-23,-25,126,127,130,-68,155,162,-49,-45,-46,-47,-48,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-29,182,-27,185,-63,-24,198,-59,212,-86,-28,-26,-62,218,219,-85,-60,234,]),'OR':([57,58,59,61,62,63,64,66,67,68,69,70,71,72,80,82,83,86,87,96,110,123,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,165,167,170,171,180,187,193,198,204,212,213,220,230,],[94,-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,94,-23,94,94,94,-68,94,94,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,94,94,94,94,94,94,94,-86,94,-85,94,94,94,]),'R_CORCHETE':([58,59,61,62,63,64,66,67,68,69,70,71,72,82,83,96,111,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,167,198,212,],[-65,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,-25,-68,156,-22,-64,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-24,-86,-85,]),'AND':([58,59,61,62,63,64,66,67,68,69,70,71,72,82,96,124,133,134,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[95,-67,-69,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,-68,-22,95,-66,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'DISTINTO_QUE':([61,62,63,64,66,67,68,69,70,71,72,82,96,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[97,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,97,-22,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'MENOR_QUE':([61,62,63,64,66,67,68,69,70,71,72,82,96,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[98,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,98,-22,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'MENOR_IGUAL_QUE':([61,62,63,64,66,67,68,69,70,71,72,82,96,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[99,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,99,-22,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'MAYOR_QUE':([61,62,63,64,66,67,68,69,70,71,72,82,96,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[100,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,100,-22,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'MAYOR_IGUAL_QUE':([61,62,63,64,66,67,68,69,70,71,72,82,96,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[101,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,101,-22,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'TRIPLE_IGUAL':([61,62,63,64,66,67,68,69,70,71,72,82,96,124,135,136,137,138,139,140,141,142,143,144,145,146,155,156,157,198,212,],[102,-76,-79,-84,-87,-88,-89,-90,-91,-92,-93,-23,102,-22,-70,-71,-72,-73,-74,-75,-77,-78,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'TIMES':([63,64,66,67,68,69,70,71,72,82,124,141,142,143,144,145,146,155,156,157,198,212,],[105,-84,-87,-88,-89,-90,-91,-92,-93,-23,-22,105,105,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'DIVIDE':([63,64,66,67,68,69,70,71,72,82,124,141,142,143,144,145,146,155,156,157,198,212,],[106,-84,-87,-88,-89,-90,-91,-92,-93,-23,-22,106,106,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'MOD':([63,64,66,67,68,69,70,71,72,82,124,141,142,143,144,145,146,155,156,157,198,212,],[107,-84,-87,-88,-89,-90,-91,-92,-93,-23,-22,107,107,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'POTENCIA':([63,64,66,67,68,69,70,71,72,82,124,141,142,143,144,145,146,155,156,157,198,212,],[108,-84,-87,-88,-89,-90,-91,-92,-93,-23,-22,108,108,-80,-81,-82,-83,-94,-100,-97,-86,-85,]),'NUMBER':([78,174,181,195,],[119,119,119,119,]),'STRING':([78,174,181,195,],[120,120,120,120,]),'BOOLEAN':([78,174,181,195,],[121,121,121,121,]),'ANY':([78,174,181,195,],[122,122,122,122,]),'TOSTRING':([109,],[148,]),'TOFIXED':([109,],[149,]),'TOEXPONENTIAL':([109,],[150,]),'TOLOWERCASE':([109,],[151,]),'TOUPPERCASE':([109,],[152,]),'SPLIT':([109,],[153,]),'CONCAT':([109,],[154,]),'OF':([117,119,120,121,122,131,194,],[-49,-45,-46,-47,-48,173,210,]),'ELSE':([205,237,],[217,217,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,168,169,172,184,201,223,224,225,235,],[2,188,189,192,203,214,227,228,229,236,]),'instruccion':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[3,29,3,3,3,3,29,29,29,3,29,29,3,3,3,29,29,29,3,29,]),'console_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaration_instruction':([0,2,55,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[5,5,88,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'assig_pro':([0,2,55,168,169,172,184,188,189,190,191,192,201,203,214,223,224,225,227,228,229,235,236,],[6,6,89,6,6,6,6,6,6,207,208,6,6,6,6,6,6,6,6,6,6,6,6,]),'if_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'while_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'for_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'for_each_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'interface_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'continue_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'break_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'return_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'function_pro':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'call_function_pro':([0,2,27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,168,169,172,173,178,184,186,188,189,192,199,201,203,210,214,223,224,225,226,227,228,229,235,236,],[16,16,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,16,16,16,70,70,16,70,16,16,16,70,16,16,70,16,16,16,16,70,16,16,16,16,16,]),'sumadores':([0,2,168,169,172,184,188,189,192,201,203,214,223,224,225,227,228,229,235,236,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'sc':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,177,],[30,32,33,34,35,36,37,38,39,40,41,42,43,44,196,]),'declaracion_list':([19,91,],[46,46,]),'assignacion_instruction':([19,77,91,],[47,116,47,]),'a':([27,49,50,53,54,65,73,79,115,125,128,129,159,166,173,178,186,199,210,226,],[57,80,83,86,87,110,83,123,165,167,170,171,180,187,193,165,204,213,220,230,]),'b':([27,49,50,53,54,65,73,79,94,115,125,128,129,159,166,173,178,186,199,210,226,],[58,58,58,58,58,58,58,58,133,58,58,58,58,58,58,58,58,58,58,58,58,]),'c':([27,49,50,53,54,65,73,79,94,95,115,125,128,129,159,166,173,178,186,199,210,226,],[59,59,59,59,59,59,59,59,59,134,59,59,59,59,59,59,59,59,59,59,59,59,]),'d':([27,49,50,53,54,60,65,73,79,94,95,115,125,128,129,159,166,173,178,186,199,210,226,],[61,61,61,61,61,96,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'e':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,115,125,128,129,159,166,173,178,186,199,210,226,],[62,62,62,62,62,62,62,62,62,62,62,135,136,137,138,139,140,62,62,62,62,62,62,62,62,62,62,62,62,]),'f':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,115,125,128,129,159,166,173,178,186,199,210,226,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,141,142,63,63,63,63,63,63,63,63,63,63,63,63,]),'g':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,173,178,186,199,210,226,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,143,144,145,146,64,64,64,64,64,64,64,64,64,64,64,64,]),'array_pro':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,173,178,186,199,210,226,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'interface_assi':([27,49,50,53,54,60,65,73,79,94,95,97,98,99,100,101,102,103,104,105,106,107,108,115,125,128,129,159,166,173,178,186,199,210,226,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'values':([50,73,],[81,111,]),'for_each_dec':([55,],[90,]),'atributos_assi':([74,],[112,]),'type':([78,174,181,195,],[118,194,200,211,]),'interface_atributos':([93,],[132,]),'nativeFun':([109,],[147,]),'parameters_pro':([114,],[161,]),'parameter_pro':([114,183,],[163,202,]),'expresion':([115,178,],[164,197,]),'interface_atributo':([132,],[177,]),'else_pro':([205,237,],[216,238,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',285),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','grammar.py',289),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',296),
  ('instruccion -> console_pro sc','instruccion',2,'p_instruccion','grammar.py',303),
  ('instruccion -> declaration_instruction sc','instruccion',2,'p_instruccion','grammar.py',304),
  ('instruccion -> assig_pro sc','instruccion',2,'p_instruccion','grammar.py',305),
  ('instruccion -> if_pro sc','instruccion',2,'p_instruccion','grammar.py',306),
  ('instruccion -> while_pro sc','instruccion',2,'p_instruccion','grammar.py',307),
  ('instruccion -> for_pro sc','instruccion',2,'p_instruccion','grammar.py',308),
  ('instruccion -> for_each_pro sc','instruccion',2,'p_instruccion','grammar.py',309),
  ('instruccion -> interface_pro sc','instruccion',2,'p_instruccion','grammar.py',310),
  ('instruccion -> continue_pro sc','instruccion',2,'p_instruccion','grammar.py',311),
  ('instruccion -> break_pro sc','instruccion',2,'p_instruccion','grammar.py',312),
  ('instruccion -> return_pro sc','instruccion',2,'p_instruccion','grammar.py',313),
  ('instruccion -> function_pro sc','instruccion',2,'p_instruccion','grammar.py',314),
  ('instruccion -> call_function_pro sc','instruccion',2,'p_instruccion','grammar.py',315),
  ('instruccion -> sumadores sc','instruccion',2,'p_instruccion','grammar.py',316),
  ('sc -> SEMI_COLON','sc',1,'p_semi_colon','grammar.py',320),
  ('sc -> <empty>','sc',0,'p_semi_colon','grammar.py',321),
  ('function_pro -> FUNCTION LITERAL L_PAREN parameters_pro R_PAREN L_LLAVE instrucciones R_LLAVE','function_pro',8,'p_instruccion_function','grammar.py',326),
  ('function_pro -> FUNCTION LITERAL L_PAREN R_PAREN L_LLAVE instrucciones R_LLAVE','function_pro',7,'p_instruccion_function2','grammar.py',330),
  ('call_function_pro -> LITERAL L_PAREN values R_PAREN','call_function_pro',4,'p_instruccion_call_function','grammar.py',335),
  ('call_function_pro -> LITERAL L_PAREN R_PAREN','call_function_pro',3,'p_instruccion_call_function2','grammar.py',339),
  ('values -> values COMA a','values',3,'p_instruccion_values','grammar.py',349),
  ('values -> a','values',1,'p_instruccion_values2','grammar.py',352),
  ('parameters_pro -> parameters_pro COMA parameter_pro','parameters_pro',3,'p_instruccion_parameters','grammar.py',357),
  ('parameters_pro -> parameter_pro','parameters_pro',1,'p_instruccion_parameters2','grammar.py',360),
  ('parameter_pro -> LITERAL COLON type','parameter_pro',3,'p_instruccion_parameter','grammar.py',364),
  ('parameter_pro -> LITERAL','parameter_pro',1,'p_instruccion_parameter2','grammar.py',367),
  ('continue_pro -> CONTINUE','continue_pro',1,'p_instruccion_continue','grammar.py',372),
  ('break_pro -> BREAK','break_pro',1,'p_instruccion_break','grammar.py',376),
  ('return_pro -> RETURN','return_pro',1,'p_instruccion_return','grammar.py',379),
  ('return_pro -> RETURN a','return_pro',2,'p_instruccion_return2','grammar.py',383),
  ('interface_pro -> INTERFACE LITERAL L_LLAVE interface_atributos R_LLAVE','interface_pro',5,'p_instruccion_declarationInterface','grammar.py',389),
  ('interface_atributos -> interface_atributos interface_atributo sc','interface_atributos',3,'p_instruccion_interfaceAtributos','grammar.py',393),
  ('interface_atributos -> <empty>','interface_atributos',0,'p_instruccion_interfaceAtributos2','grammar.py',396),
  ('interface_atributo -> LITERAL COLON type','interface_atributo',3,'p_intruccion_interfaceAtributo','grammar.py',399),
  ('interface_atributo -> LITERAL','interface_atributo',1,'p_instruccion_interfaceAtributo2','grammar.py',402),
  ('declaration_instruction -> LET declaracion_list','declaration_instruction',2,'p_instruccion_declarationInstruction','grammar.py',406),
  ('declaracion_list -> declaracion_list COMA assignacion_instruction','declaracion_list',3,'p_instruccion_declaracion_list','grammar.py',410),
  ('declaracion_list -> assignacion_instruction','declaracion_list',1,'p_instruccion_declaracion_list2','grammar.py',414),
  ('assignacion_instruction -> LITERAL COLON type IGUAL a','assignacion_instruction',5,'p_instruccion_assignacion_instruction','grammar.py',419),
  ('assignacion_instruction -> LITERAL COLON type','assignacion_instruction',3,'p_instruccion_assingnacion_instruction2','grammar.py',423),
  ('assignacion_instruction -> LITERAL IGUAL a','assignacion_instruction',3,'p_instruccion_assignacion_instruction3','grammar.py',427),
  ('type -> NUMBER','type',1,'p_instruccion_type','grammar.py',430),
  ('type -> STRING','type',1,'p_instruccion_type','grammar.py',431),
  ('type -> BOOLEAN','type',1,'p_instruccion_type','grammar.py',432),
  ('type -> ANY','type',1,'p_instruccion_type','grammar.py',433),
  ('type -> LITERAL','type',1,'p_instruccion_type','grammar.py',434),
  ('assig_pro -> LITERAL IGUAL a','assig_pro',3,'p_instruccion_assig_pro','grammar.py',438),
  ('if_pro -> IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro','if_pro',8,'p_instruccion_if_pro','grammar.py',442),
  ('else_pro -> ELSE IF L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE else_pro','else_pro',9,'p_instruccion_else_pro','grammar.py',448),
  ('else_pro -> ELSE L_LLAVE instrucciones R_LLAVE','else_pro',4,'p_instruccion_else_pro2','grammar.py',452),
  ('else_pro -> <empty>','else_pro',0,'p_instruccion_else_pro3','grammar.py',456),
  ('while_pro -> WHILE L_PAREN a R_PAREN L_LLAVE instrucciones R_LLAVE','while_pro',7,'p_instruccion_while_pro','grammar.py',461),
  ('for_pro -> FOR L_PAREN declaration_instruction SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE','for_pro',11,'p_instruccion_for_pro','grammar.py',466),
  ('for_pro -> FOR L_PAREN assig_pro SEMI_COLON a SEMI_COLON assig_pro R_PAREN L_LLAVE instrucciones R_LLAVE','for_pro',11,'p_instruccion_for_pro','grammar.py',467),
  ('for_each_pro -> FOR L_PAREN for_each_dec R_PAREN L_LLAVE instrucciones R_LLAVE','for_each_pro',7,'p_instruccion_for_each_pro','grammar.py',474),
  ('for_each_dec -> LET LITERAL OF a','for_each_dec',4,'p_instruccion_fore_dec','grammar.py',477),
  ('for_each_dec -> LET LITERAL COLON type OF a','for_each_dec',6,'p_instruccion_fore_dec_type','grammar.py',480),
  ('console_pro -> CONSOLE PUNTO LOG L_PAREN expresion R_PAREN','console_pro',6,'p_instruccion_console','grammar.py',485),
  ('expresion -> expresion COMA a','expresion',3,'p_instruccion_expresion','grammar.py',490),
  ('expresion -> a','expresion',1,'p_instruccion_expresion2','grammar.py',493),
  ('a -> a OR b','a',3,'p_instruccion_expresion3','grammar.py',498),
  ('a -> b','a',1,'p_instruccion_expresion4','grammar.py',501),
  ('b -> b AND c','b',3,'p_instruccion_expresion5','grammar.py',505),
  ('b -> c','b',1,'p_instruccion_expresion6','grammar.py',509),
  ('c -> NOT d','c',2,'p_instruccion_expresion7','grammar.py',513),
  ('c -> d','c',1,'p_instruccion_expresion8','grammar.py',517),
  ('d -> d DISTINTO_QUE e','d',3,'p_instruccion_expresion9','grammar.py',521),
  ('d -> d MENOR_QUE e','d',3,'p_instruccion_expresion9','grammar.py',522),
  ('d -> d MENOR_IGUAL_QUE e','d',3,'p_instruccion_expresion9','grammar.py',523),
  ('d -> d MAYOR_QUE e','d',3,'p_instruccion_expresion9','grammar.py',524),
  ('d -> d MAYOR_IGUAL_QUE e','d',3,'p_instruccion_expresion9','grammar.py',525),
  ('d -> d TRIPLE_IGUAL e','d',3,'p_instruccion_expresion9','grammar.py',526),
  ('d -> e','d',1,'p_instruccion_expresion10','grammar.py',530),
  ('e -> e MAS f','e',3,'p_instruccion_expresion11','grammar.py',534),
  ('e -> e MENOS f','e',3,'p_instruccion_expresion11','grammar.py',535),
  ('e -> f','e',1,'p_instruccion_expresion12','grammar.py',539),
  ('f -> f TIMES g','f',3,'p_instruccion_expresion13','grammar.py',543),
  ('f -> f DIVIDE g','f',3,'p_instruccion_expresion13','grammar.py',544),
  ('f -> f MOD g','f',3,'p_instruccion_expresion13','grammar.py',545),
  ('f -> f POTENCIA g','f',3,'p_instruccion_expresion13','grammar.py',546),
  ('f -> g','f',1,'p_instruccion_expresion14','grammar.py',550),
  ('f -> g PUNTO nativeFun L_PAREN expresion R_PAREN','f',6,'p_instruccion_expresion15','grammar.py',554),
  ('f -> g PUNTO nativeFun L_PAREN R_PAREN','f',5,'p_instruccion_expresion15','grammar.py',555),
  ('g -> ENTERO','g',1,'p_instruccion_expresion16','grammar.py',562),
  ('g -> DECIMAL','g',1,'p_instruccion_expresion16','grammar.py',563),
  ('g -> CADENA','g',1,'p_instruccion_expresion16','grammar.py',564),
  ('g -> LITERAL','g',1,'p_instruccion_expresion16','grammar.py',565),
  ('g -> call_function_pro','g',1,'p_instruccion_expresion16','grammar.py',566),
  ('g -> array_pro','g',1,'p_instruccion_expresion16','grammar.py',567),
  ('g -> interface_assi','g',1,'p_instruccion_expresion16','grammar.py',568),
  ('g -> L_PAREN a R_PAREN','g',3,'p_instruccion_expresion17','grammar.py',572),
  ('sumadores -> LITERAL MAS MAS','sumadores',3,'p_instruccion_sumadores','grammar.py',577),
  ('sumadores -> LITERAL MENOS MENOS','sumadores',3,'p_instruccion_sumadores','grammar.py',578),
  ('interface_assi -> L_LLAVE atributos_assi R_LLAVE','interface_assi',3,'p_instruccion_interfaceAssi','grammar.py',587),
  ('atributos_assi -> atributos_assi COMA LITERAL COLON a','atributos_assi',5,'p_instruccion_inter_atributesAssi','grammar.py',592),
  ('atributos_assi -> LITERAL COLON a','atributos_assi',3,'p_instruccion_inter_atributesAssi2','grammar.py',595),
  ('array_pro -> L_CORCHETE values R_CORCHETE','array_pro',3,'p_instruccion_array_pro','grammar.py',599),
  ('nativeFun -> TOSTRING','nativeFun',1,'p_instruccion_nativas','grammar.py',606),
  ('nativeFun -> TOFIXED','nativeFun',1,'p_instruccion_nativas','grammar.py',607),
  ('nativeFun -> TOEXPONENTIAL','nativeFun',1,'p_instruccion_nativas','grammar.py',608),
  ('nativeFun -> TOLOWERCASE','nativeFun',1,'p_instruccion_nativas','grammar.py',609),
  ('nativeFun -> TOUPPERCASE','nativeFun',1,'p_instruccion_nativas','grammar.py',610),
  ('nativeFun -> SPLIT','nativeFun',1,'p_instruccion_nativas','grammar.py',611),
  ('nativeFun -> CONCAT','nativeFun',1,'p_instruccion_nativas','grammar.py',612),
]
