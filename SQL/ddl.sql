CREATE TABLE Member (
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
);