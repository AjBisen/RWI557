package hello;


import java.util.*;
class YourAge extends  RuntimeException{
	YourAge(String Msg){
		super(Msg);
	}
}

public class ExcThrow {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		Scanner sc=new Scanner(System.in);
		 System.out.println("enter a age");
	    int age=sc.nextInt();
	   
			
		
//         int age=22;
	
		if(age<18) {
			throw new YourAge ("yor are not eligible ");
		}
		else {
			System.out.println("you are eligible for vole");
		}
	}

	
}
