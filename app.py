import streamlit as st
from urllib.parse import quote_plus

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Student Opportunity Finder",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# STYLING
# =========================================================

st.markdown("""
<style>
.main {
    background-color: #f7f8fa;
}

h1 {
    font-size: 38px !important;
}

.subtitle {
    color: #6b7280;
    font-size: 16px;
    margin-bottom: 25px;
}

.card {
    padding: 20px;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    background: white;
    margin-bottom: 15px;
}

.small {
    color: #6b7280;
    font-size: 13px;
}

.match {
    font-size: 14px;
    color: #374151;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================

def clean(text):
    return text.strip()


def first_skill(skills):
    if skills:
        return skills[0]
    return ""


def first_interest(interests):
    if interests:
        return interests[0]
    return ""


# =========================================================
# PERSONALIZED LINK GENERATORS
# =========================================================

def linkedin_jobs(skills, interests, location):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://www.linkedin.com/jobs/search/?"
        "keywords=" + quote_plus(keyword) +
        "&location=" + quote_plus(location)
    )


def indeed_jobs(skills, interests, location):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://www.indeed.com/jobs?"
        "q=" + quote_plus(keyword) +
        "&l=" + quote_plus(location)
    )


def internshala(skills, location):

    skill = first_skill(skills)

    if location:
        return (
            "https://internshala.com/internships/"
            + quote_plus(skill)
            + "-internship-in-"
            + quote_plus(location)
            + "/"
        )

    return (
        "https://internshala.com/internships/"
        + quote_plus(skill)
        + "-internship/"
    )


def unstop(skills, interests):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://unstop.com/search?"
        "search=" + quote_plus(keyword)
    )


def wellfound(skills, interests, location):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://wellfound.com/jobs?"
        "q=" + quote_plus(keyword) +
        "&location=" + quote_plus(location)
    )


def coursera(skills, interests):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://www.coursera.org/search?"
        "query=" + quote_plus(keyword)
    )


def edx(skills, interests):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://www.edx.org/search?"
        "q=" + quote_plus(keyword)
    )


def kaggle(skills, interests):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://www.kaggle.com/search?"
        "q=" + quote_plus(keyword)
    )


def devpost(skills, interests):

    keyword = " ".join(
        skills[:2] + interests[:2]
    ).strip()

    return (
        "https://devpost.com/search?"
        "query=" + quote_plus(keyword)
    )


# =========================================================
# OPPORTUNITY CREATOR
# =========================================================

def create_opportunities(
    education,
    year,
    location,
    skills,
    interests,
    duration,
    selected_types
):

    opportunities = []

    # -----------------------------------------------------
    # INTERNSHIPS
    # -----------------------------------------------------

    if "Internships" in selected_types:

        opportunities.append({
            "type": "Internship",
            "name": "Internshala",
            "description":
                f"Internships related to {', '.join(skills)} "
                f"in {location}.",
            "url":
                internshala(skills, location)
        })

        opportunities.append({
            "type": "Internship",
            "name": "LinkedIn Jobs",
            "description":
                f"{', '.join(skills + interests)} "
                f"opportunities around {location}.",
            "url":
                linkedin_jobs(
                    skills,
                    interests,
                    location
                )
        })

        opportunities.append({
            "type": "Internship",
            "name": "Indeed",
            "description":
                f"Student internships matching "
                f"{', '.join(skills)} in {location}.",
            "url":
                indeed_jobs(
                    skills,
                    interests,
                    location
                )
        })

        opportunities.append({
            "type": "Internship",
            "name": "Unstop",
            "description":
                f"Student opportunities involving "
                f"{', '.join(interests)}.",
            "url":
                unstop(
                    skills,
                    interests
                )
        })

        opportunities.append({
            "type": "Internship",
            "name": "Wellfound",
            "description":
                f"Startup roles related to "
                f"{', '.join(skills)}.",
            "url":
                wellfound(
                    skills,
                    interests,
                    location
                )
        })

    # -----------------------------------------------------
    # COURSES
    # -----------------------------------------------------

    if "Courses" in selected_types:

        opportunities.append({
            "type": "Course",
            "name": "Coursera",
            "description":
                f"Courses matching {', '.join(interests)} "
                f"and {', '.join(skills)}.",
            "url":
                coursera(
                    skills,
                    interests
                )
        })

        opportunities.append({
            "type": "Course",
            "name": "edX",
            "description":
                f"Learning programs related to "
                f"{', '.join(interests)}.",
            "url":
                edx(
                    skills,
                    interests
                )
        })

        opportunities.append({
            "type": "Course",
            "name": "Kaggle Learn",
            "description":
                f"Practical learning related to "
                f"{', '.join(skills)}.",
            "url":
                kaggle(
                    skills,
                    interests
                )
        })

    # -----------------------------------------------------
    # HACKATHONS
    # -----------------------------------------------------

    if "Hackathons" in selected_types:

        opportunities.append({
            "type": "Hackathon",
            "name": "Devpost",
            "description":
                f"Hackathons related to "
                f"{', '.join(interests)} "
                f"and {', '.join(skills)}.",
            "url":
                devpost(
                    skills,
                    interests
                )
        })

        opportunities.append({
            "type": "Hackathon",
            "name": "Unstop",
            "description":
                f"Hackathons and student challenges "
                f"related to {', '.join(interests)}.",
            "url":
                unstop(
                    skills,
                    interests
                )
        })

    # -----------------------------------------------------
    # COMPETITIONS
    # -----------------------------------------------------

    if "Competitions" in selected_types:

        opportunities.append({
            "type": "Competition",
            "name": "Kaggle",
            "description":
                f"Competitions related to "
                f"{', '.join(interests)}.",
            "url":
                kaggle(
                    skills,
                    interests
                )
        })

        opportunities.append({
            "type": "Competition",
            "name": "Unstop",
            "description":
                f"Student competitions matching "
                f"{', '.join(interests)}.",
            "url":
                unstop(
                    skills,
                    interests
                )
        })

    # -----------------------------------------------------
    # JOBS
    # -----------------------------------------------------

    if "Jobs" in selected_types:

        opportunities.append({
            "type": "Job",
            "name": "LinkedIn Jobs",
            "description":
                f"Jobs matching {', '.join(skills)} "
                f"and {', '.join(interests)} in {location}.",
            "url":
                linkedin_jobs(
                    skills,
                    interests,
                    location
                )
        })

        opportunities.append({
            "type": "Job",
            "name": "Indeed",
            "description":
                f"Jobs related to {', '.join(skills)} "
                f"in {location}.",
            "url":
                indeed_jobs(
                    skills,
                    interests,
                    location
                )
        })

        opportunities.append({
            "type": "Job",
            "name": "Wellfound",
            "description":
                f"Startup jobs involving "
                f"{', '.join(skills)}.",
            "url":
                wellfound(
                    skills,
                    interests,
                    location
                )
        })

    return opportunities


# =========================================================
# HEADER
# =========================================================

st.title("Student Opportunity Finder")

st.markdown(
    '<div class="subtitle">'
    'Enter your profile and get personalized search links '
    'for trusted opportunity platforms.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# COLUMNS
# =========================================================

left, right = st.columns(
    [1, 1.6],
    gap="large"
)


# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.subheader("Student Profile")

    with st.container(border=True):

        education = st.selectbox(
            "Education",
            [
                "Computer Science",
                "Information Technology",
                "Electronics",
                "Electrical Engineering",
                "Mechanical Engineering",
                "Civil Engineering",
                "Business",
                "Commerce",
                "Science",
                "Arts",
                "Other"
            ]
        )

        year = st.selectbox(
            "Current Year",
            [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year",
                "Final Year",
                "Graduate"
            ]
        )

        location = st.text_input(
            "Location",
            placeholder="Bengaluru"
        )

        skills_text = st.text_input(
            "Skills",
            placeholder="Python, SQL, React"
        )

        interests_text = st.text_input(
            "Interests",
            placeholder="AI, Data Science"
        )

        duration = st.selectbox(
            "Preferred Duration",
            [
                "Any duration",
                "1 month",
                "2 months",
                "3 months",
                "6 months",
                "1 year"
            ]
        )

        st.markdown("### Opportunity Type")

        select_all = st.checkbox(
            "Select All"
        )

        internships = st.checkbox(
            "Internships",
            value=select_all
        )

        courses = st.checkbox(
            "Courses",
            value=select_all
        )

        hackathons = st.checkbox(
            "Hackathons",
            value=select_all
        )

        competitions = st.checkbox(
            "Competitions",
            value=select_all
        )

        jobs = st.checkbox(
            "Jobs",
            value=select_all
        )

        st.write("")

        find_button = st.button(
            "Find Personalized Opportunities",
            type="primary",
            use_container_width=True
        )


# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    st.subheader("Your Opportunities")

    if not find_button:

        with st.container(border=True):

            st.markdown(
                "### Your personalized links will appear here"
            )

            st.write(
                "Fill in your skills, interests and location, "
                "then click the button."
            )

    else:

        selected_types = []

        if internships:
            selected_types.append("Internships")

        if courses:
            selected_types.append("Courses")

        if hackathons:
            selected_types.append("Hackathons")

        if competitions:
            selected_types.append("Competitions")

        if jobs:
            selected_types.append("Jobs")

        skills = [
            clean(x)
            for x in skills_text.split(",")
            if clean(x)
        ]

        interests = [
            clean(x)
            for x in interests_text.split(",")
            if clean(x)
        ]

        if not selected_types:

            st.warning(
                "Select at least one opportunity type."
            )

        elif not skills and not interests:

            st.warning(
                "Enter at least one skill or interest "
                "so the links can be personalized."
            )

        else:

            opportunities = create_opportunities(
                education,
                year,
                location,
                skills,
                interests,
                duration,
                selected_types
            )

            # ---------------------------------------------
            # PROFILE SUMMARY
            # ---------------------------------------------

            st.markdown(
                f"""
                **Profile:** {education} · {year}

                **Location:** {location or "Any location"}

                **Skills:** {", ".join(skills) or "Any"}

                **Interests:** {", ".join(interests) or "Any"}

                **Duration:** {duration}
                """
            )

            st.divider()

            # ---------------------------------------------
            # RESULTS
            # ---------------------------------------------

            for opportunity in opportunities:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        f"### {opportunity['name']}"
                    )

                    st.caption(
                        opportunity["type"]
                    )

                    st.write(
                        opportunity["description"]
                    )

                    st.link_button(
                        f"Open personalized {opportunity['name']} search",
                        opportunity["url"],
                        use_container_width=True
                    )