display dialog "Are you sure!?" buttons {"No", "Yes"}

display dialog "Just accept it!" buttons {"Accept"} default button 1

display dialog "The answer is C" buttons {"A", "B", "C"} default button 3

display dialog "Who are you?" default answer "nobody"

set theDialogText to "The curent date and time is " & (current date) & "."
display dialog theDialogText 
