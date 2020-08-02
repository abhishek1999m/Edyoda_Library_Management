class fine:

    def calcBill(days):
        max_days = 10
        per_day_fine = 5
        if days > max_days:
            fine_days = days - max_days
            fine = fine_days * per_day_fine
            print("Extra days {}, Fine amount {} Rs.".format(fine_days, fine))
        else:
            print("Thank you for returning book on time!")