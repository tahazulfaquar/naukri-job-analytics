TRUNCATE TABLE clean_jobs;

INSERT INTO clean_jobs (
    job_id,
    title,
    company,
    rating,
    reviews,
    min_experience,
    max_experience,
    location,
    job_url,
    salary,
    posted,
    skills,
    scraped_at
)
SELECT
    job_id,
    title,
    company,
    NULLIF(rating, '')::NUMERIC(3,1),
    NULLIF(REPLACE(reviews, ' Reviews', ''),'')::INTEGER,
    NULLIF(split_part(experience, '-', 1),'')::INTEGER,
    NULLIF(split_part(split_part(experience, '-', 2),' ',1),'')::INTEGER,
    location,
    job_url,
    salary,
    posted,
    skills,
    scraped_at::TIMESTAMP
FROM raw_jobs;
