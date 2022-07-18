package forreal;

class Solution {
    public int solution (int bridge_length, int weight, int[] worker_weights){
      int answer = 0;
      int[] bridge = new int[bridge_length];
      for (int i =0; i< bridge_length; i++){
        bridge[i] = 0;
      }
      int sum_bridge = 0;
      for (int i = 0; i <= bridge_length-1; i++){        
        for (int j=0; j<= worker_weights.length-1; j++){      
          bridge[i] = worker_weights[j];
          sum_bridge += bridge[i];
          if (sum_bridge > weight){
            bridge[i] = worker_weights[j+1];
            answer ++;
          }
        }
      }
      return answer;
      
    }
    public static void main(String[] args) {
      int b_l = 2;
      int w = 10;
      int[] arr = {7,4,5,6};
      Solution sol = new Solution();
      System.out.println(sol.solution(b_l, w, arr));
    }
  }