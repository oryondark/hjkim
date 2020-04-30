/* hj Kim */
// N == 11 --> 11소수 출력
// N == 30 --> 2,3,5 소인수 값 출력
// example 
//소수 : 11
//소인 수 값 : 2
//소인 수 값 : 3
//소인 수 값 : 5
public class primeFactorization {
//소인수 분해 예제

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int N = 30;
		int i = 2;
		int k = 0; // 최초로 분해된 값에서 k 가 카운팅이 되지 않았을 경우, 이는 소수다. 
		
		
		while(true) {
			
			if( N % i == 0) {
				//System.out.printf("입력 값 : %d\n", N);
				if( N == i ) {
					if( k == 0)
						System.out.printf("소수 : %d\n", i);
					else
						System.out.printf("소인 수 값 : %d\n", i);
					break;
					
				}
				
				k++;
				N = N / i;
				System.out.printf("소인 수 값 : %d\n", i);
				
			} else {
				i++;
				
			}
					
		}
		
	}

}
