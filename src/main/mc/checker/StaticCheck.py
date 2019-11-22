
"""
 * @author nhphung
 * Student: Bui Quoc Khai
 * Id: 1711726
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

def flatten(lst):
    retLst = lst
    return reduce(lambda x,y: x + y[1:],retLst,[])

class StaticChecker(BaseVisitor,Utils):

    

    def __init__(self,ast):
        self.reachLst = []
        self.global_envi = [[
        False,
        Symbol("getInt",MType([],IntType())),
        Symbol("putInt",MType([IntType()],VoidType())),
        Symbol("putIntLn",MType([IntType()],VoidType())),
        Symbol("getFloat",MType([],FloatType())),
        Symbol("putFloat",MType([FloatType()],VoidType())),
        Symbol("putFloatLn",MType([FloatType()],VoidType())),
        Symbol("putBool",MType([BoolType()],VoidType())),
        Symbol("putBoolLn",MType([BoolType()],VoidType())),
        Symbol("putString",MType([StringType()],VoidType())),
        Symbol("putStringLn",MType([StringType()],VoidType())),
        Symbol("putLn",MType([],VoidType()))
        ]]
        self.ast = ast

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def RedeclaredFunc(self,ast,c,isParam):
        lst = c[-1][1:]
        if type(ast) is VarDecl:
            if not self.lookup(ast.variable,lst,lambda x: x.name) is None:
                if isParam:
                    raise Redeclared(Parameter(),ast.variable)
                else:
                    raise Redeclared(Variable(),ast.variable)
        elif type(ast) is FuncDecl:
            if not self.lookup(ast.name.name,lst,lambda x: x.name) is None:
                raise Redeclared(Function(),ast.name.name)
        return False

    def NoEntryPoint(self,c):
        c = list(filter(lambda x: type(x) is FuncDecl,c))
        c = reduce(lambda env,decl: env + [Symbol(decl.name.name,MType(decl.param,decl.returnType))],c,[])
        res = self.lookup("main",c,lambda x: x.name)
        if  res is None:
            raise NoEntryPoint()

    def UnreachableFunction(self,c,lst):
        c1 = list(filter(lambda x: type(x) is FuncDecl,c))
        for decl in c1:
            res = self.lookup(decl.name.name,lst,lambda x: x.name)
            if decl.name.name == "main":
                continue
            if res is None:
                raise UnreachableFunction(decl.name.name)

    def BuildContruct(self,ast,lst,isLoop,isNewScope,isParam):
        retLst = list(lst)
        if isNewScope:
            return retLst + [[isLoop]]
        else:
            if type(ast) is FuncDecl or type(ast) is VarDecl:
                if not self.RedeclaredFunc(ast,lst,isParam):
                    retLst[-1].append(Symbol(ast.name.name,MType(ast.param,ast.returnType))) if type(ast) is FuncDecl else retLst[-1].append(Symbol(ast.variable,ast.varType))
        return retLst

    def visitProgram(self,ast,c):
        # Define c list (#c, #function name, # isLoop, #isParam)
        c = [c,"",False,False]
        
        for decl in ast.decl:
            c[0] = self.BuildContruct(decl,c[0],False,False,False)
        lst = list(c)
        for decl in ast.decl:
            c = list(lst)
            if not type(decl) is VarDecl:
                temp = self.visit(decl,c)
        self.UnreachableFunction(ast.decl,self.reachLst)
        self.NoEntryPoint(ast.decl)
        return None

    def visitFuncDecl(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        c[1] = ast.name.name
        c[3] = True
        # c[0] = self.BuildContruct("",c[0],False,True,False)
        # for param in ast.param:
        #     c[0] = self.BuildContruct(param,c[0],False,False)
        if not self.visit(ast.body,c):
            raise FunctionNotReturn(ast.name.name)
        return None

    def visitVarDecl(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        return self.BuildContruct(ast,c[0],False,False,False)

    def visitBlock(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        retIf = False
        retNoIf = False
        retBlock = False
        retDoWhile = False
        res = self.lookup(c[1],c[0][0][1:],lambda x: x.name)
        if c[2]:
            c[2] = False
            c[0] = self.BuildContruct("",c[0],True,True,False)
        else:
            c[0] = self.BuildContruct("",c[0],False,True,False)
        #Get parameter
        if c[3]:
            c[3] = False
            for param in res.mtype.partype:
                c[0] = self.BuildContruct(param,c[0],False,False,True)
        #Visit member
        saveLst = list(c)
        for member in ast.member:
            c = list(saveLst)
            if type(member) is VarDecl:
                c[0] = self.visit(member,c)
            elif type(member) is If:
                retIf = self.visit(member,c)
            elif type(member) is Return:
                retNoIf = self.visit(member,c)
            elif type(member) is Block:
                retBlock = self.visit(member,c)
            elif type(member) is Dowhile:
                retDoWhile = self.visit(member,c)
            else:
                temp = self.visit(member,c)
        c = list(saveLst)
        if type(res.mtype.rettype) is VoidType:
            return True
        return retIf or retNoIf or retBlock or retDoWhile

    def visitIf(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        retThen = False
        retElse = False
        if not type(self.visit(ast.expr,c)) is BoolType:
            raise TypeMismatchInStatement(ast)
        retThen = self.visit(ast.thenStmt,c)
        if not ast.elseStmt is None:
            retElse = self.visit(ast.elseStmt,c)
        if not isinstance(retElse,bool):
            retElse = False
        if not isinstance(retThen,bool):
            retThen = False
        return retThen and retElse

    def visitFor(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        if not type(self.visit(ast.expr2,c)) is BoolType:
            raise TypeMismatchInStatement(ast)
        if not type(self.visit(ast.expr1,c)) is IntType or not type(self.visit(ast.expr3,c)) is IntType:
            raise TypeMismatchInStatement(ast)
        c[2] = True
        self.visit(ast.loop,c)
        return None

    def visitDowhile(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        retDoWhile = False
        if not type(self.visit(ast.exp,c)) is BoolType:
            raise TypeMismatchInStatement(ast)
        c[0] = self.BuildContruct("",c[0],True,True,False)
        saveLst = list(c)
        for stmt in ast.sl:
            c = list(saveLst)
            if type(stmt) is Return:
                retDoWhile = self.visit(stmt,c)
            else:
                self.visit(stmt,c)
        return retDoWhile
        
    def visitBreak(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        for i in c[0][::-1]:
            if i[0]:
                return None
        raise BreakNotInLoop()

    def visitContinue(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        for i in c[0][::-1]:
            if i[0]:
                return None
        raise ContinueNotInLoop()

    def visitReturn(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        sym = self.lookup(c[1],c[0][0][1:],lambda x: x.name)
        if ast.expr is None and type(sym.mtype.rettype) is VoidType:
            return True
        res = self.visit(ast.expr,c)
        if type(sym.mtype.rettype) is VoidType and not type(res) is None:
            raise TypeMismatchInStatement(ast)
        if not type(sym.mtype.rettype) is type(res):
            if type(sym.mtype.rettype) is FloatType:
                if not type(res) is IntType and not type(res) is FloatType:
                    raise TypeMismatchInStatement(ast)
            elif type(sym.mtype.rettype) is ArrayPointerType:
                if type(res) is ArrayPointerType or type(res) is ArrayType:
                    if not isinstance(res.eleType,type(sym.mtype.rettype.eleType)):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        if type(res) is ArrayType or type(sym.mtype.rettype) is ArrayPointerType:
            if not isinstance(res.eleType,type(sym.mtype.rettype.eleType)):
                raise TypeMismatchInStatement(ast)
        return True

    def visitCallExpr(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        res = self.lookup(ast.method.name,c[0][0][1:],lambda x: x.name)
        resVar = self.lookup(ast.method.name,flatten(c[0][1:]),lambda x: x.name)
        if not resVar is None or res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        if c[1] != ast.method.name:
            self.reachLst.append(ast.method)
        # Check parameter args
        paramLst = ast.param
        paramType = reduce(lambda env,param: env + [self.visit(param,c)],ast.param,[])
        if len(paramLst) != len(res.mtype.partype):
            raise TypeMismatchInExpression(ast)
        for element in zip(paramType,res.mtype.partype):
            if type(element[1]) is VarDecl and type(element[1].varType) is ArrayPointerType:
                if type(element[0]) is ArrayPointerType or type(element[0]) is ArrayType:
                    if type(element[1]) is VarDecl:
                        if not type(element[0].eleType) is type(element[1].varType.eleType):
                            raise TypeMismatchInExpression(ast)
                    else:
                        if not type(element[0].eleType) is type(element[1].eleType):
                            raise TypeMismatchInExpression(ast)
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                if type(element[1]) is VarDecl:
                    if not isinstance(element[0],type(element[1].varType)):
                        raise TypeMismatchInExpression(ast)
                else:
                    if element[0] != element[1]:
                        raise TypeMismatchInExpression(ast)
                

        return self.lookup(ast.method.name,c[0][0][1:],lambda x: x.name).mtype.rettype

    def visitId(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        lst = flatten(c[0])
        res = self.lookup(ast.name,lst[::-1],lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(),ast.name)
        return res.mtype

    def visitArrayCell(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        # Type Mismatch In Expression
        res = None
        if type(ast.arr) is Id:
            res = self.visit(ast.arr,c)
            if not type(res) is ArrayType and not type(res) is ArrayPointerType:
                raise TypeMismatchInExpression(ast)
        else:
            res = self.visit(ast.arr,c)
            if not type(res) is ArrayPointerType:
                raise TypeMismatchInExpression(ast)
        
        if not isinstance(self.visit(ast.idx,c),IntType):
            raise TypeMismatchInExpression(ast)

        return res.eleType
       
    def visitBinaryOp(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        op = ast.op
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)
        if op=="&&" or op=="||":
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op=="+" or op=="-" or op=="*" or op=="/":
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            elif type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op=="=":
            if not type(ast.left) is Id and not type(ast.left) is ArrayCell:
                raise NotLeftValue(ast.left)
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            elif type(left) is FloatType and type(right) is FloatType:
                return FloatType()
            elif type(left) is FloatType and type(right) is IntType:
                return FloatType()
            elif type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            elif type(left) is StringType and type(right) is StringType:
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op==">" or op=="<" or op==">=" or op=="<=":
            if type(left) is IntType and type(right) is IntType:
                return BoolType()
            elif type(left) is FloatType or type(right) is FloatType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op=="==" or op=="!=":
            if type(left) is IntType and type(right) is IntType:
                return BoolType()
            elif type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op=="%":
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)
            
    def visitUnaryOp(self,ast,c):
        #c[0] is list 
        #c[1] is function name
        #c[2] is loop flag
        op = ast.op
        body = self.visit(ast.body,c)
        if op=="-":
            if type(body) is IntType:
                return IntType()
            elif type(body) is FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op=="!":
            if type(body) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitIntLiteral(self,ast,c):
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitStringLiteral(self,ast,c):
        return StringType()


            
            
            

    






