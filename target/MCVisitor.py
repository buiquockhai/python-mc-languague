# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#manyDecl.
    def visitManyDecl(self, ctx:MCParser.ManyDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varDecl.
    def visitVarDecl(self, ctx:MCParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#typeList.
    def visitTypeList(self, ctx:MCParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idList.
    def visitIdList(self, ctx:MCParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcDecl.
    def visitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramList.
    def visitParamList(self, ctx:MCParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramTemp.
    def visitParamTemp(self, ctx:MCParser.ParamTempContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param.
    def visitParam(self, ctx:MCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockStmt.
    def visitBlockStmt(self, ctx:MCParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#singStmt.
    def visitSingStmt(self, ctx:MCParser.SingStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MCParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifStmt.
    def visitIfStmt(self, ctx:MCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forStmt.
    def visitForStmt(self, ctx:MCParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakStmt.
    def visitBreakStmt(self, ctx:MCParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#contiStmt.
    def visitContiStmt(self, ctx:MCParser.ContiStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnStmt.
    def visitReturnStmt(self, ctx:MCParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_1.
    def visitExpression_1(self, ctx:MCParser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_2.
    def visitExpression_2(self, ctx:MCParser.Expression_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_3.
    def visitExpression_3(self, ctx:MCParser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_4.
    def visitExpression_4(self, ctx:MCParser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_5.
    def visitExpression_5(self, ctx:MCParser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_6.
    def visitExpression_6(self, ctx:MCParser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_7.
    def visitExpression_7(self, ctx:MCParser.Expression_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_8.
    def visitExpression_8(self, ctx:MCParser.Expression_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_9.
    def visitExpression_9(self, ctx:MCParser.Expression_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_0.
    def visitExpression_0(self, ctx:MCParser.Expression_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primary.
    def visitPrimary(self, ctx:MCParser.PrimaryContext):
        return self.visitChildren(ctx)



del MCParser