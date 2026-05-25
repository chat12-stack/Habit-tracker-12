# Habit Tracker GUI Walkthrough

This document provides a detailed walkthrough of the Habit Tracker application's graphical user interface, including all key features and user interactions.

## 📸 Interface Overview

The Habit Tracker System features a clean, intuitive desktop interface with the following sections:
- **Title Bar**: "Habit Tracker System" header
- **Input Fields**: For entering habit names and IDs
- **Action Buttons**: Four primary action buttons for managing habits
- **Display Area**: Text box showing all habits with status and streak information
- **Window Size**: 700x500 pixels

---

## 🎯 Feature Walkthrough

### 1. Initial State - No Habits
When the application first launches, it displays an empty state:
- Display area shows "No habits found."
- All input fields are ready for user input
- All buttons are enabled and awaiting interaction

**Available Actions:**
- Add your first habit using the "Add Habit" button

---

### 2. Add Habit

**Step:**
1. Enter a habit name in the text input field (e.g., "drinking")
2. Click the "Add Habit" button

**Result:**
- Habit is saved to the database with initial values:
  - **Status**: Not Done (0)
  - **Streak**: 0
- Habit appears in the display area with a unique ID
- Display format: `ID: [id] | [habit_name] | Not Done | Streak: 0`

**Example Output:**
```
ID: 1 | drinking | Not Done | Streak: 0
```

---

### 3. Mark Habit as Done

**Step:**
1. Enter the habit ID in the second text input field (e.g., "1")
2. Click the "Mark Done" button

**Action:**
- Updates the habit's status in the database
- Increments the streak counter by 1
- Updates the display area immediately

**Result Before:**
```
ID: 1 | drinking | Not Done | Streak: 0
```

**Result After:**
```
ID: 1 | drinking | Done | Streak: 1
```

---

### 4. Reset Day

**Step:**
1. Click the "Reset Day" button

**Action:**
- Resets ALL habits' status to "Not Done" (0)
- Clears ALL streak counters back to 0
- Updates the display area to reflect changes

**Result After Reset:**
```
ID: 1 | drinking | Not Done | Streak: 0
```

---

### 5. Delete Habit

**Step:**
1. Enter the habit ID to delete in the text input field (e.g., "1")
2. Click the "Delete Habit" button

**Action:**
- Removes the habit from the database permanently
- The habit no longer appears in the display area
- If last habit is deleted, display shows "No habits found."

---

## 🎛️ Button Functions

| Button | Function | Input Required | Result |
|--------|----------|-----------------|--------|
| **Add Habit** | Create a new habit | Habit name in first field | Habit added with ID, status "Not Done", streak 0 |
| **Delete Habit** | Remove a habit | Habit ID in second field | Habit removed from database |
| **Mark Done** | Mark habit as completed | Habit ID in second field | Status changes to "Done", streak increments by 1 |
| **Reset Day** | Reset all habits daily | None | All statuses reset to "Not Done", all streaks reset to 0 |

---

## 📊 Habit Display Format

Each habit in the display area shows:

```
ID: [habit_id] | [habit_name] | [status] | Streak: [streak_count]
```

### Status Values:
- **Not Done** = Habit not completed today
- **Done** = Habit completed today

### Example Display:
```
ID: 1 | drinking | Done | Streak: 1
ID: 2 | exercise | Not Done | Streak: 0
ID: 3 | reading | Done | Streak: 3
```

---

## 🔄 Workflow Example

### Day 1 - Building Your First Habit

1. **Add Habit**: Enter "drinking" → Click "Add Habit"
   - Output: `ID: 1 | drinking | Not Done | Streak: 0`

2. **Mark as Done**: Enter "1" → Click "Mark Done"
   - Output: `ID: 1 | drinking | Done | Streak: 1`

3. **End of Day**: Click "Reset Day" (prepares for next day)
   - Output: `ID: 1 | drinking | Not Done | Streak: 1`

### Day 2 - Continuing the Streak

1. **Mark as Done**: Enter "1" → Click "Mark Done"
   - Output: `ID: 1 | drinking | Done | Streak: 2`

2. **End of Day**: Click "Reset Day"
   - Output: `ID: 1 | drinking | Not Done | Streak: 2`

---

## ⚠️ Important Notes

- **Reset Day** affects ALL habits at once - it's designed to be used once per day
- **Streak counter** persists across days but is only incremented when "Mark Done" is used
- **Habit IDs** are auto-generated and cannot be changed
- All data is stored in the MySQL database and persists after closing the application
- **Empty Fields**: Attempting to add a habit with an empty name will not create a habit
- **Invalid IDs**: Entering a non-existent ID for Mark Done or Delete will show an error message

---

## 🎓 Best Practices

1. **Add Habits** at the beginning of your tracking journey
2. **Mark Done** each time you complete a habit during the day
3. **Check Status** regularly to see your progress and streak counts
4. **Reset Day** once daily (typically at midnight or day start) to reset all habits for the new day
5. **Delete** only when you want to stop tracking a specific habit permanently

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Habit not appearing after adding | Check database connection and ensure MySQL is running |
| Mark Done not working | Verify habit ID exists and is entered correctly |
| Display not updating | Click a button to refresh, or check database connection |
| No habits found message | Add a new habit or check if all habits were deleted |

---

## 🔗 Related Documentation

- See [README.md](../README.md) for technical setup and requirements
- See source code for implementation details
