from oops_proj import chatbook

# print(user1._chatbook__name)  #used to retrive hidden/private attribute

#getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

#static variable/method call
# user1 = chatbook()
# print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

#setter and getter call for static variable
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)


# lst = [1,2,3]

# function
# a1 = len(lst)
# print(a1)

# method
# user1 = chatbook()
# user1.sendmsg()
