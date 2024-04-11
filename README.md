# ist-303-xr-team-ex-2

Team reviewed the code and independently found some improvements, self-assigned tasks and using git hub we implemented the changes.
Assignments listed below under Tasks.
We collaborated "in person" (on Zoom call) in live conversation as we made changes.
A couple issues would have needed more time; we opted to list the proposed solution and just complete the other tasks

**Issues found**

	• Concurrent_Process function doesn't seem to write any files; the other two functions work
 
	• Round the second count to 0 or 1 digits… the float is too precise and not useful
 
	• Timer should be a helper function, not repeated
 
	• Need more error handling, also handle the issue (new reqt) where wiki_dl folder doesn't exist yet

**Tasks**
Task #; Description;	Assigned;	Solution

1;	DONE: (New) Search term should be parameter;	MARCIE;	Add parameter to each function

2;	DONE: (New) Check for term too short; use original value as default;	MARCIE;	Check len() of string, default value if < 4

3;	DONE: (New) Put generated files into a "wiki_dl" folder;	TREVOR;	Add "/wiki_dl" to file path

4;	NOT DONE; Fix the Concurrent Process function which doesn't seem to return results;	HJ;	Checked task manager, polling every second but function is sub-second, so can't see whether traffic is going to wikipedia site. Tested for 'resource exhaustion' and there is plenty of CPU capacity & memory left... no errors... simply can't see why no files are returned.

5;	DONE: Make timer seconds more readable (e.g. one digit);	TREVOR;	Round function to single digit

6;	DONE: Add error handling for the string;	HJ;	We'll just add a try/catch in case or error.

7;	NOT DONE: Create helper function for timer instead of duplicating output;	HJ;	New helper function... we would create a new function with a parameter of the calling function and have it print to screen.

8;	DONE: Create wiki_dl sub folder if it doesn't exist; TREVOR;  Call file.open parameter or option

