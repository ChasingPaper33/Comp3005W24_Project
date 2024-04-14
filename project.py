import os
import datetime
import psycopg2


connection = psycopg2.connect(dbname= "FitnessClub", user="postgres", password = "REPLACE_WITH_OWN_PASSWORD", host="localhost",port="5432")


cur = connection.cursor()

cur.execute("""CREATE TABLE Member (
    MemberID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(100),
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(30),
    Weight REAL,
    BMI REAL
);

CREATE TABLE FitnessGoal (
    GoalID SERIAL PRIMARY KEY,
    MemberID INTEGER REFERENCES Member(MemberID),
    Description TEXT,
    DeadlineDate DATE,
    Completed BOOLEAN
);

CREATE TABLE ExerciseRoutine (
    MemberID INTEGER REFERENCES Member(MemberID),
    RoutineName VARCHAR(255),
    Description TEXT,
    PRIMARY KEY (MemberID, RoutineName)
);

CREATE TABLE Trainer (
    TrainerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(100),
    Email VARCHAR(255),
    Phone VARCHAR(30)
);

CREATE TABLE TrainerSchedule (
    TrainerID INTEGER REFERENCES Trainer(TrainerID),
    DayOfWeek VARCHAR(15),
    StartTime TIME,
    EndTime TIME,
    PRIMARY KEY (TrainerID, DayOfWeek)
);


CREATE TABLE TrainingSession (
    SessionID SERIAL PRIMARY KEY,
    MemberID INTEGER REFERENCES Member(MemberID),
    TrainerID INTEGER REFERENCES Trainer(TrainerID),
    DayOfWeek VARCHAR(15),
    SessionDate DATE,
    StartTime TIME,
    EndTime TIME
);


CREATE TABLE GroupFitnessClass (
    ClassID SERIAL PRIMARY KEY,
    ClassName VARCHAR(100) NOT NULL,
    Description TEXT,
    StartTime TIME,
    EndTime TIME,
    DayOfWeek VARCHAR(15),
    TrainerID INTEGER REFERENCES Trainer(TrainerID),
    ClassDate DATE
);


CREATE TABLE ClassRegistrations (
    MemberID INTEGER REFERENCES Member(MemberID),
    ClassID INTEGER REFERENCES GroupFitnessClass(ClassID),
    PRIMARY KEY (MemberID, ClassID)
);

CREATE TABLE AdministrativeStaff (
    StaffID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(100),
    Email VARCHAR(255),
    Phone VARCHAR(30)
);


CREATE TABLE RoomBooking (
    BookingID SERIAL PRIMARY KEY,
    RoomNumber INTEGER NOT NULL,
    StaffID INTEGER REFERENCES AdministrativeStaff(StaffID),
    BookingDate DATE,
    StartTime TIME,
    EndTime TIME,
    BookedOn DATE,
    ReservedBy VARCHAR(255)
);


CREATE TABLE Billing (
    BillingID SERIAL PRIMARY KEY,
    MemberID INTEGER REFERENCES Member(MemberID),
    ServiceType VARCHAR(255),
    Amount NUMERIC,
    BillingDate DATE,
    Paid BOOLEAN
);


CREATE TABLE Payment (
    BillingID INTEGER REFERENCES Billing(BillingID),
    PaymentDate DATE,
    PRIMARY KEY (BillingID,PaymentDate)
);


CREATE TABLE EquipmentMaintenance (
    MaintenanceID SERIAL PRIMARY KEY,
    StaffID INTEGER REFERENCES AdministrativeStaff(StaffID),
    MaintenanceDate DATE,
    Details TEXT
);""")

connection.commit()

cur.execute(""" INSERT INTO Member (FirstName, LastName, Email, Phone, Weight, BMI)
VALUES
    ('John', 'Allen', 'john_allen@example.com', '3435686179', 75.5, 19.3),
    ('Belle', 'Hadge', 'bella_hadge@example.com', '5196527371', 62.1, 26.7),
    ('Alice', 'Dreams', 'alice_dreams@example.com', '8195617289', 68.9, 18.1);



INSERT INTO Trainer (FirstName, LastName, Email, Phone)
VALUES
    ('Michael', 'James', 'michael_james@example.com', '3432529303'),
    ('Celine', 'Wayne', 'celine_wayne@example.com', '6839557686'),
    ('Ulriel', 'Brawn', 'ulriel_brawn@example.com', '7429218990');



INSERT INTO AdministrativeStaff (FirstName, LastName, Email, Phone)
VALUES
    ('Emily', 'Perkins', 'emily_perkins@example.com', '6139137585'),
    ('Roland', 'Keath', 'roland_keath@example.com', '6835198043'),
    ('Amy', 'Lancia', 'amy_lancia@example.com', '3435892711');



""")

connection.commit()

cur.execute(""" INSERT INTO ExerciseRoutine (MemberID, RoutineName, Description) 
VALUES
    (1, 'Morning Workout', '10-minute warm-up, push-ups->3 sets->10 reps, sit-ups - 2 sets of 40 reps, squats 4 sets of 10 reps, end with 5-minute cool down.'),
    (1, 'Afterwork Workout', '15-minute stretch routine focusing on for hamstrings and splits, 3km treadmill'),
    (2, 'Arm Workout', '15 bicep curls, 10 tricep curls, benchpress till failure'),
    (2, 'Abs Workout', '5 2-minute plank routine with variations, 3 sets with 15 reps of crunches, legs raise and hanging leg raise: 2 sets and 7 reps each'),
    (3, 'Cardio', '15-minute HIIT workout, 5-minute rest, 10-minute HIIT workout, 10-minute rest, stretch lower body then finish with 1 hr light treadmill');

INSERT INTO FitnessGoal (MemberID, Description, DeadlineDate, Completed)
VALUES
    (1, 'Lose weight', '2024-12-31', TRUE),
    (2, 'Improve cardio', '2024-12-31', TRUE),
    (3, 'Increase bench press', '2024-12-31', TRUE);


INSERT INTO TrainerSchedule (TrainerID, DayOfWeek, StartTime, EndTime)
VALUES
    (1, 'Monday', '09:00', '17:00'),
    (1, 'Tuesday', '09:00', '17:00'),
    (2, 'Wednesday', '08:00', '16:00'),
    (2, 'Thursday', '08:00', '16:00'),
    (3, 'Friday', '10:00', '18:00'),
    (3, 'Saturday', '10:00', '18:00');


INSERT INTO TrainingSession (MemberID, TrainerID, DayOfWeek, SessionDate, StartTime, EndTime)
VALUES
    (1, 1, 'Monday', '2024-04-15', '09:00', '11:00'),
    (2, 2, 'Wednesday','2024-04-17', '10:00', '12:00'),
    (3, 3, 'Friday', '2024-04-19', '11:00', '13:00');


INSERT INTO GroupFitnessClass (ClassName, Description, StartTime, EndTime, DayOfWeek, TrainerID, ClassDate)
VALUES
    ('Zumba', 'Dance, Dance, Dance', '19:00', '20:00', 'Thursday', 2, '2024-03-21'),
    ('Yoga', 'Come Relax through Yoga', '14:00', '15:00', 'Monday', 1, '2024-04-15'),
    ('Zumba', 'Dance and Workout', '15:00', '17:00', 'Tuesday', 1, '2024-04-16'),
    ('Pilates', 'strengthen your the body', '14:00', '15:00', 'Wednesday', 2, '2024-04-17');


INSERT INTO ClassRegistrations (MemberID, ClassID)
VALUES
    (1, 1), 
    (1, 3),
    (2, 1),
    (2, 2),
    (3, 2),
    (3, 3);


INSERT INTO Billing (MemberID, ServiceType, Amount, BillingDate, Paid)
VALUES
    (1, 'Membership Fees', 50.00, '2024-04-01', FALSE),
    (2, 'Membership Fees', 50.00, '2024-04-03', FALSE),
    (3, 'Membership Fees', 50.00, '2024-04-07', FALSE);


INSERT INTO RoomBooking (RoomNumber, StaffID, BookingDate, StartTime, EndTime, BookedOn, ReservedBy)
VALUES
    (1, 1, '2024-05-26', '10:00', '11:00', '2024-04-02' , 'Charles Wright'),
    (2, 2, '2024-06-11', '16:00', '17:00', '2024-04-08' , 'MontC Ltd.'),
    (3, 3, '2024-05-01', '11:00', '12:00', '2024-04-10' , 'Mr.Rogers');


INSERT INTO EquipmentMaintenance(StaffID, MaintenanceDate, Details)
VALUES
    (1, '2024-03-31', 'N/A'),
    (2,'2024-02-29', 'Treadmill 4 need replacement'),
    (3, '2024-01-31', 'SCR 7 permanently removed');""")

connection.commit()

def clear_console():
    if (os.name == "nt"):
        os.system("cls")
    elif (os.name == "posix"):
        os.system("clear")
    else:
        return

def register_member():
    clear_console()
    print("Welcome to H&H Health and Fitness Club")
    print("Please share with us some of your info to get you started. All of them are required, don't leave anything blank")
    print()
    fname = (input("what is your first name? ")).strip()
    lname = (input("what is your last name? ")).strip()
    email = (input("what is your email address? ")).strip()
    cur.execute("SELECT MemberID FROM Member WHERE Email = %s",(email,))
    used = cur.fetchall()
    if (len(used)==0):
        phone = (input("what is your phone number? ")).strip()
        weight = float((input("what is your weight in kg? ")).strip())
        bmi = float((input("what is your bmi?(to 2 decimal places only please): ")).strip())

        cur.execute("""INSERT INTO Member (FirstName, LastName, Email, Phone, Weight, BMI) VALUES
                        (%s, %s, %s, %s, %s, %s);""",(fname, lname, email, phone, weight, bmi))
        
        connection.commit()

        cur.execute("SELECT MemberID FROM Member WHERE Email = %s", (email,))
        memberId = cur.fetchall()

        cur.execute("""INSERT INTO Billing (MemberID, ServiceType, Amount, BillingDate, Paid) VALUES
                        (%s, 'Membership Fees', %s, %s, %s);""",(memberId[0][0], 50.00, datetime.date.today(), False))
        connection.commit()

        print()
        print("Thank your for joining us. You have been billed membership fees, you can pay them from your dashboard or with a staff at front desk.")
        k = input("press Enter to be redirected to your dashboard")
        member_dashboard(memberId[0][0])
    else:
        print("Error, that email address is already in used by a user")
        k = input("You'll be redirected to portal. Press Enter to continue")
    
def login_member():
    clear_console()
    print()
    email = (input("Please input your email address: ")).strip()
    cur.execute("SELECT MemberID, FirstName, LastName FROM Member WHERE Email = %s ;",(email,))
    member = cur.fetchall()

    if (len(member)==0):
        print("Error; no such user.")
        k = input("Redirecting you to portal. Press Enter to continue: ")
    else:
        member_dashboard(member[0][0])
    
def login_trainer():
    clear_console()
    email = (input("Please input your email address: ")).strip()
    cur.execute("SELECT TrainerID, FirstName, LastName FROM Trainer WHERE Email = %s ;",(email,))
    the_trainer = cur.fetchall()

    if (len(the_trainer)==0):
        print("Error, no such trainer registered with that email")
        x = input("You'll be redirected to portal. Please press Enter: ")
    else:
        trainer_dashboard(the_trainer[0][0],the_trainer[0][1], the_trainer[0][2])

def login_staff():
    clear_console()
    email = (input("Please input your email address: ")).strip()
    cur.execute("SELECT StaffID, FirstName, LastName FROM AdministrativeStaff WHERE Email = %s",(email,))
    the_staff = cur.fetchall()

    if (len(the_staff)==0):
        print("No such staff exists")
        p = input("Redirecting you to portal. Press Enter to continue: ")

    else:
        staff_dashboard(the_staff[0][0],the_staff[0][1],the_staff[0][2])

def member_health_metric(memberId):
    clear_console()
    print("Your health metrics are as follows")
    cur.execute("SELECT Weight, BMI FROM Member WHERE MemberID = %s",(memberId,))
    hlm = cur.fetchall()
    print(f"Weight: {hlm[0][0]}     BMI: {hlm[0][1]}")
    print()
    print()
    up = (input("Would you like to update your weight and bmi? (y/n): ")).strip().lower()
    if (up=='y'):
        weight = float((input("What is your new weight (in kg)? ")).strip())
        bmi = float((input("What is your new bmi? ")).strip())
        cur.execute("UPDATE Member SET Weight = %s, BMI = %s WHERE MemberID = %s ;",(weight,bmi,memberId))
        connection.commit()
        print("Your health metrics have been updated")
    
    t = input("Press Enter to get back to your dashboard: ")

def member_fitness_goal(memberId):
    while True:
        clear_console()
        print("Menu")
        print("1. View ongoing fitness goals")
        print("2. Add a fitness goal")
        print("3. View fitness achievements")
        print("4. Update ongoing fitness goals")
        print("0. go back")
        print()

        ch = (input("What is your choice? (input number): ")).strip()
        if (ch =='1'):
            cur.execute("SELECT Description, DeadlineDate FROM FitnessGoal WHERE (MemberID = %s and Completed = %s);",(memberId, False))
            goals = cur.fetchall()

            if (len(goals)!=0):
                for i in range(len(goals)):
                    print(f"{i+1}. {goals[i][0]}  Deadline:{goals[i][1]}")
            else:
                print("You have no ongoing fitness goals")

            t = input("Press Enter to continue")
        elif (ch == '2'):
            descri = (input("What is the description of your new fitness goal: ")).strip()
            deadline = input("What is the deadline date for this goal (in format YYY-MM-DD (numbers only)): ")
            deadline = datetime.datetime.strptime(deadline,"%Y-%m-%d")
            cur.execute("""INSERT INTO FitnessGoal (MemberID, Description, DeadlineDate, Completed) VALUES 
                        (%s,%s,%s,%s);""",(memberId,descri,deadline,False))
            connection.commit()
            t = input("New fitness goal was added. Press Enter to continue")

        elif (ch == '3'):
            cur.execute("SELECT Description FROM FitnessGoal WHERE (MemberID = %s and Completed = %s);",(memberId, True))
            achievements = cur.fetchall()

            if (len(achievements)!=0):
                print("You have achived the following goals you have set for yourself")
                for an_achivement in achievements:
                    print(f"{an_achivement[0]}")
            else:
                print("You have no achievements yet")
            t = input("Press Enter to continue")
            
        elif (ch == '4'):
            cur.execute("SELECT GoalID, Description, DeadlineDate FROM FitnessGoal WHERE (MemberID = %s and Completed = %s);",(memberId, False))
            goals = cur.fetchall()

            if (len(goals)!=0):
                print("Your fitness goals are as follows")
                for i in range(len(goals)):
                    print(f"{i+1}. {goals[i][1]}  Deadline:{goals[i][2]}")
                print()
            else:
                print("You have no ongoing fitness goals. Hence you cannot make any updates")
                t = input("Press Enter to continue")
                continue

            print("Menu")
            print("1. Mark a goal complete")
            print("2. Delete a fitness goal")
            print("3. Change a fitness goal")
            print("0. go back")
            print()

            fitchoice = (input("What is option choice? (input number): ")).strip()

            if (fitchoice == '1'):
                index= int((input("What number is the fitness goal you want to mark complete: ")).strip())
                if (index>=1 and index<=len(goals)):
                    cur.execute("UPDATE FitnessGoal SET Completed = %s WHERE GoalID = %s", (True,goals[index-1][0]))
                    connection.commit()
                    t = input("Your goal was marked completed. Press Enter to continue")

            elif (fitchoice=='2'):
                index= int((input("What number is the fitness goal you want to delete: ")).strip())
                if (index>=1 and index<=len(goals)):
                    cur.execute("DELETE FROM FitnessGoal WHERE GoalID = %s", (goals[index-1][0],))
                    connection.commit()
                    t = input("Your goal was deleted. Press Enter to continue: ")

            elif (fitchoice == '3'):
                index= int((input("What number is the fitness goal you want to update: ")).strip())
                if (index>=1 and index<=len(goals)):
                    des = (input("do you want to change the description? (y/n): ")).strip().lower()
                    if (des=='y'):
                        descri = (input("what is your new description? ")).strip()
                    else:
                        descri = goals[index-1][1]
                    deadline = (input("do you want to change the deadline date? (y/n): ")).strip().lower()
                    if (deadline == 'y'):
                        ddate = input ("what is your new deadline date (input in the format YYYY-MM-DD (only numbers)): ")
                        ddate = datetime.datetime.strptime(ddate,"%Y-%m-%d")
                    else:
                        ddate = goals[index-1][2]
                    cur.execute("UPDATE FitnessGoal SET Description = %s, DeadlineDate = %s WHERE GoalID = %s", (descri,ddate,goals[index-1][0]))
                    connection.commit()
                    t = input("Update was made. Press Enter to continue: ")
            else:
                continue
        else:
            break

def view_exercise_routine(memberId):
    cur.execute("SELECT * FROM ExerciseRoutine WHERE MemberID = %s",(memberId,))
    eRoutines = cur.fetchall()
    if (len(eRoutines)==0):
        print("You have no exercise routines")
        return False
    
    print("Exercise routines;")
    print()
    for i in range(len(eRoutines)):
        print(f"{i+1}. {eRoutines[i][1]} : {eRoutines[i][2]}")
    print()
    return True

def member_exercise_routine(memberId):
    while True:
        clear_console()
        print("Menu")
        print("1. View my exercise routines")
        print("2. Add an exercise routine")
        print("3. Delete an exercise routine")
        print("4. Update an exercise routine")
        print("0. go back")
        print()

        e_choice = (input("What is your choice (Input number): ")).strip()

        if (e_choice=='1'):
            view_exercise_routine(memberId)
            k = input("Press Enter to continue")

        elif (e_choice == '2'):
            routine_name = (input("What is the new exercise routine's name (Please make sure your routines have unique names): ")).strip()
            routine_descri = (input("What is the descriptiion of this routine. (write in a single line. Only press Enter when you are done): ")).strip()
            cur.execute(""" INSERT INTO  ExerciseRoutine (MemberID, RoutineName, Description) VALUES
                        (%s,%s,%s)""",(memberId,routine_name,routine_descri))
            connection.commit()
            k = input("Your routine was added. Press Enter to continue")

        elif (e_choice =='3'):
            cur.execute("SELECT * FROM ExerciseRoutine WHERE MemberID = %s",(memberId,))
            eRoutines = cur.fetchall()
            if (len(eRoutines)==0):
                print("You have no exercise routines")
            else:
                print("Exercise routines;")
                print()
                for i in range(len(eRoutines)):
                    print(f"{i+1}. {eRoutines[i][1]} : {eRoutines[i][2]}")
                print()
                index = int((input("what is the index of the routine you want to delete: ")).strip())
                if (index<1 or index > len(eRoutines)):
                    print("Invalid index")
                else:
                    cur.execute("DELETE FROM ExerciseRoutine WHERE (MemberID = %s AND RoutineName = %s AND Description = %s)",(memberId,eRoutines[index-1][1],eRoutines[index-1][2]))
                    connection.commit()
                    print("Exercise Routine was deleted")
            k = input("Press Enter to continue")

        elif(e_choice == '4'):
            cur.execute("SELECT * FROM ExerciseRoutine WHERE MemberID = %s",(memberId,))
            eRoutines = cur.fetchall()
            if (len(eRoutines)==0):
                print("You have no exercise routines")
            else:
                print("Exercise routines;")
                print()
                for i in range(len(eRoutines)):
                    print(f"{i+1}. {eRoutines[i][1]} : {eRoutines[i][2]}")
                print()
                index = int((input("what is the index of the routine you want to update: ")).strip())
                if (index<1 or index > len(eRoutines)):
                    print("Invalid index")
                else:
                    change_name = (input("Do you want to change the routine name ? (y/n): ")).strip()
                    if (change_name=='y'):
                        r_name = (input("What is the new name of the exercise routine: ")).strip()
                    else:
                        r_name = eRoutines[index-1][1]

                    change_descri = input("Do you want to change the description of the routine? (y/n): ")
                    if (change_descri=='y'):
                        r_descri = (input("what is the new description of the routine: ")).strip()
                    else:
                        r_descri = eRoutines[index-1][2]

                    cur.execute("UPDATE ExerciseRoutine SET RoutineName = %s, Description = %s WHERE (MemberID = %s AND RoutineName = %s)",(r_name,r_descri,eRoutines[index-1][0],eRoutines[index-1][1]))
                    connection.commit()
                    print("Exercise Routine was updated")
            k = input("Press Enter to continue: ")
        else:
            break

def member_personal_info(memberId):
    clear_console()
    print("Your personal info is as follows:")
    cur.execute("SELECT MemberID, FirstName, LastName, Email, Phone FROM Member WHERE MemberID = %s",(memberId,))
    pinfo = cur.fetchall()
    print(f"MemberID:{pinfo[0][0]} first name: {pinfo[0][1]}, last name: {pinfo[0][2]}  email adress: {pinfo[0][3]}  phone number: {pinfo[0][4]}")
    print()

    updIn = input("Would you like to update your personal information? (y/n): ")
    if (updIn=='y'):
        print("Which one would you like to update")
        print("1. Full name")
        print("2. Email address")
        print("3. Phone number")
        change = input("Option (number): ")
        if change =='1':
            firstname = (input("What is your first name: ")).strip()
            lastname = (input("What is your last name: ")).strip()
            cur.execute("UPDATE Member SET FirstName = %s, LastName = %s WHERE MemberID = %s",(firstname, lastname, memberId))
            connection.commit()
            t = input("Change made. Press Enter to continue")

        elif change == '2':
            new_email = (input("What is your new email address ? ")).strip()
            cur.execute("SELECT MemberID FROM Member WHERE Email = %s",(new_email,))
            used = cur.fetchall()
            if (len(used)==0):
                cur.execute("UPDATE Member SET Email = %s WHERE MemberID = %s",(new_email,memberId))
                connection.commit()
                print("Your email address was changed")
            else:
                print("Error, that email is already used by another member")
            t = input("Press Enter to continue")

        elif change=='3':
            phone_number = (input("What is your new phone number? ")).strip()
            cur.execute("UPDATE Member SET Phone = %s WHERE MemberID = %s",(phone_number,memberId))
            connection.commit()
            t = input('Phone number was updated. Press Enter to continue')

def member_billing_and_payment(memberId):
    while True:
        clear_console()
        print("Menu")
        print("1. View Pending Bills")
        print("2. Make a payment")
        print("0. go back")
        print()

        billchoice = (input("What option number are you choosing? ")).strip()
        if (billchoice=='1'):
            viewMemberBills(memberId)
            t = input("Press Enter to continue")

        elif (billchoice =='2'):
            cur.execute("SELECT BillingID, ServiceType, Amount, BillingDate FROM Billing WHERE MemberID = %s AND Paid= %s",(memberId,False))
            pending_bills = cur.fetchall()
            if (len(pending_bills)==0):
                print("You have no pending bills")
            else:
                print("Your pending bills are")
                for a_bill in pending_bills:
                    print(f"BillingID: {a_bill[0]} {a_bill[1]}  CAD {a_bill[2]}  Billed On: {a_bill[3]}")
                
                print()
                billId = (input("What is the BillingID of the bill you wish to pay for: ")).strip()
                cur.execute("SELECT 1 FROM Billing WHERE (BillingID = %s AND MemberID = %s)",(billId,memberId))
                bill_exists = cur.fetchall()
                if (len(bill_exists)!=0):
                    cur.execute("UPDATE Billing SET Paid = %s WHERE BillingID = %s ",(True,billId))
                    connection.commit()
                    cur.execute(""" INSERT INTO Payment (BillingID, PaymentDate) VALUES
                                (%s,%s)""",(billId,datetime.date.today()))
                    connection.commit()
                    print("Payment was successful")
                else:
                    print("Billing with that ID doesn't exists")

            k = input("Press Enter to continue")
            
        else:
            break

def member_fitness_class(memberId):
    while True:
        clear_console()
        print("Menu")
        print("1. View my upcoming group fitness classes")
        print("2. Register for a group fitness class")
        print("0. go back")

        fclass_choice = (input("What is your choice (input number): ")).strip()
        if (fclass_choice=='1'):
            cur.execute("""SELECT ClassName, Description, DayOfWeek, ClassDate, StartTime, EndTime FROM 
                        Member JOIN ClassRegistrations ON Member.MemberID = ClassRegistrations.MemberID JOIN GroupFitnessClass ON ClassRegistrations.ClassID = GroupFitnessClass.ClassID
                        WHERE (Member.MemberID = %s AND ClassDate >= %s);""",(memberId,datetime.date.today()))
            fit_class = cur.fetchall()
            if (len(fit_class)==0):
                print("You are not registered in any upcoming group fitness class")
            else:
                print("Your upcoming fitness classes are: ")
                for a_fclass in fit_class:
                    print(f"{a_fclass[0]} : {a_fclass[1]} on {a_fclass[2]} {a_fclass[3]} from {a_fclass[4]} to {a_fclass[5]}") 
            
            print()
            k = input("Press Enter to continue")   

        elif(fclass_choice=='2'):
            cur.execute("SELECT ClassID, ClassName, Description, DayOfWeek, ClassDate, StartTime, EndTime FROM GroupFitnessClass WHERE ClassDate > CURRENT_DATE")
            up_classes = cur.fetchall()
            if (len(up_classes)==0):
                print("No upcoming classes are being offered")
            else:
                for x in range(len(up_classes)):
                    print(f"{x+1}. {up_classes[x][1]} : {up_classes[x][2]} on {up_classes[x][3]} from {up_classes[x][4]} to {up_classes[x][5]}")
                print()

                index = int((input("What is the index/number of the fitness class you want to register in?: ")).strip())
                if (index<1 or index >len(up_classes)):
                    print("invalid index")
                else:
                    cur.execute("SELECT * FROM ClassRegistrations WHERE (ClassID = %s AND MemberID = %s)",(up_classes[index-1][0],memberId))
                    already_registered = cur.fetchall()
                    if (len(already_registered)==0):
                        cur.execute("INSERT INTO ClassRegistrations (MemberID, ClassID) VALUES (%s, %s)",(memberId,up_classes[index-1][0]))
                        connection.commit()
                        cur.execute("INSERT INTO Billing (MemberID, ServiceType, Amount, BillingDate, Paid) VALUES (%s,%s,%s,%s,%s)",(memberId,'Group Fitness Class Fees', 8.00, datetime.date.today(), False))
                        connection.commit()
                        print("Registration confirmed. You have been billed for this class")
                    else:
                        print("You have already registered in that class")
            print()
            k = input("Press Enter to continue")
        else:
            break

def view_upcoming_training_sessions(memberId):
    cur.execute("SELECT * FROM TrainingSession WHERE (MemberID = %s AND SessionDate >= %s )",(memberId,datetime.date.today()))
    uts = cur.fetchall()
    if (len(uts)==0):
        k = input("You have no upcoming personal training sessions. Press Enter to continue")
        return False
    else:
        print("Your upcoming training sessions are")
        for a_uts in uts:
            cur.execute("SELECT FirstName, LastName From Trainer WHERE TrainerID = %s ",(a_uts[2],))
            name = cur.fetchall()
            print(f"SessionID:{a_uts[0]}  {a_uts[3]} {a_uts[4]} from {a_uts[5]} to {a_uts[6]} with trainer {name[0][0]} {name[0][1]}")
        print()
        k = input("Press Enter to continue")
        return True

def member_schedule_pt_session(memberId):
    abandon = False
    trainer_found = False
    while (abandon==False and trainer_found==False):
        clear_console()
        print("Note: Personal Training Sessions are of 2 hours only.")
        session_date = input("What date do you want your session to be (give format YYYY-MM-DD only)? ")
        session_date = datetime.datetime.strptime(session_date,"%Y-%m-%d")
        cur.execute("SELECT TrainerID, FirstName, LastName, StartTime, EndTime FROM Trainer NATURAL INNER JOIN TrainerSchedule WHERE DayOfWeek = %s",(session_date.strftime("%A"),))
        trainers = cur.fetchall()
        if (len(trainers)==0):
            print("There are no trainers working on that day")
            cont = input("Do you want to retry with another date (y/n)[n will bring you back to Personal-Training-Sessions General Menu]: ")
            if (cont=='n'):
                abandon = True
                break
        else:
            print("Trainers available are")
            for i in range(len(trainers)):
                print(f"{i+1}. {trainers[i][1]}  {trainers[i][2]}")
            print()
            while (trainer_found==False and abandon==False):
                index = int((input("What is the number/index of the trainer you want to schedule a personal training session with: ")).strip())
                if (index <1 or index>len(trainers)):
                    print("invalid index")
                else:
                    print(f"Trainer {trainers[index-1][1]} {trainers[index-1][2]} works from {trainers[index-1][3]} to {trainers[index-1][4]} on {session_date.strftime("%A")}s ")
                    print(f"Trainer {trainers[index-1][1]} {trainers[index-1][2]} is unvailable on that day during those times: ")
                    cur.execute("SELECT StartTime, EndTime FROM TrainingSession WHERE (TrainerID = %s AND SessionDate = %s);",(trainers[index-1][0],session_date))
                    ts_unv = cur.fetchall()
                    cur.execute("SELECT StartTime, EndTime FROM GroupFitnessClass WHERE (TrainerID = %s AND ClassDate = %s);",(trainers[index-1][0],session_date))
                    gfc_unv = cur.fetchall()
                    if (len(ts_unv) == 0) and (len(gfc_unv)==0):
                        print("NIL")
                    else:
                        for a_ts_unv in ts_unv:
                            print(f"{a_ts_unv[0]} - {a_ts_unv}")
                        print()
                        for a_gfc_unv in gfc_unv:
                            print(f"{a_gfc_unv[0]} - {a_gfc_unv[1]}")
                        print()
                    start_time = (input("What time do you want your session to start (HH:MM format only in 24hr clock/military time): ")).strip()
                    start_time = datetime.datetime.strptime(start_time,"%H:%M")
                    end_time = start_time + datetime.timedelta(hours=2)
                    start_time = start_time.time()
                    end_time = end_time.time()
                    if (TrainerAvailable(trainers[index-1][0],session_date.strftime("%A"),session_date,start_time,end_time)==True):
                        trainer_found = True
                        cur.execute("""INSERT INTO TrainingSession (MemberID, TrainerID, DayOfWeek, SessionDate, StartTime, EndTime) VALUES
                                    (%s,%s,%s,%s,%s,%s)""",(memberId,trainers[index-1][0],session_date.strftime("%A"),session_date,start_time,end_time))
                        connection.commit()
                        cur.execute("""INSERT INTO Billing (MemberID, ServiceType, Amount, BillingDate, Paid) VALUES
                                    (%s,%s,%s,%s,%s)""",(memberId,'Personal Training Session Fees',60,datetime.date.today(),False))
                        k = input ("Your personal training session has been scheduled and you have been billed accordingly. Press Enter to continue")
                        break
                    else:
                        retry = (input("Do you want to retry with another trainer: (y/n): ")).strip().lower()
                        if (retry=='n'):
                            abandon = True
                            break

def member_reSchedule_session(memberId):
    print("Please note that rescheduling is subject to trainer's availability. In many instances rescheduling may not be permissible")
    if (view_upcoming_training_sessions(memberId) == True):
        sid = (input("What is the sessionID of the sessions you would like to reschedule ? ")).strip()
        cur.execute("SELECT * FROM TrainingSession WHERE (SessionID = %s AND MemberID = %s)",(sid,memberId))
        session = cur.fetchall()
        if (len(session)==0):
            print("There is no training session with that ID")
        else:
            session_date = input("What new date do you want your session to be (give format YYYY-MM-DD only)? ")
            session_date = datetime.datetime.strptime(session_date,"%Y-%m-%d")
            start_time = (input("What new time do you want your session to start (HH:MM format only in 24hr clock/military time): ")).strip()
            start_time = datetime.datetime.strptime(start_time,"%H:%M")
            end_time = start_time + datetime.timedelta(hours=2)
            start_time = start_time.time()
            end_time = end_time.time()
            if (TrainerAvailable(session[0][2],session_date.strftime("%A"),session_date,start_time,end_time)==True):
                cur.execute("UPDATE TrainingSession SET SessionDate = %s, DayOfWeek = %s, StartTime = %s, EndTime = %s WHERE SessionID = %s",(session_date, session_date.strftime("%A"), start_time, end_time, sid))
                connection.commit()
                print("Your session was rescheduled successfully. No extra fees apply")
                
    k = input("Press Enter to continue")

def member_cancel_session(memberId):
    if (view_upcoming_training_sessions(memberId)==True):
        sid = (input("What is the SessionID of the session you wish to cancel: ")).strip()
        cur.execute("SELECT * FROM TrainingSession WHERE (SessionID = %s AND MemberID = %s )",(sid,memberId))
        session = cur.fetchall()
        if (len(session)==0):
            print("You have no session with that ID")
        else:
            cur.execute("DELETE FROM TrainingSession WHERE (SessionID=%s)",(sid,))
            connection.commit()
            print("Your session was cancelled")
            print("Please enquire at front desk for possibility of refunds")

    k = input("Press Enter to continue")

def member_training_session(memberId):
    while True:
        clear_console()
        print("Menu.")
        print("1. View upcoming personal training sesssions")
        print("2. Schedule a personal training sessions")
        print("3. Cancel a personal training session")
        print("4. Reschedule a personal training session")
        print("0. go back")
        print()

        ts_choice = (input("What option do you choose: ")).strip()
        if (ts_choice=='1'):
            view_upcoming_training_sessions(memberId)
        elif (ts_choice =='2'):
            member_schedule_pt_session(memberId)
        elif (ts_choice =='3'):
            member_cancel_session(memberId)
        elif (ts_choice == '4'):
            member_reSchedule_session(memberId)
        else:
            break


def member_dashboard(memberId):
    while True:
        clear_console()
        print("-------H&H Health and Fitness Club-------")
        print()
        print("Menu: ")
        print("1. Health Metrics")
        print("2. Fitness Goals&Achievements")
        print("3. Exercise routines")
        print("4. 1-On-1 Training Sessions")
        print("5. Group Fitness Classes")
        print("6. Bills and Payments")
        print("7. Personal info")
        print("0. Logout")
        print()

        activity = (input("What menu choice would you like to go to? (input number): ")).strip()

        if (activity=='1'):
            member_health_metric(memberId)
        elif (activity=='2'):
            member_fitness_goal(memberId)
        elif (activity == '3'):
            member_exercise_routine(memberId)
        elif (activity == '4'):
            member_training_session(memberId)
        elif (activity == '5'):
            member_fitness_class(memberId)
        elif (activity == '6'):
            member_billing_and_payment(memberId)
        elif (activity == '7'):
            member_personal_info(memberId)

        else:
            break

def viewMemberBills(memberID):
    cur.execute("SELECT BillingID, ServiceType, Amount, BillingDate FROM Billing WHERE MemberID = %s AND Paid= %s",(memberID,False))
    pending_bills = cur.fetchall()
    if (len(pending_bills)==0):
        print("No pending bills")
        return False
    else:
        cur.execute("SELECT FirstName, LastName FROM Member WHERE MemberID = %s",(memberID,))
        name = cur.fetchall()
        print(f"Pending Bills for {name[0][0]} {name[0][1]}    MemberID: {memberID} ")
        for a_bill in pending_bills:
            print(f"BillingID: {a_bill[0]} {a_bill[1]}  CAD {a_bill[2]}  Billed On: {a_bill[3]}")
        return True
    
def trainer_dashboard(trainerId, fname, lname):
    while True:
        clear_console()
        print(f"Welcome back {fname} {lname}")
        print(f"Trainer ID: {trainerId}")
        print()
        print("Menu.")
        print("1. View upcoming training sessions")
        print("2. View upcoming group classes")
        print("3. View a member profile")
        print("4. Shifts schedule")
        print("0. Logout")
        print()

        choice = (input("What option would you like(Input number)? ")).strip()
        if (choice == '1'):
            trainer_upcoming_sessions(trainerId)

        elif (choice =='2'):
            trainer_upcoming_classes(trainerId)

        elif (choice == '3'):
            trainer_view_member_profile()
            
        elif (choice =='4'):
            trainer_shifts(trainerId)

        else:
            break

def trainer_upcoming_sessions(trainerId):
    clear_console()
    cur.execute("SELECT DayOfWeek, SessionDate, StartTime, EndTime, MemberID FROM TrainingSession WHERE (TrainerID = %s AND SessionDate >= CURRENT_DATE);",(trainerId,))
    upcomingSessions = cur.fetchall()
    if (len(upcomingSessions)==0):
        print("No upcoming training sessions")
    else:
        for a_session in upcomingSessions:
            cur.execute("SELECT FirstName, LastName FROM Member WHERE MemberID = %s", (a_session[4],))
            client_name = cur.fetchall()
            print(f"{a_session[0]} { a_session[1]} :  {a_session[2]} - {a_session[3]} with {client_name[0][0]} {client_name[0][1]} ")
            print()
    x = input("Press Enter to go back to dashboard")

def trainer_upcoming_classes(trainerId):
    clear_console()
    cur.execute("SELECT ClassName, DayOfWeek, ClassDate, StartTime, EndTime FROM GroupFitnessClass WHERE (TrainerID = %s AND ClassDate >= CURRENT_DATE);",(trainerId,))
    grclass = cur.fetchall()

    if (len(grclass)==0):
        print("You have no group fitness class to teach")
        print()
    else:
        for a_class in grclass:
            print(f"{a_class[0]} : {a_class[1]} {a_class[2]} : {a_class[3]} - {a_class[4]}")
            print()
    x = input("Press Enter to go back to dashboard: ")

def trainer_view_member_profile():
    memberfname = (input("What is that member's first name: ")).strip().lower().title()
    memberlname = (input("What is that member's last name: ")).strip().lower().title()

    cur.execute("SELECT FirstName, LastName, Weight, BMI, Email, Phone FROM Member WHERE (FirstName = %s AND LastName = %s) ;",(memberfname,memberlname))
    the_member = cur.fetchall()
    if (len(the_member)==0):
        print("No such member with this name")
        k = input("Press Enter to continue")
    else:
        print("Member profile requested:")
        print(f"{the_member[0][0]} {the_member[0][1]} : Weight of {the_member[0][2]} kg, bmi of {the_member[0][3]}")
        print(f"Contact info; email: {the_member[0][4]}  phone number: {the_member[0][5]}")
        print()
        k = input("Press Enter to continue")
    
def trainer_shifts(trainerId):
    while True:
        clear_console()
        print("Your shifts are as follows")
        cur.execute("SELECT DayOfWeek, StartTime, EndTime FROM TrainerSchedule WHERE TrainerID = %s ORDER BY DayOfWeek ASC",(trainerId,))
        shifts = cur.fetchall()
        if (len(shifts)==0):
            print("None")
        else:
            for a_shift in shifts:
                print(f"{a_shift[0]} from {a_shift[1]} to {a_shift[2]}")

        print()
        print()
        print("Would you like to:")
        print("1. Add a shift")
        print("2. Delete a shift")
        print("3. Update a shift")
        print("0. go back")
        print()

        ch = input("Your choice is (input number): ")

        if (ch=='1'):
            print("Please note that you cannot add a shift to a day you already have a shift for")
            cont = (input("Knowing this, would you like to continue? (y/n): ")).strip().lower()
            if (cont == 'y'):
                dayOfW = (input("what day of the week would you like to add a shift to (monday/tuesday etc): ")).strip().lower().title()
                cur.execute("SELECT * FROM TrainerSchedule WHERE (TrainerID = %s AND DayOfWeek = %s)",(trainerId,dayOfW))
                onShift = cur.fetchall()
                if (len(onShift)==0):
                    startT = (input("what is your start time (Please give your time in that format HH:MM [e.g 14:30] in 24hr clock/military time): ")).strip()
                    startT = datetime.datetime.strptime(startT, "%H:%M").time()
                    endT = (input("What is your end time (Please give your time in that format HH:MM [e.g 22:00] in 24hr clock/military time): ")).strip()
                    endT = datetime.datetime.strptime(endT, "%H:%M").time()
                    cur.execute ("""INSERT INTO TrainerSchedule (TrainerID, DayOfWeek, StartTime, EndTime) VALUES
                                (%s, %s, %s, %s );""",(trainerId,dayOfW,startT,endT))
                    connection.commit()
                    k = input("Shift added, press Enter to continue: ")
                else:
                    k = input("You already have a shift for that day. Press Enter to continue")

        elif (ch =='2'):
            if (len(shifts)==0):
                print("You have no shifts")
                q = input("Press Enter to continue:")
            else:
                dayOfW = (input("What day of the week is the shift you would like to delete (monday/friday etc): ")).strip().lower().title()
                cur.execute("DELETE FROM TrainerSchedule WHERE (TrainerID = %s AND DayOfWeek = %s);",(trainerId,dayOfW))
                connection.commit()
                cur.execute("DELETE FROM TrainingSession WHERE (TrainerID = %s AND DayOfWeek = %s)",(trainerId,dayOfW))
                k = input ("Shift deleted. Affected members will be notified by email. Press Enter to continue: ")

        elif (ch =='3'):
            if (len(shifts)==0):
                print("You have no shifts to update")
            else:
                dayOfW = (input("what day of the week would you update (monday/tuesday etc): ")).strip().lower().title()
                startT = (input("what is your new start time (please give in the format HH:MM in 24hr clock/military time): ")).strip()
                startT = datetime.datetime.strptime(startT, "%H:%M").time()
                endT = (input("What is your new end time (please give in the format HH:MM in 24hr clock/military time): ")).strip()
                endT = datetime.datetime.strptime(endT, "%H:%M").time()
                cur.execute("UPDATE TrainerSchedule SET StartTime = %s, EndTime = %s WHERE (TrainerID = %s AND DayOfWeek = %s)", (startT,endT,trainerId,dayOfW))
                connection.commit()
        else:
            break

def roomBookingManagement(staffId):
    while True:
        clear_console()
        print("Options:")
        print("1. View all  upcoming room bookings")
        print("2. Register a new room booking")
        print("3. Cancel a room booking")
        print("4. Update a room booking")
        print("0. go back")

        ch = (input("What option are you choosing (input number)? ")).strip()

        if (ch == '1'):
            cur.execute("SELECT * FROM RoomBooking WHERE BookingDate >= CURRENT_DATE ORDER BY BookingDate ASC")
            roomBookings = cur.fetchall()
            if (len(roomBookings)==0):
                print("no upcoming room bookings")
            else:
                for a_booking in roomBookings:
                    print(f"booking id:{a_booking[0]} room number: {a_booking[1]} last update made by staff with id: {a_booking[2]}")
                    print(f"room booked for {a_booking[3]} from {a_booking[4]} to {a_booking[5]}")
                    print(f"Booking done on {a_booking[6]} under name {a_booking[7]}")
                    print()
            print()
            t = input("Press Enter to continue")

        elif (ch == '2'):
            rnum = (input("for what room number is that booking? ")).strip()
            bdate = (input("what date is that booking for (give in format YYYY-MM-DD only numbers): ")).strip()
            bdate = datetime.datetime.strptime(bdate, "%Y-%m-%d")

            cur.execute("SELECT BookingID FROM RoomBooking WHERE (RoomNumber = %s AND BookingDate = %s );",(rnum,bdate))
            already_booked = cur.fetchall()

            if (len(already_booked)==0):
                staT = (input("what is the starting time of the booking? (give in format HH:MM in 24hr clock/ military time only) ")).strip()
                staT = datetime.datetime.strptime(staT, "%H:%M").time()
                endT = (input("what is the ending time of the booking? (give in format HH:MM in 24hr clock/ military time only) ")).strip()
                endT = datetime.datetime.strptime(endT, "%H:%M").time()
                rsename = (input("Under what name is that booking being made? ")).strip()
                cur.execute("""INSERT INTO RoomBooking (RoomNumber, StaffID, BookingDate, StartTime, EndTime, BookedOn, ReservedBy) VALUES
                            (%s, %s, %s, %s, %s, %s, %s );""",(rnum,staffId,bdate,staT,endT,datetime.date.today(),rsename))
                connection.commit()
                print("Room booking created")
            else:
                print("Error; This room is already booked for that day.")

            t = input("Press Enter to continue")

        elif (ch == '3'):
            roomid = (input("what is the room booking id ?: ")).strip()
            cur.execute("SELECT BookingID FROM RoomBooking WHERE BookingID = %s ",(roomid,))
            exists = cur.fetchall()
            if (len(exists)==0):
                print("Error, there is no booking with that ID")
                t = input("Press Enter to continue")
            else:
                cur.execute("DELETE FROM RoomBooking WHERE BookingID = %s ",(roomid,))
                connection.commit()
                print("Room Booking was cancelled. Process refund of customer on card external terminal")
                t = input("Press Enter to continue")

        elif (ch =='4'):
            print("What you would like to change about the booking ?")
            print("1. The  room number of the room that is booked")
            print("2. The name under which booking is made")
            print()

            print("Changes to date and time of the room booking cannot be made as different fees may apply")

            change = input("what is your choice (input number): ")
            bid = (input("what is the room booking id you wish to make that change on: ")).strip()
            cur.execute("SELECT BookingID, BookingDate, RoomNumber FROM RoomBooking WHERE BookingID = %s", (bid,))
            rbid = cur.fetchall()
            if (len(rbid)==0):
                print("There's no room booking with that ID")
                t = input("Press Enter to continue")
                continue

            if (change == '1'):
                rnum = (input("what is the new room number?" )).strip()
                cur.execute("SELECT BookingID FROM RoomBooking WHERE (RoomNumber = %s AND BookingDate = %s );",(rnum,rbid[0][1]))
                already_booked = cur.fetchall()
                if (len(already_booked)==0):
                    cur.execute("UPDATE RoomBooking SET RoomNumber = %s, StaffID = %s WHERE BookingID = %s",(rnum,staffId,bid))
                    connection.commit()
                    print("room change made")
                else:
                    print("Error, that room is already booked for that day")
                t = input("Press Enter to continue")

            elif (change == '2'):
                rsvname = (input("What is the new name to put the booking under:")).strip()
                cur.execute("UPDATE RoomBooking SET ReservedBy = %s, StaffID = %s WHERE BookingID = %s",(rsvname,staffId,bid))
                connection.commit()
                print("booked-under name changed")
                t = input("Press Enter to continue")
            else:
                t = input("Press Enter to continue")

        else:
            break

def EquipmentMaintenaceMonitoring(staffId):
    while True:
        clear_console()
        print("Menu")
        print("1. View last 3 maintenace reports")
        print("2. Record a maintenace report")
        print("0. go back")

        ch = (input("What is your choice number:")).strip()
        if (ch=='1'):
            cur.execute("SELECT * FROM EquipmentMaintenance ORDER BY MaintenanceDate DESC LIMIT 3")
            reports = cur.fetchall()
            if (len(reports)!= 0):
                for a_report in reports:
                    print(f"Report Id: {a_report[0]} made by Staff with ID {a_report[1]} on {a_report[2]} details as follows: {a_report[3]}")

            t = input("Press Enter to continue")

        elif (ch == '2'):
            details = input("What are is your report on equipment maintenance (write in a single line, press enter when you are done): ")
            cur.execute("""INSERT INTO EquipmentMaintenance(StaffID, MaintenanceDate, Details) VALUES
                        (%s,%s,%s);""",(staffId,datetime.date.today(),details))
            connection.commit()
            print("report made")
            t = input("Press Enter to continue")
        else:
            break
    
def TrainerAvailable(trainerId,dayOfW,the_day,the_startT,the_endT):
    cur.execute("SELECT TrainerID FROM Trainer WHERE TrainerID = %s",(trainerId,))
    tid = cur.fetchall()
    if (len(tid)==0):
        print("Trainer with that ID not found")
        return False
    
    cur.execute("SELECT StartTime, EndTime FROM TrainerSchedule WHERE (TrainerID = %s AND DayOfWeek = %s)",(trainerId,dayOfW))
    shifts = cur.fetchall()
    if (len(shifts)==0):
        print("Trainer doesn't work on that day")
        return False 
    else:
        if (((shifts[0][0]<= the_startT <= shifts[0][1]) and (shifts[0][0]<= the_endT <=shifts[0][1]))!= True):
            print("Trainer isn't on the clock on those times")
            return False
    
    available = True
    cur.execute("SELECT StartTime, EndTime FROM TrainingSession WHERE (TrainerID = %s AND SessionDate = %s)",(trainerId,the_day))
    session = cur.fetchall()
    if (len(session)!=0):
        for a_session in session:
            if (a_session[0]<= the_startT <= a_session[1]) or (a_session[0]<= the_endT <= a_session[1]):
                available = False
    
    if (available == False):
        print("Trainer is unvailable")
        return False
    
    cur.execute("SELECT StartTime, EndTime FROM GroupFitnessClass WHERE (TrainerID = %s AND ClassDate = %s)",(trainerId,the_day))
    gclasses = cur.fetchall()
    if (len(gclasses)!=0):
        for a_gclass in gclasses:
            if (a_gclass[0]<= the_startT <= a_gclass[1]) or (a_gclass[0]<= the_endT <=a_gclass[1]):
                available = False

    if (available == False):
        print("Trainer is unvailable")
    
    return available

def FitnessGroupClassScheduling():
    while True:
        clear_console()
        print("Menu.")
        print("1. View upcoming fitness classes")
        print("2. Add a new fitness group class")
        print("3. Cancel a class")
        print("4. Change trainer for a class")
        print("0. go back")
        print()

        ch = (input("What is your choice (input option number): ")).strip()
        if (ch=='1'):
            cur.execute("SELECT ClassID, ClassName, Description, DayOfWeek, StartTime, EndTime, ClassDate, TrainerID, FirstName, LastName FROM GroupFitnessClass NATURAL INNER JOIN Trainer WHERE ClassDate >= CURRENT_DATE ;")
            upcomingC = cur.fetchall()
            if (len(upcomingC)==0):
                print("No upcoming classes")
            else:
                for a_class in upcomingC:
                    print(f"ClassID: {a_class[0]} ClassName: {a_class[1]} taught by trainer {a_class[7]}: {a_class[8]} {a_class[9]}")
                    print(f"On {a_class[3]} {a_class[6]} from {a_class[4]} till {a_class[5]}")
                    print(f"Class Description: {a_class[2]}")
                    print()
                
            t = input("Press Enter to continue ")

        elif (ch=='2'):
            print("Before making the class make sure the Trainer in charge of that class is free")
            y = (input("Do you want to continue (y/n): ")).strip().lower()

            if (y=='y'):
                classname = input("what is the name of the new class: ")
                descri = input("give a brief description of the class: ")
                cdate = (input("what is the date of the class (give in format YYYY-MM-DD): ")).strip()
                cdate = datetime.datetime.strptime(cdate, "%Y-%m-%d")
                doW = cdate.strftime("%A")
                stT = (input("what is the start time of the class (give in format HH:MM 24 hr clock/military time): ")).strip()
                stT = datetime.datetime.strptime(stT, "%H:%M").time()
                enT = (input("what is the ending time of the class (give in format HH:MM 24 hr clock/military time): ")).strip()
                enT = datetime.datetime.strptime(enT, "%H:%M").time()
                trainerId = (input("What is the trainerID of the trainer for that class: ")).strip()
                if (TrainerAvailable(trainerId,doW,cdate,stT,enT)):
                    cur.execute("""INSERT INTO GroupFitnessClass (ClassName, Description, StartTime, EndTime, DayOfWeek, TrainerID, ClassDate) VALUES
                                (%s,%s,%s,%s,%s,%s,%s);""",(classname,descri,stT,enT,doW,trainerId,cdate))
                    connection.commit()
                    print("Fitness group class created")
            
            t = input("Press Enter to continue")

        elif (ch=='3'):
            print("Please make sure you know beforehand the classID of the class to cancel")
            y = (input("Do you want to continue (y/n): ")).strip().lower()
            if (y=='y'):
                classID = (input("what is the classID of the class to cancel:  ")).strip()
                cur.execute("DELETE FROM ClassRegistrations WHERE ClassID = %s",(classID,))
                connection.commit()
                cur.execute("DELETE FROM GroupFitnessClass WHERE ClassID = %s",(classID,))
                connection.commit()
                print("Class was cancelled. The members previously registered will be notified by email.")
                print()

            t = input("Press Enter to continue")

        elif (ch=='4'):
            print("Please make sure that the new trainer for that class is available")
            y = (input("do you want to still change trainer (y/n): ")).strip().lower()
            if (y=='y'):
                classId = (input("What is the classID of the related class: ")).strip()
                cur.execute("SELECT StartTime,EndTime,ClassDate,DayOfWeek FROM GroupFitnessClass WHERE ClassID = %s",(classId,))
                clI = cur.fetchall()
                if (len(clI)!=0):
                    trainer_Id = (input("what is the trainerID of the new trainer for the class: ")).strip()
                    if (TrainerAvailable(trainer_Id,clI[0][3],clI[0][2],clI[0][0],clI[0][1])==True):
                        cur.execute("UPDATE GroupFitnessClass SET TrainerID = %s WHERE ClassID = %s",(trainer_Id,classId))
                        connection.commit()
                        print("Class was updated")
                else:
                    print("No class with that ID exists")

            t = input("Press Enter to continue")
        else:
            break

def FileBilling():
    print("Make sure you have the memberID of the member you wish to bill beforehand")
    y = (input("Would you like to continue (y/n): ")).strip().lower()
    if (y=='y'):
        clear_console()
        memberId = (input("What is the ID of the member you wish to bill: ")).strip()
        cur.execute("SELECT MemberID, FirstName, LastName FROM Member WHERE MemberID = %s ",(memberId,))
        mid = cur.fetchall()
        if (len(mid)==0):
            print("There is no such member with that id. Please get a proper member ID")
        else:
            print(f"You are billing member {mid[0][0]} , {mid[0][1]}  {mid[0][2]} ")
            print()

            serviceT = (input("For what kind of service is the bill (one of: membership fess/personal training session fees/group fitness class fees/other): ")).strip().title()
            amt = float((input("What is the amount of this bill in CAD (only numbers please): ")).strip())
            cur.execute("""INSERT INTO Billing (MemberID, ServiceType, Amount, BillingDate, Paid) VALUES
                        (%s,%s,%s,%s,%s)""",(memberId,serviceT,amt,datetime.date.today(),False))
            connection.commit()
            print("Bill was filed to member")
    else:
        print("Alright!")

    print()
    k = input("Redirecting you to dashboard. Press Enter to continue: ")

def ProcessMemberPayment():
    print("Please make sure you have the memberID of the member beforehand")
    y = (input("Do you have the memberID? (y/n): ")).strip().lower()
    if (y=='y'):
        memberID = (input("What is the memberID of the member to process payment for: ")).strip()
        if (viewMemberBills(memberID) == True):
            billingId = (input("What is the billingID of bill to process payment: ")).strip()
            cur.execute("SELECT BillingID, Amount FROM Billing WHERE (BillingID = %s AND MemberID = %s)",(billingId, memberID))
            bill = cur.fetchall()
            if (len(bill)==0):
                print("Invalid BillingID")
            else:
                cur.execute("UPDATE Billing SET Paid = %s WHERE BillingID = %s",(True,billingId))
                connection.commit()    
                cur.execute("""INSERT INTO PAYMENT (BillingID, PaymentDate) VALUES 
                            (%s,%s)""",(bill[0][0], datetime.date.today()))
                connection.commit()
                print("Payment was processed")

    t = input("Press Enter to continue: ")

def findMemberID():
    memberfname = (input("What is that member's first name: ")).strip().lower().title()
    memberlname = (input("What is that member's last name: ")).strip().lower().title()
    cur.execute("SELECT MemberID  FROM Member WHERE (FirstName = %s AND LastName = %s) ;",(memberfname,memberlname))
    the_member = cur.fetchall()
    if (len(the_member)==0):
        print("No such member with this name")
        k = input("Press Enter to continue")
    else:
        print(f"Member ID requested: {the_member[0][0]}")
        k = input("Press Enter to continue")

def staff_dashboard(staffId,fname, lname):
    while True:
        clear_console()
        print(f"Welcome back {fname} {lname}")
        print(f"StaffId: {staffId}")

        print()
        print("Menu")
        print("1. Room Bookings")
        print("2. Equipment Maintenance Monitoring")
        print("3. Fitness Group Class Scheduling")
        print("4. File a Billing")
        print("5. Process a Payment")
        print("6. Find MemberID of a member")
        print("0. Logout")
        print()

        activity = (input("What is your choice (input number): ")).strip()
        if (activity == '1'):
            roomBookingManagement(staffId)
        
        elif (activity == '2'):
            EquipmentMaintenaceMonitoring(staffId)

        elif (activity == '3'):
            FitnessGroupClassScheduling()

        elif (activity == '4'):
            FileBilling()
        
        elif (activity == '5'):
            ProcessMemberPayment()

        elif (activity == '6'):
            findMemberID()
        else:
            break



def portal():
    while True:
        clear_console()
        print()
        print("Welcome to H&H Health and Fitness Club")
        print()
        print("Menu")
        print("1. Login")
        print("2. Sign up")
        print("0. exit and power off")
        print()

        choice = (input("Input your choice (as a number): ")).strip()

        if (choice == "1"):
            clear_console()
            print("Would you like to login as a; ")
            print("1. Member")
            print("2. Trainer")
            print("3. Administrative Staff")
            print("0. go back")

            login = input("Input your choice (as a number); ")

            if (login=="1"):
                login_member()

            elif (login=="2"):
                login_trainer()

            elif (login == "3"):
                login_staff()

            else:
                k = input("Getting you back to portal. Press Enter to continue")

        elif (choice == "2"):
            register_member()

        else:
            break
            
portal()

cur.close()
connection.close()