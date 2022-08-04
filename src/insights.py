from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    list_of_unique_type = []
    for line in data:
        types = line.get("job_type")
        list_of_unique_type.append(types)
    job_type = set(list_of_unique_type)
    return job_type

# teste de execução da função get_unique_job_types


# if __name__ == "__main__":
#     types = get_unique_job_types("src/jobs.csv")
#     print(types)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    data = read(path)
    list_of_unique_industry = []
    for line in data:
        industries = line.get("industry")
        if industries != "":
            list_of_unique_industry.append(industries)
    industry = set(list_of_unique_industry)
    return industry

# teste de execução da função get_unique_industries


# if __name__ == "__main__":
#     industry = get_unique_industries("src/jobs.csv")
#     print(industry)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    data = read(path)
    max_salary = 0
    for line in data:
        check_salary = line["max_salary"].isdigit()
        if check_salary:
            salary = int(line["max_salary"])
        else:
            salary = 0
        if salary >= max_salary:
            max_salary = salary
    return max_salary

# teste de execução da função get_max_salary


if __name__ == "__main__":
    salary = get_max_salary("src/jobs.csv")
    print(salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
