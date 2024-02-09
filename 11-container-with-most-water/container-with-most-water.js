/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    leftWall = 0
    rightWall = height.length - 1
    maxWaterVol = Number.MIN_VALUE
    while(leftWall < rightWall){
        dist = rightWall - leftWall
        waterVol = (Math.min(height[rightWall], height[leftWall])) * dist
        maxWaterVol = Math.max(maxWaterVol, waterVol)
        if(height[leftWall] <= height[rightWall]){
            leftWall += 1
        }
        else{
            rightWall -= 1
        }
    }
    return maxWaterVol
};