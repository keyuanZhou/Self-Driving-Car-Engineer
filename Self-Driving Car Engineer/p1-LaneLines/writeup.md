# Finding Lane Lines on the Road

Keyuan Zhou

***
The goals / steps of this project are the following:

* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report
***

## Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

Although it was easy to build a pipeline to detect the lane lines in segments, I spent some time on adjusting the parameters of the hough_lines function, especially the min_line_len and max_line_gap. And finally I got good pictures that matched the example very well. 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by calculating the regression line of the points on the left and on the right separately. After applying this method at the beginning, the line I got was not good enough and sometimes had offset. So I filtered points of a segment whose slope was smaller than .5 to avoid some outliers. Then I got some good lines.

### 2. Identify potential shortcomings with your current pipeline

One potential shortcoming was that the lines were not stable, for the lines shaked greatly from frame to frame.

### 3. Suggest possible improvements to your pipeline

Currently I am not sure how to improve this pipeline...