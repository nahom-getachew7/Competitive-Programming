class Solution {
    public List<String> fizzBuzz(int n) {
        ArrayList <String> answer= new ArrayList <String>();
        for (int i=1; i<=n; i++)
        {
            if(i % 3 !=0 && i % 5 !=0)
            {
                answer.add(Integer.toString(i));
            }
            else if (i % 3 == 0 && i % 5 == 0)
            {
                answer.add("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                answer.add("Fizz");
            }
            else if (i % 5 == 0)
            {
                answer.add("Buzz");
            }
        }
        return answer;
    }
}