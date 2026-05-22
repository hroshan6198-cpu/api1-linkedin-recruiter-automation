from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_resume(job_role):
    name = "Alex Morgan"
    email = "alex.morgan@email.com"
    phone = "+1 555 014 7890"
    location = "New York, USA"
    linkedin = "https://www.linkedin.com/in/alex-morgan"
    portfolio = "https://alexmorgan.dev"

    resumes = {
        "JAVA DEVELOPER": {
            "summary": """
Professional and detail-oriented Java Developer with strong knowledge of Java, Python, Object-Oriented Programming, backend development, REST API integration, database handling, and web technologies. Experienced in building automation-based applications, recruiter workflow systems, job search automation, dynamic resume generation, and professional email automation.

Skilled in writing clean and maintainable code, debugging application issues, understanding business requirements, and developing practical software solutions. Strong understanding of software development lifecycle, backend logic, API communication, data handling, and workflow automation.
""",
            "skills": [
                "Java Programming", "Python Programming", "OOP Concepts",
                "Backend Development", "REST API Integration", "MySQL Basics",
                "HTML5", "CSS3", "JavaScript", "Git & GitHub",
                "Automation Workflow", "Debugging", "Problem Solving"
            ],
            "project": """
Developed an API1 LinkedIn Recruiter Automation Project that automatically searches LinkedIn job roles, filters Java Developer C2C opportunities, generates customized PDF resumes, and sends professional recruiter emails with resume attachments.

The system reduces manual job application effort by combining LinkedIn search automation, recruiter email workflow, dynamic resume generation, and Gmail SMTP integration.
"""
        },

        "BUSINESS ANALYST": {
            "summary": """
Professional Business Analyst with strong knowledge of requirement analysis, workflow documentation, business process improvement, reporting, communication, and project coordination. Skilled in understanding business needs, organizing information, preparing structured documentation, and supporting teams with clear process flows.

Experienced in automation workflow projects involving recruiter data handling, job requirement analysis, professional communication, and role-based document generation. Strong ability to connect business requirements with technical implementation.
""",
            "skills": [
                "Requirement Analysis", "Business Documentation", "Workflow Analysis",
                "Excel & Reporting", "Communication Skills", "Process Improvement",
                "Stakeholder Coordination", "Problem Solving", "Data Organization",
                "Project Support", "Professional Documentation"
            ],
            "project": """
Created an API1 recruiter workflow automation system that analyzes job roles, organizes recruiter information, prepares role-based resume documents, and automates professional email communication.

The project improves business workflow efficiency by reducing repetitive manual work and creating a structured process for recruiter communication.
"""
        },

        "PROJECT MANAGER": {
            "summary": """
Organized and responsible Project Manager with knowledge of project planning, task coordination, team communication, workflow management, documentation, and project execution. Skilled in managing project activities, tracking progress, organizing resources, and ensuring timely completion of project tasks.

Experienced in handling automation workflow projects involving recruiter data, LinkedIn search process, email automation, dynamic resume generation, and professional communication management.
""",
            "skills": [
                "Project Planning", "Task Management", "Team Coordination",
                "Workflow Management", "Communication Management", "Documentation",
                "Leadership", "Time Management", "Project Reporting",
                "Problem Solving", "Process Optimization"
            ],
            "project": """
Managed and developed an API1 recruiter automation project that performs LinkedIn job search automation, recruiter communication, role-based resume generation, and automated email sending.

The project demonstrates planning, coordination, automation workflow design, and execution of a complete recruitment communication system.
"""
        },

        "DATA ANALYST": {
            "summary": """
Analytical and detail-oriented Data Analyst with strong knowledge of Python, Pandas, Excel, CSV handling, data cleaning, reporting, and data processing automation. Skilled in organizing raw data, identifying useful information, preparing structured reports, and improving workflow efficiency through automation.

Experienced in recruiter data processing, LinkedIn job filtering, CSV-based data handling, dynamic resume creation, and automated email workflow systems.
""",
            "skills": [
                "Python Programming", "Pandas Library", "Excel",
                "CSV Data Handling", "Data Cleaning", "Data Analysis",
                "Reporting", "Data Organization", "Workflow Automation",
                "Analytical Thinking", "Problem Solving"
            ],
            "project": """
Developed an API1 recruiter data processing automation system using Python and Pandas to filter LinkedIn job roles, organize recruiter data, generate dynamic PDF resumes, and automate professional email communication.

The system improves data handling efficiency and reduces manual recruitment workflow effort.
"""
        }
    }

    details = resumes[job_role]

    file_name = job_role + "_Resume.pdf"

    pdf = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph(name, styles["Title"]))
    content.append(Paragraph("Email: " + email, styles["Normal"]))
    content.append(Paragraph("Phone: " + phone, styles["Normal"]))
    content.append(Paragraph("Location: " + location, styles["Normal"]))
    content.append(Paragraph("LinkedIn: " + linkedin, styles["Normal"]))
    content.append(Paragraph("Portfolio: " + portfolio, styles["Normal"]))
    content.append(Spacer(1, 14))

    content.append(Paragraph("Professional Summary", styles["Heading2"]))
    content.append(Paragraph(details["summary"], styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Applied Role", styles["Heading2"]))
    content.append(Paragraph(job_role + " - C2C", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Technical Skills", styles["Heading2"]))
    for skill in details["skills"]:
        content.append(Paragraph("• " + skill, styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Project Experience", styles["Heading2"]))
    content.append(Paragraph("API1 - LinkedIn Recruiter Automation Project", styles["Heading3"]))
    content.append(Paragraph(details["project"], styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Education", styles["Heading2"]))
    content.append(Paragraph("Bachelor Degree in Computer Science - Pursuing", styles["Normal"]))
    content.append(Paragraph("Higher Secondary Education - Completed", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Additional Strengths", styles["Heading2"]))
    strengths = [
        "Quick Learner",
        "Strong Communication Skills",
        "Team Collaboration",
        "Problem Solving",
        "Professional Work Ethics",
        "Adaptability",
        "Time Management"
    ]

    for strength in strengths:
        content.append(Paragraph("• " + strength, styles["Normal"]))

    pdf.build(content)

    return file_name


if __name__ == "__main__":
    job_roles = [
        "JAVA DEVELOPER",
        "BUSINESS ANALYST",
        "PROJECT MANAGER",
        "DATA ANALYST"
    ]

    for job_role in job_roles:
        resume_file = create_resume(job_role)
        print("Resume Created:", resume_file)