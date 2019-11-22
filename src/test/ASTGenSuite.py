import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_function_declaration_1(self):
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_function_declaration_2(self):
        input = """int main() {
            a = 1 + 2;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_function_declaration_3(self):
        input = """int main(string a) {}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",StringType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_function_declaration_4(self):
        input = """int main() {
            a = a + 2;
            print("Hello Python3");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))),CallExpr(Id("print"),[StringLiteral("Hello Python3")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_function_declaration_5(self):
        input = """int main(int a, float b, string c[]) {}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(StringType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_function_declaration_6(self):
        input = """int main() {}
        void foo() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_function_declaration_7(self):
        input = """int main(float b) {}
        string[] foo(int a[]) {}"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",FloatType())],IntType(),Block([])),FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_function_declaration_8(self):
        input = """int main() {
            foo();
        }
        void foo() {
            print("Hello Python3");
            a = a + 2;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[])])),FuncDecl(Id("foo"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("Hello Python3")]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    
    def test_function_declaration_9(self):
        input = """string[] foo(boolean check) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("check",BoolType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_function_declaration_10(self):
        input = """int main(float b, boolean c[]) {}
        string[] foo(int a[]) {
            print("Hello Python3");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(BoolType()))],IntType(),Block([])),FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([CallExpr(Id("print"),[StringLiteral("Hello Python3")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
   
    def test_var_declaration_1(self):
        input = """int main() {}
        int a;"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_var_declaration_2(self):
        input = """int main() {
            float a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_var_declaration_3(self):
        input = """int main() {}
        boolean a,b,c[10];"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",ArrayType(10,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_var_declaration_4(self):
        input = """int main() {
            string a,b[100];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",StringType()),VarDecl("b",ArrayType(100,StringType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_var_declaration_5(self):
        input = """int main() {
            float b;
            string c[5];
        }
        int a[5];"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",FloatType()),VarDecl("c",ArrayType(5,StringType()))])),VarDecl("a",ArrayType(5,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_var_declaration_6(self):
        input = """int main(int a[]) {
            string c;
        }
        void foo(int a) {
            boolean b[10];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("c",StringType())])),FuncDecl(Id("foo"),[VarDecl("a",IntType())],VoidType(),Block([VarDecl("b",ArrayType(10,BoolType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_var_declaration_7(self):
        input = """int main() {
            int a;
            float b[5];
            print(a);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,FloatType())),CallExpr(Id("print"),[Id("a")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_var_declaration_8(self):
        input = """int main() {}
        void foo() {
            float a[10], b[10], d;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",ArrayType(10,FloatType())),VarDecl("b",ArrayType(10,FloatType())),VarDecl("d",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_var_declaration_9(self):
        input = """int[] main() {
            string b[0];
        }
        int a[10];"""
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([VarDecl("b",ArrayType(0,StringType()))])),VarDecl("a",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_var_declaration_10(self):
        input = """int main() {}
        int a;
        float b[10];
        string c;
        boolean d, e[5], f;"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",IntType()),VarDecl("b",ArrayType(10,FloatType())),VarDecl("c",StringType()),VarDecl("d",BoolType()),VarDecl("e",ArrayType(5,BoolType())),VarDecl("f",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_do_while_1(self):
        input = """int[] main() {
            int a;
            do print("Hello Python3"); while (true);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),Dowhile([CallExpr(Id("print"),[StringLiteral("Hello Python3")])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_do_while_2(self):
        input = """int main() {
            do {} while (1);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_do_while_3(self):
        input = """int main() {
            do {
                a = 1 + 2;
            } {} while (false);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]),Block([])],BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_do_while_4(self):
        input = """int main() {
            do {
                a = 1 + 2;
            } while (false);
        }
        void foo() {
            int a[5];
            do {
                int a[10];
            } while (0);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))])],BooleanLiteral(False))])),FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",ArrayType(5,IntType())),Dowhile([Block([VarDecl("a",ArrayType(10,IntType()))])],IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_do_while_5(self):
        input = """void foo(int a) {
            do {
                {}
                a = a - 1;
            } while (1+1);
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],VoidType(),Block([Dowhile([Block([Block([]),BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))])],BinaryOp("+",IntLiteral(1),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_if_1(self):
        input = """int main() {
            if (1) {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_if_2(self):
        input = """int main() {
            if (1) {
                print("Hello Python3");
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([CallExpr(Id("print"),[StringLiteral("Hello Python3")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_if_3(self):
        input = """int main() {
            if (true) {
                {}
                int a;
                float b[10];
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),Block([Block([]),VarDecl("a",IntType()),VarDecl("b",ArrayType(10,FloatType()))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_if_4(self):
        input = """int main() {
            if (1) {}
        }
        void foo(int a) {
            if (a) {
                a = a + 1;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([]))])),FuncDecl(Id("foo"),[VarDecl("a",IntType())],VoidType(),Block([If(Id("a"),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_if_5(self):
        input = """int main() {
            if (1) {} {}
            if (1+1) {
                do print("Hello Python3"); while (true);
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([])),Block([]),If(BinaryOp("+",IntLiteral(1),IntLiteral(1)),Block([Dowhile([CallExpr(Id("print"),[StringLiteral("Hello Python3")])],BooleanLiteral(True))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_if_6(self):
        input = """int main() {
            if (1) {} else {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([]),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_if_7(self):
        input = """int main() {
            if (1) {} else print("Hello Python3");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([]),CallExpr(Id("print"),[StringLiteral("Hello Python3")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_if_8(self):
        input = """int main() {
            if (true) {
                if (a==2) a = a + 1;
                else a = a - 1;
            }
            else {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp('-',Id("a"),IntLiteral(1))))]),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_if_9(self):
        input = """int main() {
            int a;
            do {
                if (true) print(a);
                else print(a+1);
            } while(flase);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),Dowhile([Block([If(BooleanLiteral(True),CallExpr(Id("print"),[Id("a")]),CallExpr(Id("print"),[BinaryOp("+",Id("a"),IntLiteral(1))]))])],Id("flase"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_if_10(self):
        input = """int main() {
            if (a && false) {
                if (true) int a;
            }
            else {
                if (false) int b;
                else int c;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",Id("a"),BooleanLiteral(False)),Block([If(BooleanLiteral(True),Block([VarDecl("a",IntType())]))]),Block([If(BooleanLiteral(False),Block([VarDecl("b",IntType())]),Block([VarDecl("c",IntType())]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_for_1(self):
        input = """int main() {
            for (a;a>2;i=i+1) {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("a"),BinaryOp(">",Id("a"),IntLiteral(2)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_for_2(self):
        input = """int main() {
            for (1;true;true) int a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),BooleanLiteral(True),BooleanLiteral(True),Block([VarDecl("a",IntType())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_for_3(self):
        input = """int main() {
            for (1;true;true) print("Hello Python3");
            int a;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),BooleanLiteral(True),BooleanLiteral(True),CallExpr(Id("print"),[StringLiteral("Hello Python3")])),VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_for_4(self):
        input = """int main() {
            for (1;true;true) {
                a = a + 2;
                print("Hello Python3");
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),BooleanLiteral(True),BooleanLiteral(True),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))),CallExpr(Id("print"),[StringLiteral("Hello Python3")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_for_5(self):
        input = """int main() {
            for (1;true;true) {}
            for (1;a+2;false) {
                string a, b[10];
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),BooleanLiteral(True),BooleanLiteral(True),Block([])),For(IntLiteral(1),BinaryOp("+",Id("a"),IntLiteral(2)),BooleanLiteral(False),Block([VarDecl("a",StringType()),VarDecl("b",ArrayType(10,StringType()))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    def test_for_6(self):
        input = """int main() {
            for (1;true;true) {
                for (true;true;true) a = a + 2;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(1),BooleanLiteral(True),BooleanLiteral(True),Block([For(BooleanLiteral(True),BooleanLiteral(True),BooleanLiteral(True),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_for_7(self):
        input = """int[] main(int a) {
            for (1;true;true) {
                if (a==2) a = a +2;
                else {
                    for (1;2;3) {}
                }
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([For(IntLiteral(1),BooleanLiteral(True),BooleanLiteral(True),Block([If(BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))),Block([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_for_8(self):
        input = """int main() {
            for (a>3;true;1+2) {
                print("Hello Python3");
            }
        }
        void foo() {
            for (1;2;3) {}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp(">",Id("a"),IntLiteral(3)),BooleanLiteral(True),BinaryOp("+",IntLiteral(1),IntLiteral(2)),Block([CallExpr(Id("print"),[StringLiteral("Hello Python3")])]))])),FuncDecl(Id("foo"),[],VoidType(),Block([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_for_9(self):
        input = """int main() {
            do {
                int a;
                for (a;a>2;a=a+1) {
                    print(a);
                }
            } while (true);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp(">",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("print"),[Id("a")])]))])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_for_10(self):
        input = """int main() {
            {}
            {
                for (a;b;c) {
                    {}
                }
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([]),Block([For(Id("a"),Id("b"),Id("c"),Block([Block([])]))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_break_key_1(self):
        input = """int main() {
            break;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_break_key_2(self):
        input = """int main() {
            continue;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_break_key_3(self):
        input = """int main() {
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_break_key_4(self):
        input = """int main() {
            return 2;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_break_key_5(self):
        input = """int main() {
            return (a+b)>(c+d);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp(">",BinaryOp("+",Id("a"),Id("b")),BinaryOp("+",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_break_key_6(self):
        input = """int main() {
            return CallExpr("parameter");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(CallExpr(Id("CallExpr"),[StringLiteral("parameter")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_break_key_7(self):
        input = """int main() {
            int a;
            for (a;a<10;a=a+1) break;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_break_key_8(self):
        input = """int main() {
            int a;
            for (a;a<10;a=a+1) {
                print("Hello Python3");
                if (a%10) break;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("print"),[StringLiteral("Hello Python3")]),If(BinaryOp("%",Id("a"),IntLiteral(10)),Break())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_break_key_9(self):
        input = """float foo(float a) {
            return a*a;
        }
        int main() {
            int a;
            for (a;a<10;a=a+1) {
                if (a%10) continue;
                print(foo(a));
            }
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",FloatType())],FloatType(),Block([Return(BinaryOp("*",Id("a"),Id("a")))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([If(BinaryOp("%",Id("a"),IntLiteral(10)),Continue()),CallExpr(Id("print"),[CallExpr(Id("foo"),[Id("a")])])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_break_key_10(self):
        input = """int main() {
            int a;
            do 
                for(a;a<10;a=a+1) return foo(a);
                if(a==5) break;
            while(true);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),Dowhile([For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Return(CallExpr(Id("foo"),[Id("a")]))),If(BinaryOp("==",Id("a"),IntLiteral(5)),Break())],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_expression_1(self):
        input = """int main() {
            a = a + b * c;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_expression_2(self):
        input = """int main() {
            int a[10];
            a[1] = a[0] + b * c;
            print(a[2]);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),BinaryOp("+",ArrayCell(Id("a"),IntLiteral(0)),BinaryOp("*",Id("b"),Id("c")))),CallExpr(Id("print"),[ArrayCell(Id("a"),IntLiteral(2))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_expression_3(self):
        input = """void foo(string a) {
            print(a);
        }
        int main() {
            if (!a == !b) return foo("Hello Python3");
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",StringType())],VoidType(),Block([CallExpr(Id("print"),[Id("a")])])),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",UnaryOp("!",Id("a")),UnaryOp("!",Id("b"))),Return(CallExpr(Id("foo"),[StringLiteral("Hello Python3")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_expression_4(self):
        input = """int main() {
            boolean bool_1, bool_2;
            bool_1 = (!bool_2 || (bool_2 && true));
            print(bool_1);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("bool_1",BoolType()),VarDecl("bool_2",BoolType()),BinaryOp("=",Id("bool_1"),BinaryOp("||",UnaryOp("!",Id("bool_2")),BinaryOp("&&",Id("bool_2"),BooleanLiteral(True)))),CallExpr(Id("print"),[Id("bool_1")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_expression_5(self):
        input = """int count(string arr[]){
            return len(arr);
        }
        int main() {
            if (!a && !b) print(count(arr));
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("count"),[VarDecl("arr",ArrayPointerType(StringType()))],IntType(),Block([Return(CallExpr(Id("len"),[Id("arr")]))])),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",UnaryOp("!",Id("a")),UnaryOp("!",Id("b"))),CallExpr(Id("print"),[CallExpr(Id("count"),[Id("arr")])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_expression_6(self):
        input = """int main() {
            a = a + b * c;
            do {} while (a);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c")))),Dowhile([Block([])],Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_expression_7(self):
        input = """void main() {
            int a;
            a =  CallExpr(a[b[2]]);
            print(a);
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("CallExpr"),[ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2)))])),CallExpr(Id("print"),[Id("a")]),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_expression_8(self):
        input = """int[] main() {
            string str;
            if (str!=isempty(null)) {
                int a;
                for (a;a<10;a=a+1) print(str[a]);
            }
            else{
                break;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([VarDecl("str",StringType()),If(BinaryOp("!=",Id("str"),CallExpr(Id("isempty"),[Id("null")])),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),CallExpr(Id("print"),[ArrayCell(Id("str"),Id("a"))]))]),Block([Break()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_expression_9(self):
        input = """int main() {
            string a,b,c;
            a = a + b * c = foo(2) +b = arr[a[10]];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),BinaryOp("=",Id("a"),BinaryOp("=",BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c"))),BinaryOp("=",BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(2)]),Id("b")),ArrayCell(Id("arr"),ArrayCell(Id("a"),IntLiteral(10))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_expression_10(self):
        input = """boolean check(string a) {
            if(!isempty(a)) return true;
            else return false;
        }
        int main() {
            int a;
            string arr;
            for (a;a<10;a=a+1) {
                do print("Hello Python3"); while (arr[a]);
                if(!arr[a]) break;
            }
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("check"),[VarDecl("a",StringType())],BoolType(),Block([If(UnaryOp("!",CallExpr(Id("isempty"),[Id("a")])),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("arr",StringType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([Dowhile([CallExpr(Id("print"),[StringLiteral("Hello Python3")])],ArrayCell(Id("arr"),Id("a"))),If(UnaryOp("!",ArrayCell(Id("arr"),Id("a"))),Break())])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_expression_11(self):
        input = """int main () {
            boolean a, b;
            b = true;
            a = !(!(!b));
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",BoolType()),VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BooleanLiteral(True)),BinaryOp("=",Id("a"),UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("b")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_expression_12(self):
        input = """boolean foo (boolean a){
            if (a) return true;
            else return false;
        }
        int main () {
            print(foo(!foo(true)));
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",BoolType())],BoolType(),Block([If(Id("a"),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("print"),[CallExpr(Id("foo"),[UnaryOp("!",CallExpr(Id("foo"),[BooleanLiteral(True)]))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_expression_13(self):
        input = """int main () {
            return (foo(!(a==2)==true));
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(CallExpr(Id("foo"),[BinaryOp("==",UnaryOp("!",BinaryOp("==",Id("a"),IntLiteral(2))),BooleanLiteral(True))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_expression_14(self):
        input = """int main () {
            float a, b, c[10];
            a = ((b * c[0] + (b - c[1]) / c[2]) == 3);
            print(a);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",ArrayType(10,FloatType())),BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("+",BinaryOp("*",Id("b"),ArrayCell(Id("c"),IntLiteral(0))),BinaryOp("/",BinaryOp("-",Id("b"),ArrayCell(Id("c"),IntLiteral(1))),ArrayCell(Id("c"),IntLiteral(2)))),IntLiteral(3))),CallExpr(Id("print"),[Id("a")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_expression_15(self):
        input = """int main () {
            boolean a, b;
            a = -10;
            b = -(-20);
            print(a+b);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",BoolType()),VarDecl("b",BoolType()),BinaryOp("=",Id("a"),UnaryOp("-",IntLiteral(10))),BinaryOp("=",Id("b"),UnaryOp("-",UnaryOp("-",IntLiteral(20)))),CallExpr(Id("print"),[BinaryOp("+",Id("a"),Id("b"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_simple_exercise_1(self):
        input = """int main() {
            int x;
            float y;
            printf("Input total distance in km: ");
            scanf("%d",x);
            printf("Input total fuel spent in liters: ");
            scanf("%f", y);
            printf("Average consumption (km/lt) %.3f ",x/y);
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),VarDecl("y",FloatType()),CallExpr(Id("printf"),[StringLiteral("Input total distance in km: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("x")]),CallExpr(Id("printf"),[StringLiteral("Input total fuel spent in liters: ")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("y")]),CallExpr(Id("printf"),[StringLiteral("Average consumption (km/lt) %.3f "),BinaryOp("/",Id("x"),Id("y"))]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_simple_exercise_2(self):
        input = """int main() {
            int x, y;
            printf("Input the first number: "); 
            scanf("%d", x);
            printf("Input the second number: ");
            scanf("%d", y);
            if(x > y) {
                int temp;
                temp = x;
                x = y;
                y = temp;
            }
            if((y % x)== 0) printf("Multiplied!");
            else printf("Not Multiplied!");
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),CallExpr(Id("printf"),[StringLiteral("Input the first number: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("x")]),CallExpr(Id("printf"),[StringLiteral("Input the second number: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("y")]),If(BinaryOp(">",Id("x"),Id("y")),Block([VarDecl("temp",IntType()),BinaryOp("=",Id("temp"),Id("x")),BinaryOp("=",Id("x"),Id("y")),BinaryOp("=",Id("y"),Id("temp"))])),If(BinaryOp("==",BinaryOp("%",Id("y"),Id("x")),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Multiplied!")]),CallExpr(Id("printf"),[StringLiteral("Not Multiplied!")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_simple_exercise_3(self):
        input = """int main() {
            float N[10];
            int i;
            printf("Input the 5 members of the array:");
            for(i = 0; i < AL; i=i+1) {
                scanf("%f", N[0]);
            }
            for(i = 0; i < AL; i=i+1) {
                if(N[0] < MAX) printf("A[%d] = %.1f", i, N[0]);
            }
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("N",ArrayType(10,FloatType())),VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("Input the 5 members of the array:")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("AL")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("scanf"),[StringLiteral("%f"),ArrayCell(Id("N"),IntLiteral(0))])])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("AL")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("<",ArrayCell(Id("N"),IntLiteral(0)),Id("MAX")),CallExpr(Id("printf"),[StringLiteral("A[%d] = %.1f"),Id("i"),ArrayCell(Id("N"),IntLiteral(0))]))])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_simple_exercise_4(self):
        input = """int main (){
            int x;

            printf ("Is command processor available?");
            if (system(NULL)) printf ("Command processor available!");
            else {
                printf ("Command processor not available!");
                exit (1);
            }
            printf ("Executing command DIR");
            x=system ("dir");
            printf ("Returned value is: %d.",x);
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),CallExpr(Id("printf"),[StringLiteral("Is command processor available?")]),If(CallExpr(Id("system"),[Id("NULL")]),CallExpr(Id("printf"),[StringLiteral("Command processor available!")]),Block([CallExpr(Id("printf"),[StringLiteral("Command processor not available!")]),CallExpr(Id("exit"),[IntLiteral(1)])])),CallExpr(Id("printf"),[StringLiteral("Executing command DIR")]),BinaryOp("=",Id("x"),CallExpr(Id("system"),[StringLiteral("dir")])),CallExpr(Id("printf"),[StringLiteral("Returned value is: %d."),Id("x")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_simple_exercise_5(self):
        input = """int main () {
            int number, input;
            /* initialize random seed: */
            srand (time(NULL));
            /* Generate a random number: */
            number = rand() % 10 + 1;
            do {
                    printf ("Guess the number (1 to 10): ");
                    scanf ("%d",input);
                    if (number > input) printf ("The number is higher");
                } while (number!=input);
            printf ("That is correct!");
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),VarDecl("input",IntType()),CallExpr(Id("srand"),[CallExpr(Id("time"),[Id("NULL")])]),BinaryOp("=",Id("number"),BinaryOp("+",BinaryOp("%",CallExpr(Id("rand"),[]),IntLiteral(10)),IntLiteral(1))),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Guess the number (1 to 10): ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("input")]),If(BinaryOp(">",Id("number"),Id("input")),CallExpr(Id("printf"),[StringLiteral("The number is higher")]))])],BinaryOp("!=",Id("number"),Id("input"))),CallExpr(Id("printf"),[StringLiteral("That is correct!")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_simple_exercise_6(self):
        input = """int main() {
            printf("%d",test(1, 2));
            printf("%d",test(2, 2));
        }    
        int test(int x, int y){
            return ifStmt(x == y , (x + y)*3 , x + y);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(1),IntLiteral(2)])]),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(2),IntLiteral(2)])])])),FuncDecl(Id("test"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([Return(CallExpr(Id("ifStmt"),[BinaryOp("==",Id("x"),Id("y")),BinaryOp("*",BinaryOp("+",Id("x"),Id("y")),IntLiteral(3)),BinaryOp("+",Id("x"),Id("y"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_simple_exercise_7(self):
        input = """int main() {
            printf("%d",test(25, 5));
            printf("%d",test(20, 30));
            printf("%d",test(20, 25));
        }    
        int test(int x, int y) {
            return x == 30 || y == 30 || (x + y == 30);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(25),IntLiteral(5)])]),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(20),IntLiteral(30)])]),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(20),IntLiteral(25)])])])),FuncDecl(Id("test"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([Return(BinaryOp("||",BinaryOp("||",BinaryOp("==",Id("x"),IntLiteral(30)),BinaryOp("==",Id("y"),IntLiteral(30))),BinaryOp("==",BinaryOp("+",Id("x"),Id("y")),IntLiteral(30))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_simple_exercise_8(self):
        input = """int main() {
            printf("%d",test(25, 5));
            printf("%d",test(20, 30));
            printf("%d",test(20, 25));
        }    
        int test(int x, int y) {
            return x == 30 || y == 30 || (x + y == 30);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(25),IntLiteral(5)])]),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(20),IntLiteral(30)])]),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[IntLiteral(20),IntLiteral(25)])])])),FuncDecl(Id("test"),[VarDecl("x",IntType()),VarDecl("y",IntType())],IntType(),Block([Return(BinaryOp("||",BinaryOp("||",BinaryOp("==",Id("x"),IntLiteral(30)),BinaryOp("==",Id("y"),IntLiteral(30))),BinaryOp("==",BinaryOp("+",Id("x"),Id("y")),IntLiteral(30))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_simple_exercise_9(self):
        input = """int main() {
            int arr_size;
            int array1[10];
            arr_size = sizeof(array1)/sizeof(array1[0]);
            printf("%d",test(array1, arr_size));
            int array2[10];
            arr_size = sizeof(array2)/sizeof(array2[0]);
            printf("%d",test(array2, arr_size));
            int array3[10];
            arr_size = sizeof(array3)/sizeof(array3[0]);
            printf("%d",test(array3, arr_size));
        }
        int test(int nums[], int arr_size) {
            int ctr;
            for (i = 0; i < arr_size - 1; i=i+1) {
                if (nums[0] == 5 && (nums[1] == 5 || nums[1] == 6)) ctr=ctr+1;
            }
            return ctr;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("arr_size",IntType()),VarDecl("array1",ArrayType(10,IntType())),BinaryOp("=",Id("arr_size"),BinaryOp("/",CallExpr(Id("sizeof"),[Id("array1")]),CallExpr(Id("sizeof"),[ArrayCell(Id("array1"),IntLiteral(0))]))),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[Id("array1"),Id("arr_size")])]),VarDecl("array2",ArrayType(10,IntType())),BinaryOp("=",Id("arr_size"),BinaryOp("/",CallExpr(Id("sizeof"),[Id("array2")]),CallExpr(Id("sizeof"),[ArrayCell(Id("array2"),IntLiteral(0))]))),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[Id("array2"),Id("arr_size")])]),VarDecl("array3",ArrayType(10,IntType())),BinaryOp("=",Id("arr_size"),BinaryOp("/",CallExpr(Id("sizeof"),[Id("array3")]),CallExpr(Id("sizeof"),[ArrayCell(Id("array3"),IntLiteral(0))]))),CallExpr(Id("printf"),[StringLiteral("%d"),CallExpr(Id("test"),[Id("array3"),Id("arr_size")])])])),FuncDecl(Id("test"),[VarDecl("nums",ArrayPointerType(IntType())),VarDecl("arr_size",IntType())],IntType(),Block([VarDecl("ctr",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("arr_size"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("&&",BinaryOp("==",ArrayCell(Id("nums"),IntLiteral(0)),IntLiteral(5)),BinaryOp("||",BinaryOp("==",ArrayCell(Id("nums"),IntLiteral(1)),IntLiteral(5)),BinaryOp("==",ArrayCell(Id("nums"),IntLiteral(1)),IntLiteral(6)))),BinaryOp("=",Id("ctr"),BinaryOp("+",Id("ctr"),IntLiteral(1))))])),Return(Id("ctr"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_simple_exercise_10(self):
        input = """void main() {
            int i,j,rows,k;
            k = 1;
            printf("Input number of rows : ");
            scanf("%d",rows);
            for(i=1;i<=rows;i=i+1) {
                for(j=1;j<=i;j=j+1)
                printf("%d ",k+1);
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),VarDecl("rows",IntType()),VarDecl("k",IntType()),BinaryOp("=",Id("k"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral("Input number of rows : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("rows")]),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),Id("rows")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(1)),BinaryOp("<=",Id("j"),Id("i")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("%d "),BinaryOp("+",Id("k"),IntLiteral(1))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_simple_exercise_11(self):
        input = """
        float temp_f;     /* degrees fahrenheit */
        float temp_c;     /* degrees centigrade */
        string line_text[50];        /* a line of input */

        int main() {
            printf("Input a temperature (in Centigrade): ");
            fgets(line_text, sizeof(line_text), stdin);
            sscanf(line_text, "%f", temp_c);
            temp_f = ((9.0 / 5.0) * temp_c) + 32.0;
            printf("%f degrees Fahrenheit.", temp_f);
            return(0);
        }"""
        expect = str(Program([VarDecl("temp_f",FloatType()),VarDecl("temp_c",FloatType()),VarDecl("line_text",ArrayType(50,StringType())),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Input a temperature (in Centigrade): ")]),CallExpr(Id("fgets"),[Id("line_text"),CallExpr(Id("sizeof"),[Id("line_text")]),Id("stdin")]),CallExpr(Id("sscanf"),[Id("line_text"),StringLiteral("%f"),Id("temp_c")]),BinaryOp("=",Id("temp_f"),BinaryOp("+",BinaryOp("*",BinaryOp("/",FloatLiteral(9.0),FloatLiteral(5.0)),Id("temp_c")),FloatLiteral(32.0))),CallExpr(Id("printf"),[StringLiteral("%f degrees Fahrenheit."),Id("temp_f")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_simple_exercise_12(self):
        input = """
        float temp_f;     /* degrees fahrenheit */
        float temp_c;     /* degrees centigrade */
        string line_text[50];        /* a line of input */

        int main() {
            printf("Input a temperature (in Centigrade): ");
            fgets(line_text, sizeof(line_text), stdin);
            sscanf(line_text, "%f", temp_c);
            temp_f = ((9.0 / 5.0) * temp_c) + 32.0;
            printf("%f degrees Fahrenheit.", temp_f);
            return(0);
        }"""
        expect = str(Program([VarDecl("temp_f",FloatType()),VarDecl("temp_c",FloatType()),VarDecl("line_text",ArrayType(50,StringType())),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Input a temperature (in Centigrade): ")]),CallExpr(Id("fgets"),[Id("line_text"),CallExpr(Id("sizeof"),[Id("line_text")]),Id("stdin")]),CallExpr(Id("sscanf"),[Id("line_text"),StringLiteral("%f"),Id("temp_c")]),BinaryOp("=",Id("temp_f"),BinaryOp("+",BinaryOp("*",BinaryOp("/",FloatLiteral(9.0),FloatLiteral(5.0)),Id("temp_c")),FloatLiteral(32.0))),CallExpr(Id("printf"),[StringLiteral("%f degrees Fahrenheit."),Id("temp_f")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_simple_exercise_13(self):
        input = """void main()
        {
            int chk_year;
            printf("Input a year :");
            scanf("%d", chk_year);
            if ((chk_year % 400) == 0)
                printf("%d is a leap year.", chk_year);
            else if ((chk_year % 100) == 0)
                printf("%d is a not leap year.", chk_year);
            else if ((chk_year % 4) == 0)
                printf("%d is a leap year.", chk_year);
            else
                printf("%d is not a leap year ", chk_year);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("chk_year",IntType()),CallExpr(Id("printf"),[StringLiteral("Input a year :")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("chk_year")]),If(BinaryOp("==",BinaryOp("%",Id("chk_year"),IntLiteral(400)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is a leap year."),Id("chk_year")]),If(BinaryOp("==",BinaryOp("%",Id("chk_year"),IntLiteral(100)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is a not leap year."),Id("chk_year")]),If(BinaryOp("==",BinaryOp("%",Id("chk_year"),IntLiteral(4)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is a leap year."),Id("chk_year")]),CallExpr(Id("printf"),[StringLiteral("%d is not a leap year "),Id("chk_year")]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_simple_exercise_14(self):
        input = """void main() {
            int m,n;
            printf("Input the  value of m :");
            scanf("%d",m);
            if(m!=0)
                if(m>0)
                    n=1;
                else
                    n=-1;
            else
                n=0;
            printf("The value of m = %d ",m);
            printf("The value of n = %d ",n);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("m",IntType()),VarDecl("n",IntType()),CallExpr(Id("printf"),[StringLiteral("Input the  value of m :")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("m")]),If(BinaryOp("!=",Id("m"),IntLiteral(0)),If(BinaryOp(">",Id("m"),IntLiteral(0)),BinaryOp("=",Id("n"),IntLiteral(1)),BinaryOp("=",Id("n"),UnaryOp("-",IntLiteral(1)))),BinaryOp("=",Id("n"),IntLiteral(0))),CallExpr(Id("printf"),[StringLiteral("The value of m = %d "),Id("m")]),CallExpr(Id("printf"),[StringLiteral("The value of n = %d "),Id("n")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_simple_exercise_15(self):
        input = """void main() {
            float PerHeight;
            printf("Input the height of the person (in centimetres) :");
            scanf("%f", PerHeight);
            if (PerHeight < 150.0)
                printf("The person is Dwarf. ");
            else if ((PerHeight >= 150.0) && (PerHeight < 165.0))
                printf("The person is  average heighted. ");
            else if ((PerHeight >= 165.0) && (PerHeight <= 195.0))
                printf("The person is taller. ");
            else
                printf("Abnormal height.");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("PerHeight",FloatType()),CallExpr(Id("printf"),[StringLiteral("Input the height of the person (in centimetres) :")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("PerHeight")]),If(BinaryOp("<",Id("PerHeight"),FloatLiteral(150.0)),CallExpr(Id("printf"),[StringLiteral("The person is Dwarf. ")]),If(BinaryOp("&&",BinaryOp(">=",Id("PerHeight"),FloatLiteral(150.0)),BinaryOp("<",Id("PerHeight"),FloatLiteral(165.0))),CallExpr(Id("printf"),[StringLiteral("The person is  average heighted. ")]),If(BinaryOp("&&",BinaryOp(">=",Id("PerHeight"),FloatLiteral(165.0)),BinaryOp("<=",Id("PerHeight"),FloatLiteral(195.0))),CallExpr(Id("printf"),[StringLiteral("The person is taller. ")]),CallExpr(Id("printf"),[StringLiteral("Abnormal height.")]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_simple_exercise_16(self):
        input = """int main() {  
            int sidea, sideb, sidec; //are three sides of a triangle  
            /* 
            * Reads all sides of a triangle 
            */  
            printf("Input three sides of triangle: ");  
            scanf("%d %d %d", sidea, sideb, sidec);  
            if(sidea==sideb && sideb==sidec) //check whether all sides are equal  
            {  
                printf("This is an equilateral triangle.");  
            }  
            else if(sidea==sideb || sidea==sidec || sideb==sidec) //check whether two sides are equal  
            {  
                printf("This is an isosceles triangle.");  
            }  
            else //check whether no sides are equal  
            {  
                printf("This is a scalene triangle.");  
            }  
            return 0;  
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("sidea",IntType()),VarDecl("sideb",IntType()),VarDecl("sidec",IntType()),CallExpr(Id("printf"),[StringLiteral("Input three sides of triangle: ")]),CallExpr(Id("scanf"),[StringLiteral("%d %d %d"),Id("sidea"),Id("sideb"),Id("sidec")]),If(BinaryOp("&&",BinaryOp("==",Id("sidea"),Id("sideb")),BinaryOp("==",Id("sideb"),Id("sidec"))),Block([CallExpr(Id("printf"),[StringLiteral("This is an equilateral triangle.")])]),If(BinaryOp("||",BinaryOp("||",BinaryOp("==",Id("sidea"),Id("sideb")),BinaryOp("==",Id("sidea"),Id("sidec"))),BinaryOp("==",Id("sideb"),Id("sidec"))),Block([CallExpr(Id("printf"),[StringLiteral("This is an isosceles triangle.")])]),Block([CallExpr(Id("printf"),[StringLiteral("This is a scalene triangle.")])]))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_simple_exercise_17(self):
        input = """int getSum(int n) {
            int sum;
            for (i; i<=sqrt(n); i=i+1) {
                if (n%i==0) {
                    if (n/i == i)
                        sum = sum + i;
                    else {
                        sum = sum + i;
                        sum = sum + (n / i);
                    }
                }
            }
            sum = sum - n;
            return sum;
        }
        bool checkAbundant(int n) {
            return getSum(n) > n;
        }
        int main() {
            int n;
            printf(" Check whether a given number is an Abundant number:");
            printf(" --------------------------------------------------------");
            printf(" Input an integer number: ");
            scanf("%d",n);
            ifStmt (checkAbundant(n), printf(" The number is Abundant."), printf(" The number is not Abundant."));
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("getSum"),[VarDecl("n",IntType())],IntType(),Block([VarDecl("sum",IntType()),For(Id("i"),BinaryOp("<=",Id("i"),CallExpr(Id("sqrt"),[Id("n")])),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([If(BinaryOp("==",BinaryOp("/",Id("n"),Id("i")),Id("i")),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),Id("i"))),Block([BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),Id("i"))),BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),BinaryOp("/",Id("n"),Id("i"))))]))]))])),BinaryOp("=",Id("sum"),BinaryOp("-",Id("sum"),Id("n"))),Return(Id("sum"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_simple_exercise_18(self):
        input = """
        void main() {
            string str[100]; /* Declares a string of size 100 */
            int l,i;
            printf("Print individual characters of string in reverse order :");
            printf("------------------------------------------------------"); 	
            printf("Input the string : ");
            fgets(str, sizeof(str), stdin);
            l=strlen(str);
            printf("The characters of the string in reverse are : ");
            for(i=l;i>=0;i=i-1)
                {
                printf("%c  ", str);
                }
            printf("");
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("str",ArrayType(100,StringType())),VarDecl("l",IntType()),VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("Print individual characters of string in reverse order :")]),CallExpr(Id("printf"),[StringLiteral("------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral("Input the string : ")]),CallExpr(Id("fgets"),[Id("str"),CallExpr(Id("sizeof"),[Id("str")]),Id("stdin")]),BinaryOp("=",Id("l"),CallExpr(Id("strlen"),[Id("str")])),CallExpr(Id("printf"),[StringLiteral("The characters of the string in reverse are : ")]),For(BinaryOp("=",Id("i"),Id("l")),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("%c  "),Id("str")])])),CallExpr(Id("printf"),[StringLiteral("")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_simple_exercise_19(self):
        input = """
        int main () {
            int total;
            printf(" Function : a simple structure of function :");
            printf("------------------------------------------------");	
            total = sum (5, 6); //function call
            printf ("The total is :  %d", total);
            return 0;
        }
        int sum (int a, int b) {
            int s;
            s=a+b;
            return s; //function returning a value
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("total",IntType()),CallExpr(Id("printf"),[StringLiteral(" Function : a simple structure of function :")]),CallExpr(Id("printf"),[StringLiteral("------------------------------------------------")]),BinaryOp("=",Id("total"),CallExpr(Id("sum"),[IntLiteral(5),IntLiteral(6)])),CallExpr(Id("printf"),[StringLiteral("The total is :  %d"),Id("total")]),Return(IntLiteral(0))])),FuncDecl(Id("sum"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([VarDecl("s",IntType()),BinaryOp("=",Id("s"),BinaryOp("+",Id("a"),Id("b"))),Return(Id("s"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_simple_exercise_20(self):
        input = """
        int main() {
            int n;
            printf(" Recursion : print first 50 natural numbers :");
            printf("-------------------------------------------------"); 
            printf(" The natural numbers are :");
            numPrint(n);
            return 0;
        }
        int numPrint(int n) {
            if(n<=50) {
                printf(" %d ",n);
                numPrint(n+1);
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : print first 50 natural numbers :")]),CallExpr(Id("printf"),[StringLiteral("-------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" The natural numbers are :")]),CallExpr(Id("numPrint"),[Id("n")]),Return(IntLiteral(0))])),FuncDecl(Id("numPrint"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("<=",Id("n"),IntLiteral(50)),Block([CallExpr(Id("printf"),[StringLiteral(" %d "),Id("n")]),CallExpr(Id("numPrint"),[BinaryOp("+",Id("n"),IntLiteral(1))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_simple_exercise_21(self):
        input = """
        int main() {
            int n1;
            int sum;
            printf(" Recursion : calculate the sum of numbers from 1 to n :");
            printf("-----------------------------------------------------------");    
            printf(" Input the last number of the range starting from 1 : ");
            scanf("%d", n1);
            sum = sumOfRange(n1); 
            printf(" The sum of numbers from 1 to %d : %d", n1, sum);
            return (0);
        }
        
        int sumOfRange(int n1) {
            int res;
            if (n1 == 1) {
                return (1);
            } 
            else {
                res = n1 + sumOfRange(n1 - 1); //calling the function sumOfRange itself
            }
            return (res);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("sum",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : calculate the sum of numbers from 1 to n :")]),CallExpr(Id("printf"),[StringLiteral("-----------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input the last number of the range starting from 1 : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),BinaryOp("=",Id("sum"),CallExpr(Id("sumOfRange"),[Id("n1")])),CallExpr(Id("printf"),[StringLiteral(" The sum of numbers from 1 to %d : %d"),Id("n1"),Id("sum")]),Return(IntLiteral(0))])),FuncDecl(Id("sumOfRange"),[VarDecl("n1",IntType())],IntType(),Block([VarDecl("res",IntType()),If(BinaryOp("==",Id("n1"),IntLiteral(1)),Block([Return(IntLiteral(1))]),Block([BinaryOp("=",Id("res"),BinaryOp("+",Id("n1"),CallExpr(Id("sumOfRange"),[BinaryOp("-",Id("n1"),IntLiteral(1))])))])),Return(Id("res"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_simple_exercise_22(self):
        input = """
        int main() {
            int n1, sum;
            printf(" Recursion : Find the sum of digits of a number :");
            printf("-----------------------------------------------------");     
            printf(" Input any number to find sum of digits: ");
            scanf("%d", n1);
            sum = DigitSum(n1); //call the function for calculation
            printf(" The Sum of digits of %d = %d", n1, sum);
            return 0;
        }
        int DigitSum(int n1) {
            if(n1 == 0) return 0;
            return ((n1 % 10) + DigitSum(n1 / 10)); //calling the function DigitSum itself
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("sum",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Find the sum of digits of a number :")]),CallExpr(Id("printf"),[StringLiteral("-----------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input any number to find sum of digits: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),BinaryOp("=",Id("sum"),CallExpr(Id("DigitSum"),[Id("n1")])),CallExpr(Id("printf"),[StringLiteral(" The Sum of digits of %d = %d"),Id("n1"),Id("sum")]),Return(IntLiteral(0))])),FuncDecl(Id("DigitSum"),[VarDecl("n1",IntType())],IntType(),Block([If(BinaryOp("==",Id("n1"),IntLiteral(0)),Return(IntLiteral(0))),Return(BinaryOp("+",BinaryOp("%",Id("n1"),IntLiteral(10)),CallExpr(Id("DigitSum"),[BinaryOp("/",Id("n1"),IntLiteral(10))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_simple_exercise_23(self):
        input = """
        int main()
        {
            int n1,f;
            printf(" Recursion : Find the Factorial of a number :");
            printf("-------------------------------------------------");	  
            printf(" Input  a number : ");
            scanf("%d",n1);
            f = findFactorial(n1); //call the function findFactorial for factorial
            printf(" The Factorial of %d is : %d",n1,f);
            return 0;
        }

        int findFactorial(int n) {
            if(n==1) return 1;
            else return(n*findFactorial(n-1));// calling the function findFactorial to itself recursively
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("f",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Find the Factorial of a number :")]),CallExpr(Id("printf"),[StringLiteral("-------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input  a number : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),BinaryOp("=",Id("f"),CallExpr(Id("findFactorial"),[Id("n1")])),CallExpr(Id("printf"),[StringLiteral(" The Factorial of %d is : %d"),Id("n1"),Id("f")]),Return(IntLiteral(0))])),FuncDecl(Id("findFactorial"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("==",Id("n"),IntLiteral(1)),Return(IntLiteral(1)),Return(BinaryOp("*",Id("n"),CallExpr(Id("findFactorial"),[BinaryOp("-",Id("n"),IntLiteral(1))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_simple_exercise_24(self):
        input = """
        int i;
        int main() {
            int n1,primeNo;
            printf(" Recursion : Check a number is prime number or not :");
            printf("--------------------------------------------------------");
            printf(" Input any positive number : ");
            scanf("%d",n1);
            i = n1/2;
            primeNo = checkForPrime(n1); //call the function checkForPrime
            if(primeNo==1) printf(" The number %d is a prime number. ",n1);
            else printf(" The number %d is not a prime number.",n1);
            return 0;
        }

        int checkForPrime(int n1) {
            if(i==1) return 1;
            if(n1 %i==0) return 0;
            else {
                i = i -1; 
                checkForPrime(n1); //calling the function checkForPrime itself recursively
            }
        }
        """
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("primeNo",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Check a number is prime number or not :")]),CallExpr(Id("printf"),[StringLiteral("--------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input any positive number : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),BinaryOp("=",Id("i"),BinaryOp("/",Id("n1"),IntLiteral(2))),BinaryOp("=",Id("primeNo"),CallExpr(Id("checkForPrime"),[Id("n1")])),If(BinaryOp("==",Id("primeNo"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral(" The number %d is a prime number. "),Id("n1")]),CallExpr(Id("printf"),[StringLiteral(" The number %d is not a prime number."),Id("n1")])),Return(IntLiteral(0))])),FuncDecl(Id("checkForPrime"),[VarDecl("n1",IntType())],IntType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(1)),Return(IntLiteral(1))),If(BinaryOp("==",BinaryOp("%",Id("n1"),Id("i")),IntLiteral(0)),Return(IntLiteral(0)),Block([BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),CallExpr(Id("checkForPrime"),[Id("n1")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_simple_exercise_25(self):
        input = """
        int main() {
            int n1, n2, lcmOf;
            printf(" Recursion : Find the LCM of two numbers :");
            printf("----------------------------------------------");
            printf(" Input 1st number for LCM : ");
            scanf("%d", n1);
            printf(" Input 2nd number for LCM : ");
            scanf("%d", n2);
            // Ensures that first parameter of lcm must be smaller than 2nd
            if(n1 >  n2) lcmOf = lcmCalculate(n2, n1); //call the function lcmCalculate for lcm calculation
            else lcmOf = lcmCalculate(n1, n2);//call the function lcmCalculate for lcm calculation
            printf(" The LCM of %d and %d :  %d", n1, n2, lcmOf);
            return 0;
        }
        int lcmCalculate(int a, int b) //the value of n1 and n2 is passing through a and b
        {
            int m;
            //Increments m by adding max value to it
            m = m+b;
            // If found a common multiple then return the m.
            if((m % a == 0) && (m % b == 0)) return m;
            else lcmCalculate(a, b); //calling the function lcmCalculate itself
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("n2",IntType()),VarDecl("lcmOf",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Find the LCM of two numbers :")]),CallExpr(Id("printf"),[StringLiteral("----------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input 1st number for LCM : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),CallExpr(Id("printf"),[StringLiteral(" Input 2nd number for LCM : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n2")]),If(BinaryOp(">",Id("n1"),Id("n2")),BinaryOp("=",Id("lcmOf"),CallExpr(Id("lcmCalculate"),[Id("n2"),Id("n1")])),BinaryOp("=",Id("lcmOf"),CallExpr(Id("lcmCalculate"),[Id("n1"),Id("n2")]))),CallExpr(Id("printf"),[StringLiteral(" The LCM of %d and %d :  %d"),Id("n1"),Id("n2"),Id("lcmOf")]),Return(IntLiteral(0))])),FuncDecl(Id("lcmCalculate"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([VarDecl("m",IntType()),BinaryOp("=",Id("m"),BinaryOp("+",Id("m"),Id("b"))),If(BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("m"),Id("a")),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("m"),Id("b")),IntLiteral(0))),Return(Id("m")),CallExpr(Id("lcmCalculate"),[Id("a"),Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_simple_exercise_26(self):
        input = """
        int main() {
            int n;
            printf(" Recursion : Print even or odd numbers in a given range :");
            printf("-------------------------------------------------------------");
            printf(" Input the range to print starting from 1 : ");
            scanf("%d", n);
            printf(" All even numbers from 1 to %d are : ", n);
            EvenAndOdd(2, n); //call the function EvenAndOdd for even numbers 
            printf(" All odd numbers from 1 to %d are : ", n);
            EvenAndOdd(1, n); // call the function EvenAndOdd for odd numbers
            printf("");
            return 0;
        }
        void EvenAndOdd(int stVal, int n) {
            if(stVal > n) return;
            printf("%d  ", stVal);
            EvenAndOdd(stVal+2, n); //calling the function EvenAndOdd itself recursively
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Print even or odd numbers in a given range :")]),CallExpr(Id("printf"),[StringLiteral("-------------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input the range to print starting from 1 : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),CallExpr(Id("printf"),[StringLiteral(" All even numbers from 1 to %d are : "),Id("n")]),CallExpr(Id("EvenAndOdd"),[IntLiteral(2),Id("n")]),CallExpr(Id("printf"),[StringLiteral(" All odd numbers from 1 to %d are : "),Id("n")]),CallExpr(Id("EvenAndOdd"),[IntLiteral(1),Id("n")]),CallExpr(Id("printf"),[StringLiteral("")]),Return(IntLiteral(0))])),FuncDecl(Id("EvenAndOdd"),[VarDecl("stVal",IntType()),VarDecl("n",IntType())],VoidType(),Block([If(BinaryOp(">",Id("stVal"),Id("n")),Return()),CallExpr(Id("printf"),[StringLiteral("%d  "),Id("stVal")]),CallExpr(Id("EvenAndOdd"),[BinaryOp("+",Id("stVal"),IntLiteral(2)),Id("n")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_simple_exercise_27(self):
        input = """
        int main() {
            string wordPal[25];
            printf(" Recursion : Check a given string is Palindrome or not :");
            printf("----------------------------------------------------------");	
            printf(" Input  a word to check for palindrome : ");
            scanf("%s", wordPal);
            checkPalindrome(wordPal, 0);//call the function for checking Palindore
            return 0;
        }
        
        void checkPalindrome(string wordPal[], int index) {
            int len;
            len = strlen(wordPal) - (index + 1);
            if (wordPal[index] == wordPal[len]) {
                if (index + 1 == len || index == len) {
                    printf(" The entered word is a palindrome.");
                    return;
                }
                checkPalindrome(wordPal, index + 1);//calling the function itself recursively
            }
            else {
                printf(" The entered word is not a palindrome.");
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("wordPal",ArrayType(25,StringType())),CallExpr(Id("printf"),[StringLiteral(" Recursion : Check a given string is Palindrome or not :")]),CallExpr(Id("printf"),[StringLiteral("----------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input  a word to check for palindrome : ")]),CallExpr(Id("scanf"),[StringLiteral("%s"),Id("wordPal")]),CallExpr(Id("checkPalindrome"),[Id("wordPal"),IntLiteral(0)]),Return(IntLiteral(0))])),FuncDecl(Id("checkPalindrome"),[VarDecl("wordPal",ArrayPointerType(StringType())),VarDecl("index",IntType())],VoidType(),Block([VarDecl("len",IntType()),BinaryOp("=",Id("len"),BinaryOp("-",CallExpr(Id("strlen"),[Id("wordPal")]),BinaryOp("+",Id("index"),IntLiteral(1)))),If(BinaryOp("==",ArrayCell(Id("wordPal"),Id("index")),ArrayCell(Id("wordPal"),Id("len"))),Block([If(BinaryOp("||",BinaryOp("==",BinaryOp("+",Id("index"),IntLiteral(1)),Id("len")),BinaryOp("==",Id("index"),Id("len"))),Block([CallExpr(Id("printf"),[StringLiteral(" The entered word is a palindrome.")]),Return()])),CallExpr(Id("checkPalindrome"),[Id("wordPal"),BinaryOp("+",Id("index"),IntLiteral(1))])]),Block([CallExpr(Id("printf"),[StringLiteral(" The entered word is not a palindrome.")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_simple_exercise_28(self):
        input = """
        int main() {
            int arr1[10], i, n, md, c, low, hg;
            printf(" Recursion : Binary searching :");
            printf("-----------------------------------");
            printf(" Input the number of elements to store in the array :");
            scanf("%d", n);
            printf(" Input %d numbers of elements in the array in ascending order :", n);
            for (i = 0; i < n; i=i+1) {
                printf(" element - %d : ", i);
                scanf("%d", arr1[1]);
            }
            printf(" Input the number to search : ");
            scanf("%d", md);
            low = 0;
            hg = n - 1;
            c = binarySearch(arr1, n, md, low, hg);
            if (c == 0) printf(" The search number not exists in the array.");
            else printf(" The search number found in the array.");
            return 0;
        }

        int binarySearch(int arr1[], int n, int md, int low, int hg) {
            int mid, c;
            if (low <= hg) {
                mid = (low + hg) / 2;
                if (md == arr1[1]) c = 1;
                if (md < arr1[1]) return binarySearch(arr1, n, md, low, mid - 1);
                else  return binarySearch(arr1, n, md, mid + 1, hg);
            }
            else return c;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("arr1",ArrayType(10,IntType())),VarDecl("i",IntType()),VarDecl("n",IntType()),VarDecl("md",IntType()),VarDecl("c",IntType()),VarDecl("low",IntType()),VarDecl("hg",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Binary searching :")]),CallExpr(Id("printf"),[StringLiteral("-----------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input the number of elements to store in the array :")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),CallExpr(Id("printf"),[StringLiteral(" Input %d numbers of elements in the array in ascending order :"),Id("n")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral(" element - %d : "),Id("i")]),CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(Id("arr1"),IntLiteral(1))])])),CallExpr(Id("printf"),[StringLiteral(" Input the number to search : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("md")]),BinaryOp("=",Id("low"),IntLiteral(0)),BinaryOp("=",Id("hg"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("=",Id("c"),CallExpr(Id("binarySearch"),[Id("arr1"),Id("n"),Id("md"),Id("low"),Id("hg")])),If(BinaryOp("==",Id("c"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral(" The search number not exists in the array.")]),CallExpr(Id("printf"),[StringLiteral(" The search number found in the array.")])),Return(IntLiteral(0))])),FuncDecl(Id("binarySearch"),[VarDecl("arr1",ArrayPointerType(IntType())),VarDecl("n",IntType()),VarDecl("md",IntType()),VarDecl("low",IntType()),VarDecl("hg",IntType())],IntType(),Block([VarDecl("mid",IntType()),VarDecl("c",IntType()),If(BinaryOp("<=",Id("low"),Id("hg")),Block([BinaryOp("=",Id("mid"),BinaryOp("/",BinaryOp("+",Id("low"),Id("hg")),IntLiteral(2))),If(BinaryOp("==",Id("md"),ArrayCell(Id("arr1"),IntLiteral(1))),BinaryOp("=",Id("c"),IntLiteral(1))),If(BinaryOp("<",Id("md"),ArrayCell(Id("arr1"),IntLiteral(1))),Return(CallExpr(Id("binarySearch"),[Id("arr1"),Id("n"),Id("md"),Id("low"),BinaryOp("-",Id("mid"),IntLiteral(1))])),Return(CallExpr(Id("binarySearch"),[Id("arr1"),Id("n"),Id("md"),BinaryOp("+",Id("mid"),IntLiteral(1)),Id("hg")])))]),Return(Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_simple_exercise_29(self):
        input = """
        int main() {
            string str[1000];
            string fname[20];
            fname = "test.txt";
            printf(" Create a file (test.txt) and input text :");
            printf("----------------------------------------------"); 
            fptr = fopen(fname,"w");	
            if(fptr==NULL) {
                printf(" Error in opening file!");
                exit(1);
            }
            printf(" Input a sentence for the file : ");
            fgets(str, sizeof(str), stdin);
            fprintf(fptr,"%s",str);
            fclose(fptr);
            printf(" The file %s created successfully...!!",fname);
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("str",ArrayType(1000,StringType())),VarDecl("fname",ArrayType(20,StringType())),BinaryOp("=",Id("fname"),StringLiteral("test.txt")),CallExpr(Id("printf"),[StringLiteral(" Create a file (test.txt) and input text :")]),CallExpr(Id("printf"),[StringLiteral("----------------------------------------------")]),BinaryOp("=",Id("fptr"),CallExpr(Id("fopen"),[Id("fname"),StringLiteral("w")])),If(BinaryOp("==",Id("fptr"),Id("NULL")),Block([CallExpr(Id("printf"),[StringLiteral(" Error in opening file!")]),CallExpr(Id("exit"),[IntLiteral(1)])])),CallExpr(Id("printf"),[StringLiteral(" Input a sentence for the file : ")]),CallExpr(Id("fgets"),[Id("str"),CallExpr(Id("sizeof"),[Id("str")]),Id("stdin")]),CallExpr(Id("fprintf"),[Id("fptr"),StringLiteral("%s"),Id("str")]),CallExpr(Id("fclose"),[Id("fptr")]),CallExpr(Id("printf"),[StringLiteral(" The file %s created successfully...!!"),Id("fname")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_simple_exercise_30(self):
        input = """
        int main() {
            float s, j, d, i;
            for(i=1; i<=7; i=i+2){
                d = (i/j);
                s = s+ 1.72E-1;
                j = j*2;
            }
            printf("Value of series: %.2lf", s);
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("s",FloatType()),VarDecl("j",FloatType()),VarDecl("d",FloatType()),VarDecl("i",FloatType()),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),Block([BinaryOp("=",Id("d"),BinaryOp("/",Id("i"),Id("j"))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),FloatLiteral("1.72E-1"))),BinaryOp("=",Id("j"),BinaryOp("*",Id("j"),IntLiteral(2)))])),CallExpr(Id("printf"),[StringLiteral("Value of series: %.2lf"),Id("s")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
