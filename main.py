from recommender import recommend_job, skill_gap_analysis
from utils.skill_extractor import analyze_skills, extract_text_from_pdf
import joblib


def main():
    print("==== AI Job Recommendation System ====")
    print("1. Analyze Resume and Recommend Job")
    print("2. Exit")


    choice = input("Select an option: ")


    if choice == '1':
        file_path = input("Enter the path to your resume PDF: ")
        resume_text = extract_text_from_pdf(file_path)


        if resume_text:
            # Load all possible skills from dataset
            df = joblib.load('models/job_data.pkl')
            all_skills = set()
            for skills in df['skills']:
                all_skills.update([s.strip() for s in skills.split(';')])


            found_skills = analyze_skills(resume_text, all_skills)


            if found_skills:
                print("\n✅ Skills Found in Resume:")
                print(', '.join(found_skills))


                print("\n🔍 Recommending Jobs Based on Your Skills...")
                top_jobs = recommend_job(found_skills, top_n=5)


                # For each job, perform skill gap analysis
                for idx, job in enumerate(top_jobs, 1):
                    print(f"\n📌 Skill Gap for Job {idx}: {job['job_title']}")
                    skill_gap_analysis(found_skills, job['skills'])
            else:
                print("⚠️ No known skills found in the resume.")
        else:
            print("❌ Could not extract text from the PDF.")


    elif choice == '2':
        print("👋 Exiting the system. Goodbye!")


    else:
        print("❌ Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
