
// IDEA:
// 1. convert time to minutes for easy comparison
// 2. store converted time points to an array (n2)
// 3. sort the array - now we only have to check timeDiff in a single flow (nlogn)
// 4. NOTE: Only catch is clock is round, i.e 22:00 is closer to 01:00 then 06:00 to 01:00;
// hence to roundoff time, use 1440 + firstTime - lastTime (24:00 == 00:00 => 24*60+0 = 1440)

// COMPLEXITY:
// time : O(nLogn)
// space: O(n)

class Solution {
    public int findMinDifference(List<String> timePoints) {
        int size = timePoints.size();
        int[] timePointsInMin = new int[size];
        for(int i = 0; i<timePointsInMin.length; i++){
            timePointsInMin[i] = minutes(timePoints.get(i));
        }
        Arrays.sort(timePointsInMin);

        int minTimeDiff = 1440 + timePointsInMin[0] - timePointsInMin[size - 1];

        for(int i = 0; i < size-1; i++){
            int consecutiveTimeDiff = timePointsInMin[i+1] - timePointsInMin[i];
            minTimeDiff = Math.min(minTimeDiff, consecutiveTimeDiff);
        }
        return minTimeDiff;
    }

    public int minutes(String time){
        String[] parts = time.split(":");
        int hr = Integer.parseInt(parts[0]);
        int min = Integer.parseInt(parts[1]);
        return hr*60 + min;
    }
}
