import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_redeclared_custom_function(self):
        """
        int foo(){
            return 0;
        }
        int foo(){
            foo();
            return 1;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(0))])),FuncDecl(Id("foo"),[],IntType(),Block([CallExpr(Id("foo"),[]),Return(IntLiteral(1))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_available_function(self):
        """
        int getInt(){
            return 123;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("getInt"),[],IntType(),Block([Return(IntLiteral(123))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Redeclared Function: getInt"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_main_function(self):
        """
        void main(){
            return;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([Return()])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_global_variable(self):
        """
        int a;
        float a;
        void main(){
            return;
        }
        """
        input = (Program([VarDecl("a",IntType()),VarDecl("a",FloatType()),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_local_variable(self):
        """
        int a;
        void main(){
            int a;
            float a;
            return;
        }
        """
        input = (Program([VarDecl("a",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("a",FloatType()),Return()]))]))
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_difftype_variable(self):
        """
        int foo(){
            float a;
            int a;
            return 123;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("a",IntType()),Return(IntLiteral(123))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_parameter_outside_main(self):
        """
        void foo(int a, int a){
            return;
        }
        void main(){
            foo(0,1);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("a",IntType())],VoidType(),Block([Return()])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(0),IntLiteral(1)]),Return()]))]))
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_parameter_and_local(self):
        """
        int foo(int a){
            float a;
            return 123;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([VarDecl("a",FloatType()),Return(IntLiteral(123))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_undeclared_custom_function(self):
        """
        void main(){
            print("Hello Python 3");
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("print"),[IntLiteral("Hello Python 3")]),Return()]))]))
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_undeclared_function_undefined(self):
        """
        int a;
        void main(){
            a = foo(1) + 2;
            return;
        }
        """
        input = (Program([VarDecl("a",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(1)]),IntLiteral(2))),Return()]))]))
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_undeclared_two_function(self):
        """
        int foo(){
            return 1;
        }
        int foo2(){
            return foo1();
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl(Id("foo2"),[],IntType(),Block([Return(CallExpr(Id("foo1"),[]))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_available_function(self):
        """
        void main(){
            getint();
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("getint"),[]),Return()]))]))
        expect = "Undeclared Function: getint"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_normal_variable(self):
        """
        void main(){
            a = 1;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),IntLiteral(1)),Return()]))]))
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_difftype_variable(self):
        """
        int a;
        void main(){
            arr[1] = 0;
            return;
        }
        """
        input = (Program([VarDecl("a",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(1)),IntLiteral(0)),Return()]))]))
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_variable_scope(self):
        """
        int foo(int a){
            return b;
        }
        void main(){
            foo(2);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(2)]),Return()]))]))
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclared_variable_difffunction(self):
        """
        void foo(){
            int a;
            return;
        }
        void main(){
            foo();
            if(a==1){
                putIntLn(5);
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",IntType()),Return()])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([CallExpr(Id("putIntLn"),[IntLiteral(5)])])),Return()]))]))
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_parameter(self):
        """
        int foo(int a, int b){
            return c + 1;
        }
        void main(){
            foo(1,"Hello");
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([Return(BinaryOp("+",Id("c"),IntLiteral(1)))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(1),IntLiteral("Hello")]),Return()]))]))
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_arraypointer(self):
        """
        int[] foo(int a[]){
            return b;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_in_if(self):
        """
        void main(){
            if(a==2){
                putIntLn(2);
            }
            else{
                putInt(2);
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(2)),Block([CallExpr(Id("putIntLn"),[IntLiteral(2)])]),Block([CallExpr(Id("putInt"),[IntLiteral(2)])])),Return()]))]))
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_in_for(self):
        """
        void foo(){
            for(a;a<10;a=a+1){
                putIntLn(2);
            }
            return;
        }
        void main(){
            foo();
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],VoidType(),Block([For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[IntLiteral(2)])])),Return()])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))]))
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_in_call(self):
        """
        void main(){
            putFloatLn(floatLit);
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putFloatLn"),[Id("floatLit")]),Return()]))]))
        expect = "Undeclared Identifier: floatLit"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_in_dowhile(self):
        """
        void main(){
            do a = 1;
            while (a<2);
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1))],BinaryOp("<",Id("a"),IntLiteral(2))),Return()]))]))
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_in_arraycell(self):
        """
        void main(){
            int a[10];
            a[b[1]] = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(1))),IntLiteral(10)),Return()]))]))
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_mismatch_sintle_if(self):
        """
        void main(){
            int a;
            if(a+2){
                putIntLn(2);
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("+",Id("a"),IntLiteral(2)),Block([CallExpr(Id("putIntLn"),[IntLiteral(2)])])),Return()]))]))
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(2)),Block([CallExpr(Id(putIntLn),[IntLiteral(2)])]))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_mismatch_multiple_if(self):
        """
        void main(){
            int a,b;
            if(a==1){
                if(b+2){
                    putIntLn(2);
                }
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([If(BinaryOp("+",Id("b"),IntLiteral(2)),Block([CallExpr(Id("putIntLn"),[IntLiteral(2)])]))])),Return()]))]))
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(b),IntLiteral(2)),Block([CallExpr(Id(putIntLn),[IntLiteral(2)])]))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_mismatch_sintle_for_exppr1(self):
        """
        void main(){
            int a;
            float b;
            for(b;a<10;a=a+1){
                putint("Wrong in expression 1");
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),For(Id("b"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putint"),[IntLiteral("Wrong in expression 1")])])),Return()]))]))
        expect = "Type Mismatch In Statement: For(Id(b);BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putint),[IntLiteral(Wrong in expression 1)])]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_mismatch_signle_for_exppr2(self):
        """
        void main(){
            int a;
            float b;
            for(1;b;a=a+1){
                putint("Wrong in expression 2");
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),For(IntLiteral(1),Id("b"),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putint"),[IntLiteral("Wrong in expression 2")])])),Return()]))]))
        expect = "Type Mismatch In Statement: For(IntLiteral(1);Id(b);BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putint),[IntLiteral(Wrong in expression 2)])]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_mismatch_signle_for_exppr3(self):
        """
        void main(){
            int a;
            float b;
            for(1;a<10;b){
                putint("Wrong in expression 3");
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),For(IntLiteral(1),BinaryOp("<",Id("a"),IntLiteral(10)),Id("b"),Block([CallExpr(Id("putint"),[IntLiteral("Wrong in expression 3")])])),Return()]))]))
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BinaryOp(<,Id(a),IntLiteral(10));Id(b);Block([CallExpr(Id(putint),[IntLiteral(Wrong in expression 3)])]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_mismatch_sintle_dowhile(self):
        """
        void main(){
            int a;
            do putIntLn(2);
            while(a);
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),Dowhile([CallExpr(Id("putIntLn"),[IntLiteral(2)])],Id("a")),Return()]))]))
        expect = "Type Mismatch In Statement: Dowhile([CallExpr(Id(putIntLn),[IntLiteral(2)])],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_mismatch_nest_dowhile(self):
        """
        void main(){
            int a,b;
            do do a=1; while(a<10);
            while(b);
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),Dowhile([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1))],BinaryOp("<",Id("a"),IntLiteral(10)))],Id("b")),Return()]))]))
        expect = "Type Mismatch In Statement: Dowhile([Dowhile([BinaryOp(=,Id(a),IntLiteral(1))],BinaryOp(<,Id(a),IntLiteral(10)))],Id(b))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_mismatch_void_return(self):
        """
        void main(){
            return 2;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([Return(IntLiteral(2))]))]))
        expect = "Type Mismatch In Statement: Return(IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_mismatch_wrong_normal_type_return(self):
        """
        int foo(){
            int a;
            return a;
        }
        void main(){
            int a;
            a = foo();
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],IntType(),Block([VarDecl("a",IntType()),Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[])),Return()]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_mismatch_coercion_return(self):
        """
        float foo(int a){
            return a;
        }
        void main(){
            float a;
            int b;
            a = foo(b);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],FloatType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),VarDecl("b",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[Id("b")])),Return()]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_mismatch_arraypointer_return(self):
        """
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([VarDecl("a",ArrayType(10,IntType())),Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_mismatch_difftype(self):
        """
        int foo(){
            int a,b,c;
            return a==b||a!=c;
        }
        void main(){
            int a;
            a = foo();
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Return(BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("!=",Id("a"),Id("c"))))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[])),Return()]))]))
        expect = "Type Mismatch In Statement: Return(BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(a),Id(c))))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_mismatch_arr_eppr_wrong_type(self):
        """
        void main(){
            int arr;
            arr[0] = 100;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("arr",IntType()),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(0)),IntLiteral(100)),Return()]))]))
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_mismatch_arr_eppr_wrong_func(self):
        """
        int foo(int a){
            return a;
        }
        void main(){
            foo(10)[0] = 100;
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(10)]),IntLiteral(0)),IntLiteral(100)),Return()]))]))
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[IntLiteral(10)]),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_mismatch_arr_eppr_nested(self):
        """
        void main(){
            float arr[10];
            int a;
            arr[a[0]] = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("arr",ArrayType(10,FloatType())),VarDecl("a",IntType()),BinaryOp("=",ArrayCell(Id("arr"),ArrayCell(Id("a"),IntLiteral(0))),IntLiteral(10)),Return()]))]))
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_mismatch_indx_wrong_type(self):
        """
        void main(){
            float idx;
            int arr[10],str[10];
            arr[str[idx]] = 10;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("idx",FloatType()),VarDecl("arr",ArrayType(10,IntType())),VarDecl("str",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("arr"),ArrayCell(Id("str"),Id("idx"))),IntLiteral(10))]))]))
        expect = "Type Mismatch In Expression: ArrayCell(Id(str),Id(idx))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_mismatch_idx_in_stmt(self):
        """
        int foo(int a){
            return a;
        }
        void main(){
            int a;
            if(a==1){
                int arr[10];
                arr[foo("int")] = 10;
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([VarDecl("arr",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("arr"),CallExpr(Id("foo"),[StringLiteral("int")])),IntLiteral(10))])),Return()]))]))
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[StringLiteral(int)])"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_mismatch_multi_eppr(self):
        """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int arr[10];
            boolean bool;
            foo(arr)[arr[bool]] = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("arr",ArrayType(10,IntType())),VarDecl("bool",BoolType()),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[Id("arr")]),ArrayCell(Id("arr"),Id("bool"))),IntLiteral(10)),Return()]))]))
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),Id(bool))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_mismatch_binary_booltype(self):
        """
        void main(){
            boolean bool;
            bool = 1 + 2;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("bool",BoolType()),BinaryOp("=",Id("bool"),BinaryOp("+",IntLiteral(1),IntLiteral(2))),Return()]))]))
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(bool),BinaryOp(+,IntLiteral(1),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_mismatch_binary_IntType(self):
        """
        float foo(){
            return 1;
        }
        void main(){
            int a;
            a = foo();
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],FloatType(),Block([Return(IntLiteral(1))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[])),Return()]))]))
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_mismatch_binary_assgn(self):
        """
        void main(){
            int a;
            boolean b;
            a = 2 + 3 / 4 - b;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",BoolType()),BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",IntLiteral(2),BinaryOp("/",IntLiteral(3),IntLiteral(4))),Id("b"))),Return()]))]))
        expect = "Type Mismatch In Expression: BinaryOp(-,BinaryOp(+,IntLiteral(2),BinaryOp(/,IntLiteral(3),IntLiteral(4))),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_mismatch_binary_int(self):
        """
        void main(){
            int a,b;
            a = 1 + b;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(1),Id("b"))),Return()]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_mismatch_binary_func(self):
        """
        boolean foo(){
            return true;
        }
        void main(){
            int a;
            a = foo();
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],BoolType(),Block([Return(BooleanLiteral("true"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[]))]))]))
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,445))

    #* Failed
    def test_mismatch_unary_neg(self):
        """
        int foo(int a){
            return -a;
        }
        void main(){
            int a;
            float b;
            b = foo(a);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(UnaryOp("-",Id("a")))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),BinaryOp("=",Id("b"),CallExpr(Id("foo"),[Id("a")])),Return()]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_mismatch_unary_not(self):
        """
        void main(){
            int bool;
            if(!bool){
                putInt(10);
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("bool",IntType()),If(UnaryOp("!",Id("bool")),Block([CallExpr(Id("putInt"),[IntLiteral(10)])])),Return()]))]))
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(bool))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_mismatch_wrong_size_param(self):
        """
        int foo(int a, int b){
            return a + b;
        }
        void main(){
            int a;
            a = foo(10);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[IntLiteral(10)])),Return()]))]))
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_mismatch_wrong_type_param(self):
        """
        int foo(int a, float b, int c[]){
            return a;
        }
        void main(){
            int a;
            int arr[10];
            a = foo(10,"int",arr);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("arr",ArrayType(10,IntType())),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[IntLiteral(10),StringLiteral("int"),Id("arr")])),Return()]))]))
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(10),StringLiteral(int),Id(arr)])"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_mismatch_wrong_type_in_stmt(self):
        """
        int foo(int a, int b, int c[]){
            return a;
        }
        void main(){
            int a;
            if(true){
                int arr[10];
                a = foo(a,"int",arr);
            }
            else{
                a = foo(10);
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BooleanLiteral("true"),Block([VarDecl("arr",ArrayType(10,IntType())),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[Id("a"),StringLiteral("int"),Id("arr")]))]),Block([BinaryOp("=",Id("a"),CallExpr(Id("foo"),[IntLiteral(10)]))])),Return()]))]))
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),StringLiteral(int),Id(arr)])"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_main_not_return(self):
        """
        void main(){}
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_func_custom_not_return(self):
        """
        void foo(int a){
            a = 10;
        }
        void main(){
            foo(10);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],VoidType(),Block([BinaryOp("=",Id("a"),IntLiteral(10))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(10)]),Return()]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_if_stmt_not_return(self):
        """
        void main(){
            int a;
            if(a==1){
                return;
            }
            else{
                a = 10;
            }
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Return()]),Block([BinaryOp("=",Id("a"),IntLiteral(10))]))]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_else_stmt_not_return(self):
        """
        void main(){
            boolean b;
            if(b){
                putIntLn(1);
            }
            else{
                return;
            }
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("b",BoolType()),If(Id("b"),Block([CallExpr(Id("putIntLn"),[IntLiteral(1)])]),Block([Return()]))]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_nest_if_not_return(self):
        """
        void main(){
            int a;
            if(a=="abc"){
                int b;
                if(b==1){
                    return;
                }
                else{

                }
            }
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral("abc")),Block([VarDecl("b",IntType()),If(BinaryOp("==",Id("b"),IntLiteral(1)),Block([Return()]),Block([]))]))]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_nest_for_not_return(self):
        """
        void main(){
            int a;
            for(a;a<10;a=a+1){
                if(a<5) return;
                else a = 2;
            }
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([If(BinaryOp("<",Id("a"),IntLiteral(5)),Return(),BinaryOp("=",Id("a"),IntLiteral(2)))]))]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_nest_else_not_return(self):
        """
        void main(){
            boolean bool;
            if(bool){
                int a;
            }
            else{
                if(bool==true){
                    return;
                }
            }
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("bool",BoolType()),If(Id("bool"),Block([VarDecl("a",IntType())]),Block([If(BinaryOp("==",Id("bool"),BooleanLiteral("true")),Block([Return()]))]))]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_break_in_main(self):
        """
        void main(){
            break;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([Break(),Return()]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_wrong_type_array_return(self):
        """
        int[] foo(boolean b[]){
            return b;
        }
        void main(){
            boolean b[10];
            foo(b);
            return ;
        }
        """
        input = Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("b",ArrayType(10,BoolType())),CallExpr(Id("foo"),[Id("b")]),Return()]))])
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_break_in_nest_for(self):
        """
        void main(){
            int a;
            if(a==1){
                for(a;a<10;a=a+1){
                    putIntLn(10);
                }
                break;
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[IntLiteral(10)])])),Break()])),Return()]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_continue_in_main(self):
        """
        void main(){
            continue;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([Continue(),Return()]))]))
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_break_in_if(self):
        """
        void main(){
            int a;
            if(a==1){
                do a=10;
                while(a>10);
                break;
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(10))],BinaryOp(">",Id("a"),IntLiteral(10))),Break()])),Return()]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_break_and_continue_in_if(self):
        """
        void main(){
            int a;
            if(a==1){
                break;
            }
            else{
                continue;
            }
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Break()]),Block([Continue()]))]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_break_true_and_false(self):
        """
        void main(){
            int a;
            for(a;a<10;a=a+1){
                putIntLn(10);
                if(a==1){
                    break;
                }
            }
            if(a==10){
                break;
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[IntLiteral(10)]),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Break()]))])),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([Break()])),Return()]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_break_nest_two_loop(self):
        """
        void main(){
            int a;
            for(a;a<10;a=a+1){
                int b;
                for(0;b<10;b=b+1){
                    if(a==1){
                        break;
                    } else{
                        return;
                    }
                }
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([VarDecl("b",IntType()),For(IntLiteral(0),BinaryOp("<",Id("b"),IntLiteral(10)),BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Break()]),Block([Return()]))]))])),Return()]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_blank_func(self):
        """
        int a;
        """
        input = (Program([VarDecl("a",IntType())]))
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_recall_foo_type_mismatch_in_block(self):
        """
        void foo(){
        }
        void main(){
            foo = 1;
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("foo"),IntLiteral(1)),CallExpr(Id("foo"),[])]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_wrong_main_type(self):
        """
        int a;
        void foo(){
            return;
        }
        int main(){
            foo();
            return 1;
        }
        """
        input = (Program([VarDecl("a",IntType()),FuncDecl(Id("foo"),[],VoidType(),Block([Return()])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[]),Return(IntLiteral(1))]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_unreachable_func(self):
        """
        int foo(int a){
            return a;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_recursive(self):
        """
        int foo(int a){
            a = a -1;
            return foo(a);
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Return(CallExpr(Id("foo"),[Id("a")]))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_many_func(self):
        """
        int foo1(int a){
            return a;
        }
        void foo2(){
            int a;
            a = foo1(10);
            return;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo1"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("foo2"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo1"),[IntLiteral(10)])),Return()])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_wrong_left_type(self):
        """
        void main(){
            1 + 2 = 3;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),Return()]))]))
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_wrong_left_type_is_func(self):
        """
        void main(){
            putIntLn() = 20;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",CallExpr(Id("putIntLn"),[]),IntLiteral(20)),Return()]))]))
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_left_is_not_storage(self):
        """
        void main(){
            int a;
            a + 1 = a;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(1)),Id("a")),Return()]))]))
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_not_return_block(self):
        """
        void main(){
            int a;
            a + 1 = a;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([Return()])]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_return_in_loop(self):
        """
        string foo(){
            do
                return "hello";
                continue;
                {
                    1 + 1;
                }
            while(true);
            int i;
            for (i=0;i<=10;i=i+1){
                return "hello";
            }
        }
        void main(){
            foo();
            return;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Dowhile([Return(StringLiteral("hello")),Block([BinaryOp("+",IntLiteral(1),IntLiteral(1))])],BooleanLiteral("true")),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Return(StringLiteral("hello"))]))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_var_undeclared_outsit_small_scope(self):
        """
        void main(){
            int a;
            for(a;a<10;a=a+1){
                putIntLn(10);
                if(a==1){
                    break;
                }
            }
            if(a==10){
                int b;
            }
            b = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[IntLiteral(10)]),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Break()]))])),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([VarDecl("b",IntType())])),BinaryOp("=",Id("b"),IntLiteral(10)),Return()]))]))
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_mismatch_argument_is_type(self):
        """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int arr[10];
            boolean bool;
            foo(arr[1])[arr[bool]] = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("arr",ArrayType(10,IntType())),VarDecl("bool",BoolType()),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[ArrayCell(Id("arr"),IntLiteral(1))]),ArrayCell(Id("arr"),Id("bool"))),IntLiteral(10)),Return()]))]))
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(arr),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_wrong_return_array_type(self):
        """
        int[] foo1(int a[]){
            return a;
        }
        int foo2(int a[]){
            return a[10];
        }
        void main(){
            int a[10];
            foo2(foo1(a[10]));
            return;
        }
        """
        input =Program([FuncDecl(Id("foo1"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("foo2"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([Return(ArrayCell(Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo2"),[CallExpr(Id("foo1"),[ArrayCell(Id("a"),IntLiteral(1))])]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo1),[ArrayCell(Id(a),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_wrong_binayry_op_in_if(self):
        """
        void main(){
            int a[10];
            if (a==10){
                return;
            }
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([Return()])),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_return_in_single_if(self):
        """
        void main(){
            int a[10];
            if (a[0]==10){
                return;
            }  
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),If(BinaryOp("==",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(10)),Block([Return()]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_var_outside_do_scope(self):
        """
        void main(){
            int i;
            do {
                int a;
                a=a+1;
            }
            a=a+1;
            while(true);
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BooleanLiteral("true"))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_return_many_if(self):
        """
        void main(){
            int a;
            a=0;
            if (a==10){
                for (a=0;a<=10;a=a+1){
                    return ;
                }
            }
            else{
                if (a==1){
                    return ;
                }
                else{
                    return ;
                }
            }
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(0)),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([Return()]))]),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Return()]),Block([Return()]))]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_blank_error(self):
        """
        void main(){
            int a,b,c;
            do 
            for (a=0;a<=10;a=a+1){
                return ;
            }
            if (b==10) return ;
            while(true);
            
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([Return()])),If(BinaryOp("==",Id("b"),IntLiteral(10)),Return())],BooleanLiteral("true"))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_continue_outside_do(self):
        """
        void main(){
            do 
            {
                int a;
                a=a+1;
                break;
            }
            while(true);
            continue;
            return;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Break()])],BooleanLiteral("true")),Continue(),Return()]))])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_many_param_same_name(self):
        """
        int a,b,c;
        int[] foo(int a,int a){
            int b[10];
            return foo(10);
        }
        void main(){
            foo(10);
            return ;
        }
        """
        input =Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([VarDecl("b",ArrayType(10,IntType())),Return(CallExpr(Id("foo"),[IntLiteral(10)]))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(10)]),Return()]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_wrong_argument_for_foo(self):
        """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int a[10];
            if (a[0]==10){
                a[0]=foo(a)[foo(a)[a]];
            }
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),If(BinaryOp("==",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(10)),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(CallExpr(Id("foo"),[Id("a")]),ArrayCell(CallExpr(Id("foo"),[Id("a")]),Id("a"))))])),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[Id(a)]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_continue_inside_do_nonblock(self):
        """
        string foo(){
            do
                return "hello";
                continue;
                {
                    1 + 1;
                }
            while(true);
        }
        void main(){
            foo();
            return;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Dowhile([Return(StringLiteral("hello")),Continue(),Block([BinaryOp("+",IntLiteral(1),IntLiteral(1))])],BooleanLiteral("true"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_function_return_string(self):
        """
        string foo(){
            int i;
            for(i = 0; i < -1; i = i + 1){
                return "hello";
            }
        }
        void main(){
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Return(StringLiteral("hello"))]))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_nested_block_having_return(self):
        """
        string foo(){
            {
                {
                    return "hello";
                }
            }
        }
        void main(){
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Block([Block([Return(StringLiteral("hello"))])])])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_small_level_declared(self):
        """
        int foo(int a){
            if (a<10){
                string a;
                a="hello";
            }
            else{
                int a[10];
                int i;
                for (i=0;i<=10;i=i+1){
                    a[i]=0;
                }
            }
            return a[10];
        }
        void main(){
            foo(10);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([VarDecl("a",StringType()),BinaryOp("=",Id("a"),StringLiteral("hello"))]),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("a"),Id("i")),IntLiteral(0))]))])),Return(ArrayCell(Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(10)]),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_wrong_type_great_scope(self):
        """
        string a;
        int foo(int a){
            if (a<10){
                string a;
                a="hello";
            }
            else{
                int a;
                int i;
                for (i=0;i<=10;i=i+1){
                    a[i]=0;
                }
            }
            return a[10];
        }
        void main(){
            foo(10);
            return ;
        }
        """
        input =Program([VarDecl("a",StringType()),FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([VarDecl("a",StringType()),BinaryOp("=",Id("a"),StringLiteral("hello"))]),Block([VarDecl("a",IntType()),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("a"),Id("i")),IntLiteral(0))]))])),Return(ArrayCell(Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(10)]),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_left_is_binary(self):
        """
        void main(){
            int a;
            if (a==1){
                a+1=a;
                return ;
            }
            else{
                a=a-1;
                return ;
            }
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(1)),Id("a")),Return()]),Block([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Return()]))]))])
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_return_in_nest_block(self):
        """
        string foo(){
            {
                {
                    if(false){
                        return "hello";
                    }
                    else{
                        return "too";
                    }
                    {}
                }
            }
        }
        void main(){
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Block([Block([If(BooleanLiteral("false"),Block([Return(StringLiteral("hello"))]),Block([Return(StringLiteral("too"))])),Block([])])])])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_return_not_enough(self):
        """
        string foo(){
            {
                {
                    if(false){
                        return "hello";
                    }else{
                      }
                      {
                    }
                }
            }
        }
        void main(){
            foo();
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Block([Block([If(BooleanLiteral("false"),Block([Return(StringLiteral("hello"))]),Block([])),Block([])])])])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_use_var_in_diffscope(self):
        """
        void main(){
            do {
                int a,b,c[10];
            }{
                if (a==10) return 10;
            }while(true);
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(10,IntType()))]),Block([If(BinaryOp("==",Id("a"),IntLiteral(10)),Return(IntLiteral(10)))])],BooleanLiteral("true"))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_argument_not_enough(self):
        """
        int[] foo(int a[], int b){
            return a;
        }
        void main(){
            int a[10];
            int b;
            if (a[10]==10) foo(foo(foo(a,b),b));
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType())],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),If(BinaryOp("==",ArrayCell(Id("a"),IntLiteral(10)),IntLiteral(10)),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("a"),Id("b")]),Id("b")])])),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[Id(a),Id(b)]),Id(b)])])"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_wrong_type_for_void(self):
        """
        void main(){
            int a[10];
            int i;
            for (i=0;i<=10;i=i+1){
                if (i==10) return i;
            }
            return i;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(10)),Return(Id("i")))])),Return()]))])
        expect = "Type Mismatch In Statement: Return(Id(i))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_wrong_type_in_expr1_for(self):
        """
        void main(){
            for (i==0;i<=10;i=i+1){
                if (i==10) return ;
                else return ;
            }
            return ;
        }
        int i;
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("==",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(10)),Return(),Return())])),Return()])),VarDecl("i",IntType())])
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),IntLiteral(10));BinaryOp(==,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),IntLiteral(10)),Return(),Return())]))"
        self.assertTrue(TestChecker.test(input,expect,499))