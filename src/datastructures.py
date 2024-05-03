
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
       self.last_name = last_name
       self._next_id = 1
       self._members = [
           { 
               "age": 33,
        "first_name": "John",
        "last_name": "Jackson",
        "id": 1,
        "lucky_numbers": [
             7, 13, 22
        ]
        },
        {
            "age": 35,
        "first_name": "Jane",
        "last_name": "Jackson"
        "id": 2,
        "lucky_numbers": [
             10, 14, 3
        ]
        },{
                "age": 5,
        "first_name": "Jimmy",
        "last_name": "Jackson"
        "id": 3,
        "lucky_numbers": [
            1
        ]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):   
        member["id"] = self._generateId()    
        self._members.append(member)
        return self._members
    
    def delete_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                del self._members[i]
                break  
        return self._members  

        
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
           

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
