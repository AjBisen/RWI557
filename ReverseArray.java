package hello;

public class ReverseArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
    int a[]={12,23,34,45,56};
    
    System.out.println("number of Array");
    
    for(int i=0;i<a.length;i++) {
    	System.out.println(a[i]);
    	
    }
    System.out.println();  
    System.out.println("Array in reverse order: ");  
    for (int i = a.length-1; i >= 0; i--) {  
        System.out.print(a[i] + " ");  
    }  
	}

}
