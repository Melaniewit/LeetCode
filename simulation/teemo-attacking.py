class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        

        #result variable
        ans=0

        #the time position each time poisoned end
        expired=0

        #traversel the list timeSeries
        for i in range(len(timeSeries)):

        #if current time > the lastest poisoned time end
            if timeSeries[i]>=expired:
                ans=ans+duration


        #get poisoned, add duration
            
        #else:if current time <=the lastest poisoned time end

        #add posion can't overlap
        #the new poisoned  end time is timeSeries[i]+duration
        #the last position end time is expired variable

        #substract them to get last poisoned time
            else:
                ans=ans+timeSeries[i]+duration-expired
                

            #update the the time position each time poisoned end
            #same for if and else siuation
            expired=timeSeries[i]+duration

        #return the result variable
        return ans
