# HRMS – Human Resource Management System

## Overview

HRMS (Human Resource Management System) is a Python-based project developed to simplify employee management operations inside an organization. The system provides separate Admin and Employee roles and includes modules for employee management, attendance tracking, leave handling, and salary management.

## Features

### Admin Features

* Add employee
* View employee list
* Search employee by ID
* Update employee details
* Delete employee record
* View all leave requests
* Approve leave
* Reject leave
* Update salary

### Employee Features

* View personal profile
* Mark attendance
* View attendance history
* Apply for leave
* View leave request status
* View salary details

## Tech Stack

* Python
* Lists and dictionaries for in-memory data storage
* GitHub for version control

## Project Structure

* `main.py` – contains the complete HRMS logic in a single file

## How It Works

1. User signs up as Admin or Employee
2. Admin logs in and manages employee records
3. Employee logs in to access attendance, leave, and salary features
4. Admin manages leave requests and salary updates

## Current Limitation

This project currently stores data in memory, so data resets whenever the program restarts.

## Future Scope

* Database integration
* Web-based interface
* Payroll automation
* Attendance with timestamps
* Reports and analytics dashboard
* Notifications and email integration
