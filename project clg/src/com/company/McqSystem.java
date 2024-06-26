package com.company;

import java.util.*;

public class McqSystem{


    public static void main(String[] args)

    {
        Scanner sc=new Scanner(System.in);
        int ch;




        while(true)
        {
            System.out.println("01. JAVA");               //WILL ENTER TO JAVA QUESTION
            System.out.println("02. C");                  //WILL ENTER TO C QUESTION
            System.out.println("03. C++");                //WILL ENTER TO C++ QUESTION
            System.out.println("04. PHP");		   //WILL ENTER TO HTML QUESTION
            System.out.println("05. HTML");  		   //WILL ENTER TO HTML QUESTION
            System.out.println("06. PYTHON");             //WILL ENTER TO PYTHON QUESTION
            System.out.println("07. EXIT");               //WILL EXIT THE PROGRAM
            System.out.println("Enter Your Choice: ");    //HERE THE USER WILL ENTER THIER CHOICE FOR QUESTION!
            ch=sc.nextInt();
            switch(ch)
            {
                case 1:
                {
                    String q1 = "Q1. Front End Web Design consist of (Select all that apply)\n" +
                            "\n" +
                            "\n \n"
                            + "(a)UI Design\n(b)Layout\n(c)Database\n(d)Server Side Scripts";

                    String q2 = "Q2. Which is not part of Front End Web Design\n"
                            + "(a)HTML\n(b)CSS\n(c)Javascript\n(d)Shell Script";

                    String q3 = "Q3. Front End Web Developer does not develop\n"
                            + "(a)CSS\n(bJQuery\n(c)Ajax\n(d)Templating Languages";

                    String q4 = "Q4. HTML stands for\n"
                            + "(a)Hightext Markup Language\n(b)Hypertext Markup Language\n(c)High-Definition Text Markup Language\n(d)Host Text Markup Language";

                    String q5 = "Q5. Head Tag is inside Body Tag\n"
                            + "(a)True\n(b)False\n(c)trdient()\n(d)drawString()";



                    Java [] javas = {
                            new Java(q1, "a,b"),
                            new Java(q2, "d"),
                            new Java(q3, "a"),
                            new Java(q4, "b"),
                            new Java(q5, "b"),

                    };
                    takeTest(javas);
                    break;
                }


                case 2:
                {
                    String q1 = "Q1. #include<stdio.h>\n" +
                            "\n" +
                            "main() \n" +
                            "{ \n" +
                            "   const int a = 5; \n" +
                            "   \n" +
                            "   a++; \n" +
                            "   printf(\"%d\", a); \n" +
                            "}\n"
                            + "(a)5\n(b)6\n(c)Runtime Error\n(d)Compiler Error";

                    String q2 = "Q2.  What is the 16-bit compiler allowable range for integer constants?\n"
                            + "(a)-3.4e38 to 3.4e38\n(b)-32767 to 32768\n(c)-32668 to 32667\n(d)-32768 to 32767";

                    String q3 = "Q3.  What is required in each C program?\n"
                            + "(a)The program must have at least one function.\n(b)The program does not require any function.\n(c)Input data\n(d)Output data";

                    String q4 = "Q4. What is a lint?\n"
                            + "(a)C compiler\n(b)Interactive debugger\n(c)Analyzing tool\n(d)C interpreter";

                    String q5 = "Q5.What is the output of this statement \"printf(\"%d\", (a++))\"?\n"
                            + "(a)The value of (a + 1)\n(b)The current value of a\n(c)Error message\n(d)Garbage";




                    Clang [] clangs = {
                            new Clang(q1, "a"),
                            new Clang(q2, "d"),
                            new Clang(q3, "a"),
                            new Clang(q4, "c"),
                            new Clang(q5, "b"),

                    };
                    takeTest(clangs);
                    break;
                }


                case 3:
                {
                    String q1 = "Q1.Who invented C++?\n" +
                            "\n" +
                            "\n \n"
                            + "(a) Dennis Ritchie\n(b)Ken Thompson\n(c)Brian Kernighan\n(d)Bjarne Stroustrup";

                    String q2 = "Q2. What is C++?\n" +
                            "\n" +
                            "\n\n"
                            + "(a)C++ is an object oriented programming language\n(b) C++ is a procedural programming language\n(c)C++ supports both procedural and object oriented programming language\n(d)C++ is a functional programming language";

                    String q3 = "Q3. Which of the following is the correct syntax of including a user defined header files in C++?\n" +
                            "\n" +
                            "\n\n"
                            + "(a)#include [userdefined]\n(b) #include “userdefined”\n(c)#include <userdefined.h>\n(d)#include <userdefined>";

                    String q4 = "Q4.  Which of the following is used for comments in C++?\n" +
                            "\n" +
                            "\n\n"
                            + "(a)/* comment */\n(b)// comment */\n(c) // comment\n(d)both // comment or /* comment */";

                    String q5 = "Q5.Which of the following user-defined header file extension used in c++?\n"
                            + "(a)hg\n(b)cpp\n(c)h\n(d)hf";



                    Cplus [] cpluss = {
                            new Cplus(q1, "d"),
                            new Cplus(q2, "c"),
                            new Cplus(q3, "b"),
                            new Cplus(q4, "d"),
                            new Cplus(q5, "c"),

                    };
                    takeTest(cpluss);
                    break;
                }

                case 4:
                {
                    String q1 = "Q1. PHP stands for -\n"
                            + "(a)Hypertext Preprocessor\n(b)Pretext Hypertext Preprocessor\n(c)Personal Home Processor\n(d)None of the above";

                    String q2 = "Q2.Who is known as the father of PHP?\n"
                            + "(a)Drek Kolkevi\n(b)List Barely\n(c)Rasmus Lerdrof\n(d)None of the above";

                    String q3 = "Q3.Variable name in PHP starts with -\n"
                            + "(a)! (Exclamation)\n(b)$ (Dollar)\n(c)& (Ampersand)\n(d)# (Hash)";

                    String q4 = "Q4. Which of the following is the default file extension of PHP?\n"
                            + "(a).php\n(b).hphp\n(c).xml\n(d).html";

                    String q5 = "Q5. Which of the following is not a variable scope in PHP?\n"
                            + "(a)Extern\n(b)Local\n(c)Static\n(d)Global";




                    Php [] phps = {
                            new Php(q1, "a"),
                            new Php(q2, "c"),
                            new Php(q3, "a"),
                            new Php(q4, "a"),
                            new Php(q5, "a"),

                    };
                    takeTest(phps);
                    break;
                }




                case 5:
                {
                    String q1 = "Q1. \t\n" +
                            "HTML is what type of language ?\n"
                            + "(a)Scripting Language\n(b)Markup Language\n(c)Programming Language\n(d)Network Protocol\n";

                    String q2 = "Q2. HTML uses\n"
                            + "(a)User defined tags\n(b)Pre-specified tags\n(c)Fixed tags defined by the language\n(d)Tags only for linking";

                    String q3 = "Q3.The year in which HTML was first proposed _______.\n"
                            + "(a)1990\n(b)1980\n(c)2000\n(d)1995";

                    String q4 = "Q4. Fundamental HTML Block is known as ___________.\n"
                            + "(a)HTML Body\n(b)HTML Tag\n(c)HTML Attribute\n(d)HTML Element";

                    String q5 = "Q5. Apart from <b> tag, what other tag makes text bold ?\n"
                            + "(a)<fat>\n(b)<strong>\n(c)<black>\n(d)<emp>";




                    Html [] htmls = {
                            new Html(q1, "b"),
                            new Html(q2, "c"),
                            new Html(q3, "a"),
                            new Html(q4, "b"),
                            new Html(q5, "b"),

                    };
                    takeTest(htmls);
                    break;
                }



                case 6:
                {
                    String q1 = "Q1. Which of the following symbols are used for comments in Python?\n"
                            + "(a)#\n(b)''\n(c)//\n(d)/**/";

                    String q2 = "Q2. Which keyword is used to define methods in Python?\n"
                            + "(a)Function\n(b)Method\n(c)Def\n(d)All of the above";

                    String q3 = "Q3. Which of the following is correct way to declare string variable in Python?\n"
                            + "(a)fruit = banana\n(b)fruit = [banana]\n(c)fruit = (banana)\n(d)fruit = 'banana'";

                    String q4 = "Q4. Which predefined Python function is used to find length of string?\n"
                            + "(a)stringlength()\n(b)strlen()\n(c)len()\n(d)length()";

                    String q5 = "Q5. Syntax of constructor in Python?\n"
                            + "(a) def __init__()\n(b)def _init_()\n(c)_init_()\n(d)All of the above.";




                    Python [] pythons = {
                            new Python(q1, "a"),
                            new Python(q2, "c"),
                            new Python(q3, "d"),
                            new Python(q4, "c"),
                            new Python(q5, "a"),

                    };
                    takeTest(pythons);
                    break;
                }




            }
        }
    }

    public static void takeTest(Java [] javas) {

        int score = 0;
        Scanner sc=new Scanner(System.in);

        System.out.println("Enter Name= ");
        String name=sc.nextLine();

        System.out.println("Enter Rollno= ");
        int rollno = sc.nextInt();

        System.out.println("");
        String n1ame=sc.nextLine();

        for (int i=0;i<javas.length;i++) {
            System.out.println(javas[i].a);
            String b = sc.nextLine();
            if (b.equals(javas[i].b)) {
                score++;
            }
        }
        System.out.println("Congratulation!" + " "+ name + " " + "Roll no.= " + " " + rollno + " " + "\n" + "You Scored " + score + "/" + javas.length + "\n");

    }

    public static void takeTest(Clang [] clangs) {

        int sco = 0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Name= ");
        String name=sc.nextLine();
        System.out.println("Enter Rollno= ");
        int rollno = sc.nextInt();

        System.out.println("");
        String n1ame=sc.nextLine();
        for (int i=0;i<clangs.length;i++) {
            System.out.println(clangs[i].c);
            String d = sc.nextLine();
            if (d.equals(clangs[i].d)) {
                sco++;
            }
        }
        System.out.println("Congratulation!" + " "+ name + " " + "Roll no.= " + " " + rollno + " " + "\n" + "You Scored " + sco + "/" + clangs.length + "\n");


    }


    public static void takeTest(Cplus [] cpluss) {

        int s = 0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Name= ");
        String name=sc.nextLine();
        System.out.println("Enter Rollno= ");
        int rollno = sc.nextInt();

        System.out.println("");
        String n1ame=sc.nextLine();
        for (int i=0;i<cpluss.length;i++) {
            System.out.println(cpluss[i].p);
            String q = sc.nextLine();
            if (q.equals(cpluss[i].q)) {
                s++;
            }
        }
        System.out.println("Congratulation!" + " "+ name + " " + "Roll no.= " + " " + rollno + " " + "\n" + "You Scored " + s + "/" + cpluss.length + "\n");



    }

    public static void takeTest(Php [] phps) {

        int scoress = 0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Name= ");
        String name=sc.nextLine();
        System.out.println("Enter Rollno= ");
        int rollno = sc.nextInt();

        System.out.println("");
        String n1ame=sc.nextLine();
        for (int i=0;i<phps.length;i++) {
            System.out.println(phps[i].z);
            String s = sc.nextLine();
            if (s.equals(phps[i].s)) {
                scoress++;
            }
        }
        System.out.println("Congratulation!" + " "+ name + " " + "Roll no.= " + " " + rollno + " " + "\n" + "You Scored " + scoress + "/" + phps.length + "\n");


    }



    public static void takeTest(Html[] htmls) {

        int score1 = 0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Name= ");
        String name=sc.nextLine();
        System.out.println("Enter Rollno= ");
        int rollno = sc.nextInt();

        System.out.println("");
        String n1ame=sc.nextLine();
        for (int i=0;i<htmls.length;i++) {
            System.out.println(htmls[i].g);
            String h = sc.nextLine();
            if (h.equals(htmls[i].h)) {
                score1++;
            }
        }
        System.out.println("Congratulation!" + " "+ name + " " + "Roll no.= " + " " + rollno + " " + "\n" + "You Scored " + score1 + "/" + htmls.length + "\n");

    }




    public static void takeTest(Python [] pythons) {

        int scores = 0;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Name= ");
        String name=sc.nextLine();
        System.out.println("Enter Rollno= ");
        int rollno = sc.nextInt();

        System.out.println("");
        String n1ame=sc.nextLine();
        for (int i=0;i<pythons.length;i++) {
            System.out.println(pythons[i].r);
            String s = sc.nextLine();
            if (s.equals(pythons[i].s)) {
                scores++;
            }
        }
        System.out.println("Congratulation!" + " "+ name + " " + "Roll no.= " + " " + rollno + " " + "\n" + "You Scored " + scores + "/" + pythons.length + "\n");



    }


}


class Java {
    String a;
    String b;

    public Java(String a, String b) {
        this.a = a;
        this.b = b;

    }
}

class Php {
    String z;
    String s;

    public Php(String z, String s) {
        this.z = z;
        this.s = s;

    }
}


class Python {
    String r;
    String s;

    public Python(String r, String s) {
        this.r = r;
        this.s = s;

    }
}

class Clang {
    String c;
    String d;

    public Clang(String c, String d) {
        this.c = c;
        this.d = d;

    }
}

class Html {
    String g;
    String h;

    public Html(String g, String h0) {
        this.g = g;
        this.h = h;

    }
}

class Cplus {
    String p;
    String q;

    public Cplus(String p, String q) {
        this.p = p;
        this.q = q;

    }
}



