
// IDEA:
// 1. All idea explained in comments

// COMPLEXITY:
// Time - O(1)
// Constant - O(1)

class Solution {
    public int findMinDifference(List<String> timePoints) {
        // note: in a 24hr clock we can only have 24*60min = 1440 minutes
        // i.e 1440 unique values only, so if timePoints.length > 1440, it sure contains duplicates
        int size = timePoints.size();
        if(size > 1440) return 0;

        // now to check if any duplicate present in remaining 1440 values
        // we are using an boolean array of 1440 values, which will cover all possible timestamps
        // index value will be the value of time in minutes and timeStamps[index] will tell if this time exists or not, also check for duplicates
        boolean[] timeStamps = new boolean[1440];
        for(String time : timePoints){
            int timeInMin = minutes(time);
            if(timeStamps[timeInMin]){
                // time already exists - duplicate
                return 0;
            }
            timeStamps[timeInMin] = true;
        }

        // Now, there are two cases - 
        // 1. diff between time in series
        // 2. diff between first timeStamp and lastTimeStamp (clock is 24hrs from lastTimeStamp or FirstTimeStamp)

        // case 1
        int firstTimeStamp = Integer.MAX_VALUE;
        int prevTimeStamp = Integer.MAX_VALUE;  // put anyvalue, does not matter
        int minTimeDiff = Integer.MAX_VALUE;
        
        for(int i=0; i < 1440; i++){
            if(timeStamps[i]){
                if(firstTimeStamp == Integer.MAX_VALUE){
                    // first timestamp only gets updated once
                    firstTimeStamp = i;                   
                } else{
                    // if not the first timeStamp
                    minTimeDiff = Math.min(minTimeDiff, i - prevTimeStamp);
                }
                // prevTimeStamp always gets updated if a timeStamp is found(true)
                prevTimeStamp = i;
            }
        }

        // case 2 - NOTE: prevTimeStamp contains the last valid timePoint
        minTimeDiff = Math.min(minTimeDiff, 1440 + firstTimeStamp - prevTimeStamp);

        return minTimeDiff;
    }

    public int minutes(String time){
        // hh:mm, index: 01234, 01-hh, 34-mm
        int hr = Integer.parseInt(time.substring(0,2));
        int min = Integer.parseInt(time.substring(3));
        return hr * 60 + min;
    }
}
