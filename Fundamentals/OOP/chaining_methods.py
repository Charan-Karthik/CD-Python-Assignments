
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

        return self
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("You have successfully enrolled in the rewards program! You have 200 Gold Card Points.")
        else:
            print("User already a member.")

        return self
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
            print("Points remaining:", self.gold_card_points)
        else:
            print("Not enough points.")
        
        return self


user1 = User("Ash", "Ketchum", "gottacatchemall@outlook.com", 10)
user1.display_info().enroll().spend_points(50).display_info().enroll()

user2 = User("Kaguya", "Shinomiya", "shinomiya_kaguya@gmail.com", 17)
user2.spend_points(80).display_info()

user3 = User("Miyuki", "Shirogane", "shiromiyu@gmail.com", 18)
user3.display_info().spend_points(40)