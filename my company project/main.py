from dynamic_resume import create_resume
import webbrowser
import time
from urllib.parse import quote
import yagmail

gmail_id = "hroshan6198@gmail.com"
gmail_password = "lleukvfqvsxbmqgo"

candidate_name = "Hrithik Roshan"
candidate_email = "hroshan6198@gmail.com"
candidate_phone = "9361097450"

current_location = "Chennai"
preferred_location = "USA"

availability = "Immediate"
experience = "Fresher"
salary = "Negotiable"

resume_file = "dynamic_resume.py" 

daily_email_capacity = 200

cc_emails = [
    "quinn@jpitstaffing.com",
    "kim@jpitstaffing.com"
]

job_roles = [
  "JAVA DEVELOPER+C2C",
  "BUSINESS ANALYST+C2C",
  "PROJECT MANAGER+C2C",
  "DATA ANALYST+C2C"
]

recruiter_email = "hroshan6198@gmail.com"


yag = yagmail.SMTP(gmail_id, gmail_password)



email_count = 0

for role in job_roles:

    if email_count >= daily_email_capacity:
        print("Daily Email Limit Reached")
        break


    search_role = quote(role)
    search_location = quote(preferred_location)

    linkedin_link = (
        f"https://www.linkedin.com/jobs/search/"
        f"?keywords={search_role}&location={search_location}&f_TPR=r86400"
    )

    print("====================================")
    print("Opening LinkedIn Search For:", role)
    print("LinkedIn Link:", linkedin_link)

# webbrowser.open(linkedin_link)

    
    time.sleep(3)


    subject = f"Application for {role} Position 🚀"


    body = f"""
Dear Recruiter 👋,

I recently came across your LinkedIn job posting for the {role} position in {preferred_location} 🇺🇸 and I am very interested in this opportunity.

Your requirement closely matches my skills, learning interests, and passion for software development and technology 💻✨

📌 Please find my updated resume attached for your review and consideration.

🔗 LinkedIn Job Search Link:
{linkedin_link}

👨‍💻 Candidate Details:

✅ Full Name: {candidate_name}
✅ Email Address: {candidate_email}
✅ Phone Number: {candidate_phone}
✅ My linkedin profile: https://www.linkedin.com/in/hrithik-roshan-132423372/
✅ Current Location: {current_location}
✅ Preferred Location: {preferred_location} 🇺🇸
✅ Open To Relocate: Yes
✅ Availability: {availability}
✅ Experience Level: {experience}
✅ Expected Salary: {salary}

I would truly appreciate the opportunity to discuss how my skills and enthusiasm can contribute to your organization 🚀

Thank you for your valuable time and consideration 🙏

Looking forward to hearing from you soon 😊

Best Regards,
{candidate_name}
"""
    clean_role = role.replace("+C2C", "")
    resume_file = create_resume(clean_role)

    yag.send(
        to=recruiter_email,
        subject="Application for " + role,
        contents=body,
        attachments=[resume_file]
    )

    email_count += 1
    print("✅ Email Sent Successfully For:", role)

print("====================================")
print("🎉 API1 Project Completed Successfully")
print("📧 Total Emails Sent:", email_count)
print("🇺🇸 USA Location Filter Added")
print("🔗 LinkedIn Link Added")
print("📄 Resume Attachment Added")
print("📨 Daily Email Capacity:", daily_email_capacity)