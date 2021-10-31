# Calendar-AI-API


## User Experience

On opening the app for the first time, the user is asked to login. Once logged in, everything else can be done using preferred Calendar.

Once logged in, the app will work on Notification method:

1. _5 mins before Event:_ A notification will pop up asking if the user wishes to `Act` or `Reschedule`
2. _After Task is complete:_ A notification will pop up asking if user wishes to `Add on`, `Move On`, `Completed`
3. If the user clicks on `Move On`, the event will be marked as not done and ignored.
4. If the user clicks on `Add On`, another menu will continue asking:
> What percent of task is completed: [_____________] <br>
>       * Auto [ ]<br>
>       * Most Favourable Next [ ] <br>
>       * Closest Possible Next [ ] <br>
5. If the user clicks on `Auto`, the ML Engine will schedule the task according to training
6. If the user clicks on `Most Favourable Next`, the ML Engine will find a time which is free and not consequently followed by or preceded by another task
7. If the user clicks on `Closest Possible Next`, the ML engine will

If the user selects `Add On` the rescheduling will only happen according to the amount of task left.
Say if user has completed 3 hrs of a 4 hr long event, only the remaining 1 hr will be rescheduled.

