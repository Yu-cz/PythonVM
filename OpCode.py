
op_code = {
    0: "STOP_CODE",
    1: "POP_TOP",                   #
    2: "ROT_TWO",                   #
    3: "ROT_THREE",                 #
    4: "DUP_TOP",                   #
    5: "ROT_FOUR",                  #
    9: "NOP",                       #
    10: "UNARY_POSITIVE",           #
    11: "UNARY_NEGATIVE",           #
    12: "UNARY_NOT",                #
    13: "UNARY_CONVERT",            #
    15: "UNARY_INVERT",             #
    19: "BINARY_POWER",             #
    20: "BINARY_MULTIPLY",          #
    21: "BINARY_DIVIDE",            #
    22: "BINARY_MODULO",            #
    23: "BINARY_ADD",               #
    24: "BINARY_SUBTRACT",          #
    25: "BINARY_SUBSCR",            #
    26: "BINARY_FLOOR_DIVIDE",      #
    27: "BINARY_TRUE_DIVIDE",       #
    28: "INPLACE_FLOOR_DIVIDE",     #
    29: "INPLACE_TRUE_DIVIDE",      #
    30: "SLICE",
    31: "SLICE_1",
    32: "SLICE_2",
    33: "SLICE_3",
    40: "STORE_SLICE",
    41: "STORE_SLICE_1",
    42: "STORE_SLICE_2",
    43: "STORE_SLICE_3",
    50: "DELETE_SLICE",
    51: "DELETE_SLICE_1",
    52: "DELETE_SLICE_2",
    53: "DELETE_SLICE_3",
    54: "STORE_MAP",
    55: "INPLACE_ADD",              #
    56: "INPLACE_SUBTRACT",         #
    57: "INPLACE_MULTIPLY",         #
    58: "INPLACE_DIVIDE",           #
    59: "INPLACE_MODULO",           #
    60: "STORE_SUBSCR",
    61: "DELETE_SUBSCR",
    62: "BINARY_LSHIFT",            #
    63: "BINARY_RSHIFT",            #
    64: "BINARY_AND",               #
    65: "BINARY_XOR",               #
    66: "BINARY_OR",                #
    67: "INPLACE_POWER",            #
    68: "GET_ITER",                 #
    70: "PRINT_EXPR",
    71: "PRINT_ITEM",               #
    72: "PRINT_NEWLINE",            #
    73: "PRINT_ITEM_TO",
    74: "PRINT_NEWLINE_TO",
    75: "INPLACE_LSHIFT",           #
    76: "INPLACE_RSHIFT",           #
    77: "INPLACE_AND",              #
    78: "INPLACE_XOR",              #
    79: "INPLACE_OR",               #
    80: "BREAK_LOOP",               #
    81: "WITH_CLEANUP",
    82: "LOAD_LOCALS",
    83: "RETURN_VALUE",             #
    84: "IMPORT_STAR",
    85: "EXEC_STMT",
    86: "YIELD_VALUE",
    87: "POP_BLOCK",                #
    88: "END_FINALLY",              #
    89: "BUILD_CLASS",
    90: "HAVE_ARGUMENT",            # Opcodes from here have an argument:
    90: "STORE_NAME",               #
    91: "DELETE_NAME",
    92: "UNPACK_SEQUENCE",
    93: "FOR_ITER",                 #
    94: "LIST_APPEND",
    95: "STORE_ATTR",
    96: "DELETE_ATTR",
    97: "STORE_GLOBAL",
    98: "DELETE_GLOBAL",
    99: "DUP_TOPX",
    100: "LOAD_CONST",              #
    101: "LOAD_NAME",               #
    102: "BUILD_TUPLE",             #
    103: "BUILD_LIST",              #
    104: "BUILD_SET",
    105: "BUILD_MAP",               #
    106: "LOAD_ATTR",
    107: "COMPARE_OP",              #
    108: "IMPORT_NAME",
    109: "IMPORT_FROM",
    110: "JUMP_FORWARD",            #
    111: "JUMP_IF_FALSE_OR_POP",
    112: "JUMP_IF_TRUE_OR_POP",
    113: "JUMP_ABSOLUTE",           #
    114: "POP_JUMP_IF_FALSE",       #
    115: "POP_JUMP_IF_TRUE",        #
    116: "LOAD_GLOBAL",             #
    119: "CONTINUE_LOOP",
    120: "SETUP_LOOP",              #
    121: "SETUP_EXCEPT",
    122: "SETUP_FINALLY",
    124: "LOAD_FAST",               #
    125: "STORE_FAST",              #
    126: "DELETE_FAST",
    130: "RAISE_VARARGS",           #
    131: "CALL_FUNCTION",           #
    132: "MAKE_FUNCTION",           #
    133: "BUILD_SLICE",
    134: "MAKE_CLOSURE",
    135: "LOAD_CLOSURE",
    136: "LOAD_DEREF",
    137: "STORE_DEREF",
    140: "CALL_FUNCTION_VAR",
    141: "CALL_FUNCTION_KW",
    142: "CALL_FUNCTION_VAR_KW",
    143: "SETUP_WITH",
    145: "EXTENDED_ARG",
    146: "SET_ADD",
    147: "MAP_ADD"
}


def has_arg(op):
    return op >= 90


def has_const():
    return [100]


def has_names():
    return [90, 101]
