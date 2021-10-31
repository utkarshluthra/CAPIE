# Calendar-AI-API


## User Experience

### A. Basic User Experience
On opening the app for the first time, the user is asked to login. Once logged in, everything else can be done using preferred Calendar.

Once logged in, the app will work on Notification method:

1. _5 mins before Event:_ A notification will pop up asking if the user wishes to `Reschedule` the event. If yes, it moves directly to automatically rescheduling it to most appropriable time.
2. _After Task is complete:_ A notification will pop up asking if user wishes to `Add on`, `Move On`, `Completed`
3. By Default, if user doesn't click on anything the event will be rescheduled to most appropriate time.
4. If the user clicks on `Move On` in After-Event Notification, the event will be marked as not done and ignored, hence, the rescheduled event will be deleted.
5. If the user clicks on `Completed` in After-Event Notification, the reschedule will undo and marked as complete.
6. If the user clicks on `Add On`, another menu will continue asking:
> What percent of task is completed: [_____________] <br>
>       * Auto [ ]<br>
>       * Most Favourable Next [ ] <br>
>       * Closest Possible Next [ ] <br>
7. If the user clicks on `Auto`, the ML Engine will schedule the task according to training.
8. If the user clicks on `Most Favourable Next`, the ML Engine will find a time which is free and not consequently followed by or preceded by another task.
9. If the user clicks on `Closest Possible Next`, the ML engine will find the closest possible time, even if it means splitting the task into two parts.

If the user selects `Add On` the rescheduling will only happen according to the amount of task left.
Say if user has completed 3 hrs of a 4 hr long event, only the remaining 1 hr will be rescheduled.

### B. Creating Tasks directly from API
1. From main menu, user can create a new menu in a procedural manner.
2. The user can select sub-tasks which can be used to determine how to reschedule and break an event.
3. The user can provide deadline instead of a fixed time to further automatically set the time of the event according to current schedule.
