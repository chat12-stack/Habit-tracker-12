# Habit Tracker Application

A desktop-based habit tracking system built with Python that helps users manage, track, and maintain their daily habits with streak counting functionality.

## 📋 Features

- **Add Habits** - Create new habits with custom names
- **Delete Habits** - Remove habits by entering their ID
- **Mark Done** - Mark a habit as completed and automatically increment its streak counter
- **View Habits** - Display all habits with their ID, name, completion status (Done/Not Done), and current streak
- **Reset Day** - Reset all habits' status to "Not Done" and clear all streaks for daily tracking

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Programming language |
| **Tkinter** | GUI framework for creating desktop interface |
| **MySQL** | Relational database for storing habit data |
| **MySQL Connector** | Python library for MySQL database connection and query execution |

## 📦 Modules/Libraries

```
tkinter           - GUI components (Tk, messagebox, Entry, Button, Label, Frame, Text)
mysql.connector   - Database connectivity and query execution
```

## 🗄️ Database Structure

**Table:** `habits`

| Column | Type | Description |
|--------|------|-------------|
| `id` | INT (Primary Key) | Unique identifier for each habit |
| `name` | VARCHAR | Name of the habit |
| `status` | INT | Completion status (1 = Done, 0 = Not Done) |
| `streak` | INT | Consecutive days counter |

## 🎨 GUI Components

- **Title Label** - "Habit Tracker System" header
- **Input Fields**:
  - Habit name entry field
  - Habit ID entry field (for delete/mark operations)
- **Action Buttons**:
  - Add Habit
  - Delete Habit
  - Mark Done
  - Reset Day
- **Display Area** - Text box showing all habits with their details
- **Window Specifications** - 700x500 pixels

## 🚀 How to Use

1. **Add a Habit** - Enter a habit name in the first text field and click "Add Habit"
2. **Mark Habit as Done** - Enter the habit ID and click "Mark Done" to increment streak
3. **Delete a Habit** - Enter the habit ID and click "Delete Habit" to remove it
4. **Reset Daily** - Click "Reset Day" to reset all habits and streaks for a new day
5. **View Habits** - All habits are displayed in the text box with their current status and streak count

## ⚙️ Prerequisites

- Python 3.x
- MySQL Server running locally
- MySQL database named `habit_tracker` with `habits` table
- mysql-connector-python library

Install the required library:
```bash
pip install mysql-connector-python
```

## 🔧 Configuration

Update the database connection details in the code:
```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="habit_tracker"
)
```
