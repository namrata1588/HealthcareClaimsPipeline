CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(10),
    Age INT
);

CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY,
    PatientID INT,
    ClaimAmount DECIMAL(10,2),
    ClaimDate DATE,
    ClaimStatus VARCHAR(20)
);

INSERT INTO Patients VALUES
(1, 'Rita', 'F', 34),
(2, 'Amit', 'M', 45),
(3, 'Sneha', 'F', 29);

INSERT INTO Claims VALUES
(101, 1, 1200.50, '2023-05-10', 'Approved'),
(102, 1, 500.00,  '2023-06-02', 'Pending'),
(103, 2, 800.00,  '2023-06-15', 'Approved'),
(104, 3, 1000.00, '2023-07-01', 'Rejected');
