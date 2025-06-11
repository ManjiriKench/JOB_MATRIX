import joblib
import numpy as np


def recommend_job(user_skills, top_n=5):
    # Load pre-trained models and dataset
    nn_model = joblib.load('models/job_recommender.pkl')
    bert_model = joblib.load('models/bert_model.pkl')
    df = joblib.load('models/job_data.pkl')


    # Clean and preprocess user input skills
    skills_str = ' '.join(user_skills)


    # Generate sentence embedding for the user's skills
    user_embedding = bert_model.encode([skills_str])[0]


    # Get the nearest neighbors for the user's skills
    dist, idx = nn_model.kneighbors([user_embedding], n_neighbors=top_n)


    top_jobs = []


    print(f"\n🎯 Top {top_n} Job Recommendations:")
    for i in range(top_n):
        job_idx = idx[0][i]
        job_title = df.iloc[job_idx]['job_title']
        job_skills = df.iloc[job_idx]['skills']
        job_desc = df.iloc[job_idx].get('description', 'No description available')
        salary_range = df.iloc[job_idx].get('salary', 'Not available')


        job_skill_list = [s.strip() for s in job_skills.split(';')]
        match_score = 100 - dist[0][i] * 100  # Convert cosine distance to percentage


        print(f"{i + 1}. {job_title}")
        print(f"   - Match Score: {match_score:.2f}%")
        print(f"   - Skills: {job_skills}")
        print(f"   - Job Description: {job_desc}")
        print(f"   - Salary Range: {salary_range}")


        # Skill gap analysis
        skill_gap_analysis(user_skills, job_skill_list)


        print("---")


        top_jobs.append({
            'job_title': job_title,
            'skills': job_skill_list,
            'match_score': match_score
        })


    return top_jobs


def skill_gap_analysis(user_skills, job_required_skills):
    user_skills_lower = [s.lower() for s in user_skills]
    missing_skills = [skill for skill in job_required_skills if skill.lower() not in user_skills_lower]


    if missing_skills:
        print("🚧 Missing Skills You May Need to Learn:")
        print(', '.join(missing_skills))
    else:
        print("🎉 You meet all the listed job requirements!")
