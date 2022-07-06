class Solution {
    public String sortSentence(String s) {
        Map<Integer, String> wordMap = new HashMap<>();
        for (String w : s.split(" ")){
            int indexLast = w.length() - 1;
            int wordNumber = w.charAt(indexLast) - '0';
            String realWord = w.substring(0, indexLast);
            wordMap.put(wordNumber, realWord);
        }
        StringBuilder finalWord = new StringBuilder();
        for (Map.Entry<Integer, String> indexWord : wordMap.entrySet()){
            finalWord.append(indexWord.getValue());
            finalWord.append(" ");
        }
        return finalWord.toString().trim();
    }
}