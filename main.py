import json
import cal


def add(data):
    with open("Events.json", 'w') as fh:
        EventsName = input("Enter Name of Events: ")
        EventsDate = input("Enter Date of Events (ddmmyyyy): ")
        EventsTime = input("Enter Time of Events (hhmm): ")
        Priority = input("Enter Priority (Low, Med, High): ")
        Break = input("Is the Events breakable? y/n: ")
        Status=0
        Subtasks=[]
        subtaskCount = int(input("Enter number of Subtasks: "))
        for i in range(subtaskCount):
          Subtask = input("Enter Subtask: ")
          Subtasks.append(Subtask)
        
        CalendarAdd = {
            "EventsName": EventsName,
            "EventsDate": EventsDate,
            "EventsTime": EventsTime,
            "Priority": Priority,
            "Break": Break,
            "Status": Status,
            "Subtasks":Subtasks,
        }
        data["Events"].append(CalendarAdd)
        fh.write(json.dumps(data))


def remove(data):
    keyword = input("Enter Name of Events to be delete: ")
    with open("Events.json", "w") as fh:
        for i in range(len(data["Events"]) - 1):
            if data["Events"][i]['EventsName'] == keyword:
                data["Events"].pop(i)
        fh.write(json.dumps(data))


def move(data):
    with open("Events.json", "w") as fh:
        keyword = input("Enter Name of Events to be move: ")
        newDate = input("Enter Date to move to (ddmmyyyy): ")
        newTime = input("Enter Time to move to (hhmm): ")
        for i in range(len(data["Events"]) - 1):
            if data["Events"][i]['EventsName'] == keyword:
                data["Events"][i]['Eventsdate'] = newDate
                data["Events"][i]['EventsTime'] = newTime
        fh.write(json.dumps(data))


def priority(data):
    with open("Events.json", "w") as fh:
        keyword = input("Enter Name of Events to be move: ")
        newPriority = input("Enter Date to move to (ddmmyyyy): ")
        for i in range(len(data["Events"]) - 1):
            if data["Events"][i]['EventsName'] == keyword:
                data["Events"][i]['Priority'] = newPriority
        fh.write(json.dumps(data))


def edit(data):
    with open("Events.json", "w") as fh:
        keyword = input("Enter Name of Events to be move: ")
        newEventsName = input("Enter Name of Events: ")
        newEventsDate = input("Enter Date of Events (ddmmyyyy): ")
        newEventsTime = input("Enter Time of Events (hhmm): ")
        newPriority = input("Enter Priority (Low, Med, High): ")
        newBreak = input("Is the Events breakable? y/n: ")
        for i in range(len(data["Events"]) - 1):
            if data["Events"][i]['EventsName'] == keyword:
                data["Events"][i]['EventsName'] = newEventsName
                data["Events"][i]['EventsDate'] = newEventsDate
                data["Events"][i]['EventsTime'] = newEventsTime
                data["Events"][i]['Priority'] = newPriority
                data["Events"][i]['Break'] = newBreak
        fh.write(json.dumps(data))


def search(data):
    keyword = input("Enter Name of Events to be search: ")
    count = 0
    for i in range(len(data["Events"]) - 1):
        if data["Events"][i]['EventsName'] == keyword:
            print(data["Events"][i])
            count += 1
    if count > 1:
        print(keyword + " was found " + str(count) + " times.")
    elif count == 1:
        print(keyword + " was found once.")
    else:
        print("No such Events exists!")

def show():
    cal.show()


def connect():
    print("Work in Progress")

def countSubtask(data):
  keyword = input("Enter Name of Events to update: ")
  for i in range(len(data["Events"])):
    if data["Events"][i]['EventsName']==keyword:
      return len(data["Events"][i]['Subtasks'])

def addSubtask(data):
  with open("Events.json", "w") as fh:
    keyword = input("Enter Name of Events to update: ")
    contd='y'
    while(contd!='n'):
      task=input("Enter name of task: ")
      for i in range(len(data["Events"])):
        if data["Events"][i]['EventsName']==keyword:
          data["Events"][i]['Subtasks'].append(task)
      contd=input("Do you want to add another task? (y/n)")
    fh.write(json.dumps(data))

def changeStatus(data):
  with open("Events.json", "w") as fh:
    keyword = input("Enter Name of Events to update: ")
    for i in range(len(data["Events"])):
      if data["Events"][i]['EventsName']==keyword:
        if countSubtask(data)==0:
            done=input("Are you sure you have completed this task? ")
            if done=='y':
              data["Events"][i]['Status']=1
        else:
          for j in range(len(data['Events'][i]['Subtasks'])):
            done=input("Have you completed this task? ")
            if done=='y':
              print(j)
              print(data['Events'][i]['Subtasks'].pop(j))
              data['Events'][i]['Status']=0.5  
    fh.write(json.dumps(data))

def Menu(data):
    print('''
  1. Add
  2. Remove
  3. Move
  4. Priority
  5. Edit
  6. Search
  7. Show Calendar
  8. Connect to Calendar
  9. Change Status
  10. Add Subtask
  ''')
    try:
        mainChoice = int(input("Select from menu: "))
    except ValueError:
        print("Invalid Choice")
        Menu()

    menuChoice(mainChoice, data)


def menuChoice(choice, data):
    if choice == 1:
        add(data)
    elif choice == 2:
        remove(data)
    elif choice == 3:
        move(data)
    elif choice == 4:
        priority(data)
    elif choice == 5:
        edit(data)
    elif choice == 6:
        search(data)
    elif choice == 7:
        show()
    elif choice == 8:
        connect()
    elif choice == 9:
        changeStatus(data)
    elif choice == 10:
        addSubtask(data)
    elif choice == 11:
        countSubtask(data)
    else:
        print("Invalid Choice")
        Menu()


def connectJSON():
    try:
        with open("Events.json", 'r') as fh:
            data = json.load(fh)
    except:
        with open("Events.json", 'w+') as fh:
            baseJSON = {"Events": []}
            fh.write(json.dumps(baseJSON))
            fh.close()
        with open("Events.json", "r") as fh:
            data = json.load(fh)
    return data


if __name__ == '__main__':
    loopChoice = 'y'
    while loopChoice != 'n':
        Menu(connectJSON())

        loopChoice = input("Continue? ")
