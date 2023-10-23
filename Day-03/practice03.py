#without using variable 
# print("project-01-instance")

#with variable
# ec2_instance_name = "project-01-instance"
# print(ec2_instance_name)


#program to explain global variable
# a = 10
# b = 10

# def addition():
#     print(a+b)

# def substraction():
#     print(a-b)

# addition()
# substraction()


#program to define local variable and it will throw the error for substraction function.
# def addition():
#     a = 10
#     b = 10
#     print(a+b)

# def substraction():
#     print(a-b)

# addition()
# substraction()


#glabal and local variable together

a = 10
b = 10

def addition():
    c = 10
    print(f"Additiion is: {a + b + c}" )

def substraction():
    print( a - b )

addition()
substraction()



# # Define configuration variables for a web server
# server_name = "my_server"
# port = 80
# is_https_enabled = True
# max_connections = 1000

# # Print the configuration
# print("Server Name:",server_name)
# print(f"Port: {port}")
# print(f"HTTPS Enabled: {is_https_enabled}")
# print(f"Max Connections: {max_connections}")

# # Update configuration values
# port = 443
# is_https_enabled = False

# # Print the updated configuration
# print(f"Updated Port: {port}")
# print(f"Updated HTTPS Enabled: {is_https_enabled}")
