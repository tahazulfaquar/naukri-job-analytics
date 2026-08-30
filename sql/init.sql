CREATE TABLE IF NOT EXISTS raw_jobs (
    job_id TEXT,
    title TEXT,
    company TEXT,
    rating TEXT,
    reviews TEXT,
    experience TEXT,
    location TEXT,
    job_url TEXT,
    salary TEXT,
    posted TEXT,
    skills TEXT,
    scraped_at TIMESTAMP
);

CREATE TABLE clean_jobs (
    job_id VARCHAR(50),
    title TEXT,
    company TEXT,
    rating NUMERIC(3,1),
    reviews INTEGER,
    min_experience INTEGER,
    max_experience INTEGER,
    location TEXT,
    job_url TEXT,
    salary TEXT,
    posted TEXT,
    skills TEXT,
    scraped_at TIMESTAMP
);
