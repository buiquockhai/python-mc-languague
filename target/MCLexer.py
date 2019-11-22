# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0188\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\5\t\u0092\n\t\3\t\6\t\u0095\n\t\r\t\16\t\u0096\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a4")
        buf.write("\n\f\3\r\3\r\3\r\3\r\7\r\u00aa\n\r\f\r\16\r\u00ad\13\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\7\16\u00b8\n")
        buf.write("\16\f\16\16\16\u00bb\13\16\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3#\3#\3$\6$\u0107\n$\r$\16$\u0108\3")
        buf.write("%\6%\u010c\n%\r%\16%\u010d\3%\3%\7%\u0112\n%\f%\16%\u0115")
        buf.write("\13%\3%\5%\u0118\n%\3%\3%\6%\u011c\n%\r%\16%\u011d\3%")
        buf.write("\5%\u0121\n%\3%\6%\u0124\n%\r%\16%\u0125\3%\5%\u0129\n")
        buf.write("%\5%\u012b\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0136\n&\3")
        buf.write("\'\3\'\7\'\u013a\n\'\f\'\16\'\u013d\13\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\6\60\u0150\n\60")
        buf.write("\r\60\16\60\u0151\3\60\3\60\3\61\3\61\3\61\7\61\u0159")
        buf.write("\n\61\f\61\16\61\u015c\13\61\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u0162\n\61\f\61\16\61\u0165\13\61\3\61\3\61\3\61\7\61")
        buf.write("\u016a\n\61\f\61\16\61\u016d\13\61\3\61\3\61\5\61\u0171")
        buf.write("\n\61\3\62\3\62\3\62\7\62\u0176\n\62\f\62\16\62\u0179")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\7\63\u0180\n\63\f\63\16")
        buf.write("\63\u0183\13\63\3\63\3\63\3\64\3\64\3\u00ab\2\65\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\2\27\2\31\n\33\13")
        buf.write("\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63\27")
        buf.write("\65\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'")
        buf.write("U(W)Y*[+],_-a.c/e\60g\61\3\2\16\4\2GGgg\4\2--//\3\2\62")
        buf.write(";\n\2$$))^^ddhhppttvv\4\2$$^^\7\2$$))^^ddhh\3\2pp\4\2")
        buf.write("\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"")
        buf.write("\3\2$$\2\u01a1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5l\3\2\2\2\7r\3\2\2")
        buf.write("\2\tu\3\2\2\2\13y\3\2\2\2\r\177\3\2\2\2\17\u0088\3\2\2")
        buf.write("\2\21\u008f\3\2\2\2\23\u0098\3\2\2\2\25\u009b\3\2\2\2")
        buf.write("\27\u00a3\3\2\2\2\31\u00a5\3\2\2\2\33\u00b3\3\2\2\2\35")
        buf.write("\u00be\3\2\2\2\37\u00c0\3\2\2\2!\u00c2\3\2\2\2#\u00c4")
        buf.write("\3\2\2\2%\u00c6\3\2\2\2\'\u00c8\3\2\2\2)\u00ca\3\2\2\2")
        buf.write("+\u00cc\3\2\2\2-\u00ce\3\2\2\2/\u00d1\3\2\2\2\61\u00d4")
        buf.write("\3\2\2\2\63\u00d7\3\2\2\2\65\u00da\3\2\2\2\67\u00dd\3")
        buf.write("\2\2\29\u00e0\3\2\2\2;\u00e2\3\2\2\2=\u00e6\3\2\2\2?\u00ec")
        buf.write("\3\2\2\2A\u00f4\3\2\2\2C\u00fb\3\2\2\2E\u0100\3\2\2\2")
        buf.write("G\u0106\3\2\2\2I\u012a\3\2\2\2K\u0135\3\2\2\2M\u0137\3")
        buf.write("\2\2\2O\u013e\3\2\2\2Q\u0140\3\2\2\2S\u0142\3\2\2\2U\u0144")
        buf.write("\3\2\2\2W\u0146\3\2\2\2Y\u0148\3\2\2\2[\u014a\3\2\2\2")
        buf.write("]\u014c\3\2\2\2_\u014f\3\2\2\2a\u0170\3\2\2\2c\u0172\3")
        buf.write("\2\2\2e\u017c\3\2\2\2g\u0186\3\2\2\2ij\7f\2\2jk\7q\2\2")
        buf.write("k\4\3\2\2\2lm\7y\2\2mn\7j\2\2no\7k\2\2op\7n\2\2pq\7g\2")
        buf.write("\2q\6\3\2\2\2rs\7k\2\2st\7h\2\2t\b\3\2\2\2uv\7h\2\2vw")
        buf.write("\7q\2\2wx\7t\2\2x\n\3\2\2\2yz\7d\2\2z{\7t\2\2{|\7g\2\2")
        buf.write("|}\7c\2\2}~\7m\2\2~\f\3\2\2\2\177\u0080\7e\2\2\u0080\u0081")
        buf.write("\7q\2\2\u0081\u0082\7p\2\2\u0082\u0083\7v\2\2\u0083\u0084")
        buf.write("\7k\2\2\u0084\u0085\7p\2\2\u0085\u0086\7w\2\2\u0086\u0087")
        buf.write("\7g\2\2\u0087\16\3\2\2\2\u0088\u0089\7t\2\2\u0089\u008a")
        buf.write("\7g\2\2\u008a\u008b\7v\2\2\u008b\u008c\7w\2\2\u008c\u008d")
        buf.write("\7t\2\2\u008d\u008e\7p\2\2\u008e\20\3\2\2\2\u008f\u0091")
        buf.write("\t\2\2\2\u0090\u0092\t\3\2\2\u0091\u0090\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0095\t\4\2\2")
        buf.write("\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0096\u0097\3\2\2\2\u0097\22\3\2\2\2\u0098\u0099")
        buf.write("\7^\2\2\u0099\u009a\t\5\2\2\u009a\24\3\2\2\2\u009b\u009c")
        buf.write("\n\6\2\2\u009c\26\3\2\2\2\u009d\u009e\7^\2\2\u009e\u00a4")
        buf.write("\n\7\2\2\u009f\u00a0\7^\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7^\2\2\u00a2\u00a4\n\b\2\2\u00a3\u009d\3\2\2\2\u00a3")
        buf.write("\u009f\3\2\2\2\u00a4\30\3\2\2\2\u00a5\u00a6\7\61\2\2\u00a6")
        buf.write("\u00a7\7,\2\2\u00a7\u00ab\3\2\2\2\u00a8\u00aa\13\2\2\2")
        buf.write("\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00ac\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ae\u00af\7,\2\2\u00af\u00b0\7\61\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b2\b\r\2\2\u00b2\32\3\2\2\2\u00b3")
        buf.write("\u00b4\7\61\2\2\u00b4\u00b5\7\61\2\2\u00b5\u00b9\3\2\2")
        buf.write("\2\u00b6\u00b8\n\t\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb")
        buf.write("\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\b\16\2")
        buf.write("\2\u00bd\34\3\2\2\2\u00be\u00bf\7#\2\2\u00bf\36\3\2\2")
        buf.write("\2\u00c0\u00c1\7,\2\2\u00c1 \3\2\2\2\u00c2\u00c3\7\61")
        buf.write("\2\2\u00c3\"\3\2\2\2\u00c4\u00c5\7\'\2\2\u00c5$\3\2\2")
        buf.write("\2\u00c6\u00c7\7-\2\2\u00c7&\3\2\2\2\u00c8\u00c9\7/\2")
        buf.write("\2\u00c9(\3\2\2\2\u00ca\u00cb\7>\2\2\u00cb*\3\2\2\2\u00cc")
        buf.write("\u00cd\7@\2\2\u00cd,\3\2\2\2\u00ce\u00cf\7@\2\2\u00cf")
        buf.write("\u00d0\7?\2\2\u00d0.\3\2\2\2\u00d1\u00d2\7>\2\2\u00d2")
        buf.write("\u00d3\7?\2\2\u00d3\60\3\2\2\2\u00d4\u00d5\7?\2\2\u00d5")
        buf.write("\u00d6\7?\2\2\u00d6\62\3\2\2\2\u00d7\u00d8\7#\2\2\u00d8")
        buf.write("\u00d9\7?\2\2\u00d9\64\3\2\2\2\u00da\u00db\7(\2\2\u00db")
        buf.write("\u00dc\7(\2\2\u00dc\66\3\2\2\2\u00dd\u00de\7~\2\2\u00de")
        buf.write("\u00df\7~\2\2\u00df8\3\2\2\2\u00e0\u00e1\7?\2\2\u00e1")
        buf.write(":\3\2\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7v\2\2\u00e5<\3\2\2\2\u00e6\u00e7\7h\2\2\u00e7")
        buf.write("\u00e8\7n\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7c\2\2\u00ea")
        buf.write("\u00eb\7v\2\2\u00eb>\3\2\2\2\u00ec\u00ed\7d\2\2\u00ed")
        buf.write("\u00ee\7q\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7n\2\2\u00f0")
        buf.write("\u00f1\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("@\3\2\2\2\u00f4\u00f5\7u\2\2\u00f5\u00f6\7v\2\2\u00f6")
        buf.write("\u00f7\7t\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\u00fa\7i\2\2\u00faB\3\2\2\2\u00fb\u00fc\7x\2\2\u00fc")
        buf.write("\u00fd\7q\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7f\2\2\u00ff")
        buf.write("D\3\2\2\2\u0100\u0101\7g\2\2\u0101\u0102\7n\2\2\u0102")
        buf.write("\u0103\7u\2\2\u0103\u0104\7g\2\2\u0104F\3\2\2\2\u0105")
        buf.write("\u0107\t\4\2\2\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109H\3\2\2")
        buf.write("\2\u010a\u010c\t\4\2\2\u010b\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0113\7\60\2\2\u0110\u0112\t\4\2")
        buf.write("\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write("\u0113\3\2\2\2\u0116\u0118\5\21\t\2\u0117\u0116\3\2\2")
        buf.write("\2\u0117\u0118\3\2\2\2\u0118\u012b\3\2\2\2\u0119\u011b")
        buf.write("\7\60\2\2\u011a\u011c\t\4\2\2\u011b\u011a\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u0120\3\2\2\2\u011f\u0121\5\21\t\2\u0120\u011f")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u012b\3\2\2\2\u0122")
        buf.write("\u0124\t\4\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3")
        buf.write("\2\2\2\u0127\u0129\5\21\t\2\u0128\u0127\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u010b\3\2\2\2")
        buf.write("\u012a\u0119\3\2\2\2\u012a\u0123\3\2\2\2\u012bJ\3\2\2")
        buf.write("\2\u012c\u012d\7v\2\2\u012d\u012e\7t\2\2\u012e\u012f\7")
        buf.write("w\2\2\u012f\u0136\7g\2\2\u0130\u0131\7h\2\2\u0131\u0132")
        buf.write("\7c\2\2\u0132\u0133\7n\2\2\u0133\u0134\7u\2\2\u0134\u0136")
        buf.write("\7g\2\2\u0135\u012c\3\2\2\2\u0135\u0130\3\2\2\2\u0136")
        buf.write("L\3\2\2\2\u0137\u013b\t\n\2\2\u0138\u013a\t\13\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013cN\3\2\2\2\u013d\u013b\3\2\2")
        buf.write("\2\u013e\u013f\7*\2\2\u013fP\3\2\2\2\u0140\u0141\7+\2")
        buf.write("\2\u0141R\3\2\2\2\u0142\u0143\7}\2\2\u0143T\3\2\2\2\u0144")
        buf.write("\u0145\7\177\2\2\u0145V\3\2\2\2\u0146\u0147\7]\2\2\u0147")
        buf.write("X\3\2\2\2\u0148\u0149\7_\2\2\u0149Z\3\2\2\2\u014a\u014b")
        buf.write("\7=\2\2\u014b\\\3\2\2\2\u014c\u014d\7.\2\2\u014d^\3\2")
        buf.write("\2\2\u014e\u0150\t\f\2\2\u014f\u014e\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("\u0153\3\2\2\2\u0153\u0154\b\60\2\2\u0154`\3\2\2\2\u0155")
        buf.write("\u015a\7$\2\2\u0156\u0159\5\23\n\2\u0157\u0159\5\25\13")
        buf.write("\2\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015c")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u0171\n\r\2\2")
        buf.write("\u015e\u0163\7$\2\2\u015f\u0162\5\23\n\2\u0160\u0162\5")
        buf.write("\25\13\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0166\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u016b\t")
        buf.write("\t\2\2\u0167\u016a\5\23\n\2\u0168\u016a\5\25\13\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u0168\3\2\2\2\u016a\u016d\3\2\2\2")
        buf.write("\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e\3")
        buf.write("\2\2\2\u016d\u016b\3\2\2\2\u016e\u0171\7$\2\2\u016f\u0171")
        buf.write("\7$\2\2\u0170\u0155\3\2\2\2\u0170\u015e\3\2\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171b\3\2\2\2\u0172\u0177\7$\2\2\u0173")
        buf.write("\u0176\5\25\13\2\u0174\u0176\5\23\n\2\u0175\u0173\3\2")
        buf.write("\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017b\5\27\f\2\u017bd\3\2\2\2\u017c")
        buf.write("\u0181\7$\2\2\u017d\u0180\5\23\n\2\u017e\u0180\5\25\13")
        buf.write("\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u0180\u0183")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\7$\2\2")
        buf.write("\u0185f\3\2\2\2\u0186\u0187\13\2\2\2\u0187h\3\2\2\2\37")
        buf.write("\2\u0091\u0096\u00a3\u00ab\u00b9\u0108\u010d\u0113\u0117")
        buf.write("\u011d\u0120\u0125\u0128\u012a\u0135\u013b\u0151\u0158")
        buf.write("\u015a\u0161\u0163\u0169\u016b\u0170\u0175\u0177\u017f")
        buf.write("\u0181\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    COMMENT = 8
    COMMENT_LINE = 9
    NOT = 10
    MUL = 11
    DIV = 12
    MOD = 13
    ADD = 14
    SUB = 15
    LRELA = 16
    MRELA = 17
    MERELA = 18
    LERELA = 19
    EQUAL = 20
    NOTEQUAL = 21
    AND = 22
    OR = 23
    ASSG = 24
    INTTYPE = 25
    FLOATTYPE = 26
    BOOLEANTYPE = 27
    STRINGTYPE = 28
    VOIDTYPE = 29
    ELSE = 30
    INTLIT = 31
    FLOATLIT = 32
    BOOLEANLIT = 33
    ID = 34
    LB = 35
    RB = 36
    LP = 37
    RP = 38
    LS = 39
    RS = 40
    SEMI = 41
    COMMA = 42
    WS = 43
    UNCLOSE_STRING = 44
    ILLEGAL_ESCAPE = 45
    STRINGLIT = 46
    ERROR_CHAR = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'do'", "'while'", "'if'", "'for'", "'break'", "'continue'", 
            "'return'", "'!'", "'*'", "'/'", "'%'", "'+'", "'-'", "'<'", 
            "'>'", "'>='", "'<='", "'=='", "'!='", "'&&'", "'||'", "'='", 
            "'int'", "'float'", "'boolean'", "'string'", "'void'", "'else'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "COMMENT_LINE", "NOT", "MUL", "DIV", "MOD", "ADD", 
            "SUB", "LRELA", "MRELA", "MERELA", "LERELA", "EQUAL", "NOTEQUAL", 
            "AND", "OR", "ASSG", "INTTYPE", "FLOATTYPE", "BOOLEANTYPE", 
            "STRINGTYPE", "VOIDTYPE", "ELSE", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
            "ID", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", "COMMA", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRINGLIT", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "EXPONENT", "ESC_SEQ", "STR_CHAR", "NOT_ESC_SEQ", "COMMENT", 
                  "COMMENT_LINE", "NOT", "MUL", "DIV", "MOD", "ADD", "SUB", 
                  "LRELA", "MRELA", "MERELA", "LERELA", "EQUAL", "NOTEQUAL", 
                  "AND", "OR", "ASSG", "INTTYPE", "FLOATTYPE", "BOOLEANTYPE", 
                  "STRINGTYPE", "VOIDTYPE", "ELSE", "INTLIT", "FLOATLIT", 
                  "BOOLEANLIT", "ID", "LB", "RB", "LP", "RP", "LS", "RS", 
                  "SEMI", "COMMA", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STRINGLIT", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            result.text = result.text[1:]
            for i in range(len(result.text)):
                if result.text[i] == '\n' or result.text[i] == '\r':
                    result.text = result.text[0:i]
                    break
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            result.text = result.text[1:]
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        elif tk == self.STRINGLIT:
            result = super().emit();
            result.text = result.text[1:-1]
            return result
        else:
            return super().emit();


