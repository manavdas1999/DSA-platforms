
// Idea: Simple question, just need to put down thoughts correctly
// COMPLEXITY:
// time: O(n), space: O(n)


class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        // HashMap to store all words
        HashMap<String, Integer> map = new HashMap<>();
        
        // extracting words from s1
        for(String word : s1.split(" ")){
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        // extracting words from s2
        for(String word : s2.split(" ")){
            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        List<String> uncommonWords = new ArrayList<>();
        // adding words to list if its count is 1
        // i.e appears only once in both the strings.
        for(String word : map.keySet()){
            if(map.get(word) == 1){
                uncommonWords.add(word);
            }
        }

        // this somehow converts ArrayList<String> to String[]
        String[] result = uncommonWords.toArray(new String[0]);
        return result;
    }
}
