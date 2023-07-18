class Phone:
    "A SIMPLE CLASS FOR TEST"
    phone_version="M31"
    brand_name="Samsung"
    user_name=" "

    model="S10+"
    #defining a getter
    def get_model(self):
        return self.model

    #definig setter
    def set_model(self,val):
        self.model="S10+ ," + val

    #CONSTRUCTOR=> WHENEVER AN OBJECT OF THIS CLASS IS CREATED THE CONSTRUCTOR GETS INVOKED.
    #THE CONSTRUCTOR IS DEFAULTLY PRESENT IF U HAVE NOT CREATED ONE..

    def __init__(self , user_name):
        self.user_name=user_name


    def BootLogo(self):
        print("SAMSUNG" , self.phone_version)


# priya=Phone("Priya phone")
# # creating an object and calling constructor-- arguments matching constructor argument.
# # priya.phone_version="IPHONE-X567" #CANNOT MODIFY .. THIS ISSUE CAN BE RESOLVED USING "GETTERS_AND_SETTERS"
# priya.BootLogo()
# priya.model="iphone"  #overriding the value.
priya=Phone("my phone")
priya.set_model("iPhone")
print(priya.get_model())

print(priya.model,"here")
