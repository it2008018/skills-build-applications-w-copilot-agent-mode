from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the octofit_db database
db = client["octofit_db"]

# Insert test data into the users collection
users = [
    {"email": "user1@example.com", "name": "User One", "age": 25, "team": "Team A"},
    {"email": "user2@example.com", "name": "User Two", "age": 30, "team": "Team B"},
    {"email": "user3@example.com", "name": "User Three", "age": 22, "team": "Team A"},
]
db.users.insert_many(users)

# Insert test data into the teams collection
teams = [
    {"name": "Team A", "members": ["user1@example.com", "user3@example.com"]},
    {"name": "Team B", "members": ["user2@example.com"]},
]
db.teams.insert_many(teams)

# Insert test data into the activity collection
activities = [
    {"user_email": "user1@example.com", "activity": "Running", "duration": 30},
    {"user_email": "user2@example.com", "activity": "Cycling", "duration": 45},
    {"user_email": "user3@example.com", "activity": "Swimming", "duration": 60},
]
db.activity.insert_many(activities)

# Insert test data into the leaderboard collection
leaderboard = [
    {"user_email": "user1@example.com", "points": 100},
    {"user_email": "user2@example.com", "points": 150},
    {"user_email": "user3@example.com", "points": 200},
]
db.leaderboard.insert_many(leaderboard)

# Insert test data into the workouts collection
workouts = [
    {"name": "Morning Run", "type": "Cardio", "duration": 30},
    {"name": "Evening Yoga", "type": "Flexibility", "duration": 60},
]
db.workouts.insert_many(workouts)

print("Test data has been added to the database.")