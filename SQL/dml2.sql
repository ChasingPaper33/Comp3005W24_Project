INSERT INTO ExerciseRoutine (MemberID, RoutineName, Description) 
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
    (3, '2024-01-31', 'SCR 7 permanently removed');