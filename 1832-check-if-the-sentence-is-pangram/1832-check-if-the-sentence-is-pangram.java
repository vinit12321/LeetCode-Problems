class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] mark = new boolean[26];
        int index=0;
        
        for(int i=0;i<sentence.length();i++){
            if(sentence.charAt(i)>='a' && sentence.charAt(i)<='z'){
                index=sentence.charAt(i)-'a';
            }
            else{
                continue;
            }
            mark[index]=true;

        }
        for(int i=0;i<mark.length;i++){
            if (mark[i] == false)
                return (false);


    }
          // If all characters were present
        return (true);
  }
}