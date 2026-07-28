def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func(is_logged_in)
        else:
            print("Access Denied! Please log in first.")
    return wrapper


@login_required
def view_dashboard(is_logged_in):
    print("Welcome! You have successfully accessed the dashboard.")


status = input("Are you logged in? (yes/no): ").lower()

if status == "yes":
    logged_in = True
else:
    logged_in = False

view_dashboard(logged_in)