package hello;

public class ArrayGreter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a[]= {12, 23, 345, 67, 78,89};
		
		int b=a[0];
		
		for(int i=0;i< a.length; i++){
			
			if(a[i]>b) {
				b=a[i];
			}
			
		}
		
		
		System.out.println("gretest number=" +b);

	}

}
