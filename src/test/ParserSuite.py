# /*
#  * header
#  * name :   Bui Quoc Khai
#  * id   :   1711726
#  */

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_simple_program2(self):
        input = """int main(int a) {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_simple_program3(self):
        input = """int main() {{abc}"""
        expect = "Error on line 1 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_simple_program4(self):
        input = """int main() {
            printf("Hello Antlr4");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_simple_program5(self):
        input = """int main() {
            printf("Hello Antlr4"));
        }"""
        expect = "Error on line 2 col 34: )"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_simple_program6(self):
        input = """int main() {
            printf("Hello Antlr4")
        }"""
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_simple_program7(self):
        input = """int main() {
            printf("Hello Antlr4");
            {}
            {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_simple_program8(self):
        input = """
        float Dog_Function(){}
        int main() {
            printf("Hello Antlr4");
            {}
            {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_simple_program9(self):
        input = """
        float Dog_Function() {}
        void Cat_Function()
        int main() {
            printf("Hello Antlr4");
            {}
            {}
        }"""
        expect = "Error on line 4 col 8: int"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_simple_program10(self):
        input = """
        float Dog_Function() {}
        void Cat_Function() {}
        def Bird_Function() {}
        int main() {
            printf("Hello Antlr4");
            {}
            {}
        }"""
        expect = "Error on line 4 col 8: def"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_simple_program11(self):
        input = """
        float Dog_Function() {}
        void +() {}
        int main() {
            printf("Hello Antlr4");
            {}
            {}
        }"""
        expect = "Error on line 3 col 13: +"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_simple_program12(self):
        input = """
        float Dog_Function() {}
        void Cat_Function() {
            // Not having main function
            printf("Hello Antlr4");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_simple_program13(self):
        input = """
        float Dog_Function() {}
        void Cat_Function() {
            // Wrong main type function
            printf("Hello Antlr4");
        }
        boolean main() {}"""
        expect = "Error on line 7 col 16: main"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_simple_program14(self):
        input = """
        float int Dog_Function() {}
        int main() {}"""
        expect = "Error on line 2 col 14: int"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_simple_program15(self):
        input = """
        float Dog_Function(int a,float b[]) {}
        int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_simple_program16(self):
        input = """
        float[] foo(int a,float b[]) {}
        int main() {}
        string Cat_Function() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_simple_program17(self):
        input = """
        float[] foo(int a,float b[]) {}
        int main() {}
        void[] () {}"""
        expect = "Error on line 4 col 12: ["
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_simple_program18(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    
    def test_simple_program19(self):
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_simple_program20(self):
        input = """int main() {
            int Dog_Function(float a) {}
        }"""
        expect = "Error on line 2 col 28: ("
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_declare_program1(self):
        input = """
        float Dog_Function(){
            int a,b,arr[5];
        }
        int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_declare_program2(self):
        input = """
        int a,float f[5];
        float Dog_Function() {}
        int main() {}"""
        expect = "Error on line 2 col 14: float"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_declare_program3(self):
        input = """
        var a,b;
        float Dog_Function() {}
        int main() {}"""
        expect = "Error on line 2 col 8: var"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_declare_program4(self):
        input = """
        float var = 2.5;
        void Dog_Function() {
            int var = 3;
        }
        int main() {}"""
        expect = "Error on line 2 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_declare_program5(self):
        input = """
        float Dog_Function() {}
        void main() {
            int 123abc,xyz;
        }"""
        expect = "Error on line 4 col 16: 123"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_assign_program1(self):
        input = """
        int a = b = c;
        float Dog_Function() {}
        int main() {}"""
        expect = "Error on line 2 col 14: ="
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_assign_program2(self):
        input = """
        float a,b,c;
        void Dog_Function() {
            a = b = c = 10;
        }
        int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_assign_program3(self):
        input = """
        float a,b,c;
        void Dog_Function() {
            a = b = c = 10;
            int arr[5];
            arr[0] = [[10];
        }
        int main() {}"""
        expect = "Error on line 6 col 21: ["
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_assign_program4(self):
        input = """
        float a,b,c;
        void Dog_Function() {
            a = b = c = 10;
            int arr[5];
            arr[0] = {12};
        }
        int main() {}"""
        expect = "Error on line 6 col 21: {"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_assign_program5(self):
        input = """
        float Dog_Function(boolean bool) {}
        int main() {
            {
                float result;
                result = Dog_Function(true);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_assign_program6(self):
        input = """
        int foo(int a) {
            int b;
            b = a;
            printf("ID = ",a);
            return b;
        }
        int main() {
            int arr[5];
            arr[1] = foo(arr[0]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_assign_program7(self):
        input = """
        void Dog_Function(){
            printf("");
        }
        int main() {
            int arr[5];
            arr[1] = Dog_Function();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_assign_program8(self):
        input = """
        float foo(int a){
            float b[10];
            b[2] = a;
            return b;
        }
        int main() {
            int x;
            x = 1;
            foo(2)[x+1] = a[b[2]] + 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_assign_program9(self):
        input = """
        float foo(int a){
            float b[10];
            b[2] = a;
            return b;
        }
        int main() {
            int x;
            x = 1;
            foo(2)[x+1] = a[b[2]]] + 3;
        }"""
        expect = "Error on line 10 col 33: ]"
        self.assertTrue(TestParser.checkParser(input,expect,234))
        
    def test_assign_program10(self):
        input = """
        int main() {
            int x;
            = x = b = c = 1;
        }"""
        expect = "Error on line 4 col 12: ="
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_doWhile_program1(self):
        input = """
        do {} {} while a == b;
        int main() {
        }"""
        expect = "Error on line 2 col 8: do"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_doWhile_program2(self):
        input = """
        void Dog_Function(){
            do {
                int a;
                a = b;
            } {} while a == b;
        }
        
        int main() {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_doWhile_program3(self):
        input = """
        void Dog_Function(){
            do {
                int a;
                a = b;
            } {} while a == b
        }
        
        int main() {
        }"""
        expect = "Error on line 7 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_doWhile_program4(self):
        input = """
        void Dog_Function(){
            do {
                do {} while;
            } {} while a == b;
        }
        
        int main() {
        }"""
        expect = "Error on line 4 col 27: ;"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_doWhile_program5(self):
        input = """
        void Dog_Function(){
            do {
                int a;
                a = 0;
                do {
                    a = a * a;
                } while (true);
            } {} while (a == b);
        }
        
        int main() {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_doWhile_program6(self):
        input = """
        void Dog_Function(){
            while (a != 0) do {};
        }
        
        int main() {
        }"""
        expect = "Error on line 3 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_doWhile_program7(self):
        input = """
        void Dog_Function(){
            do {} while (a<10) while ();
        }
        
        int main() {
        }"""
        expect = "Error on line 3 col 31: while"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_doWhile_program8(self):
        input = """
        void Dog_Function(){
            do {} while (!true);
        }
        
        int main() {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_doWhile_program9(self):
        input = """
        void Dog_Function(){
            do {
                do {
                    {}
                    {}
                } while (a == 3);
            } while (!true);
        }
        
        int main() {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_doWhile_program10(self):
        input = """
        void Dog_Function(){
            do {
                void Cat_Function() {}
            } while (!true);
        }
        
        int main() {
        }"""
        expect = "Error on line 4 col 16: void"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_if_program1(self):
        input = """
        if (a==b) {} else {}

        int main() {
        }"""
        expect = "Error on line 2 col 8: if"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_if_program2(self):
        input = """
        int main() {
            if (true) {} {
                int a,b,c;
                a = b =c = 5;
            }
            else {}
        }"""
        expect = "Error on line 7 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_if_program3(self):
        input = """
        int main() {
            if a==b {} {
                int a,b,c;
                a = b =c = 5;
            }
            else {}
        }"""
        expect = "Error on line 3 col 15: a"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_if_program4(self):
        input = """
        int main() {
            if ((a==b) && (c==d)) {} {
                int a,b,c;
                a = b =c = 5;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_if_program5(self):
        input = """
        int main() {
            if(a) if(b) if(c) a; else a; else
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_if_program6(self):
        input = """
        int main() {
            if (if(a)) {} a = b = c = 3;
            else {}
        }"""
        expect = "Error on line 3 col 16: if"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_if_program7(self):
        input = """
        int main() {
            if (true) a; else {};
        }"""
        expect = "Error on line 3 col 32: ;"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_if_program8(self):
        input = """
        int main() {
            if (!true) {
                {}
                do {
                    if (false) a; 
                } while (a==b);
            } else{
                y = x*x + 3;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_if_program9(self):
        input = """
        int main() {
            if (!true) {
                {}
                do {
                    if (false) a; 
                } while (a==b);
            } else{
                y = x*x + 3;
            } else {}
        }"""
        expect = "Error on line 10 col 14: else"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_if_program10(self):
        input = """
        int main() {
            if ("string") int foo(2) {};
        }"""
        expect = "Error on line 3 col 33: ("
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_for_program1(self):
        input = """
        for(;;) {}
        int main() {
            printf("For statement");
        }"""
        expect = "Error on line 2 col 8: for"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_for_program2(self):
        input = """
        int main() {
            int i;
            for(i=0;i<=10;i=i+1) {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_for_program3(self):
        input = """
        int main() {
            int i,j;
            for(i=0, j=1; i<=10 ; i=i+1) {
                a = 5;
            }
        }"""
        expect = "Error on line 4 col 19: ,"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_for_program4(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
                if (i%2 == 0) break; else continue;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_for_program5(self):
        input = """
        int main() {
            int i,j;
            foreach(i=0; i<=10 ; i=i+1)
                if (i%2 == 0) break; else continue;
        }"""
        expect = "Error on line 4 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_for_program6(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1; i=i+1)
                if (i%2 == 0) break; else continue;
        }"""
        expect = "Error on line 4 col 34: ;"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_for_program7(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1){
                void Dog_Function() {}
            }
        }"""
        expect = "Error on line 5 col 16: void"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_for_program8(self):
        input = """
        int main() {
            int i,j;
            for(i=0;i<=1000;i=i+1){
                i = i + 1;
                do {} {} break; while(true);
                if(i>=1000) break; else continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_for_program9(self):
        input = """
        int main() {
            int i,j,arr[5];
            arr[] = for(i=0;i<=1000;i=i+1){
                        i = i + 1;
                        do {} {} break; while(true);
                        if(i>=1000) break; else continue;
                    }
        }"""
        expect = "Error on line 4 col 16: ]"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_for_program10(self):
        input = """
        void Dog_Function(){
            int i,j;
            for(i=0;i<=1000;i=i+1){
                i = i + 1;
                do {} {} break; while(true);
                for(i=0;i<=10000;i=i+1) a=10;
                if(i>=1000) break; else continue;
            }
        }
        int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_block_program1(self):
        input = """
        {a=5;}
        int main() {}"""
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    
    def test_block_program2(self):
        input = """
        int main() {
            {a=5;}
            {
                int i;
                for(i=0;i<=10;i=i+1) a=10;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_block_program3(self):
        input = """
        int main() {
            {a=5;}
            {
                int i;
                for(i=0;i<=10;i=i+1) a=10;
            };
        }"""
        expect = "Error on line 7 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_block_program4(self):
        input = """
        {int main() {
            {a=5;}
            {}
        }}"""
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_block_program5(self):
        input = """
        void Dog_Function({}){}

        int main() {
            {a=5;}
            {}
        }"""
        expect = "Error on line 2 col 26: {"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_block_program6(self):
        input = """
        void Dog_Function(){{}}

        int main() {
            {a=5; {}}
            {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_block_program7(self):
        input = """
        void Dog_Function(){{}}

        int main() {
            {a=5; {}}
            {}
            if (true) {
                {
                    a{};
                }
            }
        }"""
        expect = "Error on line 9 col 21: {"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_block_program8(self):
        input = """
        void Dog_Function(){{}}

        int main() {
            {a=5; {}}
            {}
            if (true) {
                {
                    a{}
                }
            }
        }"""
        expect = "Error on line 9 col 21: {"
        self.assertTrue(TestParser.checkParser(input,expect,273))


    def test_block_program9(self):
        input = """
        void Dog_Function(){{}}

        int main() {
            {a=5; {}}
            {}
            if (true) {
                {
                    int i;
                    for(i=0;i<=10;i=i+1) a=10;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_block_program10(self):
        input = """
        void Dog_Function(){{}}

        int main() {
            {}
            ({})
        }"""
        expect = "Error on line 6 col 13: {"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_key_program1(self):
        input = """
        break;
        void Dog_Function() {}
        int main() {}"""
        expect = "Error on line 2 col 8: break"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_key_program2(self):
        input = """
        void Dog_Function() {}
        int main() {
            printf("Hello Antlr");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_key_program3(self):
        input = """
        void Dog_Function() {}
        int main() {
            int i;
            for(i=0;i<=1000;i=i+1){
                if((a==b)||(b==5)) break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_key_program4(self):
        input = """
        break;
        void Dog_Function() {}
        int main() {}"""
        expect = "Error on line 2 col 8: break"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_key_program5(self):
        input = """
        void Dog_Function(break) {}
        int main() {}"""
        expect = "Error on line 2 col 26: break"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_key_program6(self):
        input = """
        void Dog_Function() {}
        int main() {
            { return; }
            {
                int i;
                for(i=0; i<=10; i=i+1) continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_key_program7(self):
        input = """
        void return() {}
        int main() {}"""
        expect = "Error on line 2 col 13: return"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_key_program8(self):
        input = """
        void Dog_Function() {
            return;
        }
        int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_temp_program1(self):
        input = """
        int main() {
            int i, n;
            float S;
            i = 0;
            S = 1;
            printf("Nhap n: ");
            for(i=0;i<=1000;i=i+1){
                S = 1 + 1.0/S;
                i=i+1;
                if (i<= n) break;
            }
            printf("Tong la %d", S);
            getch();
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_temp_program2(self):
        input = """
        int Fibonaci(int i) {
            if (i == 0) { return 0; }
            if(i == 1) { return 1;}
            return Fibonaci(i-1) + Fibonaci(i-2);
        }

        int  main() {
            int i;
            for (i = 0; i < 10; i=i+1) { printf("%f", Fibonaci(i)); }
            printf("===========================");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_temp_program3(self):
        input = """
        int Fibonaci(int i) {
            if (i == 0) { return 0; }
            if(i == 1) { return break; }
            return Fibonaci(i-1) + Fibonaci(i-2);
        }

        int  main() {
            int i;
            for (i = 0; i < 10; i=i+1) { printf(%d"", Fibonaci(i)); }
            printf("===========================");
            return 0;
        }"""
        expect = "Error on line 4 col 32: break"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_temp_program4(self):
        input = """
        int main() {
        int a, b;
        a = 11;
        b = 99;

        // de nhap gia tri tu ban phim, ban co the su dung phan code
        // ben trong phan comment duoi day:
        // printf("Nhap gia tri a: ");
        // scanf("%d", &a);
        // printf("Nhap gia tri b: ");
        // scanf("%d", &b);

        if(a > b)
            printf("a lon hon b");
        else
            printf("a khong lon hon b");

        return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_temp_program5(self):
        input = """
        int a, b;
        a = 11;
        b = 121;
        int main() {
            printf("Gia tri truoc khi trao doi:  a = %d, b = %d ", a, b);

            a = a + b;  // ( 11 + 121 = 132)
            b = a - b;  // ( 132 - 121 = 11)
            a = a - b;  // ( 132 - 11 = 121)

            printf("Gia tri sau khi trao doi:  a = %d, b = %d ", a, b);
        }"""
        expect = "Error on line 3 col 8: a"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_temp_program6(self):
        input = """
        int main() {
            int i, start, end;
            start = 1;
            end = 10;
            
            printf("In cac so theo thu tu tang dan:");
            for(i = start; i <= end; i++) 
                printf("%2d", i);

            return 0;
        }"""
        expect = "Error on line 8 col 39: +"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_temp_program7(self):
        input = """
        int main() {
            int i, start, end;
            start = 1;
            end = 10;
            
            printf("In cac so theo thu tu tang dan:");
            for(i = start; i <= end; i=i+1) 
                printf("%2d", i);

            return 0;
        }
        int Dog_Function(){ 
            int a;
            a = main();
        }"""
        expect = "Error on line 15 col 16: main"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_temp_program8(self):
        input = """
        int i, j, count;
        int start, end;
        int main() {
            start = 2; 
            end = 10;

            printf("In bang cuu chuong rut gon: ");
            for(i = start; i <= end; i=i+1) {
                count = i;

                for(j = 1; j <= 10; j=j+1) {
                    printf(" %3d", (count*j));
                }
                printf("");
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_temp_program9(self):
        input = """
        int main() {
            char str[100][20];
            int len;
            
            printf("Nhap mot chuoi bat ky:");
            gets(str);
            len = strlen(str);
            
            printf("nDo dai cua chuoi da cho la: %d", len);
            return(0);
        }"""
        expect = "Error on line 3 col 17: str"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_temp_program10(self):
        input = """
        int main() {
            string str[100][20];
            int len;
            
            printf("Nhap mot chuoi bat ky:");
            gets(str);
            len = strlen(str);
            
            printf("nDo dai cua chuoi da cho la: %d", len);
            return(0);
        }"""
        expect = "Error on line 3 col 27: ["
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_temp_program11(self):
        input = """
        struct stud {
            int roll;
            char name[10];
            int marks;
        };
        
        int main() {
            int size;
            stud s;
            size = sizeof(s);
            printf("nKich co cua struct la: %d", size);
            
            return(0);
        }"""
        expect = "Error on line 2 col 8: struct"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_temp_program12(self):
        input = """
        int main() {
            int a,b;
            a = 5;
            b = 10;
            int *ptr1, *ptr2;
            int num;

            num = *ptr1 + *ptr2;

            printf("Tong hai so = %d", num);
            return (0);
        }"""
        expect = "Error on line 6 col 16: *"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_temp_program13(self):
        input = """
        public class StringCompareEmp{
            public static void main(String args[]){
                String str = "Hello World";
                String anotherString = "hello world";
                Object objStr = str;

                System.out.println( str.compareTo(anotherString) );
                System.out.println( str.compareToIgnoreCase(anotherString) );
                System.out.println( str.compareTo(objStr.toString()));
                }
            }
        }"""
        expect = "Error on line 2 col 8: public"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_temp_program14(self):
        input = """
       void main() {
            int i;
            float num, temp, digit, sum;
            sum = 0;
        
            printf("Nhap vao so bat ki: ");
            scanf("%ld", num);
            temp = num;
            for (i=0;i<=1000;i=i+1){
                digit = num % 10;
                sum = sum + digit;
                num = num/10;
                if (nunm < 0) break;
            }
            printf("So ban da nhap = %ld", temp);
            printf("Tong cac chu so trong %ld = %ld", temp, sum);
            getch();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_temp_program15(self):
        input = """
        void main()
        {
            float MAX;
            float a, b, c, d;
            printf("Nhap a: ");
            scanf("%f", a);
            printf("Nhap b: ");
            scanf("%f", b);
            printf("Nhap c: ");
            scanf("%f", c);
            printf("Nhap d: ");
            scanf("%f", d);
        
            MAX = max(max(a, b), max(c, d));
            printf("MAX(%f,%f,%f,%f) = %f", a, b, c, d, MAX);
            getch();
        }
        
        float max(float x, float y)
        {
            float max;
            if(x > y)
                max = x;
            else
                max = y;
            return max;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_temp_program16(self):
        input = """
        void main()
        {
            int a, b;
            float S;
            S = 0;
            printf("Nhap vao so nguyen thu nhat = ");
            scanf("%d", a);
            printf("Nhap vao so nguyen thu hai = ");
            scanf("%d", b);
            S = a*a + b*b;
            printf("Tong binh phuong 2 so = %d^2 + %d^2 = %d ", a, b, S);
            getch();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_temp_program17(self):
        input = """
        void main()
        {
            float C;
            float F;
            printf("Nhap vao nhiet do F = ");
            scanf("%f", F);
            C = 5*(F - 32)/9.0;
            printf("Nhieu do Celcius = %f oC", C);
            getch();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    