package softeer;
import java.util.*;
import java.io.*;

public class Test {
	    public static void main(String args[]) throws IOException
	    {
	        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        StringTokenizer st;
	        double sum = 0;
	        double avg = 0;
	        st = new StringTokenizer(br.readLine()," ");
	        while(st.hasMoreTokens()) {
	        	int N = Integer.parseInt(st.nextToken());
	        	int K = Integer.parseInt(st.nextToken());
	        	//System.out.println(N);
	        	//System.out.println(K);
	        	
	        	st = new StringTokenizer(br.readLine()," ");
	        	int[] score = new int[N];
	        	while(st.hasMoreTokens()) {
	        		for(int i=0; i<N; i++) {
	        		score[i] = Integer.parseInt(st.nextToken());
	        		//System.out.println(score[i]);
	        		}
	        	}
	        	
	        		for(int i=1; i<=K; i++) {
	        			st  = new StringTokenizer(br.readLine()," ");
	        			while(st.hasMoreTokens()) {
	        				int start = Integer.parseInt(st.nextToken());
	        				int end = Integer.parseInt(st.nextToken());
	        				for(int j=start-1;j<=end-1;j++) {
	        					
	        					sum += score[j];	        				
	        				}
	        				avg = Math.round( sum/(end-start+1) *100.0) / 100.0 ;
	        				System.out.printf("%.2f", avg); 
	        				//그냥 프린트시 소수점 없이 나누어지는 수는 .0까지만 출력되어서 printf 사용해야함
	        				sum = 0;
	        			}
	        		}
	        }
	    }	    
}
