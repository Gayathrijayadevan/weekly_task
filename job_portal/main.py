class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, password):
        return self.password == password


class Employer(User):
    def __init__(self, username, password, company_name):
        super().__init__(username, password)
        self.company_name = company_name
        self.jobs_posted = []

    def post_job(self, title, description):
        job = Job(title, description, self)
        self.jobs_posted.append(job)
        return job


class JobSeeker(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def apply_for_job(self, job):
        if job not in job_portal.jobs:
            print(f"Job '{job.title}' not found in the portal.")
            return

        application = Application(self, job)
        job.applications.append(application)
        print(f"{self.username} applied for '{job.title}'")


class Job:
    def __init__(self, title, description, employer):
        self.title = title
        self.description = description
        self.employer = employer
        self.applications = []

    def __str__(self):
        return f"{self.title} at {self.employer.company_name}"


class Application:
    def __init__(self, job_seeker, job):
        self.job_seeker = job_seeker
        self.job = job

    def __str__(self):
        return f"{self.job_seeker.username} applied for {self.job.title}"


class JobPortal:
    def __init__(self):
        self.users = []
        self.jobs = []

    def register_employer(self, username, password, company_name):
        employer = Employer(username, password, company_name)
        self.users.append(employer)
        print(f"Employer '{username}' registered successfully.")
        return employer

    def register_job_seeker(self, username, password):
        job_seeker = JobSeeker(username, password)
        self.users.append(job_seeker)
        print(f"Job Seeker '{username}' registered successfully.")
        return job_seeker

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.authenticate(password):
                print(f"Welcome, {username}!")
                return user
        print("Invalid username or password.")
        return None

    def add_job(self, job):
        self.jobs.append(job)

    def list_jobs(self):
        print("\nAvailable Jobs:")
        for job in self.jobs:
            print(job)

    def list_applications_for_job(self, job):
        if job in self.jobs:
            print(f"\nApplications for '{job.title}':")
            for application in job.applications:
                print(application)
        else:
            print("Job not found in the portal.")


def main():
    global job_portal
    job_portal = JobPortal()

    while True:
        print("\nJob Portal Menu:")
        print("1. Register as Employer")
        print("2. Register as Job Seeker")
        print("3. Login as Employer")
        print("4. Login as Job Seeker")
        print("5. List All Jobs")
        print("6. Exit")

        ch =int(input("Enter your choice (1-6): "))

        if ch == 1:
            username = input("Enter employer username: ")
            password = input("Enter employer password: ")
            company_name = input("Enter company name: ")
            job_portal.register_employer(username, password, company_name)

        elif ch == 2:
            username = input("Enter job seeker username: ")
            password = input("Enter job seeker password: ")
            job_portal.register_job_seeker(username, password)

        elif ch == 3:
            username = input("Enter employer username: ")
            password = input("Enter employer password: ")
            employer = job_portal.login(username, password)
            if type(employer) is Employer:
                employer_menu(employer)


        elif ch == 4:
            username = input("Enter job seeker username: ")
            password = input("Enter job seeker password: ")
            job_seeker = job_portal.login(username, password)
            if isinstance(job_seeker, JobSeeker):
                job_seeker_menu(job_seeker)

        elif ch == 5:
            job_portal.list_jobs()

        elif ch == 6:
            print("Exiting the job portal. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def employer_menu(employer):
    while True:
        print("\nEmployer Menu:")
        print("1. Post a Job")
        print("2. View the Job and Applications")
        print("3. Logout")

        choice = input("Enter your choice from 1 to 3: ")

        if choice == '1':
            title = input("Enter job title: ")
            description = input("Enter job description: ")
            job = employer.post_job(title, description)
            job_portal.add_job(job)
            print(f"Job '{title}' posted successfully.")

        elif choice == '2':
            print("\nYour Jobs:")
            for job in employer.jobs_posted:
                print(job)
                job_portal.list_applications_for_job(job)

        elif choice == '3':
            print(f"Logging out {employer.username}.")
            break

        else:
            print("Invalid choice. Please try again.")


def job_seeker_menu(job_seeker):
    while True:
        print("\nJob Seeker Menu:")
        print("1. Apply for a Job")
        print("2. View My Applications")
        print("3. Logout")

        choice =int(input("Enter your choice : "))

        if choice == 1:
            print("\nAvailable Jobs:")
            for i, job in enumerate(job_portal.jobs, start=1):
                print(f"{i}. {job}")
            job_choice = input("Enter the number of the job you want to apply for: ")

            if job_choice.isdigit():
                job_index = int(job_choice) - 1
                if 0 <= job_index < len(job_portal.jobs):
                    job = job_portal.jobs[job_index]
                    job_seeker.apply_for_job(job)
                else:
                    print("Invalid job selection.")
            else:
                print("Invalid input. Please enter a number.")

        elif choice == 2:
            print("\nYour Applications:")
            for job in job_portal.jobs:
                for application in job.applications:
                    if application.job_seeker == job_seeker:
                        print(application)

        elif choice == 3:
            print(f"Logging out {job_seeker.username}.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
