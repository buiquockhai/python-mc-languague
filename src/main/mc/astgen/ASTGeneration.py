# header
# name :   Bui Quoc Khai
# id   :   1711726

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce

class ASTGeneration(MCVisitor):
    
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visit(ctx.manyDecl()))

    def visitManyDecl(self,ctx:MCParser.ManyDeclContext):
        return self.visit(ctx.decl()) + self.visit(ctx.manyDecl()) if ctx.manyDecl() else self.visit(ctx.decl())

    def visitDecl(self,ctx:MCParser.DeclContext):
        return self.visit(ctx.varDecl()) if ctx.varDecl() else self.visit(ctx.funcDecl())

    def visitVarDecl(self,ctx:MCParser.VarDeclContext):
        return [VarDecl(str(i[0]), self.visit(ctx.typeList())) if i[1] == -1 else VarDecl(str(i[0]), ArrayType(int(i[1]),self.visit(ctx.typeList()))) for i in self.visit(ctx.idList())]
    
    def visitTypeList(self,ctx:MCParser.TypeListContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLEANTYPE():
            return BoolType()
        else:
            return StringType()

    def visitIdList(self,ctx:MCParser.IdListContext):
        if ctx.idList():
            return [[ctx.ID().getText(),-1]] + self.visit(ctx.idList()) if ctx.getChildCount()==3 else [[ctx.ID().getText(),ctx.INTLIT().getText()]] + self.visit(ctx.idList())
        else:
            return [[ctx.ID().getText(),-1]] if ctx.getChildCount()==1 else [[ctx.ID().getText(),ctx.INTLIT().getText()]]
 
    def visitFuncDecl(self,ctx:MCParser.FuncDeclContext):
        if ctx.LS():
            return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.paramList()),ArrayPointerType(self.visit(ctx.typeList())),self.visit(ctx.blockStmt()))]
        else:
            if ctx.typeList():
                return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.paramList()),self.visit(ctx.typeList()),self.visit(ctx.blockStmt()))]
            else:
                return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.paramList()),VoidType(),self.visit(ctx.blockStmt()))]
    
    # **
    def visitParamList(self,ctx:MCParser.ParamListContext):
        return [self.visit(ctx.param())] + self.visit(ctx.paramTemp()) if ctx.param() else []

    def visitParamTemp(self,ctx:MCParser.ParamTempContext):
        return [self.visit(ctx.param())] + self.visit(ctx.paramTemp()) if ctx.param() else []

    def visitParam(self,ctx:MCParser.ParamContext):
        return  VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.typeList()))) if ctx.LS() else VarDecl(ctx.ID().getText(),self.visit(ctx.typeList()))

    def visitBlockStmt(self,ctx:MCParser.BlockStmtContext):
        result = []
        for i in ctx.singStmt():
            if isinstance(self.visit(i),list):
                result = result+self.visit(i)
            else:
                result.append(self.visit(i))
        return Block(result)

    def visitSingStmt(self,ctx:MCParser.SingStmtContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.doWhileStmt():
            return self.visit(ctx.doWhileStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.contiStmt():
            return self.visit(ctx.contiStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.blockStmt())
            
    # **
    def visitDoWhileStmt(self,ctx:MCParser.DoWhileStmtContext):
        return Dowhile([self.visit(i) for i in ctx.singStmt()],self.visit(ctx.expression()))

    def visitIfStmt(self,ctx:MCParser.IfStmtContext):
        if (ctx.ELSE()):
            if (isinstance(self.visit(ctx.singStmt(0)),list) and isinstance(self.visit(ctx.singStmt(1)),list)):
                return If(self.visit(ctx.expression()),Block(self.visit(ctx.singStmt(0))),Block(self.visit(ctx.singStmt(1))))
            if (isinstance(self.visit(ctx.singStmt(0)),list)):
                return If(self.visit(ctx.expression()),Block(self.visit(ctx.singStmt(0))),self.visit(ctx.singStmt(1)))
            if (isinstance(self.visit(ctx.singStmt(1)),list)):
                return If(self.visit(ctx.expression()),self.visit(ctx.singStmt(0)),Block(self.visit(ctx.singStmt(1))))
            return If(self.visit(ctx.expression()),self.visit(ctx.singStmt(0)),self.visit(ctx.singStmt(1)))
        else:
            if (isinstance(self.visit(ctx.singStmt(0)),list)):
                return If(self.visit(ctx.expression()),Block(self.visit(ctx.singStmt(0))),None)
            else:
                return If(self.visit(ctx.expression()),self.visit(ctx.singStmt(0)),None)

    def visitForStmt(self,ctx:MCParser.ForStmtContext):
        if (isinstance(self.visit(ctx.singStmt()),list)):
            return For(self.visit(ctx.expression(0)),self.visit(ctx.expression(1)),self.visit(ctx.expression(2)),Block(self.visit(ctx.singStmt())))
        else:
            return For(self.visit(ctx.expression(0)),self.visit(ctx.expression(1)),self.visit(ctx.expression(2)),self.visit(ctx.singStmt()))

    def visitBreakStmt(self,ctx:MCParser.BreakStmtContext):
        return Break()

    def visitContiStmt(self,ctx:MCParser.ContiStmtContext):
        return Continue() 

    def visitReturnStmt(self,ctx:MCParser.ReturnStmtContext):
        return Return(self.visit(ctx.expression())) if ctx.expression() else Return(None)

    def visitExpression(self,ctx:MCParser.ExpressionContext):
        return BinaryOp(ctx.ASSG().getText(),self.visit(ctx.expression_1()), self.visit(ctx.expression())) if ctx.expression() else self.visit(ctx.expression_1())

    def visitExpression_1(self,ctx:MCParser.Expression_1Context):
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.expression_1()), self.visit(ctx.expression_2())) if ctx.expression_1() else self.visit(ctx.expression_2())

    def visitExpression_2(self,ctx:MCParser.Expression_2Context):
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.expression_2()), self.visit(ctx.expression_3())) if ctx.expression_2() else self.visit(ctx.expression_3())

    def visitExpression_3(self,ctx:MCParser.Expression_3Context):
        if ctx.expression_3():
            return BinaryOp(ctx.EQUAL().getText(),self.visit(ctx.expression_3(0)), self.visit(ctx.expression_3(1))) if ctx.EQUAL() else BinaryOp(ctx.NOTEQUAL().getText(),self.visit(ctx.expression_3(0)), self.visit(ctx.expression_3(1)))
        else:
            return self.visit(ctx.expression_4())

    def visitExpression_4(self,ctx:MCParser.Expression_4Context):
        if ctx.expression_4():
            if ctx.LERELA():
                return BinaryOp(ctx.LERELA().getText(),self.visit(ctx.expression_4(0)), self.visit(ctx.expression_4(1)))
            elif ctx.MERELA():
                return BinaryOp(ctx.MERELA().getText(),self.visit(ctx.expression_4(0)), self.visit(ctx.expression_4(1)))
            elif ctx.LRELA():
                return BinaryOp(ctx.LRELA().getText(),self.visit(ctx.expression_4(0)), self.visit(ctx.expression_4(1)))
            else:
                return BinaryOp(ctx.MRELA().getText(),self.visit(ctx.expression_4(0)), self.visit(ctx.expression_4(1)))
        else:
            return self.visit(ctx.expression_5())

    def visitExpression_5(self,ctx:MCParser.Expression_5Context):
        if ctx.expression_5():
            return BinaryOp(ctx.ADD().getText(),self.visit(ctx.expression_5()), self.visit(ctx.expression_6())) if ctx.ADD() else BinaryOp(ctx.SUB().getText(),self.visit(ctx.expression_5()), self.visit(ctx.expression_6()))
        else:
            return self.visit(ctx.expression_6())

    def visitExpression_6(self,ctx:MCParser.Expression_6Context):
        if ctx.expression_6():
            if ctx.MUL():
                return BinaryOp(ctx.MUL().getText(),self.visit(ctx.expression_6()), self.visit(ctx.expression_7()))
            elif ctx.DIV():
                return BinaryOp(ctx.DIV().getText(),self.visit(ctx.expression_6()), self.visit(ctx.expression_7()))
            else:
                return BinaryOp(ctx.MOD().getText(),self.visit(ctx.expression_6()), self.visit(ctx.expression_7()))
        else:
            return self.visit(ctx.expression_7())

    def visitExpression_7(self,ctx:MCParser.Expression_7Context):
        if ctx.expression_7():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.expression_7())) if ctx.NOT() else UnaryOp(ctx.SUB().getText(),self.visit(ctx.expression_7()))
        else:
            return self.visit(ctx.expression_8())

    def visitExpression_8(self,ctx:MCParser.Expression_8Context):
        return ArrayCell(self.visit(ctx.expression_9()),self.visit(ctx.expression_5())) if ctx.expression_5() else self.visit(ctx.expression_9())

    def visitExpression_9(self,ctx:MCParser.Expression_9Context):
        return self.visit(ctx.expression_1()) if ctx.LB() else self.visit(ctx.expression_0())
            
    def visitExpression_0(self,ctx:MCParser.Expression_0Context):
        return self.visit(ctx.primary()) if ctx.primary() else CallExpr(Id(ctx.ID().getText()),[self.visit(i) for i in ctx.expression()]) if ctx.expression() else CallExpr(Id(ctx.ID().getText()),[])
    
    def visitPrimary(self,ctx:MCParser.PrimaryContext):
        if ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT().getText() == 'true')
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        else:
            return Id(str(ctx.ID()))

    