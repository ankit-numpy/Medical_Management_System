###### Medical Management System

A simple medical management system built using Python, MySQL, and Streamlit. This application allows users to manage patient records and appointments efficiently.

## Features

- Add new patients to the database.
- View a list of all patients.
- Schedule appointments for patients.
- View a list of all appointments.

## Technologies Used

- Python
- MySQL
- Streamlit
- mysql-connector-python

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- MySQL Server
- pip (Python package installer)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CH-Anonymous/medical-management-system.git
   cd medical-management-system
   ```

2. **Install required Python packages**:
   ```bash
   pip install mysql-connector-python streamlit
   ```

3. **Set up the MySQL database**:
   Open your MySQL client and run:
   ```sql
   CREATE DATABASE HealthCareOrgDB;

   USE HealthCareOrgDB;

   CREATE TABLE IF NOT EXISTS Patients (
       patient_id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       age INT,
       gender VARCHAR(10),
       contact_number VARCHAR(15)
   );

   CREATE TABLE IF NOT EXISTS Appointments (
       appointment_id INT AUTO_INCREMENT PRIMARY KEY,
       patient_id INT,
       appointment_date DATETIME,
       doctor_name VARCHAR(255),
       FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
   );
   ```

4. **Configure database connection**:
   In your `database.py`, replace:
   ```python
   user='your_username'
   password='your_password'
   ```
   with your actual MySQL credentials.

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open the browser**:
   Visit `http://localhost:8501` to use the app.

3. **Use the features**:
   Use the sidebar to navigate between options like adding/viewing patients and appointments.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Streamlit community for their great tools.
- Inspired by real-world healthcare record management challenges.

```
