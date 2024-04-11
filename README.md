# ist-303-xr-team-ex-2

**Issues found**

	• Concurrent_Process function doesn't seem to write any files; the other two functions work
 
	• Round the second count to 0 or 1 digits… the float is too precise and not useful
 
	• Timer should be a helper function, not repeated
 
	• Concurrent functions are nearly identical; combine them

**Tasks**
Task #; Description;	Assigned;	Solution

1;	(New) Search term should be parameter;	_____;	Add parameter to each function

2;	(New) Check for term too short; use original value as default;	_____;	Check len() of string, default value if < 4

3;	(New) Put generated files into a "wiki_dl" folder;	_____;	Add "/wiki_dl" to file path

4;	Fix the Concurrent Process function which doesn't seem to return results;	_____;	Checked task manager, polling every second but function is sub-second, so can't see whether traffic is going to wikipedia site

5;	Make timer seconds more readable (e.g. one digit);	_____;	Round function to single digit

6;	Combine concurrent functions into one;	_____;	One "concurrent" function with new parameter "Thread" or "Process". Based on that, make a call to the Process or Thread executor.

7;	Create helper function for timer instead of duplicating output;	_____;	New helper function

