package hello;

public class ExceptionDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int a[]=new int[5];
		try {
		a[0]=45;
		a[1]=46;
		a[2]=47;
		a[3]=48;
		a[4]=30;
		a[5]=49;//index not found
for(int i=0;i<a.length;i++) 
	System.out.println(a[i]);
}
catch(Exception e) {
	
	System.out.println();
    }
		
	}
}
