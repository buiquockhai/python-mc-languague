# /*
#  * header
#  * name :   Bui Quoc Khai
#  * id   :   1711726
#  */

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_right_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0507","0507,<EOF>",101))
    def test_wrong_integer(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",102))
    def test_right_float_nonEx1(self):
        self.assertTrue(TestLexer.checkLexeme("1.2abc","1.2,abc,<EOF>",103))
    def test_right_float_nonEx2(self):
        self.assertTrue(TestLexer.checkLexeme("1.def","1.,def,<EOF>",104))
    def test_right_float_nonEx3(self):
        self.assertTrue(TestLexer.checkLexeme(".1ijk",".1,ijk,<EOF>",105))
    def test_right_float_nonEx4(self):
        self.assertTrue(TestLexer.checkLexeme("12.0xyz","12.0,xyz,<EOF>",106))

    def test_right_float_posEx1(self):
        self.assertTrue(TestLexer.checkLexeme("1e22abc","1e22,abc,<EOF>",107))
    def test_right_float_posEx2(self):
        self.assertTrue(TestLexer.checkLexeme("1.E2def","1.E2,def,<EOF>",108))
    def test_right_float_posEx3(self):
        self.assertTrue(TestLexer.checkLexeme(".1e2ijk",".1e2,ijk,<EOF>",109))
    def test_right_float_posEx4(self):
        self.assertTrue(TestLexer.checkLexeme("0.12E2xyz","0.12E2,xyz,<EOF>",110))

    def test_right_float_negEx1(self):
        self.assertTrue(TestLexer.checkLexeme("1e-22abc","1e-22,abc,<EOF>",111))
    def test_right_float_negEx2(self):
        self.assertTrue(TestLexer.checkLexeme("1.E-2def","1.E-2,def,<EOF>",112))
    def test_right_float_negEx3(self):
        self.assertTrue(TestLexer.checkLexeme(".1e-2ijk",".1e-2,ijk,<EOF>",113))
    def test_right_float_negEx4(self):
        self.assertTrue(TestLexer.checkLexeme("0.12E-2xyz","0.12E-2,xyz,<EOF>",114))

    def test_wrong_float_nonDig1(self):
        self.assertTrue(TestLexer.checkLexeme("e-12","e,-,12,<EOF>",115))
    def test_wrong_float_nonDig2(self):
        self.assertTrue(TestLexer.checkLexeme("e12","e12,<EOF>",116))

    def test_wrong_float_nonExDig(self):
        self.assertTrue(TestLexer.checkLexeme("12e","12,e,<EOF>",117))

    def test_separator1(self):
        self.assertTrue(TestLexer.checkLexeme("{a x [b x c (d x e)]}","{,a,x,[,b,x,c,(,d,x,e,),],},<EOF>",118))
    def test_separator2(self):
        self.assertTrue(TestLexer.checkLexeme("Hoc,hoc nua,hoc mai;","Hoc,,,hoc,nua,,,hoc,mai,;,<EOF>",119))
    
    def test_arith_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("6+12-3=15","6,+,12,-,3,=,15,<EOF>",120))
    def test_arith_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("(2**2)*3/6 = 2","(,2,*,*,2,),*,3,/,6,=,2,<EOF>",121))
    def test_arith_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("(2**2)*3//6 = 2","(,2,*,*,2,),*,3,<EOF>",122))

    def test_logic_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("a=b=c","a,=,b,=,c,<EOF>",123))
    def test_logic_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("a||b||c","a,||,b,||,c,<EOF>",124))
    def test_logic_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("a!=b=c","a,!=,b,=,c,<EOF>",125))
    def test_logic_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("a=b!!=c","a,=,b,!,!=,c,<EOF>",126))
    

    def test_compare_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("a<b>c","a,<,b,>,c,<EOF>",127))
    def test_compare_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("!(a==b)","!,(,a,==,b,),<EOF>",128))
    def test_compare_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("a>=b<=c","a,>=,b,<=,c,<EOF>",129))
    def test_compare_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("a=<b","a,=,<,b,<EOF>",130))
    def test_compare_operator5(self):
        self.assertTrue(TestLexer.checkLexeme("a=>b","a,=,>,b,<EOF>",131))

    def test_comment_block1(self):
        self.assertTrue(TestLexer.checkLexeme("/*abc","/,*,abc,<EOF>",132))
    def test_comment_block2(self):
        self.assertTrue(TestLexer.checkLexeme("/*/*123abc","/,*,/,*,123,abc,<EOF>",133))
    def test_comment_block3(self):
        self.assertTrue(TestLexer.checkLexeme("/**/123abc","123,abc,<EOF>",134))
    def test_comment_block4(self):
        self.assertTrue(TestLexer.checkLexeme("/*123abc*/","<EOF>",135))
    def test_comment_block5(self):
        self.assertTrue(TestLexer.checkLexeme("/123abc**/","/,123,abc,*,*,/,<EOF>",136))
    def test_comment_block6(self):
        self.assertTrue(TestLexer.checkLexeme("/123abc**/","/,123,abc,*,*,/,<EOF>",137))
    def test_comment_block7(self):
        self.assertTrue(TestLexer.checkLexeme("/*$abc*/","<EOF>",138))
    def test_comment_block8(self):
        self.assertTrue(TestLexer.checkLexeme("//*abc*/","<EOF>",139))
    def test_comment_block9(self):
        self.assertTrue(TestLexer.checkLexeme("/*123abc*/*/","*,/,<EOF>",140))
    def test_comment_block10(self):
        self.assertTrue(TestLexer.checkLexeme("/*/*abc*//*123**/*/","*,/,<EOF>",141))

    def test_nested_comment_block1(self):
        self.assertTrue(TestLexer.checkLexeme("/*/*123/*abc*/","<EOF>",142))
    def test_nested_comment_block2(self):
        self.assertTrue(TestLexer.checkLexeme("/*abc/*123*/xyz/**/","xyz,<EOF>",143))

    def test_comment_line1(self):
        self.assertTrue(TestLexer.checkLexeme("//abc","<EOF>",144))
    def test_comment_line2(self):
        self.assertTrue(TestLexer.checkLexeme("/123/abc","/,123,/,abc,<EOF>",145))
    
    def test_nested_comment_line1(self):
        self.assertTrue(TestLexer.checkLexeme("///////abc//xyz","<EOF>",146))
    def test_nested_comment_line2(self):
        self.assertTrue(TestLexer.checkLexeme("/abc//$//%//abc//xyz","/,abc,<EOF>",147))

    def test_comment_line_contain_block1(self):
        self.assertTrue(TestLexer.checkLexeme("///*abc*/","<EOF>",148))
    def test_comment_line_contain_block2(self):
        self.assertTrue(TestLexer.checkLexeme("/abc*//**///*abc*/","/,abc,*,<EOF>",149))

    def test_comment_block_contain_line1(self):
        self.assertTrue(TestLexer.checkLexeme("/*//123/4/abc*/","<EOF>",150))
    def test_comment_block_contain_line2(self):
        self.assertTrue(TestLexer.checkLexeme("/*//123/4*///abc*/","<EOF>",151))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Test string 152" ""","""Test string 152,<EOF>""",152))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\n123" ""","Unclosed String: abc",153))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",154))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\t123" ""","""123a\\t123,<EOF>""",155))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\r123" ""","""123a\\r123,<EOF>""",156))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\b123" ""","""123a\\b123,<EOF>""",157))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\f123" ""","""123a\\f123,<EOF>""",158))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\"123" ""","""123a\\"123,<EOF>""",159))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\\\123" ""","""123a\\\\123,<EOF>""",160))

    def test_mix_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "/*abc123*/" ""","""/*abc123*/,<EOF>""",161))
    def test_mix_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "//abc123" ""","""//abc123,<EOF>""",162))
    def test_mix_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "12.5E2abc" ""","""12.5E2abc,<EOF>""",163))
    def test_mix_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "khaibui123123@gmail.com" ""","""khaibui123123@gmail.com,<EOF>""",164))
    def test_mix_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Python3""Antlr4" ""","""Python3,Antlr4,<EOF>""",165))
    def test_mix_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Python3"And"Antlr4" ""","""Python3,And,Antlr4,<EOF>""",166))
    def test_mix_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "Antlr4" ""","""123,Antlr4,<EOF>""",167))

    def test_unclose_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123abc\\n123 ""","""Unclosed String: 123abc\\n123 """,168))
    def test_unclose_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123abc?? ""","""Unclosed String: 123abc?? """,169))
    def test_unclose_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "abc ""","""123,Unclosed String: abc """,170))
    def test_unclose_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "/*123*/abc ""","""Unclosed String: /*123*/abc """,171))
    def test_unclose_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "//123a\\n123 ""","""Unclosed String: //123a\\n123 """,172))
    def test_unclose_string6(self):
        self.assertTrue(TestLexer.checkLexeme(''' """''',""",Unclosed String: """,173))
    def test_unclose_string7(self):
        self.assertTrue(TestLexer.checkLexeme('''"''',"""Unclosed String: """,174))

    def test_wrong_token1(self):
        self.assertTrue(TestLexer.checkLexeme("abc?123","abc,Error Token ?",175))
    def test_wrong_token2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "$USD" $USD""","$USD,Error Token $",176))
    def test_wrong_token3(self):
        self.assertTrue(TestLexer.checkLexeme("/*abc#123*/#abc","Error Token #",177))
    def test_wrong_token4(self):
        self.assertTrue(TestLexer.checkLexeme("//*abc#123*/#abc","<EOF>",178))

    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",179))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\n\\m123" ""","""123,Illegal Escape In String: 123a\\n\\m""",180))

    def test_mix_error1(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc^ "abc ""","""abc,Error Token ^""",181))
    def test_mix_error2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\k $123 ""","""Illegal Escape In String: abc\\k""",182))

    def test_type(self):
        self.assertTrue(TestLexer.checkLexeme("123void123","123,void123,<EOF>",183))
    
    def test_structure1(self):
        self.assertTrue(TestLexer.checkLexeme("int main() {}","int,main,(,),{,},<EOF>",184))
    def test_structure2(self):
        test = """ 
        <?php
            $name = "Hello Antlr4";
            echo $name;
        ?>
        """
        result = """<,Error Token ?"""
        self.assertTrue(TestLexer.checkLexeme(test,result,185))
    def test_structure3(self):
        test = """ 
        <!DOCTYPE html>
        <head>
            <title>Hello Antlr4</title>
        </head>
        """
        result = """<,!,DOCTYPE,html,>,<,head,>,<,title,>,Hello,Antlr4,<,/,title,>,<,/,head,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,186))
    def test_structure4(self):
        test = """ 
        public class Antlr4{
            public static void main(String []args){
                System.out.println("Hello Antlr4");
            }
        }
        """
        result = """public,class,Antlr4,{,public,static,void,main,(,String,[,],args,),{,System,Error Token ."""
        self.assertTrue(TestLexer.checkLexeme(test,result,187))
    def test_structure5(self):
        test = """ 
        <script>
            alert("Hello Antlr4");
        </script>
        """
        result = """<,script,>,alert,(,Hello Antlr4,),;,<,/,script,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,188))
    def test_structure6(self):
        test = """ 
        #include<stdio.h>
        int main(){
            printf("Hello Antlr4);
            return 0;
        }
        """
        result = """Error Token #"""
        self.assertTrue(TestLexer.checkLexeme(test,result,189))
    def test_structure7(self):
        test = """ 
        using namespace std;
        int main(){
            cout << "Hello Antlr4";
            return 0;
        }
        """
        result = """using,namespace,std,;,int,main,(,),{,cout,<,<,Hello Antlr4,;,return,0,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,190))
    def test_structure8(self):
        test = """ 
        var msg = "Hello Antlr4";
        console.log(msg);
        """
        result = """var,msg,=,Hello Antlr4,;,console,Error Token ."""
        self.assertTrue(TestLexer.checkLexeme(test,result,191))
    def test_structure_Go(self):
        test = """ 
        package main
        import "fmt"
        func main(){
            fmt.Printf("Hello Antlr4")
        }
        """
        result = """package,main,import,fmt,func,main,(,),{,fmt,Error Token ."""
        self.assertTrue(TestLexer.checkLexeme(test,result,192))
    def test_structure_Latex(self):
        test = """ 
        \begin{figure}[h]
		    \centering
		    \includegraphics[width=1\linewidth]{1}
		    \caption{}
		    \label{fig:1}
	    \end{figure}
        """
        result = '''egin,{,figure,},[,h,],Error Token \\'''
        self.assertTrue(TestLexer.checkLexeme(test,result,193))
    def test_structure_FS(self):
        test = """ 
        [<EntryPoint>]
        let main argv = 
            printfn "Hello Antlr4" argv
            0
        """
        result = """[,<,EntryPoint,>,],let,main,argv,=,printfn,Hello Antlr4,argv,0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,194))
    def test_structure_Kotlin(self):
        test = """ 
        fun main(args Array<String>){
            println("Hello Antlr4")
        }
        """
        result = """fun,main,(,args,Array,<,String,>,),{,println,(,Hello Antlr4,),},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,195))
    def test_structure_ObjC(self):
        test = """ 
        int main(int argc, char **argv, char **envp){
            @autoreleasepool{
                NSLog(@"Hello Antlr4");
            }
            return 0;
        }
        """
        result = """int,main,(,int,argc,,,char,*,*,argv,,,char,*,*,envp,),{,Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(test,result,196))
    def test_structure_Ruby(self):
        test = """ 
        puts "Hello Antlr4";
        """
        result = """puts,Hello Antlr4,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,197))
    def test_structure_htmlForm(self):
        test = """ 
        <form method="POST" action="" enctype="multipart/form-data">
		    <label>
			    <input type="file" name="file" placeholder="Choose your file">
			    <input type="submit" name="submit">
		    </label>
	    </form>
        """
        result = """<,form,method,=,POST,action,=,,enctype,=,multipart/form-data,>,<,label,>,<,input,type,=,file,name,=,file,placeholder,=,Choose your file,>,<,input,type,=,submit,name,=,submit,>,<,/,label,>,<,/,form,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,198))
    def test_structure_PythonClass(self):
        test = """ 
        class TestUtil:
            @staticmethod
            def makeSource(inputStr,num):
                filename = "./test/testcases/" + str(num) + ".txt"
                file = open(filename,"w")
                file.write(inputStr)
                file.close()
                return FileStream(filename)
        """
        result = """class,TestUtil,Error Token :"""
        self.assertTrue(TestLexer.checkLexeme(test,result,199))
    def test_structure_VB(self):
        test = """ 
        Module module
            Sub Main()
                Console.WriteLine("Hello Antlr4")
                Console.ReadKey()
            End Sub
        End Module
        """
        result = """Module,module,Sub,Main,(,),Console,Error Token ."""
        self.assertTrue(TestLexer.checkLexeme(test,result,200))